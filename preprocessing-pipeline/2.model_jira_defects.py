# region Imports
import asyncio
import json
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from llm_client import llm, vision_llm

# endregion

# region Configuration
_DIR = Path(__file__).resolve().parent
INPUT_PATH = _DIR / "1.jira_tickets.json"
OUTPUT_PATH = _DIR / "2.jira_modeled_chunks.json"
# endregion

# region Pydantic Schemas
class DefectKnowledgeModel(BaseModel):
    """Enforced schema for defect knowledge extraction, RCA modeling, and feature technical summaries."""
    has_valuable_information: bool = Field(
        description="Set to true if the ticket contains actionable technical knowledge (RCA, bug fix, feature implementation, or configuration details). Set to false ONLY if it is an empty placeholder, duplicate, or devoid of technical content.",
    )
    rca: str = Field(
        default="", description="Root cause analysis if identified, or concise technical context / requirement background if not a formal RCA"
    )
    resolution_pattern: str = Field(
        default="", description="Technical description of the fix applied, code changes, or feature implementation logic"
    )

    search_keywords: list[str] = Field(
        default_factory=list, description="High-relevance technical search keywords (modules, components, symptoms, technologies)"
    )


class DefectChunkMetadata(DefectKnowledgeModel):
    """Structured metadata payload inheriting LLM analysis and vector filtering fields."""
    big: str = Field(default="", description="Full markdown card for parent context")
    issue_key: str
    url: str = ""
    summary: str
    priority: str = "Normal"
    status: str = "Unknown"
    resolution: str = "Fixed"
    components: list[str] = Field(default_factory=list)
    fix_versions: list[str] = Field(default_factory=list)
    visual_symptom: str = ""
    attachments: list[dict[str, Any]] = Field(default_factory=list)
    created: str = ""


class ModeledDefectChunk(BaseModel):
    """Parent-child Small-to-Big defect chunk."""
    id: str
    small: str
    metadata: DefectChunkMetadata
# endregion

# region Ticket Processor
async def _extract_visual_symptom(attachments: list[dict[str, Any]]) -> str:
    """Extracts visual defect description from image/video attachments using Gemini."""
    media = [a for a in attachments if any(t in a.get("mime_type", "") for t in ["image", "video"])]
    if not vision_llm or not media:
        return ""
    try:
        msg = HumanMessage(
            content=[
                {"type": "text", "text": f"Attachment: {media[0].get('filename')}. Describe the visual bug/glitch in 1-2 sentences."},
                {"type": "image_url", "image_url": {"url": media[0].get("url", "")}},
            ]
        )
        res = await vision_llm.ainvoke([msg])
        return res.content.strip()
    except Exception:
        return ""


async def process_ticket(ticket: dict[str, Any]) -> ModeledDefectChunk | None:
    """Processes a single ticket from raw data to modeled Small-to-Big chunk."""
    key = ticket.get("key", "Unknown")
    summary = ticket.get("summary", "")
    ticket_url = ticket.get("url", "")

    # 1. Build text context
    comments = "\n".join([f"[{c.get('author')}] {c.get('body')}" for c in ticket.get("comments", [])])
    text = f"Key: {key}\nSummary: {summary}\nStatus: {ticket.get('status')}\nDescription:\n{ticket.get('description', '')}\nComments:\n{comments}"

    # 2. Stage 1: Text Knowledge Analysis with Pydantic Structured Output
    if not llm:
        return None

    try:
        structured_llm = llm.with_structured_output(DefectKnowledgeModel)
        model: DefectKnowledgeModel = await structured_llm.ainvoke([
            SystemMessage(
                content=(
                    "You are an expert Software Knowledge & Defect Analysis AI. Analyze this JIRA ticket and extract structured technical knowledge. "
                    "Extract RCA if available, or technical context / problem summary if it is a simple fix or feature implementation. "
                    "Extract resolution details, code changes, or implementation logic. "
                    "Retain all tickets with useful technical value. Only set has_valuable_information to false if the ticket is an empty placeholder, duplicate without content, or devoid of useful information."
                )
            ),
            HumanMessage(content=text),
        ])
    except Exception as e:
        print(f"[Model-process_ticket] Error analyzing {key}: {e}")
        return None

    # Gatekeeper: Drop ticket only if it lacks meaningful technical value
    if not model.has_valuable_information:
        print(f"[Model-process_ticket] Skipped {key}: Insufficient technical value.")
        return None

    # 3. Stage 2: Multimodal analysis if visual media exists (Gemini 3.7 Flash)
    visual_symptom = await _extract_visual_symptom(ticket.get("attachments", []))

    # 4. Build Small chunk (pure search token) and Big card (full markdown)
    keywords = model.search_keywords
    small_lines = [f"Summary: {summary}"]
    if keywords:
        small_lines.append(f"Keywords: {', '.join(keywords)}")
    if visual_symptom:
        small_lines.append(f"Visual Symptom: {visual_symptom}")
    if model.rca:
        small_lines.append(f"RCA / Context: {model.rca}")
    if model.resolution_pattern:
        small_lines.append(f"Resolution / Fix: {model.resolution_pattern}")

    attachments_md = "\n".join([f"- [{a.get('filename')}]({a.get('url')})" for a in ticket.get("attachments", [])]) or "None"
    visual_section = f"## Visual Anomaly (Multimodal AI Analysis)\n{visual_symptom}\n\n" if visual_symptom else ""
    rca_section = f"## 2. Root Cause / Technical Context\n{model.rca}\n\n" if model.rca else ""
    res_section = f"## 3. Resolution / Implementation Details\n{model.resolution_pattern}\n\n" if model.resolution_pattern else ""

    big_markdown = (
        f"# Case: [{key}]({ticket_url}) - {summary}\n\n"
        f"- **JIRA Link**: {ticket_url or 'N/A'}\n"
        f"- **Component**: {', '.join(ticket.get('components', [])) or 'Unspecified'}\n"
        f"- **Priority**: {ticket.get('priority', 'Normal')} | **Status**: {ticket.get('status', 'Unknown')} | **Resolution**: {ticket.get('resolution', 'Fixed')}\n"
        f"- **Fix Version**: {', '.join(ticket.get('fix_versions', [])) or 'Unspecified'}\n\n"
        f"## 1. Description & Requirements\n"
        f"{ticket.get('description', '')}\n\n"
        f"{visual_section}"
        f"{rca_section}"
        f"{res_section}"
        f"## 4. Attachments\n"
        f"{attachments_md}\n"
    )

    metadata = DefectChunkMetadata(
        **model.model_dump(),
        big=big_markdown,
        issue_key=key,
        url=ticket_url,
        summary=summary,
        priority=ticket.get("priority", "Normal"),
        status=ticket.get("status", "Unknown"),
        resolution=ticket.get("resolution", "Fixed"),
        components=ticket.get("components", []),
        fix_versions=ticket.get("fix_versions", []),
        visual_symptom=visual_symptom,
        attachments=ticket.get("attachments", []),
        created=ticket.get("created", ""),
    )

    print(f"[Model-process_ticket] Modeled {key}")
    return ModeledDefectChunk(
        id=f"jira-{key}",
        small="\n".join(small_lines),
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
