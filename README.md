# Theme-Based RAG Workflow

A modular, stateless Retrieval-Augmented Generation (RAG) customer service chatbot utilizing the Google Gemini API, Qdrant for vector storage, and an adaptive LangGraph multi-agent workflow featuring HyDE (Hypothetical Document Embeddings) query transformation.

---

## Business & Product Flow (Overview)

Below is a high-level view of how customer requests flow through the system, detailing the execution mechanism (LLM vs Vector Search vs Rules) of each step:

```mermaid
flowchart TD
    %% Styling Node classes
    classDef client fill:#e0e7ff,stroke:#4338ca,stroke-width:2px,color:#3730a3;
    classDef router fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#b45309;
    classDef kb fill:#f3e8ff,stroke:#7e22ce,stroke-width:2px,color:#6b21a8;
    classDef reply fill:#dcfce7,stroke:#15803d,stroke-width:2px,color:#166534;
    classDef block fill:#fee2e2,stroke:#b91c1c,stroke-width:2px,color:#991b1b;
    classDef process fill:#f9fafb,stroke:#d1d5db,stroke-width:1px,color:#374151;
    
    %% Main customer interaction entry point
    Client(["📱 Customer / User"]):::client
    
    Client -->|"1. Asks question"| ScopeCheck{"📐 Service Scope Check<br/>(Vector Similarity)"}:::router
    
    %% Classifier branches
    ScopeCheck -->|"Product & Support Question"| SupportAI["🤖 AI Customer Support Assistant<br/>(Gemini LLM)" ]:::process
    ScopeCheck -->|"Unrelated / General Chat"| OutOfScopeNotice["🤖 Scope Refusal Notice<br/>(Gemini LLM)"]:::block
    
    %% Knowledge Base Retrieval
    SupportAI -->|"Search official guides"| DB[("📚 Product Manuals & FAQs<br/>(Qdrant Vector DB)")]:::kb
    DB -->|"Return relevant text"| SupportAI
    
    %% Quality verification
    SupportAI -->|"2. Proposed answer"| QualityCheck{"🤖 Answer Quality Review<br/>(Gemini LLM Check)"}:::router
    OutOfScopeNotice -->|"Polite boundary response"| QualityCheck
    
    %% Critique outcomes
    QualityCheck -->|"Verified Answer Delivered"| VerifiedReply["Final Answer"]:::reply
    QualityCheck -->|"Needs Revision"| ScopeCheck
    
    VerifiedReply -->|"3. Delivers answer to customer"| Client
    
    %% Ingestion background flow
    subgraph Maintenance ["Knowledge Base Maintenance (Admin)"]
        style Maintenance fill:#f9fafb,stroke:#d1d5db,stroke-width:1px;
        Admin(["Support Team Admin"]):::client -->|"Uploads FAQs & Guides"| Indexer["✂️ Document Indexing Pipeline<br/>(Dense & Sparse Embeddings)"]:::process
        Indexer --> DB
    end
```

---

## Features & API Endpoints

The backend exposes HTTP endpoints via FastAPI:

- **`POST /ingest`**: Accepts raw text documents, splits them into manageable chunks (using `RecursiveCharacterTextSplitter`), generates dense Gemini embeddings and sparse BM25 embeddings, and stores them in Qdrant.
- **`POST /query`**: Accepts user queries and conversation history. Routes queries dynamically through the LangGraph workflow:
  - **`node_classifier`** *(Vector Similarity)*: Determines theme boundary adherence (`rag` vs `refuse`).
  - **`node_hyde_decision`** *(Rule Engine)*: Evaluates query patterns to decide whether to enable HyDE (`use_hyde: true/false`).
  - **`node_hyde_generator`** *(Gemini LLM)*: Generates hypothetical passage excerpts for abstract or non-technical queries.
  - **`node_rag_qa`** *(Gemini LLM)*: Performs Qdrant hybrid retrieval + FlashRank cross-encoder reranking and synthesizes answers.
  - **`node_critique`** *(Gemini LLM)*: Performs strict quality and grounding checks before returning answers.
- **`GET /health`**: Performs liveness checks, confirming vector store readiness.

---

## Configuration

The application is configured using environment variables (stored locally in a `.env` file).

| Environment Variable | Description | Default Value |
| :--- | :--- | :--- |
| `GEMINI_API_KEY` | Google Gemini API credentials | *(Required)* |
| `GEMINI_MODEL` | Gemini LLM model for routing and synthesis | `gemini-3.1-flash-lite` |
| `GEMINI_EMBED_MODEL` | Google Generative AI embeddings model | `gemini-embedding-001` |
| `GEMINI_TEMPERATURE` | Generation temperature (0.0 for deterministic RAG answers) | `0.0` |
| `PORT` | FastAPI server port for Chatbot Backend | `8000` |
| `HOST` | FastAPI server bind address | `0.0.0.0` |
| `QDRANT_URL` | URL to access Qdrant instance (e.g. `http://localhost:6333` or `:memory:`) | *(Required)* |
| `QDRANT_API_KEY` | Optional API Key if using Qdrant Cloud | `None` |
| `CHATBOT_THEME` | The primary theme boundary for retrieval routing & safeguards | `Fintech SaaS platform` |

