"""
Kanzi Docs Markdown Cleaner  v3 — RAG/VDB Optimized
Cleans all .md files in kanzi_docs/ for ingestion into a vector database.

Cleaning pipeline (in order):
  [1]  Strip Â¶ (Sphinx paragraph-anchor mojibake)
  [2]  Clean frontmatter title (remove Furo theme nav-junk)
  [3]  Remove local image tags  (![…](_images/…))
  [4]  Remove noise sections: ## See also / Prerequisites / Related topics …
  [5]  Convert relative Markdown links → plain text  [text](relative.html) → text
  [6]  Deduplicate absolute URL links: [https://x.com](https://x.com) → https://x.com
  [7]  Format callout blocks (Tip / Note / Warning / Important / Caution)
       from bare heading style into Markdown blockquotes: > **Tip:** …
  [8]  Fix broken list items: lone "-" line + blank + content → "- content"
  [9]  Remove trailing whitespace
  [10] Collapse 3+ blank lines → max 2 blank lines
  [11] Normalise final newline

File-level exclusions (entire directories deleted before cleaning):
  - kanzi_docs/licenses/**             (legal text, irrelevant to tech QA)
  - kanzi_docs/release-notes/kanzi-3.0/**  (old 3.x versions, noise for 4.x RAG)
  - Any *.md file whose body < MIN_BODY_CHARS (stub / navigation-only pages)
"""

import os
import re
import shutil
from pathlib import Path

# ─────────────────────────────────────────────
# region Configuration
# ─────────────────────────────────────────────

DOCS_DIR = Path(__file__).parent / "kanzi_docs"
BACKUP_SUFFIX = ""   # ".bak" to keep originals, "" = overwrite in-place

# Folders (relative to DOCS_DIR) deleted before cleaning.
# They add noise for a 4.x-focused RAG chatbot.
EXCLUDE_DIRS = [
    "licenses",                  # 694 KB of legal text
    "release-notes/kanzi-3.0",  # 88 files of old 3.x release notes
]

# Files whose body (after frontmatter) is shorter than this are deleted.
MIN_BODY_CHARS = 200

# endregion

# ─────────────────────────────────────────────
# region ANSI Logging
# ─────────────────────────────────────────────

CYAN   = "\033[1;96m"
GREEN  = "\033[1;92m"
YELLOW = "\033[1;93m"
RED    = "\033[1;91m"
RESET  = "\033[0m"
SCRIPT = os.path.basename(__file__)


def log_step(i: str, total: str, msg: str) -> None:
    print(f"\n{CYAN}========================================================{RESET}")
    print(f"{GREEN}>>> [{i}/{total}] [{SCRIPT}] {msg}{RESET}")
    print(f"{CYAN}========================================================{RESET}\n")


def log_info(msg: str) -> None:
    print(f"  {GREEN}ok  {msg}{RESET}")


def log_warn(msg: str) -> None:
    print(f"  {YELLOW}!!  {msg}{RESET}")

# endregion

# ─────────────────────────────────────────────
# region Rule 1 – Pilcrow (Â¶)
# ─────────────────────────────────────────────

def remove_pilcrow(text: str) -> str:
    """Remove Â¶ (mojibake of UTF-8 pilcrow ¶ read as Latin-1)."""
    return text.replace("Â¶", "").replace("¶", "")

# endregion

# ─────────────────────────────────────────────
# region Rule 2 – Frontmatter title cleanup
# ─────────────────────────────────────────────

_FM_NAV_JUNK = re.compile(
    r"\s*[-–]?\s*Kanzi framework[\d\s.]*documentation.*$",
    re.IGNORECASE,
)
_FM_NAV_EXTRAS = re.compile(
    r"(ContentsMenuExpand|Light mode|Dark mode|Auto light/dark[^\n]*)",
)


def clean_frontmatter(text: str) -> str:
    """Fix the frontmatter title field."""
    lines = text.split("\n")
    out = []
    in_fm = False
    fm_fences = 0
    for line in lines:
        if line.rstrip() == "---":
            fm_fences += 1
            in_fm = fm_fences == 1
            out.append(line)
            if fm_fences == 2:
                in_fm = False
            continue
        if in_fm and line.startswith("title:"):
            title = line[len("title:"):].strip()
            title = _FM_NAV_JUNK.sub("", title).strip()
            title = _FM_NAV_EXTRAS.sub("", title).strip()
            title = title.rstrip(" -").strip()
            out.append(f"title: {title}")
        else:
            out.append(line)
    return "\n".join(out)

