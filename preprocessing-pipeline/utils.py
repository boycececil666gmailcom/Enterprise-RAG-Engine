# region Imports
import base64
import re
from typing import Any
import httpx
# endregion


# region Media Utilities
def is_archive(a: dict[str, Any]) -> bool:
    """Checks whether an attachment is an archive file (zip, tar, gz, 7z, rar, etc.)."""
    filename = a.get("filename", "").lower()
    mime = a.get("mime_type", "").lower()
    archive_exts = (".zip", ".tar", ".gz", ".tgz", ".7z", ".rar", ".bz2", ".xz")
    archive_mimes = (
        "application/zip",
        "application/x-zip-compressed",
        "application/x-tar",
        "application/gzip",
        "application/x-7z-compressed",
        "application/x-rar-compressed",
        "application/x-bzip2",
    )
    return filename.endswith(archive_exts) or any(m in mime for m in archive_mimes)


async def fetch_media_data_uri(
    client: httpx.AsyncClient,
    a: dict[str, Any],
    auth: tuple[str, str] | None = None,
) -> str | None:
    """Fetches static image attachment with authentication and returns base64 Data URI."""
    url = a.get("url", "")
    mime = a.get("mime_type", "")
    size = a.get("size", 0)
    if not url or not mime.startswith("image/") or size > 3 * 1024 * 1024:
        return None
    try:
        res = await client.get(url, auth=auth, follow_redirects=True, timeout=15.0)
        if res.status_code == 200:
            b64 = base64.b64encode(res.content).decode("utf-8")
            return f"data:{mime};base64,{b64}"
    except Exception:
        pass
    return None


def clean_attachment_tags(text: str, valid_attachments: list[dict[str, Any]]) -> str:
    """Inlines attachment descriptions into [Attachment: filename] tags and removes skipped/unmapped references."""
    valid_map = {a.get("filename"): a.get("description", "") for a in valid_attachments if a.get("filename")}

    def _replace_att(match: re.Match) -> str:
        name = match.group(1).strip()
        if name in valid_map:
            desc = valid_map[name]
            return f"[Attachment: {name} | Description: {desc}]" if desc else f"[Attachment: {name}]"
        return ""

    cleaned = re.sub(r"\[Attachment:\s*([^\]]+)\]", _replace_att, text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()
# endregion


# region Custom Fields
def _adf_to_text(node: Any) -> str:
    """Recursively converts ADF nodes into plain text."""
    if isinstance(node, str):
        return node
    if not isinstance(node, dict):
        return ""
    if node.get("type") == "text":
        return node.get("text", "")
    content = node.get("content", [])
    parts = [_adf_to_text(c) for c in content if c]
    return " ".join(p for p in parts if p).strip()


def extract_node_text(val: Any) -> str:
    """Extracts human-readable text from ADF doc dict, option dict, or primitive."""
    if val is None:
        return ""
    if isinstance(val, str):
        return val.strip()
    if isinstance(val, (int, float, bool)):
        return str(val)
    if isinstance(val, list):
        items = [extract_node_text(x) for x in val]
        return ", ".join(x for x in items if x)
    if isinstance(val, dict):
        if "value" in val and isinstance(val["value"], str):
            return val["value"]
        if "name" in val and isinstance(val["name"], str):
            return val["name"]
        if "type" in val and "content" in val:
            return _adf_to_text(val)
        if "fields" in val and isinstance(val["fields"], dict):
            return str(val["fields"].get("summary", ""))
    return ""


def format_custom_fields(custom_fields: dict[str, Any]) -> str:
    """Extracts and formats valuable custom fields like Root cause, Solution, Self Test Report, and Component."""
    ignored = {
        "Status Category Changed", "Status Category", "Watchers",
        "Work Ratio", "Restrict to", "Rank", "Last Viewed", "Development",
    }
    lines = []
    for k, v in custom_fields.items():
        if k in ignored:
            continue
        text_val = extract_node_text(v)
        if text_val and text_val not in ("-", "None", "null", "{}"):
            lines.append(f"{k}: {text_val}")
    return "\n".join(lines)
# endregion
