import os
import logging
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, HTTPException

logger = logging.getLogger(__name__)

#region Module Imports & App Setup
from src.theme_based_rag_backend.config import HOST, PORT, GEMINI_MODEL
import src.theme_based_rag_backend.vector_db as db
import src.theme_based_rag_backend.graph_db as graph_db
from src.theme_based_rag_backend.models import QueryRequest, QueryResponse, IngestRequest, IngestResponse
from src.theme_based_rag_backend.agent_flow import agent_graph

app = FastAPI(title="Theme-Based RAG Workflow Backend")
#endregion

#region Document Ingestion Endpoints
@app.post("/ingest/vector", response_model=IngestResponse)
async def ingest_vector_document(request: IngestRequest):
    """Ingests document text specifically into Qdrant Vector Database."""
    try:
        print(f"\n\033[1;96m========================================================\033[0m")
        print(f"\033[1;92m>>> [{os.path.basename(__file__)}] Forwarding ingestion request to Vector Store\033[0m")
        print(f"\033[1;96m========================================================\033[0m\n")
        chunk_count = db.add_document_text(request.text, request.metadata)
        return IngestResponse(status="success", chunk_count=chunk_count)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest/graph", response_model=IngestResponse)
async def ingest_graph_document(request: IngestRequest):
    """Ingests document text specifically into Neo4j Graph Database."""
    try:
        print(f"\n\033[1;96m========================================================\033[0m")
        print(f"\033[1;92m>>> [{os.path.basename(__file__)}] Forwarding ingestion request to Graph Store\033[0m")
        print(f"\033[1;96m========================================================\033[0m\n")
        element_count = graph_db.ingest_graph_document(request.text)
        return IngestResponse(status="success", chunk_count=element_count)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
#endregion

@app.post("/query", response_model=QueryResponse)
async def run_query(request: QueryRequest):
    try:
        # Map input payload to LangGraph state
        inputs = {
            "message": request.message,
            "history": [{"role": msg.role, "content": msg.content} for msg in request.history],
            "category": "refuse",
            "use_hyde": True,
            "hyde_reason": None,
            "hypothetical_document": None,
            "retrieved_documents": None,
            "agent_response": "",
            "critique_feedback": None,
            "attempts": 0
        }
        
        # Execute workflow graph asynchronously
        result = await agent_graph.ainvoke(inputs)
        
        tool_calls_executed = []
        if result.get("retrieved_documents"):
            tool_calls_executed.append("retrieve_local_documents")
            
        return QueryResponse(
            response=result.get("agent_response", ""),

            tool_calls_executed=tool_calls_executed,
            use_hyde=result.get("use_hyde"),
            hyde_reason=result.get("hyde_reason"),
            hypothetical_document=result.get("hypothetical_document"),
            retrieved_documents=result.get("retrieved_documents")
        )


    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Query execution error: {str(e)}")


@app.get("/health")
async def health_check():
    try:
        db.get_vector_store()
        vector_ok = "ok"
    except Exception as e:
        logger.error(f"Health check failed to initialize vector store: {e}")
        raise HTTPException(
            status_code=503,
            detail=f"Vector store initialization failed: {str(e)}"
        )
        
    return {
        "status": "ok",
        "model": GEMINI_MODEL,
        "platform": "Theme-Based RAG Workflow",
        "vector_store": vector_ok
    }

if __name__ == "__main__":
    uvicorn.run("src.theme_based_rag_backend.main:app", host=HOST, port=PORT, reload=True)