# endregion

# ─────────────────────────────────────────────
# region Rule 3 – Remove local image tags
# ─────────────────────────────────────────────

_IMAGE_MD = re.compile(r"!\[[^\]]*\]\([^)]*_images/[^)]+\)")


def remove_local_images(text: str) -> str:
    """Remove image tags pointing to local _images/ paths."""
    return _IMAGE_MD.sub("", text)

# endregion

# ─────────────────────────────────────────────
# region Rule 4 – Remove noise sections
# ─────────────────────────────────────────────

_NOISE_SECTION_HEADINGS = re.compile(
    r"^#{1,6}\s+(See also|Prerequisites|Related topics|In this section|"
    r"On this page|Contents|Navigation|Next steps?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def remove_noise_sections(text: str) -> str:
    """Remove entire sections whose heading matches a noise pattern."""
    lines = text.split("\n")
    result = []
    skip_until_level = None

    i = 0
    while i < len(lines):
        line = lines[i]
        hm = re.match(r"^(#{1,6})\s+(.*)", line)
        if hm:
            level = len(hm.group(1))
            if skip_until_level is not None:
                if level <= skip_until_level:
                    skip_until_level = None
                else:
                    i += 1
                    continue
            if _NOISE_SECTION_HEADINGS.match(line):
                skip_until_level = level
                i += 1
                continue
        elif skip_until_level is not None:
            i += 1
            continue
        result.append(line)
        i += 1

    return "\n".join(result)

# endregion

# ─────────────────────────────────────────────
# region Rule 5 – Relative links → plain text
# ─────────────────────────────────────────────

_REL_LINK = re.compile(
    r"\[([^\]]+)\]\((?!https?://)([^)]+\.html[^)]*)\)"
)


def inline_relative_links(text: str) -> str:
    """Replace relative HTML links with their label text only."""
    return _REL_LINK.sub(r"\1", text)

# endregion

# ─────────────────────────────────────────────
# region Rule 6 – Absolute URL deduplication
# ─────────────────────────────────────────────

# Sphinx sometimes renders bare URLs as [https://x.com](https://x.com)
# where the link text IS the URL. Collapse to just the URL.
_ABS_URL_DUP = re.compile(
    r"\[(https?://[^\]]+)\]\(\1\)"
)


def dedup_absolute_links(text: str) -> str:
    """Collapse [https://x.com](https://x.com) → https://x.com"""
    return _ABS_URL_DUP.sub(r"\1", text)

# endregion

# ─────────────────────────────────────────────
# region Rule 7 – Format callout blocks
# ─────────────────────────────────────────────

_CALLOUT_KEYWORDS = re.compile(
    r"^(Tip|Note|Warning|Important|Caution|Info|Attention)\s*$",
    re.MULTILINE,
)


def format_callouts(text: str) -> str:
    """Convert bare callout labels into Markdown blockquotes."""
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _CALLOUT_KEYWORDS.match(line.strip()) if line.strip() else None

        if m:
            keyword = m.group(1)
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1

            body_lines = []
            while j < len(lines):
                bl = lines[j]
                if re.match(r"^#{1,6}\s", bl):
                    break
                if bl.strip() == "" and j + 1 < len(lines) and lines[j + 1].strip() == "":
                    break
                body_lines.append(bl)
                j += 1

            if body_lines:
                first = body_lines[0].strip()
                rest = body_lines[1:]
                result.append(f"> **{keyword}:** {first}")
                for bl in rest:
                    if bl.strip() == "":
                        result.append(">")
                    else:
                        result.append(f"> {bl.strip()}")
                i = j
                continue

        result.append(line)
        i += 1

    return "\n".join(result)

# endregion

# ─────────────────────────────────────────────
# region Rule 8 – Fix broken list items
# ─────────────────────────────────────────────

def fix_broken_list_items(text: str) -> str:
    """Merge lone list markers with the content that follows."""
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        stripped = lines[i].rstrip()
        if re.match(r"^(\s*)-\s*$", stripped):
            indent = re.match(r"^(\s*)", stripped).group(1)
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].strip():
                result.append(f"{indent}- {lines[j].strip()}")
                i = j + 1
                continue
        result.append(lines[i])
        i += 1
    return "\n".join(result)

# endregion

# ─────────────────────────────────────────────
# region Rules 9-11 – Whitespace normalisation
# ─────────────────────────────────────────────

