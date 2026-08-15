#region App Setup
import uvicorn
from fastapi import FastAPI, HTTPException

from . import vector_db
from .agent_flow import agent_graph
from .config import BACKEND_HOST, BACKEND_PORT, GEMINI_MODEL
from .models import QueryRequest, QueryResponse

app = FastAPI(title="Theme-Based RAG Backend")
#endregion

#region Query Endpoints
@app.post("/query", response_model=QueryResponse)
async def run_query(request: QueryRequest):
    """Executes the agent workflow graph for user queries."""
    try:
        inputs = {
            "query": request.query,
            "history": [msg.model_dump() for msg in request.history],
            "attempt_count": 0,
        }
        result = await agent_graph.ainvoke(inputs)
        tools_used = ["retrieve_VDB"] if result.get("retrieved_documents") else []

        return QueryResponse(
            response=result.get("final_response", ""),
            tool_calls_executed=tools_used,
            should_hyde=result.get("should_hyde"),
            hyde_reason=result.get("hyde_reason"),
            hyde_content=result.get("hyde_content"),
            retrieved_documents=result.get("retrieved_documents"),
            history=result.get("history"),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query error: {str(e)}")


@app.get("/health")
async def health_check():
    """Returns backend and vector store health status."""
    try:
        vector_db.get_layer_store(2)
        vector_ok = "ok"
    except Exception:
        vector_ok = "degraded"

    return {
        "status": "ok",
        "model": GEMINI_MODEL,
        "platform": "Theme-Based RAG Workflow",
        "vector_store": vector_ok,
    }
#endregion

#region Server Runner
if __name__ == "__main__":
    uvicorn.run("src.theme_based_rag_backend.main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=True)
#endregion
