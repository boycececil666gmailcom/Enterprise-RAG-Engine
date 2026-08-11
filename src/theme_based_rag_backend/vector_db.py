#region Imports & Configuration
import os
import sys
import logging
from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.theme_based_rag_backend.config import QDRANT_URL, QDRANT_API_KEY, GEMINI_API_KEY, GEMINI_EMBED_MODEL
#endregion

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
    try:
        if embeddings is None:
            api_key = GEMINI_API_KEY if (GEMINI_API_KEY and GEMINI_API_KEY.strip()) else "dummy_key_for_testing"
            embeddings = GoogleGenerativeAIEmbeddings(
                model=GEMINI_EMBED_MODEL,
                google_api_key=api_key
            )
            print(f"Initialized Google Gemini Embeddings Model: {GEMINI_EMBED_MODEL}")

        if sparse_embeddings is None:
            try:
                sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")
                print("Initialized FastEmbed BM25 Sparse Embeddings Model")
            except Exception as se_err:
                print(f"Sparse embeddings skipped: {se_err}")
                sparse_embeddings = None

        sparse_kwargs = {}
        if sparse_embeddings is not None:
            sparse_kwargs["sparse_embedding"] = sparse_embeddings
            sparse_kwargs["retrieval_mode"] = RetrievalMode.HYBRID

        if "pytest" in sys.modules or QDRANT_URL == ":memory:":
            print("Running in-memory Qdrant Client for testing...")
            vector_store = QdrantVectorStore.from_documents(
                [],
                embedding=embeddings,
                location=":memory:",
                collection_name="local_rag_documents",
                **sparse_kwargs
            )
        elif QDRANT_URL:
            print(f"Connecting to remote Qdrant DB server at {QDRANT_URL}")
            try:
                vector_store = QdrantVectorStore.from_existing_collection(
                    url=QDRANT_URL,
                    api_key=QDRANT_API_KEY,
                    collection_name="local_rag_documents",
                    embedding=embeddings,
                    **sparse_kwargs
                )
            except Exception:
                print("Collection 'local_rag_documents' not found. Creating a new one...")
                try:
                    init_doc = Document(page_content="System Vector DB initialized.", metadata={"system": "init"})
                    vector_store = QdrantVectorStore.from_documents(
                        [init_doc],
                        url=QDRANT_URL,
                        api_key=QDRANT_API_KEY,
                        collection_name="local_rag_documents",
                        embedding=embeddings,
                        **sparse_kwargs
                    )
                except Exception as create_err:
                    print(f"Vector DB collection creation deferred (pending valid API key): {create_err}")
                    init_error = create_err
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