---

## Technical Architecture & Logic Flow

Below is the technical flowchart detailing node execution mechanisms (**LLM** vs **Vector Similarity** vs **Rule Engine**):

```mermaid
flowchart TD
    %% Styling classes
    classDef main fill:#f9fafb,stroke:#d1d5db,stroke-width:1px,color:#374151;
    classDef ingest fill:#ecfdf5,stroke:#10b981,stroke-width:1px,color:#065f46;
    classDef lgNode fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,color:#1e40af;
    classDef decision fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#b45309;
    classDef hyde fill:#e0e7ff,stroke:#4338ca,stroke-width:2px,color:#3730a3;
    classDef endNode fill:#f3e8ff,stroke:#7e22ce,stroke-width:2px,color:#6b21a8;

    Server[FastAPI Server]:::main
    
    %% Ingest path
    Server -->|POST /ingest| Ingest[Document Ingestion Path]:::ingest
    Ingest --> Split[RecursiveCharacterTextSplitter]:::ingest
    Split --> Embed[Gemini Dense / FastEmbed Sparse]:::ingest
    Embed --> DB[(Qdrant DB)]:::ingest

    %% Query path
    Server -->|POST /query| Query[Query Processing Path]:::main
    
    subgraph LangGraph ["🤖 LangGraph Agent Flow (Node Mechanism Breakdown)"]
        style LangGraph fill:#f0f7ff,stroke:#2563eb,stroke-width:3px,stroke-dasharray: 5 5;
        
        Graph[Agent Coordinator]:::lgNode
        Classifier{node_classifier<br/>📐 Vector Similarity}:::decision
        HyDEDecision{node_hyde_decision<br/>⚡ Rule Engine}:::decision
        HyDEGen[node_hyde_generator<br/>🤖 Gemini LLM]:::hyde
        QA[node_rag_qa<br/>🤖 Gemini LLM]:::lgNode
        Safeguard[node_safeguard<br/>🤖 Gemini LLM]:::lgNode
        Critique[node_critique<br/>🤖 Gemini LLM]:::lgNode
        End([End & Return]):::endNode
        
        Graph --> Classifier
        Classifier -->|edge_category: rag| HyDEDecision
        Classifier -->|edge_category: refuse| Safeguard
        
        HyDEDecision -->|edge_hyde: enable| HyDEGen
        HyDEDecision -->|edge_hyde: skip| QA
        HyDEGen --> QA
        
        QA --> Critique
        Safeguard --> Critique
        
        Critique -->|edge_critique: approved| End
        Critique -->|edge_critique: rejected| Classifier
    end
    
    Query --> Graph
```

### 1. Ingestion Path

The ingestion pipeline splits input text and uploads semantic chunks (with both dense Gemini and sparse BM25 embeddings) to Qdrant.

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client / Ingestion Script
    participant App as FastAPI Server (main.py)
    participant VectorStore as Qdrant DB

    Client->>App: POST /ingest {"text": "...", "metadata": {...}}
    Note over App: Chunks text using<br/>RecursiveCharacterTextSplitter
    
    alt Ingestion Success
        rect rgb(220, 252, 231)
            App->>VectorStore: Add document chunks (Dense + Sparse embeddings)
            VectorStore-->>App: Confirmation
            App-->>Client: Response {"status": "success", "chunk_count": X}
        end
    else Ingestion Failure (Database Offline / Missing Credentials)
        rect rgb(254, 226, 226)
            App->>VectorStore: Connection Error / Missing Key
            App-->>Client: HTTP 500 Internal Server Error
        end
    end
