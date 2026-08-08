#!/usr/bin/env python3
"""
Direct JSON Hypothetical Question Enriched Dataset Generator

Reads directly from `kanzi_rag_chunks.json`, constructs high-precision
natural language questions for each of the 31,626 chunks using semantic section context,
and saves the result to both `kanzi_rag_chunks.json` and `kanzi_rag_chunks.json.gz`.
"""

#region Imports & Config
import os
import re
import json
import gzip
import time
from pathlib import Path

SCRIPT_DIR  = Path(__file__).parent
TARGET_JSON = (SCRIPT_DIR.parent / "rag_chunks.json").resolve()
TARGET_GZ   = (SCRIPT_DIR.parent / "rag_chunks.json.gz").resolve()

CYAN  = "\033[1;96m"
GREEN = "\033[1;92m"
RESET = "\033[0m"
SEP   = f"{CYAN}{'=' * 60}{RESET}"

def log_step(step_idx: str, msg: str) -> None:
    print(f"\n{SEP}")
    print(f"{GREEN}>>> [{step_idx}] [{os.path.basename(__file__)}] {msg}{RESET}")
    print(f"{SEP}\n")
#endregion

#region Extraction Logic
ACTION_VERBS = [
    "configure", "creating", "create", "setting", "set", "using", "use",
    "enabling", "enable", "disabling", "disable", "connecting", "connect",
    "adding", "add", "removing", "remove", "optimizing", "optimize",
    "rendering", "render", "animating", "animate", "binding", "bind"
]

def generate_questions_for_chunk(chunk: dict) -> list[str]:
    meta = chunk.get("metadata", {})
    title = meta.get("page_title", "").strip()
    section = meta.get("section_path", "").strip()
    chunk_type = meta.get("chunk_type", "prose")
    code_lang = meta.get("code_lang", "none")
    content = chunk.get("content", "")

    questions = []
    sec_parts = [p.strip() for p in section.split(">") if p.strip()]
    leaf_section = sec_parts[-1] if sec_parts else title
    parent_section = sec_parts[-2] if len(sec_parts) >= 2 else ""

    if chunk_type == "code":
        lang_str = f"in {code_lang}" if code_lang and code_lang != "none" else ""
        if parent_section and leaf_section:
            questions.append(f"How to implement {leaf_section} for {parent_section} {lang_str}?".strip())
            questions.append(f"Code example for {leaf_section} {lang_str}".strip())
        elif leaf_section:
            questions.append(f"How to write {leaf_section} code {lang_str}?".strip())
            questions.append(f"Example code for {leaf_section} {lang_str}".strip())
        else:
            questions.append(f"Code snippet example for {title} {lang_str}".strip())
    else:
        matched_action = None
        for verb in ACTION_VERBS:
            if re.search(r'\b' + verb + r'\b', content, re.IGNORECASE):
                matched_action = verb
                break

        if parent_section and leaf_section:
            questions.append(f"How to use {leaf_section} in {parent_section}?")
            questions.append(f"What is the function of {leaf_section} in {parent_section}?")
            if matched_action:
                questions.append(f"How to {matched_action} {leaf_section} in Kanzi?")
            else:
                questions.append(f"How does {leaf_section} work in Kanzi?")
        elif leaf_section:
            questions.append(f"What is {leaf_section} in Kanzi?")
            questions.append(f"How to configure {leaf_section}?")
            questions.append(f"Overview and usage of {leaf_section}")
        else:
            questions.append(f"What is {title}?")
            questions.append(f"How to work with {title} in Kanzi?")

    unique_q = []
    for q in questions:
        q_clean = q.strip()
        if q_clean and q_clean not in unique_q:
            unique_q.append(q_clean)
    return unique_q[:3]
#endregion

#region Main
def main():
    log_step("1/3", f"Reading directly from target file: {TARGET_JSON.name}")
    start_time = time.time()
    
    with open(TARGET_JSON, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    chunks = dataset.get("chunks", [])
    total = len(chunks)
    print(f"  ok Loaded {total:,} chunks directly from {TARGET_JSON.name}")

    log_step("2/3", f"Generating questions for all {total:,} chunks...")
    for chunk in chunks:
        chunk.setdefault("metadata", {})["questions"] = generate_questions_for_chunk(chunk)

    dataset["chunks"] = chunks

    log_step("3/3", f"Overwriting {TARGET_JSON.name} and synchronizing {TARGET_GZ.name}...")
    payload = json.dumps(dataset, indent=2, ensure_ascii=False)
    TARGET_JSON.write_text(payload, encoding="utf-8")
    
    with gzip.open(TARGET_GZ, "wb") as f_gz:
        f_gz.write(payload.encode("utf-8"))

    elapsed = time.time() - start_time
    json_mb = TARGET_JSON.stat().st_size / (1024 * 1024)
    gz_mb = TARGET_GZ.stat().st_size / (1024 * 1024)

    print(f"{SEP}")
    print(f"{GREEN}>>> Direct JSON Generation & Update Complete!{RESET}")
    print(f"{SEP}")
    print(f"  - Target JSON File       : {TARGET_JSON.name} ({json_mb:.2f} MB)")
    print(f"  - Synchronized GZ File   : {TARGET_GZ.name} ({gz_mb:.2f} MB)")
    print(f"  - Total Chunks Processed : {total:,}")
    print(f"  - Coverage               : 100% ({total:,} / {total:,})")
    print(f"  - Processing Time        : {elapsed:.2f} seconds")
    print(f"  - External API Cost      : $0.00 (Zero cost)")
    print(f"{SEP}\n")

if __name__ == "__main__":
    main()
#endregion
