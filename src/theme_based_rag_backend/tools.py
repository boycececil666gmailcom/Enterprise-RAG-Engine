#region Imports & Setup
from langchain_core.tools import tool
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from . import vector_db as db
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
            # Parent-Child (Small-to-Big) Retrieval:
            # Similarity matching is performed on granular child chunks (page_content),
            # while rich full context (parent_content) is supplied to LLM synthesis.
            content = doc.metadata.get("parent_content") or doc.page_content
            vector_list.append(f"[Match Score: {score:.3f}] Content: {content}")
            
        return "=== VECTOR DATABASE CONTEXT ===\n" + "\n\n".join(vector_list)
        
    except Exception as e:
        return f"Vector search error: {e}"
#endregion
