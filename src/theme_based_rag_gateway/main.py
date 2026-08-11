import os
import logging
import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.theme_based_rag_gateway.models import QueryRequest, QueryResponse, IngestRequest, IngestResponse

#region Gateway Configuration Imports
from src.theme_based_rag_gateway.config import (
    RAG_BACKEND_URL,
    GATEWAY_HOST,
    GATEWAY_PORT,
    ALLOWED_ORIGINS,
    ALLOW_CREDENTIALS
)
#endregion

logger = logging.getLogger(__name__)

app = FastAPI(title="Theme-Based RAG Workflow Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize an async HTTP client for proxy routing
# Initialize an async HTTP client for proxy routing
async_client = httpx.AsyncClient(timeout=60.0)

#region Ingestion Proxy Endpoints
async def _proxy_ingest(target_url: str, request: IngestRequest) -> IngestResponse:
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/2] [{os.path.basename(__file__)}] API Gateway proxying ingestion request to: {target_url}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")
    try:
        response = await async_client.post(target_url, json=request.dict())
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Downstream error: {response.text}"
            )
        print(f"\n\033[1;96m========================================================\033[0m")
        print(f"\033[1;92m>>> [2/2] [{os.path.basename(__file__)}] API Gateway received success response from backend\033[0m")
        print(f"\033[1;96m========================================================\033[0m\n")
        return IngestResponse(**response.json())
    except httpx.RequestError as exc:
        logger.error(f"Failed connecting to downstream backend at {target_url}: {exc}")
        raise HTTPException(
            status_code=503, 
            detail=f"Downstream service unavailable: {str(exc)}"
        )

@app.post("/ingest/vector", response_model=IngestResponse)
async def route_ingest_vector(request: IngestRequest):
    """Proxies vector store ingestion requests downstream to core RAG backend."""
    target_url = f"{RAG_BACKEND_URL.rstrip('/')}/ingest/vector"
    return await _proxy_ingest(target_url, request)

@app.post("/ingest/graph", response_model=IngestResponse)
async def route_ingest_graph(request: IngestRequest):
    """Proxies graph store ingestion requests downstream to core RAG backend."""
    target_url = f"{RAG_BACKEND_URL.rstrip('/')}/ingest/graph"
    return await _proxy_ingest(target_url, request)
#endregion

@app.post("/query", response_model=QueryResponse)
async def route_query(request: QueryRequest):
    """Proxies query requests downstream to the core RAG backend."""
    target_url = f"{RAG_BACKEND_URL.rstrip('/')}/query"
    
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/2] [{os.path.basename(__file__)}] API Gateway proxying query request to: {target_url}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")
    
    try:
        response = await async_client.post(target_url, json=request.dict())
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Downstream error: {response.text}"
            )
            
        print(f"\n\033[1;96m========================================================\033[0m")
        print(f"\033[1;92m>>> [2/2] [{os.path.basename(__file__)}] API Gateway received success response from backend\033[0m")
        print(f"\033[1;96m========================================================\033[0m\n")
        
        return QueryResponse(**response.json())
    except httpx.RequestError as exc:
        logger.error(f"Failed connecting to downstream backend at {target_url}: {exc}")
        raise HTTPException(
            status_code=503, 
            detail=f"Downstream service unavailable: {str(exc)}"
        )

@app.get("/health")
async def health_check():
    """Confirms gateway is running and pings downstream backend to verify full network connection path."""
    backend_status = "unreachable"
    target_url = f"{RAG_BACKEND_URL.rstrip('/')}/health"
    try:
        response = await async_client.get(target_url)
        if response.status_code == 200:
            backend_status = "healthy"
        else:
            backend_status = f"unhealthy (status {response.status_code})"
    except Exception as e:
        logger.warning(f"Health check failed to contact downstream backend: {e}")

    return {
        "status": "ok",
        "service": "Theme-Based RAG Workflow Gateway",
        "downstream_backend": {
            "endpoint": RAG_BACKEND_URL,
            "status": backend_status
        }
    }

if __name__ == "__main__":
    uvicorn.run("src.theme_based_rag_gateway.main:app", host=GATEWAY_HOST, port=GATEWAY_PORT, reload=True)
