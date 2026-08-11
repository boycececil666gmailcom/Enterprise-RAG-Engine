#region Imports & Setup
import os
import logging
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, HTTPException

logger = logging.getLogger(__name__)

from src.theme_based_rag_backend.config import BACKEND_HOST, BACKEND_PORT, GEMINI_MODEL
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
        element_count = graph_db.ingest_graph_document(request.text)
        return IngestResponse(status="success", chunk_count=element_count)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
#endregion

#region Query Workflow & Health Check Endpoints
@app.post("/query", response_model=QueryResponse)
async def run_query(request: QueryRequest):
    try:
        # Map input payload to LangGraph state
        inputs = {
            "query": request.query,
            "history": [{"role": msg.role, "content": msg.content} for msg in request.history],
            "should_answer": "refuse",
            "should_hyde": True,
            "hyde_reason": None,
            "hyde_content": None,
            "retrieved_documents": None,
            "final_response": "",
            "critique_feedback": None,
            "attempt_count": 0
        }
        
        # Execute workflow graph asynchronously
        result = await agent_graph.ainvoke(inputs)
        
        tool_calls_executed = []
        if result.get("retrieved_documents"):
            tool_calls_executed.append("retrieve_VDB")
            
        return QueryResponse(
            response=result.get("final_response", ""),
            tool_calls_executed=tool_calls_executed,
            should_hyde=result.get("should_hyde"),
            hyde_reason=result.get("hyde_reason"),
            hyde_content=result.get("hyde_content"),
            retrieved_documents=result.get("retrieved_documents"),
            history=result.get("history")
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
        vector_ok = "degraded (pending API key)"
        
    return {
        "status": "ok",
        "model": GEMINI_MODEL,
        "platform": "Theme-Based RAG Workflow",
        "vector_store": vector_ok
    }
#endregion

#region Execution Entry Point
if __name__ == "__main__":
    uvicorn.run("src.theme_based_rag_backend.main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=True)
#endregion
