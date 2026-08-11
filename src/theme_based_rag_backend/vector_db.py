#region Imports & Configuration
import os
import sys
import logging
from functools import lru_cache
from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_core.documents import Document
from src.theme_based_rag_backend.config import QDRANT_URL, QDRANT_API_KEY
from src.theme_based_rag_backend.llm_client import embeddings

logger = logging.getLogger(__name__)
#endregion

#region Helper & Vector Database Initialization
@lru_cache(maxsize=1)
def get_sparse_embeddings():
    """Lazily initializes and caches FastEmbed BM25 sparse embeddings model."""
    try:
        sparse = FastEmbedSparse(model_name="Qdrant/bm25")
        logger.info("Initialized FastEmbed BM25 Sparse Embeddings Model")
        return sparse
    except Exception as se_err:
        logger.warning(f"Sparse embeddings skipped: {se_err}")
        return None

@lru_cache(maxsize=1)
def get_vector_store():
    """Lazily initializes and caches QdrantVectorStore using lru_cache."""
    try:
        logger.info(f"Using shared Google Gemini Embeddings Model: {embeddings.model}")
        sparse = get_sparse_embeddings()

        sparse_kwargs = {}
        if sparse is not None:
            sparse_kwargs["sparse_embedding"] = sparse
            sparse_kwargs["retrieval_mode"] = RetrievalMode.HYBRID

        if "pytest" in sys.modules or QDRANT_URL == ":memory:":
            logger.info("Running in-memory Qdrant Client for testing...")
            return QdrantVectorStore.from_documents(
                [],
                embedding=embeddings,
                location=":memory:",
                collection_name="local_rag_documents",
                **sparse_kwargs
            )
        elif QDRANT_URL:
            logger.info(f"Connecting to remote Qdrant DB server at {QDRANT_URL}")
            try:
                return QdrantVectorStore.from_existing_collection(
                    url=QDRANT_URL,
                    api_key=QDRANT_API_KEY,
                    collection_name="local_rag_documents",
                    embedding=embeddings,
                    **sparse_kwargs
                )
            except Exception:
                logger.info("Collection 'local_rag_documents' not found. Creating a new one...")
                init_doc = Document(page_content="System Vector DB initialized.", metadata={"system": "init"})
                return QdrantVectorStore.from_documents(
                    [init_doc],
                    url=QDRANT_URL,
                    api_key=QDRANT_API_KEY,
                    collection_name="local_rag_documents",
                    embedding=embeddings,
                    **sparse_kwargs
                )
        else:
            raise ValueError("QDRANT_URL environment variable is not configured.")
    except Exception as e:
        logger.error(f"Error initializing vector database or embeddings: {e}")
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

