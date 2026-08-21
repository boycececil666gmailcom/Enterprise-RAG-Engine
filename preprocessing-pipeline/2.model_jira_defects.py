# region Imports
import json
import os
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from llm_client import llm, vision_llm

# endregion

# region Configuration
_CURRENT_DIR = Path(__file__).resolve().parent
INPUT_TICKETS_PATH = _CURRENT_DIR / "1.jira_tickets.json"
OUTPUT_MODELED_PATH = _CURRENT_DIR / "2.jira_modeled_chunks.json"
# endregion

# region Modeling Prompt
SYSTEM_PROMPT = """You are an expert Enterprise Software Defect Analysis & Quality Assurance AI.
Your task is to analyze historical JIRA defect tickets and transform each ticket into a structured Defect Knowledge Model.

First, evaluate if the ticket contains sufficient, actionable Root Cause Analysis (RCA) or technical resolution details. If the ticket is merely an uninvestigated bug report, a vague placeholder, or an unresolved discussion with no technical root cause, set `has_sufficient_rca` to false.

Output a valid JSON object matching this exact schema:

{
  "has_sufficient_rca": true,
  "rca_category": "One of: Memory Management | Thread Safety / Concurrency | Null Pointer / Boundary Check | State Machine / Lifecycle | Rendering / Pipeline | Resource Leak | Configuration / Build | Logic Flaw",
  "rca": "Precise, 2-3 sentence technical explanation of the defect's root cause.",
  "resolution_pattern": "Specific technical explanation of the fix applied and code logic changes.",
  "horizontal_expansion_scope": {
    "affected_components": ["list of sister modules or submodules sharing similar risk"],
    "inspection_checklist": ["step-by-step checklist for developers doing horizontal inspection (横展)"]
  },
  "search_keywords": ["list of high-relevance search keywords and technical terms"]
}

Ensure your output is strictly valid JSON with no conversational text or markdown code fences."""
# endregion

# region Multimodal Analysis
def _extract_visual_symptom(attachments: list[dict[str, Any]]) -> str:
    """Uses Gemini Flash (vision_llm) to extract visual defect symptoms from video/image attachments."""
    if not vision_llm or not attachments:
        return ""

    visual_media = [
        a for a in attachments
        if any(t in a.get("mime_type", "") for t in ["image", "video"])
    ]
    if not visual_media:
        return ""

    target = visual_media[0]
    prompt_text = (
        f"Attachment file: {target.get('filename')}. "
        "Describe the visual UI anomaly, defect behavior, or animation glitch in 1-2 concise sentences."
    )
    try:
        msg = HumanMessage(
            content=[
                {"type": "text", "text": prompt_text},
                {"type": "image_url", "image_url": {"url": target.get("url", "")}},
            ]
        )
        res = vision_llm.invoke([msg])
        return res.content.strip()
    except Exception as e:
        print(f"[Model-Defects] Vision analysis skipped for {target.get('filename')} ({e})")
        return ""
# endregion

# region Transformation Logic
def _model_single_ticket(ticket: dict[str, Any]) -> dict[str, Any]:
    """Uses LLM to model defect root-cause and horizontal expansion."""
    ticket_text = f"""Ticket Key: {ticket.get('key')}
Summary: {ticket.get('summary')}
Status: {ticket.get('status')} | Priority: {ticket.get('priority')} | Resolution: {ticket.get('resolution')}
Components: {', '.join(ticket.get('components', []))}
Fix Versions: {', '.join(ticket.get('fix_versions', []))}

Description:
{ticket.get('description', '')}

Discussion & Comments:
"""
    for c in ticket.get("comments", []):
        ticket_text += f"[{c.get('author')}] {c.get('body')}\n"

    if not llm:
        print(f"[Model-Defects] LLM not initialized. Using fallback heuristic modeling for {ticket.get('key')}.")
        return _fallback_heuristic_model(ticket)

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Please model this JIRA defect ticket:\n\n{ticket_text}"),
    ]

    try:
        response = llm.invoke(messages)
        content = response.content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        return json.loads(content.strip())
    except Exception as e:
        print(f"[Model-Defects] Error modeling {ticket.get('key')} via LLM ({e}). Using heuristic fallback.")
        return _fallback_heuristic_model(ticket)


def _fallback_heuristic_model(ticket: dict[str, Any]) -> dict[str, Any]:
    """Generates structured defect metadata when running offline without LLM API."""
    summary = ticket.get("summary", "")
    desc = ticket.get("description", "")
    labels = ticket.get("labels", [])

    if len(desc.strip()) < 30:
        return {"has_sufficient_rca": False}

    rca_cat = "Logic Flaw"
    if any(k in summary.lower() or k in desc.lower() for k in ["memory", "leak", "buffer"]):
        rca_cat = "Memory Management"
    elif any(k in summary.lower() or k in desc.lower() for k in ["thread", "async", "lock", "concurrency"]):
        rca_cat = "Thread Safety / Concurrency"
    elif any(k in summary.lower() or k in desc.lower() for k in ["null", "crash", "segv", "nullptr"]):
        rca_cat = "Null Pointer / Boundary Check"

    return {
        "has_sufficient_rca": True,
        "rca_category": rca_cat,
        "rca": f"Defect in {', '.join(ticket.get('components', ['core']))} related to: {summary}.",
        "resolution_pattern": "Applied state synchronization, boundary checks, and logic validation.",
        "horizontal_expansion_scope": {
            "affected_components": ticket.get("components", []),
            "inspection_checklist": [
                "Audit sister modules sharing similar lifecycle and data flow.",
                "Verify state consistency and resource cleanup in corresponding destructors.",
            ],
        },
        "search_keywords": labels + ticket.get("components", []),
    }


