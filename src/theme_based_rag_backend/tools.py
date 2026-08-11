#region Imports & Setup
import logging
from langchain_core.tools import tool
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
import src.theme_based_rag_backend.vector_db as db

logger = logging.getLogger(__name__)
#endregion


#region Vector DB Retrieval Tool
@tool
def retrieve_VDB(query: str) -> str:
    """Retrieve semantically relevant document chunks from Vector Database (Qdrant) with FlashRank reranking.
    Use this tool to find documentation, guidelines, project facts, or local workspace context."""
    
    try:
        store = db.get_vector_store()
    except Exception as e:
        return f"Error: Local Vector database is not initialized: {e}"

    # 1. Vector DB Hybrid Search (Qdrant)
    try:
        docs = store.similarity_search(query, k=5)
        if not docs:
            return "No matching vector documents found."
            
        # 2. FlashRank Cross-Encoder Reranker
        vector_docs = FlashrankRerank(top_n=2).compress_documents(docs, query)
            
        vector_list = []
        for doc in vector_docs:
            score = doc.metadata.get("relevance_score", 0.0)
            vector_list.append(f"[Match Score: {score:.3f}] Content: {doc.page_content}")
            
        return "=== VECTOR DATABASE CONTEXT ===\n" + "\n\n".join(vector_list)
        
    except Exception as e:
        logger.warning(f"Vector search failed: {e}")
        return f"Vector search error: {e}"
#endregion
