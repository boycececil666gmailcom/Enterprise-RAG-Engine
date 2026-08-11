#region Imports & Setup
from langchain_core.tools import tool
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
import src.theme_based_rag_backend.vector_db as db


@tool
def retrieve_local_documents(query: str) -> str:
    """Retrieve semantically relevant document chunks and knowledge graph relationships.
    Use this tool when the query refers to private documentation, internal guidelines,
    project names (like 'Supernova'), or local workspace facts."""
    try:
        store = db.get_vector_store()
    except Exception as e:
        return f"Error: Local Vector database is not initialized: {e}"
        
    # 1. Vector DB Hybrid Search (Qdrant)
    vector_docs = []
    try:
        docs = store.similarity_search(query, k=5)
        if docs:
            # Apply FlashRank Cross-Encoder reranker using the original user query
            try:
                vector_docs = FlashrankRerank(top_n=2).compress_documents(docs, query)
            except Exception as rerank_err:
                import logging
                logging.getLogger(__name__).warning(
                    f"FlashRank reranking failed, falling back to database rankings: {rerank_err}"
                )
                vector_docs = docs[:2]
    except Exception as e:
        import logging
        logging.getLogger(__name__).warning(f"Vector search failed: {e}")
        
    # 2. Graph DB Search (Neo4j)
    graph_context = ""
    try:
        from src.theme_based_rag_backend.graph_db import extract_query_entities, retrieve_graph_relations
        query_entities = extract_query_entities(query)
        if query_entities:
            graph_context = retrieve_graph_relations(query_entities)
    except Exception as graph_err:
        import logging
        logging.getLogger(__name__).warning(f"Graph database search failed: {graph_err}")
        
    # 3. Format and Merge Context
    if not vector_docs and not graph_context:
        return "No matching local documents or graph relations found."
        
    context_parts = []
    
    if vector_docs:
        vector_list = []
        for doc in vector_docs:
            score = doc.metadata.get("relevance_score", 0.0)
            vector_list.append(f"[Match Score: {score:.3f}] Content: {doc.page_content}")
        context_parts.append("=== VECTOR DATABASE CONTEXT ===\n" + "\n\n".join(vector_list))
    else:
        context_parts.append("=== VECTOR DATABASE CONTEXT ===\nNo matching vector documents found.")
        
    if graph_context:
        context_parts.append(f"=== KNOWLEDGE GRAPH CONTEXT ===\n{graph_context}")
    else:
        context_parts.append("=== KNOWLEDGE GRAPH CONTEXT ===\nNo relevant graph relations found.")
        
    return "\n\n".join(context_parts)
