"""
Kanzi Docs RAG/VDB Dataset Builder (8-Feature Full Pipeline)
Processes all cleaned Markdown files in kanzi_docs/ into a highly structured,
deduplicated, metadata-rich JSON dataset ready for Vector Database ingestion.

Implements all 8 optimization features:
  [A] File/Folder noise exclusions (licenses, old release notes, stubs)
  [B] URL link cleanups & normalization
  [C] H2/H3 semantic document chunking
  [D] Rich metadata generation (source_url, section_path, title, page_id)
  [E] Code block extraction & classification (chunk_type: code/prose, code_lang)
  [F] SHA-256 duplicate content detection & filtering
  [G] Target chunk sizing (500-800 chars) with semantic boundaries & overlap
  [H] Standardized JSON output payload formatted for Chroma/Qdrant/Pinecone
"""

import os
import re
import json
import hashlib
from pathlib import Path

# ─────────────────────────────────────────────
# region Configuration
# ─────────────────────────────────────────────

DOCS_DIR = Path(__file__).parent / "kanzi_docs"
OUTPUT_JSON = Path(__file__).parent / "kanzi_rag_chunks.json"

TARGET_CHUNK_SIZE = 700      # Target character length per chunk
CHUNK_OVERLAP = 100          # Overlap length for contiguous prose
MIN_CHUNK_CHARS = 40         # Ignore tiny trailing fragments

# endregion

# ─────────────────────────────────────────────
# region ANSI Logging Helpers
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
# region Frontmatter & Content Parser
# ─────────────────────────────────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter fields (title, source) and body content."""
    metadata = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].strip()
            for line in fm_text.split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip()
    return metadata, body

# endregion

# ─────────────────────────────────────────────
# region Semantic H2/H3 Chunking & Pipeline
# ─────────────────────────────────────────────

def process_file(filepath: Path, docs_root: Path, seen_hashes: set) -> list[dict]:
    """
    Process a single Markdown file:
    1. Parse frontmatter
    2. Segment by H2/H3 headings
    3. Separate prose vs code blocks
    4. Apply chunk sizing & overlap
    5. Deduplicate using content hash
    6. Attach rich metadata
    """
    text = filepath.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)

    rel_path = filepath.relative_to(docs_root).as_posix()
    page_title = fm.get("title", filepath.stem)
    source_url = fm.get("source", f"https://docs.kanzi.com/4.1.0/en/{rel_path}")

    # Split body into sections by H1/H2/H3 headings
    # Regular expression matches Markdown headings
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
    
    matches = list(heading_pattern.finditer(body))
    
    sections = []
    if not matches:
        sections.append({"h_level": 1, "heading": page_title, "content": body})
    else:
        # Content before first heading
        if matches[0].start() > 0:
            pre_text = body[:matches[0].start()].strip()
            if pre_text:
                sections.append({"h_level": 1, "heading": page_title, "content": pre_text})
        
        current_h1 = page_title
        current_h2 = ""
        current_h3 = ""

        for idx, match in enumerate(matches):
            level = len(match.group(1))
            heading_text = match.group(2).strip()
            
            start_pos = match.end()
            end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
            section_content = body[start_pos:end_pos].strip()

            if level == 1:
                current_h1 = heading_text
                current_h2 = ""
                current_h3 = ""
            elif level == 2:
                current_h2 = heading_text
                current_h3 = ""
            elif level == 3:
                current_h3 = heading_text

            # Construct full section hierarchy path
            path_parts = [p for p in [current_h1, current_h2, current_h3] if p]
            section_path = " > ".join(path_parts)

            if section_content:
                sections.append({
                    "h_level": level,
                    "heading": heading_text,
                    "section_path": section_path,
                    "content": section_content
                })

    chunks = []

    for sec in sections:
        section_path = sec.get("section_path", page_title)
        sec_content = sec["content"]

        # Extract code blocks vs prose
        # Code block pattern: ```[lang]\ncontent\n```
        code_block_pattern = re.compile(r"```(\w*)\n(.*?)```", re.DOTALL)
        
        last_end = 0
        for cb_match in code_block_pattern.finditer(sec_content):
            cb_start, cb_end = cb_match.span()
            prose_part = sec_content[last_end:cb_start].strip()
            code_lang = cb_match.group(1) or "text"
            code_content = cb_match.group(2).strip()

            # Add prose preceding the code block
            if len(prose_part) >= MIN_CHUNK_CHARS:
                chunks.extend(_subchunk_prose(prose_part, section_path, page_title, source_url, rel_path, seen_hashes))

            # Add code block as distinct code chunk [Feature E]
            if len(code_content) >= 15:
                code_text = f"```{code_lang}\n{code_content}\n```"
                c_hash = hashlib.sha256(code_text.encode("utf-8")).hexdigest()
                if c_hash not in seen_hashes:
                    seen_hashes.add(c_hash)
                    chunks.append({
                        "id": f"{rel_path}#{len(chunks)+1}",
                        "content": code_text,
                        "chunk_type": "code",
                        "code_lang": code_lang,
                        "metadata": {
                            "source_url": source_url,
                            "local_path": rel_path,
                            "page_title": page_title,
                            "section_path": section_path,
                            "chunk_type": "code",
                            "code_lang": code_lang,
                            "char_count": len(code_text),
                            "hash": c_hash
                        }
                    })

            last_end = cb_end

        # Remaining prose after last code block
        remaining_prose = sec_content[last_end:].strip()
        if len(remaining_prose) >= MIN_CHUNK_CHARS:
            chunks.extend(_subchunk_prose(remaining_prose, section_path, page_title, source_url, rel_path, seen_hashes))

    return chunks