_TRAIL_WS    = re.compile(r"[ \t]+$", re.MULTILINE)
_EXCESS_BLANK = re.compile(r"\n{4,}")


def normalise_whitespace(text: str) -> str:
    text = _TRAIL_WS.sub("", text)
    text = _EXCESS_BLANK.sub("\n\n\n", text)
    return text.strip() + "\n"

# endregion

# ─────────────────────────────────────────────
# region Stub detector
# ─────────────────────────────────────────────

def is_stub_file(text: str) -> bool:
    """Return True if the file body (after frontmatter) is too short to be useful."""
    body = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    return len(body.strip()) < MIN_BODY_CHARS

# endregion

# ─────────────────────────────────────────────
# region Master pipeline
# ─────────────────────────────────────────────

def clean_markdown(text: str) -> str:
    """Run the full RAG-optimised cleaning pipeline."""
    text = remove_pilcrow(text)           # [1]
    text = clean_frontmatter(text)        # [2]
    text = remove_local_images(text)      # [3]
    text = remove_noise_sections(text)    # [4]
    text = inline_relative_links(text)    # [5]
    text = dedup_absolute_links(text)     # [6]
    text = format_callouts(text)          # [7]
    text = fix_broken_list_items(text)    # [8]
    text = normalise_whitespace(text)     # [9-11]
    return text

# endregion

# ─────────────────────────────────────────────
# region Main
# ─────────────────────────────────────────────

def main() -> None:
    print(f"\n{CYAN}{'='*56}{RESET}")
    print(f"{GREEN}  Kanzi Docs Markdown Cleaner v3  [{SCRIPT}]{RESET}")
    print(f"{CYAN}{'='*56}{RESET}\n")

    # Step 1: delete excluded directories
    log_step("1", "4", "Removing excluded noise directories")
    deleted_dirs = 0
    for rel_dir in EXCLUDE_DIRS:
        target = DOCS_DIR / rel_dir
        if target.exists():
            shutil.rmtree(target)
            log_info(f"Deleted: {rel_dir}/")
            deleted_dirs += 1
        else:
            log_warn(f"Already absent (skipped): {rel_dir}/")

    # Step 2: discover remaining files
    log_step("2", "4", "Discovering .md files")
    md_files = sorted(f for f in DOCS_DIR.rglob("*.md") if f.suffix == ".md")
    log_info(f"Found {len(md_files)} Markdown files after exclusions")

    # Step 3: clean + delete stubs
    log_step("3", "4", f"Cleaning {len(md_files)} files (pipeline v3)")
    stats = {"cleaned": 0, "unchanged": 0, "stub_deleted": 0, "errors": 0}

    for idx, filepath in enumerate(md_files, start=1):
        try:
            original = filepath.read_text(encoding="utf-8", errors="replace")

            if is_stub_file(original):
                filepath.unlink()
                stats["stub_deleted"] += 1
                rel = filepath.relative_to(DOCS_DIR)
                print(f"  [{idx:4d}] deleted (stub)  {rel}")
                continue

            cleaned = clean_markdown(original)

            if cleaned == original:
                stats["unchanged"] += 1
                continue

            if BACKUP_SUFFIX:
                filepath.with_suffix(filepath.suffix + BACKUP_SUFFIX).write_text(
                    original, encoding="utf-8"
                )

            filepath.write_text(cleaned, encoding="utf-8")
            stats["cleaned"] += 1
            rel = filepath.relative_to(DOCS_DIR)
            print(f"  [{idx:4d}] cleaned  {rel}")

        except Exception as exc:
            log_warn(f"Error on {filepath.name}: {exc}")
            stats["errors"] += 1

    # Step 4: summary
    log_step("4", "4", "Done")
    log_info(f"Noise dirs deleted : {deleted_dirs}")
    log_info(f"Stub files removed : {stats['stub_deleted']} (body < {MIN_BODY_CHARS} chars)")
    log_info(f"Files cleaned      : {stats['cleaned']}")
    log_info(f"Unchanged          : {stats['unchanged']}")
    if stats["errors"]:
        log_warn(f"Errors             : {stats['errors']}")
    total_remaining = len(list(DOCS_DIR.rglob("*.md")))
    log_info(f"Files ready for VDB: {total_remaining}")
    log_info(f"Output folder      : {DOCS_DIR.resolve()}")


if __name__ == "__main__":
    main()

# endregion
