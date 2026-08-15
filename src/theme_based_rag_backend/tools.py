#region Retrieval Tool
from flashrank import Ranker
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from langchain_core.tools import tool

from . import vector_db as db


@tool
def retrieve_VDB(query: str) -> str:
    """Retrieve semantically relevant document chunks from Vector Database (Qdrant) with FlashRank reranking."""
    try:
        store = db.get_vector_store()
        docs = store.similarity_search(query, k=20)
        if not docs:
            return "No matching vector documents found."

        # Rerank retrieved candidate documents
        reranker = FlashrankRerank(client=Ranker(), top_n=5)
        ranked_docs = reranker.compress_documents(docs, query)

        # Build context supporting Parent-Child (Small-to-Big) retrieval
        formatted_chunks = []
        for doc in ranked_docs:
            score = doc.metadata.get("relevance_score", 0.0)
            content = doc.metadata.get("parent_content") or doc.page_content
            page_title = doc.metadata.get("page_title", "")
            formatted_chunks.append(f"[Match Score: {score:.3f}] {page_title}Content: {content}")

        return "=== VECTOR DATABASE CONTEXT ===\n" + "\n\n".join(formatted_chunks)

    except Exception as e:
        return f"Vector search error: {e}"
#endregion
