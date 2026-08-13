#region Imports & Setup
from flashrank import Ranker
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from langchain_core.tools import tool

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

    # 1. Qdrant Hybrid Search (Dense Embeddings + FastEmbed BM25 Sparse)
    try:
        # Note: store is initialized with RetrievalMode.HYBRID in vector_db.py,
        # so similarity_search automatically executes hybrid search (dense + sparse BM25).
        docs = store.similarity_search(query, k=20)
        if not docs:
            return "No matching vector documents found."
            
        # 2. FlashRank Cross-Encoder Reranker
        vector_docs = FlashrankRerank(client=Ranker(), top_n=5).compress_documents(docs, query)
            
        vector_list = []
        for doc in vector_docs:
            score = doc.metadata.get("relevance_score", 0.0)
            # Parent-Child (Small-to-Big) Retrieval:
            # Similarity matching is performed on granular child chunks (page_content),
            # while rich full context (parent_content) is supplied to LLM synthesis.
            content = doc.metadata.get("parent_content") or doc.page_content
            page_title = doc.metadata.get("page_title", "")
            vector_list.append(f"[Match Score: {score:.3f}] {page_title}Content: {content}")
            
        return "=== VECTOR DATABASE CONTEXT ===\n" + "\n\n".join(vector_list)
        
    except Exception as e:
        return f"Vector search error: {e}"
#endregion
