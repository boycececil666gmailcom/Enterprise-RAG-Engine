# region Imports
import json
import os
from pathlib import Path
from typing import Any

from atlassian import Jira
from dotenv import load_dotenv

# endregion

# region Configuration
_ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT_DIR / ".env")

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_JQL = os.getenv("JIRA_JQL", 'project = "VEL" AND text ~ "DMS" ORDER BY created DESC')
JIRA_MAX_RESULTS = int(os.getenv("JIRA_MAX_RESULTS", "5"))
OUTPUT_JSON_PATH = Path(__file__).resolve().parent / "1.jira_tickets.json"
# endregion

# region Data Parsing
def _text(node: Any) -> str:
    """Recursively converts ADF node or string into readable text, preserving media, links, and cards."""
    if isinstance(node, str):
        return node
    if not isinstance(node, dict):
        return ""

    node_type = node.get("type", "")
    attrs = node.get("attrs", {})
    content = node.get("content", [])

    if node_type == "text":
        txt = node.get("text", "")
        for m in node.get("marks", []):
            if m.get("type") == "link" and (href := m.get("attrs", {}).get("href")):
                txt = f"[{txt}]({href})"
        return txt

    if node_type == "hardBreak":
        return "\n"

    if node_type == "mention":
        return attrs.get("text") or f"@{attrs.get('id', 'user')}"

    if node_type == "media":
        media_name = attrs.get("alt") or attrs.get("id") or "file"
        return f"[Attachment: {media_name}]"

    if node_type in ("inlineCard", "blockCard"):
        return f"[Link: {attrs.get('url', '')}]"

    parts = [_text(c) for c in content]
    parts = [p for p in parts if p]

    if node_type in ("paragraph", "heading"):
        return " ".join(parts) + "\n"
    if node_type == "listItem":
        return "- " + " ".join(parts) + "\n"
    if node_type in ("bulletList", "orderedList", "doc"):
        return "\n".join(parts)

    return " ".join(parts).strip()


def _extract_ticket(issue: dict[str, Any], schema_map: dict[str, str]) -> dict[str, Any]:
    """Extracts core defect fields and dynamic custom fields."""
    f = issue.get("fields", {})
    std_keys = {
        "summary", "description", "status", "resolution", "priority",
        "components", "fixVersions", "versions", "labels", "created",
        "updated", "comment", "issuetype", "project", "reporter", "assignee",
        "attachment",
    }
    key = issue.get("key", "")
    ticket_url = f"{JIRA_BASE_URL}/browse/{key}" if JIRA_BASE_URL and key else ""
    return {
        "id": issue.get("id", ""),
        "key": key,
        "url": ticket_url,
        "issuetype": (f.get("issuetype") or {}).get("name", "Unknown"),
        "summary": f.get("summary", ""),
        "description": _text(f.get("description")),
        "status": (f.get("status") or {}).get("name", "Unknown"),
        "resolution": (f.get("resolution") or {}).get("name", "Unresolved"),
        "priority": (f.get("priority") or {}).get("name", "Normal"),
        "components": [c.get("name", "") for c in f.get("components", [])],
        "fix_versions": [v.get("name", "") for v in f.get("fixVersions", [])],
        "affects_versions": [v.get("name", "") for v in f.get("versions", [])],
        "labels": f.get("labels", []),
        "created": f.get("created", ""),
        "updated": f.get("updated", ""),
        "attachments": [
            {
                "filename": a.get("filename", ""),
                "url": a.get("content", ""),
                "size": a.get("size", 0),
                "mime_type": a.get("mimeType", ""),
            }
            for a in f.get("attachment", [])
        ],
        "comments": [
            {
                "author": (c.get("author") or {}).get("displayName", "Unknown"),
                "created": c.get("created", ""),
                "body": _text(c.get("body")),
            }
            for c in (f.get("comment") or {}).get("comments", [])
            if c.get("body")
        ],
        "custom_fields": {
            schema_map.get(k, k): v
            for k, v in f.items()
            if (k.startswith("customfield_") or k not in std_keys) and v not in (None, "", [], {})
        },
    }
# endregion

# region JIRA Fetcher
def fetch_jira_tickets() -> list[dict[str, Any]]:
    """Exports tickets from JIRA via atlassian-python-api with pagination."""
    if not JIRA_BASE_URL or not JIRA_API_TOKEN:
        raise ValueError("[JIRA-Export] Missing JIRA_BASE_URL or JIRA_API_TOKEN in .env")

    jira = Jira(
        url=JIRA_BASE_URL,
        username=JIRA_EMAIL if "atlassian.net" in JIRA_BASE_URL else None,
        password=JIRA_API_TOKEN,
        cloud="atlassian.net" in JIRA_BASE_URL,
    )

    schema_map = {f["id"]: f["name"] for f in (jira.get_all_fields() or []) if "id" in f and "name" in f}
    tickets: list[dict[str, Any]] = []
    start_at, page_size = 0, min(50, JIRA_MAX_RESULTS)

    print(f"[JIRA-Export] Querying: '{JIRA_JQL}' (Max: {JIRA_MAX_RESULTS})")
    while start_at < JIRA_MAX_RESULTS:
        data = jira.jql(jql=JIRA_JQL, start=start_at, limit=page_size, fields=["*all"])
        issues = data.get("issues", [])
        if not issues:
            break
        tickets.extend([_extract_ticket(issue, schema_map) for issue in issues])
        start_at += len(issues)
        if start_at >= data.get("total", len(tickets)) or len(tickets) >= JIRA_MAX_RESULTS:
            break

    return tickets
# endregion

# region Main Execution
def main() -> None:
    """Exports JIRA tickets and saves to 1.jira_tickets.json."""
    tickets = fetch_jira_tickets()
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)
    print(f"[JIRA-Export] Saved {len(tickets)} tickets to '{OUTPUT_JSON_PATH.name}'.")


if __name__ == "__main__":
    main()
# endregion
