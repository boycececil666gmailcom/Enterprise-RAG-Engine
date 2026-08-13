#region Imports & Configuration
import sys
from functools import lru_cache

from langchain_core.documents import Document
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

from .config import QDRANT_API_KEY, QDRANT_URL
from .llm_client import embeddings

#endregion

#region Helper & Vector Database Initialization
@lru_cache(maxsize=1)
def get_sparse_embeddings():
    """Lazily initializes and caches FastEmbed BM25 sparse embeddings model."""
    try:
        sparse = FastEmbedSparse(model_name="Qdrant/bm25")
        return sparse
    except Exception:
        return None

@lru_cache(maxsize=1)
def get_vector_store():
    """Lazily initializes and caches QdrantVectorStore using lru_cache."""
    try:
        sparse_kwargs = {}
        sparse_kwargs["sparse_embedding"] = get_sparse_embeddings()
        sparse_kwargs["retrieval_mode"] = RetrievalMode.HYBRID

        return QdrantVectorStore.from_existing_collection(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name="local_rag_documents",
            embedding=embeddings,
            **sparse_kwargs
        )

    except Exception as e:
        raise e

# Initial attempt during import, but don't block start if it fails
try:
    get_vector_store()
except Exception:
    pass
#endregion

#region Knowledge Ingestion API
def add_document_text(text: str, metadata: dict = None) -> int:
    """
    Directly ingests a pre-processed document chunk into Qdrant vector database.
    All chunking and optimization strategies are managed upstream by preprocessing-pipeline.
    """
    store = get_vector_store()
    if store is None:
        raise ValueError("Vector DB store is not initialized. Please set a valid GEMINI_API_KEY in .env file.")
    doc = Document(page_content=text, metadata=metadata or {})
    store.add_documents([doc])
    return 1
#endregion

