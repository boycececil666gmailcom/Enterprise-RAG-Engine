#region Imports
import json
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode
from qdrant_client import QdrantClient
#endregion

#region Configuration
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "models/gemini-embedding-001")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333").replace("qdrant:6333", "localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
BATCH_SIZE = 64
INPUT_JSON_PATH = Path(__file__).resolve().parent / "2.raptor_chunks.json"
#endregion

#region Ingestion Logic
def ingest_layer(
    layer: int,
    chunks: list[dict],
    dense_embed: GoogleGenerativeAIEmbeddings,
    sparse_embed: FastEmbedSparse,
    client: QdrantClient
) -> None:
    """Wipes and batch-ingests chunks into a dedicated layer collection ('raptor_layer_{N}')."""
    collection = f"raptor_layer_{layer}"
    total = len(chunks)
    if total == 0:
        return

    print(f"\n[Ingestion] Layer {layer}: '{collection}' ({total} chunks)")
    if client.collection_exists(collection):
        client.delete_collection(collection)
        print(f"[Ingestion] Cleaned existing '{collection}'.")

    # Ingest first batch to initialize collection
    first_batch = chunks[:BATCH_SIZE]
    docs = [
        Document(
            page_content=d["small"],
            metadata={**d.get("metadata", {}), "id": d.get("id", "")}
        )
        for d in first_batch
    ]
    ids = [d["id"] for d in first_batch]

    total_batches = ((total - 1) // BATCH_SIZE) + 1
    vector_store = QdrantVectorStore.from_documents(
        documents=docs,
        ids=ids,
        embedding=dense_embed,
        sparse_embedding=sparse_embed,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=collection,
        content_payload_key="small",
        retrieval_mode=RetrievalMode.HYBRID,
        force_recreate=True
    )
    print(f"[Ingestion] Batch 1/{total_batches} ({min(BATCH_SIZE, total)}/{total}) initialized.")

    # Upload remaining batches
    for b_idx, start in enumerate(range(BATCH_SIZE, total, BATCH_SIZE), start=2):
        batch = chunks[start : start + BATCH_SIZE]
        batch_docs = [
            Document(
                page_content=d["small"],
                metadata={**d.get("metadata", {}), "id": d.get("id", "")}
            )
            for d in batch
        ]
        batch_ids = [d["id"] for d in batch]
        vector_store.add_documents(documents=batch_docs, ids=batch_ids)
        print(f"[Ingestion] Batch {b_idx}/{total_batches} ({min(start + BATCH_SIZE, total)}/{total}) uploaded.")

    print(f"[Ingestion] Layer {layer} ('{collection}') completed.")


def ingest_chunks_to_qdrant() -> None:
    """Loads 2.raptor_chunks.json and ingests into 3 separate collections for tree traversal."""
    if not INPUT_JSON_PATH.exists():
        raise FileNotFoundError(f"Input file '{INPUT_JSON_PATH.name}' not found. Run 2.raptor_tree_pipeline.py first.")

    print(f"[Ingestion] Connecting to Qdrant at: {QDRANT_URL}")
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    dense_embed = GoogleGenerativeAIEmbeddings(model=GEMINI_EMBED_MODEL, google_api_key=GEMINI_API_KEY)
    sparse_embed = FastEmbedSparse(model_name="Qdrant/bm25")

    # Partition by raptor_layer (0: Root, 1: Section, 2: Leaf)
    layers: dict[int, list[dict]] = {0: [], 1: [], 2: []}
    for item in data:
        layer = item.get("metadata", {}).get("raptor_layer", 2)
        layers.setdefault(layer, []).append(item)

    print(f"[Ingestion] Loaded {len(data)} chunks -> Layer 0: {len(layers[0])}, Layer 1: {len(layers[1])}, Layer 2: {len(layers[2])}")

    for layer_num in sorted(layers.keys()):
        ingest_layer(layer_num, layers[layer_num], dense_embed, sparse_embed, client)

    print(f"\n[Ingestion] All 3 collections ('raptor_layer_0', 'raptor_layer_1', 'raptor_layer_2') ready for Tree Traversal.")


if __name__ == "__main__":
    ingest_chunks_to_qdrant()
#endregion
