# region Imports
import json
import os
from pathlib import Path

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
INPUT_JSON_PATH = _CURRENT_DIR / "2.raptor_chunks.json"
# endregion


# region Ingestion Logic
def ingest_collapsed_tree(
    chunks: list[dict],
    dense_embed: OpenAIEmbeddings,
    sparse_embed: FastEmbedSparse,
    client: QdrantClient,
    collection_name: str = "raptor_chunks",
) -> None:
    """Wipes and batch-ingests all chunks flatly into a single unified collection ('raptor_chunks') for Collapsed Tree retrieval."""
    total = len(chunks)
    if total == 0:
        return

    print(f"\n[Ingestion] Collapsed Tree: '{collection_name}' ({total} total chunks)")
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)
        print(f"[Ingestion] Cleaned existing collection '{collection_name}'.")

    # Ingest first batch to initialize collection
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

    print(f"[Ingestion] Ingested {total} chunks into '{collection_name}'.")


def ingest_chunks_to_qdrant() -> None:
    """Loads 2.raptor_chunks.json and ingests all chunks into a unified collection for Collapsed Tree."""
    if not INPUT_JSON_PATH.exists():
        raise FileNotFoundError(
            f"Input file '{INPUT_JSON_PATH.name}' not found. Run 2.raptor_tree_pipeline.py first."
        )

    print(f"[Ingestion] Connecting to Qdrant at: {QDRANT_URL}")
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    with open(INPUT_JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    dense_embed = embeddings
    sparse_embed = FastEmbedSparse(model_name="Qdrant/bm25")

    ingest_collapsed_tree(data, dense_embed, sparse_embed, client)


if __name__ == "__main__":
    ingest_chunks_to_qdrant()
# endregion
