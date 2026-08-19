# region Imports
import argparse
import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode
from llm_client import embeddings
from qdrant_client import QdrantClient

# endregion

# region Configuration
_CURRENT_DIR = Path(__file__).resolve().parent
_ROOT_DIR = _CURRENT_DIR.parent
load_dotenv(dotenv_path=_ROOT_DIR / ".env")

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333").replace(
    "qdrant:6333", "localhost:6333"
)
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
BATCH_SIZE = 64
DEFAULT_COLLECTION = "raptor_chunks"
# endregion

# region Ingestion Logic
def ingest_chunks(
    chunks: list[dict[str, Any]],
    dense_embed: OpenAIEmbeddings,
    sparse_embed: FastEmbedSparse,
    client: QdrantClient,
    collection_name: str = DEFAULT_COLLECTION,
) -> None:
    """Wipes and batch-ingests all Small-to-Big chunks into Qdrant for Hybrid (Dense + BM25) retrieval."""
    total = len(chunks)
    if total == 0:
        print(f"[Ingestion-ingest] No chunks found to ingest for collection '{collection_name}'.")
        return

    print(f"[Ingestion-ingest] Initializing collection '{collection_name}' ({total} total chunks)...")
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
        print(f"[Ingestion-ingest] Recreated clean collection '{collection_name}'.")

    # Ingest first batch to initialize vector store schema
    first_batch = chunks[:BATCH_SIZE]
    docs = [
        Document(
            page_content=d.get("small")
            or d.get("metadata", {}).get("summary")
            or d.get("metadata", {}).get("title")
            or d.get("metadata", {}).get("big", "document"),
            metadata=d.get("metadata", {}),
        )
        for d in first_batch
    ]
    ids = [d["id"] for d in first_batch]

    vector_store = QdrantVectorStore.from_documents(
        documents=docs,
        ids=ids,
        embedding=dense_embed,
        sparse_embedding=sparse_embed,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=collection_name,
        content_payload_key="small",
        retrieval_mode=RetrievalMode.HYBRID,
        force_recreate=True,
    )

    # Upload remaining batches
    for start in range(BATCH_SIZE, total, BATCH_SIZE):
        batch = chunks[start : start + BATCH_SIZE]
        batch_docs = [
            Document(
                page_content=d.get("small")
                or d.get("metadata", {}).get("summary")
                or d.get("metadata", {}).get("title")
                or d.get("metadata", {}).get("big", "document"),
                metadata=d.get("metadata", {}),
            )
            for d in batch
        ]
        batch_ids = [d["id"] for d in batch]
        vector_store.add_documents(documents=batch_docs, ids=batch_ids)
        print(f"[Ingestion-ingest] Uploaded {min(start + BATCH_SIZE, total)}/{total} chunks...")

    print(f"[Ingestion-ingest] Ingestion complete. Total {total} chunks stored in '{collection_name}'.")


def main() -> None:
    """Parses CLI args and executes knowledge ingestion into Qdrant."""
    parser = argparse.ArgumentParser(description="Ingest Small-to-Big knowledge chunks into Qdrant Vector Store.")
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        default=None,
        help="Path to JSON file containing modeled chunks (e.g. 2.jira_modeled_chunks.json or 2.raptor_chunks.json).",
    )
    parser.add_argument(
        "--collection",
        "-c",
        type=str,
        default=DEFAULT_COLLECTION,
        help=f"Target Qdrant collection name (default: '{DEFAULT_COLLECTION}').",
    )
    args = parser.parse_args()

    # Determine input JSON file
    if args.input:
        input_path = Path(args.input)
    elif (_CURRENT_DIR / "2.jira_modeled_chunks.json").exists():
        input_path = _CURRENT_DIR / "2.jira_modeled_chunks.json"
    elif (_CURRENT_DIR / "2.raptor_chunks.json").exists():
        input_path = _CURRENT_DIR / "2.raptor_chunks.json"
    else:
        raise FileNotFoundError("[Ingestion-main] No modeled chunks JSON found in preprocessing-pipeline.")

    if not input_path.exists():
        raise FileNotFoundError(f"[Ingestion-main] Input file '{input_path}' not found.")

    print(f"[Ingestion-main] Loading chunks from '{input_path.name}'...")
    with open(input_path, encoding="utf-8") as f:
        chunks = json.load(f)

    if not embeddings:
        raise ValueError("[Ingestion-main] Embedding client not initialized. Check OPENROUTER_API_KEY in .env.")

    print(f"[Ingestion-main] Connecting to Qdrant at: {QDRANT_URL}")
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    sparse_embed = FastEmbedSparse(model_name="Qdrant/bm25")

    ingest_chunks(
        chunks=chunks,
        dense_embed=embeddings,
        sparse_embed=sparse_embed,
        client=client,
        collection_name=args.collection,
    )


if __name__ == "__main__":
    main()
# endregion
