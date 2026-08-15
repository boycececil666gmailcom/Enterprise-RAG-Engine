#region Vector Store
from functools import lru_cache
from typing import Any

from langchain_core.documents import Document
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

from .config import QDRANT_API_KEY, QDRANT_URL
from .llm_client import embeddings


@lru_cache(maxsize=1)
def get_sparse_embeddings() -> FastEmbedSparse | None:
    """Lazily initializes and caches FastEmbed BM25 sparse embeddings model."""
    try:
        return FastEmbedSparse(model_name="Qdrant/bm25")
    except Exception:
        return None


@lru_cache(maxsize=1)
def get_vector_store() -> QdrantVectorStore:
    """Lazily initializes and caches QdrantVectorStore."""
    return QdrantVectorStore.from_existing_collection(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name="local_rag_documents",
        embedding=embeddings,
        sparse_embedding=get_sparse_embeddings(),
        retrieval_mode=RetrievalMode.HYBRID,
    )


def add_document_text(text: str, metadata: dict[str, Any] | None = None) -> int:
    """Ingests a pre-processed document chunk into Qdrant vector database."""
    store = get_vector_store()
    doc = Document(page_content=text, metadata=metadata or {})
    store.add_documents([doc])
    return 1
#endregion
