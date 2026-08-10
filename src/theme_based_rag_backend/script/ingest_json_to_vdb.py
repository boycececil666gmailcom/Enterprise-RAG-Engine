#region Imports & Configuration
import os
import sys
import json
import gzip
import argparse
import logging
from pathlib import Path
import httpx

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

logger = logging.getLogger(__name__)
#endregion

#region Core Ingestion Functions
def load_json_chunks(file_path: Path) -> list[dict]:
    """Loads chunks from a JSON or GZ compressed JSON dataset file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input dataset file not found: {file_path}")

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/3] [{os.path.basename(__file__)}] Reading structured JSON dataset: {file_path.name}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    if file_path.suffix == ".gz" or file_path.name.endswith(".json.gz"):
        with gzip.open(file_path, "rt", encoding="utf-8") as f:
            data = json.load(f)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    if isinstance(data, dict):
        chunks = data.get("chunks", [])
    elif isinstance(data, list):
        chunks = data
    else:
        chunks = []

    print(f"Successfully loaded {len(chunks):,} chunk records from dataset.")
    return chunks

def ingest_chunks_via_http(chunks: list[dict], endpoint_url: str, batch_size: int = 50) -> dict:
    """Sends chunk records to the target vector database ingestion HTTP endpoint."""
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [2/3] [{os.path.basename(__file__)}] Connecting to Vector DB Ingestion Endpoint: {endpoint_url}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    success_count = 0
    fail_count = 0
    total = len(chunks)

    with httpx.Client(timeout=60.0) as client:
        for idx, chunk in enumerate(chunks, start=1):
            text = chunk.get("content") or chunk.get("text") or ""
            metadata = chunk.get("metadata") or {}

            if not text:
                continue

            clean_metadata = {}
            for k, v in metadata.items():
                if isinstance(v, (list, dict)):
                    clean_metadata[k] = json.dumps(v, ensure_ascii=False)
                else:
                    clean_metadata[k] = str(v) if v is not None else ""

            payload = {
                "text": text,
                "metadata": clean_metadata
            }

            try:
                response = client.post(endpoint_url, json=payload)
                if response.status_code == 200:
                    success_count += 1
                else:
                    fail_count += 1
                    logger.warning(f"Failed chunk {idx}/{total}: HTTP {response.status_code} - {response.text}")
            except Exception as e:
                fail_count += 1
                logger.error(f"Error sending chunk {idx}/{total} to endpoint: {e}")

            if idx % batch_size == 0 or idx == total:
                print(f"Progress: [{idx}/{total}] chunks processed (Success: {success_count}, Failures: {fail_count})")

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [3/3] [{os.path.basename(__file__)}] Ingestion Complete: {success_count}/{total} Chunks Successfully Ingested into VDB\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    return {"total": total, "success": success_count, "failures": fail_count}
#endregion

#region CLI Entry Point
def main():
    parser = argparse.ArgumentParser(description="Ingest structured JSON chunks dataset into Qdrant Vector DB (K8s or Local).")
    parser.add_argument(
        "--input", "-i",
        type=str,
        default="preprocessing-pipeline/rag_chunks.json",
        help="Path to structured JSON or JSON.GZ dataset file"
    )
    parser.add_argument(
        "--endpoint", "-e",
        type=str,
        default=os.getenv("INGEST_ENDPOINT", "http://localhost:8080/ingest/vector"),
        help="Target Vector DB Ingestion Endpoint URL (default: http://localhost:8080/ingest/vector)"
    )
    parser.add_argument(
        "--batch-size", "-b",
        type=int,
        default=50,
        help="Progress logging batch interval (default: 50)"
    )

    args = parser.parse_args()
    input_path = Path(args.input).resolve()

    if not input_path.exists():
        cwd = Path.cwd()
        alt_paths = [
            cwd / "preprocessing-pipeline" / args.input,
            cwd / "preprocessing-pipeline" / "rag_chunks.json",
            cwd / "preprocessing-pipeline" / "rag_chunks.json.gz",
        ]
        for alt in alt_paths:
            if alt.exists():
                input_path = alt.resolve()
                break

    chunks = load_json_chunks(input_path)
    if not chunks:
        print("No valid chunk records found in dataset to ingest.")
        sys.exit(1)

    ingest_chunks_via_http(chunks, args.endpoint, args.batch_size)

if __name__ == "__main__":
    main()
#endregion
