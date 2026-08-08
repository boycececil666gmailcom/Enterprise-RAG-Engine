#region Imports & Configuration
import os
import sys
import logging
from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_core.documents import Document
from src.theme_based_rag_backend.config import QDRANT_URL, QDRANT_API_KEY, GEMINI_API_KEY, GEMINI_EMBED_MODEL

logger = logging.getLogger(__name__)

# Initialize embeddings and vector DB lazily
embeddings = None
sparse_embeddings = None
vector_store = None
init_error = None
#endregion

#region Vector Database Initialization
def get_vector_store():
    global vector_store, init_error, embeddings, sparse_embeddings
    if vector_store is not None:
        return vector_store

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured in the environment variables.")

    try:
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        if embeddings is None:
            embeddings = GoogleGenerativeAIEmbeddings(
                model=GEMINI_EMBED_MODEL,
                google_api_key=GEMINI_API_KEY
            )
            print(f"Initialized Google Gemini Embeddings Model: {GEMINI_EMBED_MODEL}")

        if sparse_embeddings is None:
            sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")
            print("Initialized FastEmbed BM25 Sparse Embeddings Model")

        if "pytest" in sys.modules or QDRANT_URL == ":memory:":
            print("Running in-memory Qdrant Client for testing...")
            vector_store = QdrantVectorStore.from_documents(
                [],
                embedding=embeddings,
                sparse_embedding=sparse_embeddings,
                location=":memory:",
                collection_name="local_rag_documents",
                retrieval_mode=RetrievalMode.HYBRID
            )
        elif QDRANT_URL:
            print(f"Connecting to remote Qdrant DB server at {QDRANT_URL}")
            try:
                vector_store = QdrantVectorStore.from_existing_collection(
                    url=QDRANT_URL,
                    api_key=QDRANT_API_KEY,
                    collection_name="local_rag_documents",
                    embedding=embeddings,
                    sparse_embedding=sparse_embeddings,
                    retrieval_mode=RetrievalMode.HYBRID
                )
            except Exception:
                print("Collection 'local_rag_documents' not found. Creating a new one...")
                vector_store = QdrantVectorStore.from_documents(
                    [],
                    url=QDRANT_URL,
                    api_key=QDRANT_API_KEY,
                    collection_name="local_rag_documents",
                    embedding=embeddings,
                    sparse_embedding=sparse_embeddings,
                    retrieval_mode=RetrievalMode.HYBRID
                )
        else:
            raise ValueError("QDRANT_URL environment variable is not configured.")
        init_error = None
        return vector_store
    except Exception as e:
        init_error = str(e)
        print(f"Error initializing vector database or embeddings: {e}")
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
    Directly ingests a pre-processed document chunk into Qdrant vector database and Neo4j graph database.
    All chunking and optimization strategies are managed upstream by preprocessing-pipeline.
    """
    store = get_vector_store()
    doc = Document(page_content=text, metadata=metadata or {})
    store.add_documents([doc])

    # Process Neo4j knowledge graph ingestion
    try:
        from src.theme_based_rag_backend.graph_db import extract_entities_and_relations, add_graph_relations
        extracted = extract_entities_and_relations(text)
        if extracted.get("entities") or extracted.get("relationships"):
            add_graph_relations(extracted["entities"], extracted["relationships"])
    except Exception as e:
        logger.warning(f"Failed to ingest data into Neo4j graph database: {e}")

    return 1
#endregion
