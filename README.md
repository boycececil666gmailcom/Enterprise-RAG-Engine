# Enterprise-RAG-Engine

> Modular, enterprise-grade Retrieval-Augmented Generation (RAG) backend engine template with multi-agent orchestration, hybrid vector search, and GraphRAG entity-relationship reasoning.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-1C3C3C?style=flat&logo=langchain&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=flat&logo=langchain&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-DeepSeek_V4_Flash-6366F1?style=flat)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-DC2626?style=flat&logo=qdrant&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-Graph_DB-008CC1?style=flat&logo=neo4j&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=flat&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=flat&logo=kubernetes&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## End-to-End Pipeline Architecture

```mermaid
---
config:
  theme: neutral
---
flowchart LR
    A["1. Data Ingestion<br/>(Crawl4AI & RAPTOR)"] --> B[("2. Hybrid Knowledge Store<br/>(Qdrant & Neo4j)")]
    B --> C["3. Multi-Agent Retrieval<br/>(HyDE + Dense + BM25)"]
    C --> D["4. Neural Rerank<br/>(FlashRank Cross-Encoder)"]
    D --> E["5. Self-Critique Loop<br/>& Answer Generation"]
    E --> F["6. LLMOps Evaluation<br/>(LangSmith & Ragas)"]
```

---

## 1. Core Purpose & Business Value

The **Enterprise-RAG-Engine** eliminates the guesswork from AI-powered customer support by restricting every generated answer to verified, company-owned knowledge — making hallucination structurally impossible.

- **Zero Hallucination, 100% Accuracy**: Every customer response is grounded in the company's own documentation and knowledge base, guaranteeing factual accuracy with no invented information.
- **Domain Boundary Enforcement**: The engine automatically rejects off-topic inquiries, keeping support conversations strictly within defined business domains (e.g., Fintech SaaS product documentation).
- **Comprehensive Knowledge Coverage**: Combines traditional document search with intelligent entity-relationship mapping, surfacing connections between products, pricing tiers, and organizational hierarchies that simple search cannot find.
- **Self-Correcting Quality Assurance**: An automated review loop verifies every draft answer against source material before delivery, catching errors before customers ever see them.
- **Plug-and-Play Backend Template**: The decoupled microservices architecture means this engine can be connected to any customer portal, mobile app, or internal tool with minimal integration effort.
- **Intelligent Query Enhancement**: Automatically improves vague or abstract questions via hypothetical document expansion, maximizing the chance of surfacing the most relevant knowledge for complex queries.

---

## 2. System Architecture & Technical Execution

The platform separates an API Gateway proxy (`theme_based_rag_gateway`) from the core RAG engine (`theme_based_rag_backend`). The backend runs a stateful multi-node LangGraph agent that performs domain classification, optional HyDE query expansion, hybrid vector + graph retrieval, neural reranking (FlashRank), and a self-critique quality loop before returning a response.

### Core Concept & Phased Execution Sequence

```mermaid
---
config:
  theme: neutral
---
sequenceDiagram
    autonumber
    actor Client as Client App / End User
    participant GW as API Gateway (port 8080)
    participant BE as RAG Backend (port 8000)
    participant AG as LangGraph Agent
    participant VDB as Qdrant Vector DB (port 6333)
    participant GDB as Neo4j Graph DB (port 7687)

    Note over Client, GW: Phase 1: Query Submission
    Client->>GW: POST /query (message, history)
    GW->>BE: Proxy POST /query via httpx (internal network)

    Note over BE, AG: Phase 2: Agent Execution Loop
    BE->>AG: Invoke StateGraph (AgentState)
    AG->>AG: node_classifier - Classify domain scope

    alt Query within business domain
        rect rgb(240, 243, 246)
            AG->>AG: node_hyde_decision - Evaluate HyDE necessity
            AG->>AG: node_hyde_generator - Generate hypothetical document (if enabled)
            AG->>VDB: Hybrid dense+sparse vector search (Qdrant BM25 + Gemini embeddings)
            AG->>GDB: Cypher graph query - extract entity relationships (Neo4j Bolt)
            AG->>AG: node_retrieve - Retrieve context & rerank (Qdrant + FlashRank)
            AG->>AG: node_generate - Synthesize grounded answer from context
            AG->>AG: node_critique - Self-critique quality check
        end
    else Query outside business domain
        rect rgb(250, 235, 235)
            AG->>AG: node_refuse - Generate polite refusal message
        end
    end

    Note over AG, BE: Phase 3: Response Delivery
    AG-->>BE: Return final AgentState (agent_response)
    BE-->>GW: QueryResponse (response, retrieved_documents, hyde metadata)
    GW-->>Client: Final verified answer
```

