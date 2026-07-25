from langchain_core.tools import tool
import src.theme_based_rag_backend.vector_db as db
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank

_compressor = None

def get_reranker() -> FlashrankRerank:
    """Helper to lazily instantiate and cache the FlashrankRerank instance."""
    global _compressor
    if _compressor is None:
        _compressor = FlashrankRerank(top_n=2)
    return _compressor

@tool
def retrieve_local_documents(query: str, original_query: str = None) -> str:
    """Retrieve semantically relevant document chunks from the local vector database,
    and structured relationships from the graph database.
    Use this tool when the query refers to private documentation, internal guidelines,
    project names (like 'Supernova'), or local workspace facts."""
    try:
        store = db.get_vector_store()
    except Exception as e:
        return f"Error: Local Vector database is not initialized: {e}"
    try:
        # Perform hybrid search natively in Qdrant (using query text directly or HyDE text if provided)
        docs = store.similarity_search(query, k=5)
        
        context_list = []
        if docs:
            # Apply FlashRank Cross-Encoder reranker using the original user query
            try:
                compressor = get_reranker()
                # If original_query is provided, use it for rerank query, otherwise fall back to query
                rerank_q = original_query if original_query else query
                reranked_docs = compressor.compress_documents(docs, rerank_q)
            except Exception as rerank_err:
                import logging
                logging.getLogger(__name__).warning(
                    f"FlashRank reranking failed, falling back to database rankings: {rerank_err}"
                )
                reranked_docs = docs[:2]
            
            # Format top chunks as output context
            for doc in reranked_docs:
                score = doc.metadata.get("relevance_score", 0.0)
                context_list.append(f"[Match Score: {score:.3f}] Content: {doc.page_content}")
                
        vector_context = "\n\n".join(context_list) if context_list else "No matching local documents found."
        
        # Retrieve context from Neo4j Graph Database
        graph_target = original_query if original_query else query
        try:
            import src.theme_based_rag_backend.graph_db as graph_db
            graph_context = graph_db.query_graph_context(graph_target)
        except Exception as graph_err:
            import logging
            logging.getLogger(__name__).warning(
                f"Failed to query Neo4j Graph DB: {graph_err}"
            )
            graph_context = f"Error querying Neo4j Graph DB: {graph_err}"
            
        combined_context = (
            f"=== VECTOR DATABASE CONTEXT ===\n{vector_context}\n\n"
            f"=== KNOWLEDGE GRAPH RELATIONSHIPS ===\n{graph_context}"
        )
        return combined_context
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error querying local documents: {str(e)}"
