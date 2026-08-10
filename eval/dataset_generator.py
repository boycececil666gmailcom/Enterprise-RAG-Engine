#region Imports & Configuration
import os
import sys
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

logger = logging.getLogger(__name__)
#endregion

#region Dataset Generation Functions
def generate_eval_dataset_from_chunks(
    json_chunks_path: Path,
    output_path: Path,
    max_samples: int = 20
) -> List[Dict[str, Any]]:
    """
    Extracts synthetic evaluation QA pairs from preprocessed rag_chunks.json metadata.

    Args:
        json_chunks_path: Path to rag_chunks.json dataset.
        output_path: Path to output JSON evaluation dataset.
        max_samples: Maximum number of QA pairs to generate.

    Returns:
        List of generated dataset items.
    """
    if not json_chunks_path.exists():
        raise FileNotFoundError(f"Source chunks dataset file not found at: {json_chunks_path}")

    logger.info(f"Loading chunks dataset from: {json_chunks_path}")
    with open(json_chunks_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chunks = data.get("chunks", []) if isinstance(data, dict) else data
    eval_dataset: List[Dict[str, Any]] = []

    for chunk in chunks:
        if len(eval_dataset) >= max_samples:
            break

        content = chunk.get("content", "")
        meta = chunk.get("metadata", {})
        questions = meta.get("questions", [])
        parent_content = meta.get("parent_content", "") or content
        page_title = meta.get("page_title", "")

        if not questions or not content:
            continue

        sample_question = questions[0] if isinstance(questions, list) else str(questions)

        eval_item = {
            "id": chunk.get("id", f"sample-{len(eval_dataset) + 1}"),
            "question": sample_question,
            "ground_truth": parent_content,
            "page_title": page_title,
            "source_url": meta.get("source_url", "")
        }
        eval_dataset.append(eval_item)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as out_f:
        json.dump(eval_dataset, out_f, ensure_ascii=False, indent=2)

    print(f"\033[1;92mSuccessfully generated {len(eval_dataset)} evaluation samples at: {output_path}\033[0m")
    return eval_dataset
#endregion

#region CLI Entry Point
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate RAGAS evaluation dataset from rag_chunks.json")
    parser.add_argument("--input", "-i", type=str, default="preprocessing-pipeline/rag_chunks.json", help="Path to rag_chunks.json")
    parser.add_argument("--output", "-o", type=str, default="src/theme_based_rag_backend/eval/eval_dataset.json", help="Output path for eval_dataset.json")
    parser.add_argument("--max", "-m", type=int, default=20, help="Max samples to generate")

    args = parser.parse_args()
    in_path = Path(args.input).resolve()
    out_path = Path(args.output).resolve()
    
    generate_eval_dataset_from_chunks(in_path, out_path, args.max)
#endregion
