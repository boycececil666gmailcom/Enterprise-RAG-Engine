# region Imports
import asyncio
import json
import os
import uuid
import warnings
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
import httpx
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field
from llm_client import llm, vision_llm
from utils import clean_attachment_tags, fetch_media_data_uri, format_custom_fields, is_archive

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
# endregion


# region Configuration
_DIR = Path(__file__).resolve().parent
load_dotenv(_DIR.parent / ".env")

INPUT_PATH = _DIR / "1.jira_tickets.json"
OUTPUT_PATH = _DIR / "2.jira_modeled_chunks.json"

JIRA_AUTH = (
    (os.getenv("JIRA_EMAIL", ""), os.getenv("JIRA_API_TOKEN", ""))
    if os.getenv("JIRA_EMAIL") and os.getenv("JIRA_API_TOKEN")
    else None
)
# endregion


# region Pydantic Schemas
class TicketFilterModel(BaseModel):
    """Pass 1: Lightweight evaluation of technical value to avoid unnecessary media processing."""
    has_valuable_information: bool = Field(
        description="Set to true if the ticket contains actionable technical knowledge, valid task details, or defect reports. Set to false ONLY if it is an empty placeholder, duplicate, or devoid of technical content.",
    )


class TicketKnowledgeModel(BaseModel):
    """Pass 2: Detailed technical knowledge extraction with visual attachment context."""
    llm_summary: str = Field(
        default="",
        description="Comprehensive technical summary in English synthesized from the description (incorporating the injected visual attachment descriptions) and context.",
    )
    rca: str = Field(
        default="",
        description="Root cause analysis in English if identified, or concise requirement background. Empty if unknown.",
    )
    resolution: str = Field(
        default="",
        description="Technical resolution or fix applied in English to resolve the problem. Empty if unknown or not resolved yet.",
    )


class VisualAttachmentAnalysis(BaseModel):
    """Visual analysis for a specific media attachment."""
    filename: str = Field(description="Exact filename of the attachment")
    description: str = Field(
        description="1-2 sentence technical description in English of the UI state, animation behavior, or glitch shown.",
    )


class BatchVisualAnalysisModel(BaseModel):
    """Enforced schema for batch multimodal media analysis."""
    analyses: list[VisualAttachmentAnalysis] = Field(default_factory=list)


class KnowledgeMetadata(BaseModel):
    """Unified metadata payload storing raw JIRA attributes, RCA, attachments, and comments."""
    issue_key: str
    url: str = ""
    issuetype: str = "Task"
    summary: str
    has_valuable_information: bool
    rca: str = ""
    resolution: str = ""
    llm_summary: str = ""
    description: str = ""
    status: str = "Unknown"
    fix_versions: list[str] = Field(default_factory=list)
    attachments: list[dict[str, Any]] = Field(default_factory=list)
    comments: list[dict[str, Any]] = Field(default_factory=list)
    created: str = ""


class ModeledKnowledgeChunk(BaseModel):
    """Modeled knowledge chunk pairing deterministic UUID, small retrieval anchor, and unified metadata."""
    id: str
    small: str
    metadata: KnowledgeMetadata
# endregion


# region Media Enrichment
async def _enrich_attachments(
    attachments: list[dict[str, Any]],
    ticket_context: str,
    key: str,
    summary: str,
) -> list[dict[str, Any]]:
    """Enriches all non-archive image attachments using vision LLM analysis."""
    enriched = [dict(a, description=a.get("description", "")) for a in attachments]
    image_items = [a for a in enriched if a.get("mime_type", "").startswith("image/") and a.get("url")]

    if not vision_llm or not image_items:
        return enriched

    async with httpx.AsyncClient() as client:
        tasks = [fetch_media_data_uri(client, item, auth=JIRA_AUTH) for item in image_items]
        data_uris = await asyncio.gather(*tasks)

    valid_media = [(item, uri) for item, uri in zip(image_items, data_uris) if uri]
    if not valid_media:
        return enriched

    content_parts: list[dict[str, Any]] = [
        {
            "type": "text",
            "text": f"Analyze the visual attachments for JIRA ticket {key} ({summary}).\nContext:\n{ticket_context}\n\nFor each image, provide a 1-2 sentence description in English.",
        }
    ]
    for item, uri in valid_media:
        content_parts.extend([
            {"type": "text", "text": f"\nAttachment: {item['filename']}"},
            {"type": "image_url", "image_url": {"url": uri}},
        ])

    try:
        structured_vision = vision_llm.with_structured_output(BatchVisualAnalysisModel)
        result: BatchVisualAnalysisModel = await structured_vision.ainvoke([HumanMessage(content=content_parts)], config={"callbacks": []})
        v_map = {item.filename: item.description for item in result.analyses if item.description}
        for item in enriched:
            if item["filename"] in v_map:
                item["description"] = v_map[item["filename"]]
    except Exception as e:
        print(f"[Model-_enrich_attachments] Vision analysis skipped for {key}: {e}")

    return enriched
