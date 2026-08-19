# region Imports
import json
import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

# endregion

# region Configuration
_CURRENT_DIR = Path(__file__).resolve().parent
_ROOT_DIR = _CURRENT_DIR.parent
load_dotenv(dotenv_path=_ROOT_DIR / ".env")

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "").rstrip("/")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "")
JIRA_JQL = os.getenv("JIRA_JQL", "issuetype = Bug ORDER BY created DESC")
JIRA_MAX_RESULTS = int(os.getenv("JIRA_MAX_RESULTS", "100"))
OUTPUT_JSON_PATH = _CURRENT_DIR / "1.jira_tickets.json"
# endregion

# region JIRA Fetcher
def _get_auth_headers() -> dict[str, str]:
    """Builds authorization header from environment credentials."""
    if JIRA_API_TOKEN and not JIRA_EMAIL:
        # Bearer PAT token
        return {
            "Authorization": f"Bearer {JIRA_API_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def _extract_ticket_data(issue: dict[str, Any]) -> dict[str, Any]:
    """Extracts structured defect fields from a raw JIRA issue object."""
    fields = issue.get("fields", {})

    # Extract comments
    comment_entries = fields.get("comment", {}).get("comments", [])
    comments = [
        {
            "author": (
                c.get("author", {}).get("displayName")
                or c.get("author", {}).get("name", "Unknown")
            ),
            "created": c.get("created", ""),
            "body": c.get("body", ""),
        }
        for c in comment_entries
        if c.get("body")
    ]

    # Extract components & versions
    components = [c.get("name", "") for c in fields.get("components", [])]
    fix_versions = [v.get("name", "") for v in fields.get("fixVersions", [])]
    affects_versions = [v.get("name", "") for v in fields.get("versions", [])]

    # Extract description
    raw_desc = fields.get("description") or ""
    description = raw_desc if isinstance(raw_desc, str) else json.dumps(raw_desc, ensure_ascii=False)

    return {
        "id": issue.get("id", ""),
        "key": issue.get("key", ""),
        "summary": fields.get("summary", ""),
        "description": description,
        "status": fields.get("status", {}).get("name", "Unknown"),
        "resolution": (fields.get("resolution") or {}).get("name", "Unresolved"),
        "priority": (fields.get("priority") or {}).get("name", "Normal"),
        "components": components,
        "fix_versions": fix_versions,
        "affects_versions": affects_versions,
        "labels": fields.get("labels", []),
        "created": fields.get("created", ""),
        "updated": fields.get("updated", ""),
        "comments": comments,
    }


def fetch_jira_tickets(
    base_url: str = JIRA_BASE_URL,
    jql: str = JIRA_JQL,
    max_results: int = JIRA_MAX_RESULTS,
) -> list[dict[str, Any]]:
    """Exports tickets from JIRA REST API with pagination."""
    if not base_url:
        print("[JIRA-Export] JIRA_BASE_URL not configured in .env. Generating mock dataset for demonstration.")
        return generate_mock_jira_tickets()

    headers = _get_auth_headers()
    auth = (JIRA_EMAIL, JIRA_API_TOKEN) if (JIRA_EMAIL and JIRA_API_TOKEN) else None

    endpoint = f"{base_url}/rest/api/2/search"
    tickets: list[dict[str, Any]] = []
    start_at = 0
    page_size = min(50, max_results)

    print(f"[JIRA-Export] Querying JIRA API at {base_url} with JQL: '{jql}'")

    while start_at < max_results:
        params = {
            "jql": jql,
            "startAt": start_at,
            "maxResults": page_size,
            "fields": [
                "summary",
                "description",
                "status",
                "resolution",
                "priority",
                "components",
                "fixVersions",
                "versions",
                "labels",
                "created",
                "updated",
                "comment",
            ],
        }

        resp = requests.get(endpoint, headers=headers, auth=auth, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        issues = data.get("issues", [])
        if not issues:
            break

        for issue in issues:
            tickets.append(_extract_ticket_data(issue))

        start_at += len(issues)
        total = data.get("total", len(tickets))
        print(f"[JIRA-Export] Fetched {len(tickets)}/{total} issues...")
        if start_at >= total or len(tickets) >= max_results:
            break

    return tickets
# endregion

# region Mock Dataset
def generate_mock_jira_tickets() -> list[dict[str, Any]]:
    """Provides representative mock JIRA defect data for initial offline testing."""
    return [
        {
            "id": "10001",
            "key": "KANZI-4128",
            "summary": "Memory leak in Node2D RenderBatch when switching between dynamic pages",
            "description": "When navigating between MainMenu and SettingsScreen, memory usage increases continuously by ~12MB per navigation cycle. Observed on Android QNX target.\n\nStack Trace:\nRenderBatch::allocateBuffers() at node2d_batch.cpp:142\nPageHost::switchPage() at page_host.cpp:88",
            "status": "Closed",
            "resolution": "Fixed",
            "priority": "Critical",
            "components": ["Graphics", "PageHost"],
            "fix_versions": ["4.1.2"],
            "affects_versions": ["4.1.0"],
            "labels": ["memory-leak", "render-pipeline", "horizontal-risk"],
            "created": "2026-06-15T09:30:00.000Z",
            "updated": "2026-06-18T16:45:00.000Z",
            "comments": [
                {
                    "author": "Tanaka Kenji",
                    "created": "2026-06-16T11:00:00.000Z",
                    "body": "Root cause: RenderBatch vertex buffer pool was not recycled during page exit. Needs horizontal check on 3D Viewport batching as well.",
                },
                {
                    "author": "Boyce Chen",
                    "created": "2026-06-17T14:20:00.000Z",
                    "body": "Fixed in commit c4f89a1 by implementing RAII buffer handle and explicit release in Node2D destructor.",
                },
            ],
        },
        {
            "id": "10002",
            "key": "KANZI-4155",
            "summary": "Property binding desynchronization when Slider value updated from background thread",
            "description": "Slider2D thumb position jumps back to 0 when property is dispatched asynchronously from CAN-bus worker thread.\n\nLog:\n[PropertySystem] Warning: Write to property 'Value' from non-UI thread [ThreadID: 0x7f88] without Dispatcher lock.",
            "status": "Resolved",
            "resolution": "Fixed",
            "priority": "Major",
            "components": ["PropertySystem", "Controls"],
            "fix_versions": ["4.1.2"],
            "affects_versions": ["4.1.0", "4.1.1"],
            "labels": ["concurrency", "property-system", "thread-safety"],
            "created": "2026-06-20T14:10:00.000Z",
            "updated": "2026-06-22T10:15:00.000Z",
            "comments": [
                {
                    "author": "Sato Hiroshi",
                    "created": "2026-06-21T09:30:00.000Z",
                    "body": "Properties bound to UI controls must route updates through `TaskDispatcher::post()`. Horizontal check required for ProgressBar and ToggleButton.",
                }
            ],
        },
        {
            "id": "10003",
            "key": "KANZI-4201",
            "summary": "Null pointer crash in TextBlock2D font fallback when rendering missing Japanese glyphs",
            "description": "Application crashes with SIGSEGV when displaying string containing uncommon Kanji characters.\n\nCrash Log:\nSIGSEGV at FontManager::getFallbackGlyph(unsigned int codepoint) at font_manager.cpp:215\nTextBlock2D::layoutText() at text_block_2d.cpp:310",
            "status": "Closed",
            "resolution": "Fixed",
            "priority": "Blocker",
            "components": ["TextEngine", "FontManager"],
            "fix_versions": ["4.1.3"],
            "affects_versions": ["4.1.0", "4.1.1", "4.1.2"],
            "labels": ["crash", "font", "i18n", "null-pointer"],
            "created": "2026-07-02T13:00:00.000Z",
            "updated": "2026-07-05T17:30:00.000Z",
            "comments": [
                {
                    "author": "Boyce Chen",
                    "created": "2026-07-03T15:40:00.000Z",
                    "body": "Font fallback chain returned nullptr when secondary font lacked glyph. Added default 'missing glyph' placeholder box and null-check.",
                }
            ],
        },
    ]
# endregion

# region Main Execution
def main() -> None:
    """Exports JIRA tickets and saves to 1.jira_tickets.json."""
    tickets = fetch_jira_tickets()
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)

    print(f"[JIRA-Export] Successfully saved {len(tickets)} tickets to '{OUTPUT_JSON_PATH.name}'.")


if __name__ == "__main__":
    main()
# endregion