---

### High-Level Target Production Architecture

```mermaid
---
config:
  layout: elk
  theme: neutral
---
flowchart TB

    subgraph Client["Client"]
        User["Browser / Mobile App / API Consumer"]
    end

    subgraph Edge["Edge Layer"]
        CDN["CDN (Cloudflare / AWS CloudFront)"]
        LB["Load Balancer (Nginx / HAProxy)"]
        Ingress["Kubernetes Nginx Ingress Controller"]
    end

    subgraph GatewaySvc["API Gateway Service (theme-based-rag-gateway)"]
        GW["Gateway Handler (FastAPI + Uvicorn, port 8080)"]
        GWQuery["POST /query"]
        GWIngest["POST /ingest"]
        GWHealth["GET /health"]
    end

    subgraph BackendSvc["RAG Backend Service (theme-based-rag-backend)"]
        BE["Backend Handler (FastAPI + Uvicorn, port 8000)"]
        subgraph AgentGraph["LangGraph Agent StateGraph"]
            Classifier["node_classifier"]
            HyDEDecision["node_hyde_decision"]
            HyDEGen["node_hyde_generator"]
            Retrieve["node_retrieve"]
            Generate["node_generate"]
            Critique["node_critique"]
            Refuse["node_refuse"]
        end
    end

    subgraph VectorStore["Qdrant Vector DB (StatefulSet)"]
        QdrantAPI["REST API (port 6333)"]
        QdrantGRPC["gRPC (port 6334)"]
        QdrantPVC[("PVC: qdrant-storage 5Gi")]
    end

    subgraph GraphStore["Neo4j Graph DB (StatefulSet)"]
        Neo4jBolt["Bolt Protocol (port 7687)"]
        Neo4jHTTP["HTTP Browser (port 7474)"]
        Neo4jPVC[("PVC: neo4j-data 5Gi")]
    end

    subgraph Observability["Observability"]
        LangSmith["LangSmith Tracing (api.smith.langchain.com)"]
    end

    subgraph SecretsLayer["Kubernetes Secrets"]
        GeminiSec["gemini-secrets (GEMINI_API_KEY)"]
        LangchainSec["langchain-secrets (LANGSMITH_API_KEY)"]
        Neo4jSec["neo4j-secrets (NEO4J_USERNAME / PASSWORD)"]
    end

    User --> CDN
    CDN --> LB
    LB --> Ingress
    Ingress --> GW

    GW --> BE
    BE --> AgentGraph
    AgentGraph --> QdrantAPI
    AgentGraph --> Neo4jBolt
    AgentGraph --> LangSmith

    QdrantAPI --> QdrantPVC
    Neo4jBolt --> Neo4jPVC

    BE --> GeminiSec
    BE --> LangchainSec
    BE --> Neo4jSec
```

---

### Kubernetes Network & Service Isolation Design