# endregion


# region Ticket Processor
async def process_ticket(ticket: dict[str, Any]) -> ModeledKnowledgeChunk | None:
    """Processes a single ticket through a multi-pass pipeline: Pass 1 (Value Filter) -> Media Enrichment -> Pass 2 (Deep Modeling)."""
    if not llm:
        return None

    key = ticket.get("key", "Unknown")
    summary = ticket.get("summary", "")
    valid_attachments = [a for a in ticket.get("attachments", []) if not is_archive(a)]

    raw_comments = "\n".join([f"[{c.get('author')}] {c.get('body')}" for c in ticket.get("comments", [])])
    cf_text = format_custom_fields(ticket.get("custom_fields", {}))
    raw_context = (
        f"Summary: {summary}\n"
        f"Description:\n{ticket.get('description', '')}\n"
        f"Custom Fields:\n{cf_text if cf_text else 'None'}\n"
        f"Comments:\n{raw_comments}"
    )

    # Pass 1: Lightweight Value & Relevance Filtering (Token & Cost Saving)
    try:
        filter_llm = llm.with_structured_output(TicketFilterModel)
        filter_result: TicketFilterModel = await filter_llm.ainvoke(raw_context)
    except Exception as e:
        print(f"[Model-process_ticket] Error in Pass 1 filtering for {key}: {e}")
        return None

    if not filter_result.has_valuable_information:
        print(f"[Model-process_ticket] Skipped {key}: Insufficient technical value (Pass 1).")
        return None

    # Pass 2: Media Enrichment & Deep Knowledge Extraction
    enriched_attachments = await _enrich_attachments(
        valid_attachments,
        ticket_context=raw_context,
        key=key,
        summary=summary,
    )

    cleaned_desc = clean_attachment_tags(ticket.get("description", ""), enriched_attachments)
    cleaned_comments = [
        dict(c, body=clean_attachment_tags(c.get("body", ""), enriched_attachments))
        for c in ticket.get("comments", [])
    ]
    enriched_comments_text = "\n".join([f"[{c.get('author')}] {c.get('body')}" for c in cleaned_comments])

    enriched_ticket_context = (
        f"Summary: {summary}\n"
        f"Description (with injected attachment descriptions):\n{cleaned_desc}\n"
        f"Custom Fields:\n{cf_text if cf_text else 'None'}\n"
        f"Comments:\n{enriched_comments_text}"
    )

    try:
        knowledge_llm = llm.with_structured_output(TicketKnowledgeModel)
        model: TicketKnowledgeModel = await knowledge_llm.ainvoke(enriched_ticket_context)
    except Exception as e:
        print(f"[Model-process_ticket] Error in Pass 2 modeling for {key}: {e}")
        return None

    chunk_str_id = f"jira-{key}"
    qdrant_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, chunk_str_id))

    metadata = KnowledgeMetadata(
        issue_key=key,
        url=ticket.get("url", ""),
        issuetype=ticket.get("issuetype", "Task"),
        summary=summary,
        has_valuable_information=True,
        rca=model.rca,
        resolution=model.resolution,
        llm_summary=model.llm_summary,
        description=cleaned_desc,
        status=ticket.get("status", "Unknown"),
        fix_versions=ticket.get("fix_versions", []),
        attachments=enriched_attachments,
        comments=cleaned_comments,
        created=ticket.get("created", ""),
    )

    print(f"[Model-process_ticket] Modeled [{metadata.issuetype}] {key} -> UUID {qdrant_uuid}")
    return ModeledKnowledgeChunk(
        id=qdrant_uuid,
        small=summary.strip(),
        metadata=metadata,
    )
# endregion


# region Main Execution
async def main() -> None:
    """Concurrently models all tickets from 1.jira_tickets.json."""
    if not INPUT_PATH.exists():
        print(f"[Model-main] Error: '{INPUT_PATH.name}' not found. Run 1.jira_tickets.py first.")
        return

    with open(INPUT_PATH, encoding="utf-8") as f:
        tickets = json.load(f)

    print(f"[Model-main] Processing {len(tickets)} tickets concurrently with Pydantic structured output...")
    tasks = [process_ticket(t) for t in tickets]
    results = await asyncio.gather(*tasks)

    chunks = [c.model_dump() for c in results if c is not None]
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"[Model-main] Saved {len(chunks)} valid modeled chunks to '{OUTPUT_PATH.name}'.")


if __name__ == "__main__":
    asyncio.run(main())
# endregion
