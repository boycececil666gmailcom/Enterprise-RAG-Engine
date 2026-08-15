#region Imports
import json
import os
import socket
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode
#endregion

#region Environment & Configuration
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "models/gemini-embedding-001")

raw_qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")

# Auto-resolve Docker hostname 'qdrant' to 'localhost' when running outside docker
if "qdrant:6333" in raw_qdrant_url:
    try:
        socket.gethostbyname("qdrant")
        QDRANT_URL = raw_qdrant_url
    except socket.gaierror:
        QDRANT_URL = raw_qdrant_url.replace("qdrant:6333", "localhost:6333")
else:
    QDRANT_URL = raw_qdrant_url

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
QDRANT_COLLECTION = "raptor_documents"
BATCH_SIZE = 64

INPUT_JSON_PATH = Path(__file__).resolve().parent / "2.raptor_chunks.json"
#endregion

#region Ingestion Logic
def ingest_chunks_to_qdrant():
    """Reads raptor_chunks.json and batch-ingests into Qdrant Vector Store."""
    if not INPUT_JSON_PATH.exists():
        raise FileNotFoundError(f"Input file '{INPUT_JSON_PATH.name}' not found. Please run 2.raptor_tree_pipeline.py first.")

    print(f"[Ingestion] Connecting to Qdrant at: {QDRANT_URL}")
    print(f"[Ingestion] Loading chunks from {INPUT_JSON_PATH.name}...")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_chunks = len(data)
    print(f"[Ingestion] Loaded {total_chunks} chunks. Initializing Embedding models (Model: {GEMINI_EMBED_MODEL})...")

    dense_embeddings = GoogleGenerativeAIEmbeddings(
        model=GEMINI_EMBED_MODEL,
        google_api_key=GEMINI_API_KEY
    )
    sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

    # Ingest the first batch with force_recreate=True to initialize collection
    first_batch_data = data[:BATCH_SIZE]
    first_docs = [
        Document(
            page_content=item["small"],
            metadata=item["metadata"]
        )
        for item in first_batch_data
    ]
    first_ids = [item["id"] for item in first_batch_data]

    total_batches = ((total_chunks - 1) // BATCH_SIZE) + 1
    print(f"[Ingestion] Initializing collection '{QDRANT_COLLECTION}' with batch 1/{total_batches}...")
    vector_store = QdrantVectorStore.from_documents(
        documents=first_docs,
        ids=first_ids,
        embedding=dense_embeddings,
        sparse_embedding=sparse_embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=QDRANT_COLLECTION,
        content_payload_key="small",
        retrieval_mode=RetrievalMode.HYBRID,
        force_recreate=True
    )
    print(f"[Ingestion] Progress: {len(first_docs)}/{total_chunks} ({len(first_docs)/total_chunks*100:.1f}%) uploaded.")

    # Batch upload remaining documents
    for batch_num, start_idx in enumerate(range(BATCH_SIZE, total_chunks, BATCH_SIZE), start=2):
        batch_data = data[start_idx : start_idx + BATCH_SIZE]
        batch_docs = [
            Document(
                page_content=item["small"],
                metadata=item["metadata"]
            )
            for item in batch_data
        ]
        batch_ids = [item["id"] for item in batch_data]

        vector_store.add_documents(
            documents=batch_docs,
            ids=batch_ids
        )
        processed = min(start_idx + BATCH_SIZE, total_chunks)
        print(f"[Ingestion] Batch {batch_num}/{total_batches}: {processed}/{total_chunks} ({processed/total_chunks*100:.1f}%) uploaded.")

    print(f"[Ingestion] Completed successfully. All {total_chunks} chunks ingested into Qdrant '{QDRANT_COLLECTION}'.")

if __name__ == "__main__":
    ingest_chunks_to_qdrant()
#endregion
