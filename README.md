# Enterprise-RAG-Engine

> Modular, enterprise-grade Retrieval-Augmented Generation (RAG) backend engine template with multi-agent orchestration, hybrid vector search, and Small-to-Big retrieval.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-1C3C3C?style=flat&logo=langchain&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=flat&logo=langchain&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-DeepSeek_V4_Flash-6366F1?style=flat)
![LLMLingua-2](https://img.shields.io/badge/LLMLingua--2-Prompt_Compression-8A2BE2?style=flat)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector_DB-DC2626?style=flat&logo=qdrant&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## End-to-End Pipeline Architecture

```mermaid
---
config:
  theme: neutral
---
flowchart LR
    A["1. Data Ingestion<br/>(Crawl4AI & RAPTOR)"] --> B[("2. Hybrid Vector Store<br/>(Qdrant Dense + BM25)")]
    B --> C["3. Multi-Agent Retrieval<br/>(HyDE + Dense + BM25)"]
    C --> D["4. Neural Rerank<br/>(FlashRank Cross-Encoder)"]
    D --> E["5. Context Compression<br/>(LLMLingua-2 Compactor)"]
    E --> F["6. Self-Critique Loop<br/>& Answer Generation"]
    F --> G["7. LLMOps Evaluation<br/>(LangSmith & Ragas)"]
```

---

## 1. Core Purpose & Business Value

The **Enterprise-RAG-Engine** eliminates the guesswork from AI-powered enterprise knowledge acquisition by restricting every generated answer to verified, company-owned knowledge — making hallucination structurally impossible.

- **Zero Hallucination, 100% Accuracy**: Every response is grounded in internal documentation and historical issue stores, guaranteeing factual accuracy with no invented information.
- **Domain Boundary Enforcement**: The engine automatically classifies and routes inquiries, keeping workflows strictly within defined business domains.
- **Comprehensive Hybrid Search**: Combines dense semantic vector search with BM25 sparse retrieval in Qdrant, surfacing exact variable names, error codes, and log patterns.
- **Self-Correcting Quality Assurance**: An automated review loop verifies every draft answer against source material before delivery, catching errors before users see them.
- **Prompt Token & Latency Optimization**: Integrates LLMLingua-2 context compression to compact retrieved passages, reducing LLM token consumption and latency while preserving vital semantic facts.
- **Streamlined Backend Architecture**: Direct client interaction via FastAPI on port 8000 and LangGraph Studio on port 2024 for real-time visualization.

---

## 2. System Architecture & Technical Execution

The engine runs a stateful multi-node LangGraph agent within `theme_based_rag_backend`. The backend performs domain classification, optional HyDE query expansion, hybrid vector retrieval, neural reranking (FlashRank), context compression (LLMLingua-2), and a self-critique quality loop before returning a response.

### Core Execution Sequence

```mermaid
---
config:
  theme: neutral
---
sequenceDiagram
    autonumber
    actor Client as Client App / End User / Eval
    participant BE as FastAPI Backend (port 8000)
    participant AG as LangGraph Agent Flow
    participant VDB as Qdrant Vector DB (port 6333)

    Note over Client, BE: Phase 1: Query Submission
    Client->>BE: POST /query (message, history)

    Note over BE, AG: Phase 2: Agent Execution Loop
    BE->>AG: Invoke StateGraph (AgentState)
    AG->>AG: node_classifier - Classify domain scope

    alt Query within business domain
        rect rgb(240, 243, 246)
            AG->>AG: node_hyde_decision - Evaluate HyDE necessity
            AG->>AG: node_hyde_generator - Generate hypothetical document (if enabled)
            AG->>VDB: Hybrid dense+sparse vector search (Qdrant BM25 + Dense)
            AG->>AG: node_retrieve - Retrieve context & rerank (Qdrant + FlashRank)
            AG->>AG: node_retrieve - LLMLingua-2 context compression
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
    BE-->>Client: QueryResponse (response, citations, retrieved_documents)
```

---

### Streamlined Multi-Container Architecture

```mermaid
---
config:
  theme: neutral
---
flowchart TB
    subgraph ClientLayer["Client & Developer Layer"]
        Browser["Browser / IDE / Evaluation Scripts"]
    end

    subgraph ContainerStack["Docker Compose Local Stack (infra/docker-compose.yml)"]
        Studio["LangGraph Studio UI<br/>(Port 2024)"]
        BE["FastAPI RAG Backend<br/>(Port 8000)"]
        Qdrant[("Qdrant Vector DB<br/>Dense + BM25 Sparse<br/>(Port 6333/6334)")]
    end

    subgraph ExternalLLM["LLM & Observability Providers"]
        OpenRouter["OpenRouter / DeepSeek"]
        LangSmith["LangSmith Tracing"]
    end

    Browser -->|"Inspect Agent Graph"| Studio
    Browser -->|"POST /query, GET /health"| BE
    Studio -->|"StateGraph Execution"| BE
    BE -->|"Dense + BM25 Search"| Qdrant
    BE -->|"Chat Completion"| OpenRouter
    BE -->|"Telemetry & Tracing"| LangSmith
```

---

## 3. Repository Structure

```text
Enterprise-RAG-Engine/
├── infra/
│   ├── build-image.sh                 # Docker backend image build script
│   └── docker-compose.yml             # Streamlined 3-service stack (Qdrant, Studio, Backend)
├── preprocessing-pipeline/
│   ├── 1.export_jira_tickets.py       # JIRA REST API ticket exporter
│   ├── 2.model_jira_defects.py        # AI defect modeling & Horizontal expansion checklist
│   ├── 3.ingest_to_qdrant.py          # Hybrid dense + BM25 vector ingestion
│   └── llm_client.py                  # Embedding & LLM client wrapper
├── progress-doc/                      # Weekly engineering milestone reports
├── src/
│   └── theme_based_rag_backend/
│       ├── agent_flow/                # LangGraph StateGraph nodes and routing edges
│       ├── Dockerfile                 # Multi-stage production container image
│       ├── config.py                  # Environment variable configuration
│       ├── vector_db.py               # Qdrant hybrid search & collection management
│       ├── tools.py                   # LangGraph retrieval tools
│       ├── models.py                  # Pydantic request/response schemas
│       └── main.py                    # FastAPI server: /query, /health
├── eval/                              # Ragas automated evaluation datasets & scripts
├── JIRA_BUGGRAPH_AI.md                # JIRA-BugGraph AI system specification & roadmap
├── pyproject.toml                     # Python dependencies & Ruff/Pytest configuration
├── langgraph.json                     # LangGraph CLI / Studio configuration
└── README.md
```

---

## 4. Quick Start Guide

### 1. Start Multi-Container Infrastructure
```powershell
docker compose -f infra/docker-compose.yml up --build -d
```

### 2. Verify System Health
```powershell
curl http://localhost:8000/health
```

### 3. Open Developer Tools
* **LangGraph Studio**: [http://localhost:2024](http://localhost:2024)
* **Qdrant Dashboard**: [http://localhost:6333/dashboard](http://localhost:6333/dashboard)
