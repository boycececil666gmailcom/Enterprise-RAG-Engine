#region Retrieval Tool
from flashrank import Ranker
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from langchain_core.tools import tool

from . import vector_db as db


@tool
def retrieve_VDB(query: str) -> str:
    """Retrieve semantically relevant document chunks using 3-Tier RAPTOR Tree Traversal (Root -> Section -> Leaf) with FlashRank reranking."""
    try:
        docs = db.retrieve_tree_traversal(query=query, top_k_layer0=2, top_k_layer1=3, top_k_layer2=10)
        if not docs:
            return "No matching vector documents found."

        # Rerank candidate leaf chunks using FlashRank Cross-Encoder
        reranker = FlashrankRerank(client=Ranker(), top_n=5)
        ranked_docs = reranker.compress_documents(docs, query)

        # Build context supporting Parent-Child / Small-to-Big retrieval
        formatted_chunks = []
        for doc in ranked_docs:
            score = doc.metadata.get("relevance_score", 0.0)
            breadcrumb = doc.metadata.get("breadcrumb", "")
            title = doc.metadata.get("title", "")
            # Prefer rich 'big' markdown content over 'small' summary if available
            content = doc.metadata.get("big") or doc.metadata.get("parent_content") or doc.page_content
            header = f"[{breadcrumb or title}] (Score: {score:.3f})" if (breadcrumb or title) else f"(Score: {score:.3f})"
            formatted_chunks.append(f"{header}\n{content}")

        return "=== VECTOR DATABASE CONTEXT (TREE TRAVERSAL) ===\n" + "\n\n".join(formatted_chunks)

    except Exception as e:
        return f"Vector search error: {e}"
#endregion