```mermaid
---
config:
  layout: elk
  theme: neutral
---
flowchart TB

    subgraph Outside["Outside World"]
        ExternalClient["curl / Browser / Frontend App / pytest"]
    end

    subgraph Exposed["Exposed to Host via Nginx Ingress"]
        GW["theme-based-rag-gateway (FastAPI + Uvicorn)<br/>NodePort: 30080 / Service: port 8080<br/>Routes: POST /query, POST /ingest/vector, POST /ingest/graph, GET /health"]
    end

    subgraph Internal["Kubernetes Internal Network (rag-engine namespace) - not reachable from outside"]

        subgraph BackendCtr["theme-based-rag-backend (FastAPI + Uvicorn, ClusterIP port 80 -> 8000)"]
            direction TB
            BEQueryH["POST /query - invoke LangGraph StateGraph"]
            BEIngestH["POST /ingest/vector & /ingest/graph - store embeddings & knowledge graph"]
            BEHealthH["GET /health - ping vector store"]
        end

        subgraph QdrantCtr["qdrant (StatefulSet, Headless Service port 6333/6334)"]
            direction TB
            QdrantREST["REST: port 6333"]
            QdrantGRPC["gRPC: port 6334"]
            QdrantData[("collection: local_rag_documents<br/>dense: gemini-embedding-001<br/>sparse: Qdrant/bm25<br/>PVC: qdrant-storage 5Gi")]
        end

        subgraph Neo4jCtr["neo4j (StatefulSet, Headless Service port 7474/7687)"]
            direction TB
            Neo4jBrowserPort["HTTP Browser: port 7474"]
            Neo4jBoltPort["Bolt: port 7687"]
            Neo4jData[("nodes: Entity<br/>relationships: RELATED_TO<br/>PVC: neo4j-data 5Gi")]
        end

        subgraph SecretsCtr["Kubernetes Opaque Secrets"]
            direction TB
            S1["gemini-secrets: GEMINI_API_KEY"]
            S2["neo4j-secrets: NEO4J_USERNAME / NEO4J_PASSWORD / NEO4J_AUTH"]
            S3["langchain-secrets: LANGSMITH_API_KEY"]
        end

    end

    ExternalClient -->|"NodePort 30080 / Nginx Ingress - only exposed entry point"| GW
    GW -->|"httpx POST /query or /ingest (ClusterIP internal)"| BackendCtr
    BEQueryH -->|"hybrid search: dense + BM25 sparse"| QdrantREST
    BEIngestH -->|"upsert embedding vectors"| QdrantREST
    BEQueryH -->|"Cypher MATCH query via Bolt"| Neo4jBoltPort
    BEIngestH -->|"CREATE Entity + RELATED_TO relationships"| Neo4jBoltPort
    BackendCtr -->|"env injection from secrets"| SecretsCtr
```

---

## 3. Repository Structure

```text
Enterprise-RAG-Engine/
├── infra/
│   └── terraform/
│       ├── backend.tf                 # Backend Deployment + ClusterIP Service
│       ├── gateway.tf                 # Gateway Deployment + NodePort Service
│       ├── ingress.tf                 # Nginx Ingress routing rule
│       ├── neo4j.tf                   # Neo4j StatefulSet + Headless Service + PVC
│       ├── qdrant.tf                  # Qdrant StatefulSet + Headless Service + PVC
│       ├── secrets.tf                 # Kubernetes Opaque Secrets
│       ├── namespace.tf               # Kubernetes namespace definition
│       ├── providers.tf               # Terraform provider configuration
│       ├── variables.tf               # Input variable declarations
│       ├── outputs.tf                 # Terraform output definitions
│       └── terraform.tfvars.example   # Example variable values (safe to commit)
├── scripts/
│   ├── build-image.sh                 # Docker image build and push
│   ├── deploy_aws.sh                  # AWS EKS deployment helper
│   ├── deploy_terraform.sh            # Terraform init + apply automation
│   ├── setup_env.sh                   # Local .env setup helper
│   └── test_k8s_ingress.sh            # Smoke test against K8s ingress endpoint
├── src/
│   ├── theme_based_rag_backend/
│   │   ├── agent_flow/                # LangGraph StateGraph nodes and edges
│   │   ├── Dockerfile                 # Multi-stage production container image
│   │   ├── config.py                  # Environment variable configuration
│   │   ├── graph_db.py                # Neo4j driver, entity extraction, Cypher queries
│   │   ├── vector_db.py               # Qdrant hybrid search, embedding pipeline
│   │   ├── tools.py                   # LangGraph tool: retrieve_VDB
│   │   ├── models.py                  # Pydantic request/response schemas
│   │   └── main.py                    # FastAPI app: /query, /ingest, /health
│   └── theme_based_rag_gateway/
│       ├── Dockerfile                 # Gateway container image
│       ├── main.py                    # FastAPI app: proxy routing via httpx
│       └── models.py                  # Pydantic request/response schemas
├── tests/
│   ├── conftest.py                    # Pytest fixtures and shared setup
│   ├── test_unit_gateway.py           # Unit tests: gateway proxy routing
│   ├── test_unit_hyde.py              # Unit tests: HyDE generation node
│   ├── test_unit_hyde_decision.py     # Unit tests: HyDE decision node
│   ├── test_integration_agent_flow.py # Integration: full agent graph run
│   ├── test_integration_graph_db.py   # Integration: Neo4j entity operations
│   ├── test_e2e_api.py                # E2E: full query against running services
│   ├── test_e2e_k8s.py                # E2E: smoke tests against K8s ingress
│   └── e2e_aws.py                     # E2E: AWS EKS deployment validation
├── pyproject.toml                     # Project metadata, dependencies, ruff + pytest config
├── langgraph.json                     # LangGraph API server configuration
└── README.md
```
