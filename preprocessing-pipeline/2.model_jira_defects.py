# region Imports
import json
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from llm_client import llm

# endregion

# region Configuration
_CURRENT_DIR = Path(__file__).resolve().parent
INPUT_TICKETS_PATH = _CURRENT_DIR / "1.jira_tickets.json"
OUTPUT_MODELED_PATH = _CURRENT_DIR / "2.jira_modeled_chunks.json"
# endregion

# region Modeling Prompt
SYSTEM_PROMPT = """You are an expert Enterprise Software Defect Analysis & Quality Assurance AI.
Your task is to analyze historical JIRA defect tickets and transform each ticket into a structured Defect Knowledge Model.

Analyze the given ticket's Summary, Description, and Discussion/Resolution Comments, then output a valid JSON object matching this exact schema:

{
  "rca_category": "One of: Memory Management | Thread Safety / Concurrency | Null Pointer / Boundary Check | State Machine / Lifecycle | Rendering / Pipeline | Resource Leak | API Protocol Mismatch | Configuration / Build | Logic Flaw",
  "error_signatures": ["list of exact function names, source files, exception names, error codes, and log patterns"],
  "root_cause_explanation": "Precise, 2-3 sentence technical explanation of the defect's root cause.",
  "resolution_pattern": "Specific technical explanation of the fix applied and code logic changes.",
  "horizontal_expansion_scope": {
    "affected_components": ["list of sister modules or submodules sharing similar risk"],
    "inspection_checklist": ["step-by-step checklist for developers doing horizontal inspection (横展)"]
  },
  "search_keywords": ["list of high-relevance search keywords and technical terms"]
}

Ensure your output is strictly valid JSON with no conversational text or markdown code fences."""
# endregion

# region Transformation Logic
def _model_single_ticket(ticket: dict[str, Any]) -> dict[str, Any]:
    """Uses LLM to model defect root-cause, error signatures, and horizontal expansion."""
    ticket_text = f"""Ticket Key: {ticket.get('key')}
Summary: {ticket.get('summary')}
Status: {ticket.get('status')} | Priority: {ticket.get('priority')} | Resolution: {ticket.get('resolution')}
Components: {', '.join(ticket.get('components', []))}
Fix Versions: {', '.join(ticket.get('fix_versions', []))}

Description:
{ticket.get('description', '')}

Discussion & Resolution Comments:
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

    rca = "Logic Flaw"
    if any(k in summary.lower() or k in desc.lower() for k in ["memory", "leak", "buffer"]):
        rca = "Memory Management"
    elif any(k in summary.lower() or k in desc.lower() for k in ["thread", "async", "lock", "concurrency"]):
        rca = "Thread Safety / Concurrency"
    elif any(k in summary.lower() or k in desc.lower() for k in ["null", "crash", "segv", "nullptr"]):
        rca = "Null Pointer / Boundary Check"

    signatures = []
    for line in desc.split("\n"):
        if any(token in line for token in ["::", "at ", "Warning:", "Error:", "SIGSEGV", "0x"]):
            signatures.append(line.strip())

    return {
        "rca_category": rca,
        "error_signatures": signatures or labels,
        "root_cause_explanation": f"Defect in {', '.join(ticket.get('components', ['core']))} related to: {summary}.",
        "resolution_pattern": "Applied boundary checks and state synchronization.",
        "horizontal_expansion_scope": {
            "affected_components": ticket.get("components", []),
            "inspection_checklist": [
                "Audit sister modules with similar lifecycle management.",
                "Verify thread safety and resource cleanup in corresponding destructors.",
            ],
        },
        "search_keywords": labels + ticket.get("components", []),
    }


def _build_small_to_big_chunk(ticket: dict[str, Any], model_data: dict[str, Any]) -> dict[str, Any]:
    """Constructs decoupled Small-to-Big chunk optimized for Qdrant Hybrid Search & LLM Context."""
    key = ticket.get("key", "JIRA-UNKNOWN")
    summary = ticket.get("summary", "")
    components = ticket.get("components", [])
    rca = model_data.get("rca_category", "Defect")
    signatures = " | ".join(model_data.get("error_signatures", []))
    keywords = ", ".join(model_data.get("search_keywords", []))

    # 1. Small chunk: Dense & BM25 sparse matching token
    small_chunk = (
        f"Issue: {key} - {summary}\n"
        f"Components: {', '.join(components)}\n"
        f"RCA Category: {rca}\n"
        f"Error Signatures: {signatures}\n"
        f"Keywords: {keywords}\n"
        f"Root Cause: {model_data.get('root_cause_explanation', '')}"
    )

    # 2. Big Markdown card: Full LLM context delivery
    checklist_md = "\n".join(
        [f"- [ ] {item}" for item in model_data.get("horizontal_expansion_scope", {}).get("inspection_checklist", [])]
    )
    big_markdown = f"""# Defect Case: {key} - {summary}

- **Component**: {', '.join(components)}
- **Priority**: {ticket.get('priority')} | **Status**: {ticket.get('status')} | **Resolution**: {ticket.get('resolution')}
- **Fix Version**: {', '.join(ticket.get('fix_versions', []))} | **RCA Category**: {rca}

## 1. Defect Symptom & Description
{ticket.get('description', '')}

## 2. Root Cause Analysis (RCA)
{model_data.get('root_cause_explanation', '')}

## 3. Resolution & Code Fix Pattern
{model_data.get('resolution_pattern', '')}

## 4. Horizontal Expansion & Prevention Scope (横展指导)
* **Affected Sister Components**: {', '.join(model_data.get('horizontal_expansion_scope', {}).get('affected_components', []))}
* **Horizontal Inspection Checklist**:
{checklist_md}
"""

    return {
        "id": f"jira-{key}",
        "small": small_chunk,
        "metadata": {
            "big": big_markdown,
            "issue_key": key,
            "summary": summary,
            "priority": ticket.get("priority", "Normal"),
            "status": ticket.get("status", "Unknown"),
            "resolution": ticket.get("resolution", "Fixed"),
            "components": components,
            "fix_versions": ticket.get("fix_versions", []),
            "rca_category": rca,
            "error_signatures": model_data.get("error_signatures", []),
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

    for idx, ticket in enumerate(tickets, start=1):
        key = ticket.get("key", f"Ticket-{idx}")
        print(f"[Model-Defects] ({idx}/{len(tickets)}) Modeling ticket {key}...")
        model_data = _model_single_ticket(ticket)
        chunk = _build_small_to_big_chunk(ticket, model_data)
        modeled_chunks.append(chunk)

    with open(OUTPUT_MODELED_PATH, "w", encoding="utf-8") as f:
        json.dump(modeled_chunks, f, ensure_ascii=False, indent=2)

    print(f"[Model-Defects] Successfully generated {len(modeled_chunks)} modeled chunks to '{OUTPUT_MODELED_PATH.name}'.")


if __name__ == "__main__":
    process_all_tickets()
# endregion