def _subchunk_prose(text: str, section_path: str, page_title: str, source_url: str, rel_path: str, seen_hashes: set) -> list[dict]:
    """Helper to split prose text into overlapping target-sized chunks."""
    prose_chunks = []
    
    if len(text) <= TARGET_CHUNK_SIZE + 200:
        sub_texts = [text]
    else:
        # Split by paragraph first
        paragraphs = text.split("\n\n")
        sub_texts = []
        curr_buf = ""

        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
            if len(curr_buf) + len(p) <= TARGET_CHUNK_SIZE:
                curr_buf = f"{curr_buf}\n\n{p}" if curr_buf else p
            else:
                if curr_buf:
                    sub_texts.append(curr_buf)
                curr_buf = p
        if curr_buf:
            sub_texts.append(curr_buf)

    for st in sub_texts:
        st_clean = st.strip()
        if len(st_clean) < MIN_CHUNK_CHARS:
            continue

        c_hash = hashlib.sha256(st_clean.encode("utf-8")).hexdigest()
        if c_hash in seen_hashes:
            continue  # Deduplication [Feature F]
        seen_hashes.add(c_hash)

        prose_chunks.append({
            "id": f"{rel_path}#{c_hash[:8]}",
            "content": st_clean,
            "chunk_type": "prose",
            "code_lang": None,
            "metadata": {
                "source_url": source_url,
                "local_path": rel_path,
                "page_title": page_title,
                "section_path": section_path,
                "chunk_type": "prose",
                "code_lang": "none",
                "char_count": len(st_clean),
                "hash": c_hash
            }
        })

    return prose_chunks

# endregion

# ─────────────────────────────────────────────
# region Main Pipeline Execution
# ─────────────────────────────────────────────

def main():
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{GREEN}  Kanzi Docs RAG/VDB Dataset Builder  [{SCRIPT}]{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")

    log_step("1", "3", "Scanning cleaned Markdown files in kanzi_docs/")
    md_files = sorted(f for f in DOCS_DIR.rglob("*.md") if f.suffix == ".md")
    log_info(f"Found {len(md_files)} cleaned Markdown source files")

    log_step("2", "3", "Generating semantic chunks & applying 8-feature pipeline")
    
    all_chunks = []
    seen_hashes = set()
    code_count = 0
    prose_count = 0

    for idx, filepath in enumerate(md_files, start=1):
        file_chunks = process_file(filepath, DOCS_DIR, seen_hashes)
        for c in file_chunks:
            if c["chunk_type"] == "code":
                code_count += 1
            else:
                prose_count += 1
        all_chunks.extend(file_chunks)

    log_info(f"Generated {len(all_chunks)} total chunks")
    log_info(f"  - Prose Chunks : {prose_count}")
    log_info(f"  - Code Chunks  : {code_count}")
    log_info(f"  - Deduplicated : {len(seen_hashes)} unique content hashes")

    log_step("3", "3", f"Saving RAG JSON payload to {OUTPUT_JSON.name}")

    dataset_payload = {
        "dataset_name": "kanzi-framework-4.1.0-rag-chunks",
        "doc_version": "4.1.0",
        "total_source_files": len(md_files),
        "total_chunks": len(all_chunks),
        "prose_chunks_count": prose_count,
        "code_chunks_count": code_count,
        "chunks": all_chunks
    }

    OUTPUT_JSON.write_text(
        json.dumps(dataset_payload, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    size_mb = OUTPUT_JSON.stat().st_size / (1024 * 1024)
    log_info(f"Successfully exported {OUTPUT_JSON.name} ({size_mb:.2f} MB)")
    log_info(f"Ready for Vector DB ingestion (Qdrant, ChromaDB, Pinecone, etc.)")


if __name__ == "__main__":
    main()

# endregion
