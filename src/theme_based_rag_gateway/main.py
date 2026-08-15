#region App Setup
import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .config import (
    ALLOW_CREDENTIALS,
    ALLOWED_ORIGINS,
    GATEWAY_HOST,
    GATEWAY_PORT,
    RAG_BACKEND_URL,
)
from .models import (
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse,
)

app = FastAPI(title="Theme-Based RAG Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

async_client = httpx.AsyncClient(timeout=60.0)
#endregion

#region Proxy Helper
async def _proxy_post(endpoint: str, payload: BaseModel) -> dict:
    """Forwards POST request to downstream RAG backend."""
    target_url = f"{RAG_BACKEND_URL.rstrip('/')}{endpoint}"
    try:
        response = await async_client.post(target_url, json=payload.model_dump())
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"Downstream service unavailable: {str(exc)}")
#endregion

#region Gateway Endpoints
@app.post("/ingest/vector", response_model=IngestResponse)
async def route_ingest_vector(request: IngestRequest):
    """Proxies vector store ingestion request downstream."""
    data = await _proxy_post("/ingest/vector", request)
    return IngestResponse(**data)


@app.post("/ingest/graph", response_model=IngestResponse)
async def route_ingest_graph(request: IngestRequest):
    """Proxies graph store ingestion request downstream."""
    data = await _proxy_post("/ingest/graph", request)
    return IngestResponse(**data)


@app.post("/query", response_model=QueryResponse)
async def route_query(request: QueryRequest):
    """Proxies query request downstream to core RAG backend."""
    data = await _proxy_post("/query", request)
    return QueryResponse(**data)


@app.get("/health")
async def health_check():
    """Checks gateway health and pings downstream backend."""
    backend_status = "unreachable"
    try:
        res = await async_client.get(f"{RAG_BACKEND_URL.rstrip('/')}/health")
        backend_status = "healthy" if res.status_code == 200 else f"unhealthy ({res.status_code})"
    except Exception:
        pass

    return {
        "status": "ok",
        "service": "Theme-Based RAG Gateway",
        "downstream_backend": {
            "endpoint": RAG_BACKEND_URL,
            "status": backend_status,
        },
    }
#endregion

#region Server Runner
if __name__ == "__main__":
    uvicorn.run("src.theme_based_rag_gateway.main:app", host=GATEWAY_HOST, port=GATEWAY_PORT, reload=True)
#endregion