```

### 2. Query Path & Adaptive HyDE Sequence Flow

When a query is received, the request is dispatched to a stateful LangGraph agent workflow containing dynamic classification, HyDE decision/generation, RAG QA, and grounding evaluation:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant App as FastAPI Server (main.py)
    participant Graph as LangGraph Agent (agent_flow)
    participant Classifier as node_classifier (Vector Embeddings)
    participant HyDEDecision as node_hyde_decision (Rule Engine)
    participant HyDEGen as node_hyde_generator (Gemini LLM)
    participant QA as node_rag_qa (Gemini LLM)
    participant Safeguard as node_safeguard (Gemini LLM)
    participant Critique as node_critique (Gemini LLM)
    participant VectorStore as Qdrant DB

    User->>App: POST /query {"message": "...", "history": [...]}
    App->>Graph: ainvoke(inputs)
    
    loop Max 3 attempts
        Graph->>Classifier: Determine category via Vector Similarity
        Classifier-->>Graph: Category result (rag / refuse)
        
        alt Path A: Category is 'rag'
            rect rgb(224, 242, 254)
                Graph->>HyDEDecision: Evaluate query pattern (Regex & Query Length)
                HyDEDecision-->>Graph: Decision: use_hyde (True / False)
                
                alt HyDE Enabled (Abstract / Colloquial Query)
                    rect rgb(238, 242, 255)
                        Graph->>HyDEGen: LLM generates hypothetical passage
                        HyDEGen-->>Graph: hypothetical_document
                    end
                else HyDE Skipped (Exact Error / Specific Code)
                    rect rgb(243, 244, 246)
                        Note over Graph: Bypass HyDE & use raw query
                    end
                end
                
                Graph->>VectorStore: retrieve_local_documents (Qdrant Hybrid + FlashRank Rerank)
                VectorStore-->>Graph: Chunks & Reranked Docs
                Graph->>QA: LLM synthesizes answer using retrieved docs
                QA-->>Graph: agent_response
            end
        else Path B: Category is 'refuse'
            rect rgb(254, 226, 226)
                Graph->>Safeguard: LLM generates polite refusal response
                Safeguard-->>Graph: agent_response
            end
        end
        
        Graph->>Critique: LLM evaluates agent_response & context grounding
        
        alt Validation Passes (or max attempts reached)
            rect rgb(220, 252, 231)
                Critique-->>Graph: Status: PASS
                Note over Graph: Exit loop
            end
        else Validation Fails
            rect rgb(254, 226, 226)
                Critique-->>Graph: Status: FAIL (Reason details)
                Note over Graph: Increment attempts & loop back
            end
        end
    end
    
    Graph-->>App: Final state result
    App-->>User: Response {"response": "...", "use_hyde": true, "hyde_reason": "...", "hypothetical_document": "..."}
```

---

## Agent Flow Modular Architecture & Node Mechanisms

All nodes and edges inside `src/theme_based_rag_backend/agent_flow` follow explicit prefix naming conventions, with their underlying execution mechanism (**LLM** vs **Vector Search** vs **Rules**) explicitly defined:

| Node Module | File Link | Execution Mechanism | Purpose & Model |
| :--- | :--- | :--- | :--- |
| `node_classifier` | [node_classifier.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_classifier.py) | **📐 Vector Similarity** | Embeddings Cosine Similarity against `CHATBOT_THEME` (`gemini-embedding-001`) |
| `node_hyde_decision` | [node_hyde_decision.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_hyde_decision.py) | **⚡ Rule Engine** | Fast heuristic pattern matching (Regex for error codes & Query length) |
| `node_hyde_generator` | [node_hyde_generator.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_hyde_generator.py) | **🤖 Gemini LLM** | Generates hypothetical document passage (`gemini-3.1-flash-lite`) |
| `node_rag_qa` | [node_rag_qa.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_rag_qa.py) | **🤖 Gemini LLM** | Hybrid retrieval consumer & answer synthesis (`gemini-3.1-flash-lite`) |
| `node_safeguard` | [node_safeguard.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_safeguard.py) | **🤖 Gemini LLM** | Polite boundary refusal response (`gemini-3.1-flash-lite`) |
| `node_critique` | [node_critique.py](file:///c:/Users/boyce/OneDrive/Desktop/rag-chatbot/src/theme_based_rag_backend/agent_flow/nodes/node_critique.py) | **🤖 Gemini LLM** | Quality, groundedness & hallucination check (`gemini-3.1-flash-lite`) |

---

## Local Development & Testing Setup

### 1. Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite
QDRANT_URL=http://localhost:6333
CHATBOT_THEME=Fintech SaaS platform
```

### 3. Run Automated Unit & Integration Tests

```powershell
# Run full local backend and gateway test suite
.\venv\Scripts\python.exe -m pytest tests/ --ignore=tests/test_k8s_e2e.py -v
```

### 4. Start Services

```powershell
# Backend FastAPI server (port 8000)
.\venv\Scripts\python.exe -m uvicorn src.theme_based_rag_backend.main:app --host 0.0.0.0 --port 8000 --reload

# Gateway FastAPI server (port 8080)
.\venv\Scripts\python.exe -m uvicorn src.theme_based_rag_gateway.main:app --host 0.0.0.0 --port 8080 --reload
```

---

## Terraform Infrastructure Provisioning

You can provision and manage all Kubernetes resources (Namespace, Secrets, Qdrant StatefulSet, Backend/Gateway Deployments, Services, and Ingress) declaratively using Terraform:

```powershell
# Navigate to terraform directory
cd infra/terraform


# Initialize Terraform providers
terraform init

# Validate Terraform configuration
terraform validate

# Plan infrastructure deployment
terraform plan -out=tfplan

# Apply infrastructure to Kubernetes cluster
terraform apply tfplan
```