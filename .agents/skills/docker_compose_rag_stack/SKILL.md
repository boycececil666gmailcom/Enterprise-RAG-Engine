---
name: docker_compose_rag_stack
description: Manage, build, and orchestrate the Enterprise RAG Engine multi-container stack (Qdrant, Neo4j, LangGraph Studio, Backend, Gateway, Ragas Evaluator) using Docker Compose with infra/docker-compose.yml.
---

# Enterprise RAG Engine Docker Compose Workflow

This skill provides standard operating procedures for managing the multi-container Enterprise RAG Engine stack using [`infra/docker-compose.yml`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/infra/docker-compose.yml).

## Services Overview

- **`qdrant`** (Port `6333`, `6334`): Vector database with BM25 sparse and dense embedding storage.
- **`neo4j`** (Port `7474`, `7687`): Graph database for GraphRAG entity relationships.
- **`langgraph-studio`** (Port `2024`): Interactive developer UI for LangGraph agent workflows.
- **`backend`** (Port `8000`): Stateful LangGraph FastAPI backend engine (`/query`, `/health`).
- **`gateway`** (Port `8080`): API Gateway proxy with request validation and routing.
- **`ragas-evaluator`**: Automated evaluation suite for RAG retrieval and generation metrics.

## Standard Operating Procedures

### 1. Build and Start All Services

Run the build and startup command in detached mode from the repository root:

```powershell
docker compose -f infra/docker-compose.yml up --build -d
```

### 2. Verify Container Health and Status

Check that all containers are healthy and ports are mapped correctly:

```powershell
docker compose -f infra/docker-compose.yml ps
```

### 3. Inspect Service Logs

Stream logs for specific services or the entire stack:

```powershell
# Follow backend and gateway logs
docker compose -f infra/docker-compose.yml logs -f backend gateway

# Follow all container logs
docker compose -f infra/docker-compose.yml logs -f
```

### 4. Health Check Verification

Validate that the services are answering requests:

```powershell
# Health check on Backend
curl http://localhost:8000/health

# Health check on Gateway
curl http://localhost:8080/health
```

### 5. Stop and Tear Down Stack(Only when instructed)

Stop and remove all containers and networks:

```powershell
# Stop services (preserve volumes)
docker compose -f infra/docker-compose.yml down

# Stop services and remove named volumes (clean slate)
docker compose -f infra/docker-compose.yml down -v
```