def _build_small_to_big_chunk(ticket: dict[str, Any], model_data: dict[str, Any], visual_symptom: str = "") -> dict[str, Any]:
    """Constructs decoupled Small-to-Big chunk optimized for Qdrant Hybrid Search & LLM Context."""
    key = ticket.get("key", "JIRA-UNKNOWN")
    summary = ticket.get("summary", "")
    components = ticket.get("components", [])
    rca_cat = model_data.get("rca_category", "")
    rca_text = model_data.get("rca", "")

    keywords_list = []
    if rca_cat:
        keywords_list.append(rca_cat)
    keywords_list.extend(model_data.get("search_keywords", []))

    # 1. Small chunk: Dense & BM25 sparse matching token (pure semantic content)
    small_parts = [f"Summary: {summary}"]
    if keywords_list:
        small_parts.append(f"Keywords: {', '.join(keywords_list)}")
    if visual_symptom:
        small_parts.append(f"Visual Symptom: {visual_symptom}")
    if rca_text:
        small_parts.append(f"RCA: {rca_text}")

    small_chunk = "\n".join(small_parts)

    # 2. Attachments Markdown list
    attachments_md = "\n".join(
        [f"- [{a.get('filename')}]({a.get('url')})" for a in ticket.get("attachments", [])]
    ) or "None"

    # 3. Big Markdown card: Full LLM context delivery
    checklist_md = "\n".join(
        [f"- [ ] {item}" for item in model_data.get("horizontal_expansion_scope", {}).get("inspection_checklist", [])]
    )
    ticket_url = ticket.get("url", "")
    big_markdown = f"""# Defect Case: [{key}]({ticket_url}) - {summary}

- **JIRA Link**: {ticket_url if ticket_url else 'N/A'}
- **Component**: {', '.join(components) if components else 'Unspecified'}
- **Priority**: {ticket.get('priority')} | **Status**: {ticket.get('status')} | **Resolution**: {ticket.get('resolution')}
- **Fix Version**: {', '.join(ticket.get('fix_versions', []))} | **RCA Category**: {rca_cat}

## 1. Defect Symptom & Description
{ticket.get('description', '')}

{f"## Visual Anomaly (Multimodal AI Analysis)\n{visual_symptom}\n" if visual_symptom else ""}
## 2. RCA (Root Cause Analysis)
{rca_text}

## 3. Resolution & Code Fix Pattern
{model_data.get('resolution_pattern', '')}

## 4. Horizontal Expansion & Prevention Scope (横展指导)
* **Affected Sister Components**: {', '.join(model_data.get('horizontal_expansion_scope', {}).get('affected_components', []))}
* **Horizontal Inspection Checklist**:
{checklist_md}

## 5. Attachments
{attachments_md}
"""

    return {
        "id": f"jira-{key}",
        "small": small_chunk,
        "metadata": {
            "big": big_markdown,
            "issue_key": key,
            "url": ticket_url,
            "summary": summary,
            "priority": ticket.get("priority", "Normal"),
            "status": ticket.get("status", "Unknown"),
            "resolution": ticket.get("resolution", "Fixed"),
            "components": components,
            "fix_versions": ticket.get("fix_versions", []),
            "rca_category": rca_cat,
            "rca": rca_text,
            "visual_symptom": visual_symptom,
            "attachments": ticket.get("attachments", []),
            "created": ticket.get("created", ""),
        },
    }
# endregion

# region Main Pipeline
def process_all_tickets() -> None:
    """Processes JIRA tickets and generates structured 2.jira_modeled_chunks.json."""
    if not INPUT_TICKETS_PATH.exists():
        raise FileNotFoundError(
            f"Input file '{INPUT_TICKETS_PATH.name}' not found. Run 1.export_jira_tickets.py first."
        )

    with open(INPUT_TICKETS_PATH, encoding="utf-8") as f:
        tickets = json.load(f)

    print(f"[Model-Defects] Modeling {len(tickets)} JIRA tickets with AI defect extraction...")
    modeled_chunks = []
    skipped_count = 0

    for idx, ticket in enumerate(tickets, start=1):
        key = ticket.get("key", f"Ticket-{idx}")
        print(f"[Model-Defects] ({idx}/{len(tickets)}) Modeling ticket {key}...")
        model_data = _model_single_ticket(ticket)

        if not model_data.get("has_sufficient_rca", True):
            print(f"[Model-Defects] Skipped {key}: Insufficient or uninvestigated RCA information.")
            skipped_count += 1
            continue

        visual_symptom = _extract_visual_symptom(ticket.get("attachments", []))
        chunk = _build_small_to_big_chunk(ticket, model_data, visual_symptom=visual_symptom)
        modeled_chunks.append(chunk)

    with open(OUTPUT_MODELED_PATH, "w", encoding="utf-8") as f:
        json.dump(modeled_chunks, f, ensure_ascii=False, indent=2)

    print(
        f"[Model-Defects] Finished! Saved {len(modeled_chunks)} valid chunks (Skipped {skipped_count} low-info tickets) to '{OUTPUT_MODELED_PATH.name}'."
    )


if __name__ == "__main__":
    process_all_tickets()
# endregion
