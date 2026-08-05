# Enterprise-RAG-Engine

A modular, enterprise-grade Retrieval-Augmented Generation (RAG) backend engine template utilizing Google Gemini API, LangGraph agent orchestration, Qdrant vector search, and Neo4j Knowledge Graph database for GraphRAG entity-relationship reasoning.

---

## Core Purpose & RAG Fundamental Concept

### What is RAG? (Context Provision for LLMs)
Large Language Models (LLMs) excel at general reasoning and language understanding, but lack internal knowledge of custom enterprise datasets and can hallucinate when asked about domain-specific facts. 

**Retrieval-Augmented Generation (RAG)** solves this by retrieving exact, verified context from trusted database stores (Vector DBs and Knowledge Graphs) and injecting it into the LLM prompt:

1. **Context Retrieval**: Fetches top matching passages (Qdrant hybrid vector/lexical search) and connected entity graphs (Neo4j GraphRAG).
2. **Context Injection**: Supplies the structured ground-truth facts directly to the LLM.
3. **Grounded Generation**: Restricts the LLM (Google Gemini) to synthesize responses solely based on the provided context, guaranteeing high precision and zero hallucination.

### RAG Backend Engine Template
This project is structured as a **reusable backend template**. It separates the API Gateway proxy from core retrieval and agent state graph nodes, making it effortless to plug into any customer portal, mobile app, or internal tool.

---

## Dual-Perspective Project Summarization

### Business Focus
The **Enterprise-RAG-Engine** is designed to provide high-value, enterprise customer support while guaranteeing 100% answer accuracy and zero AI hallucinations. 

- **Domain Safeguard Enforcement**: Automatically screens every customer inquiry to ensure it remains strictly within defined business domain boundaries (e.g., Fintech SaaS platform documentation), immediately preventing off-topic usage.
- **GraphRAG & Hybrid Vector Knowledge Retrieval**: Combines semantic text retrieval with Neo4j graph relationship mapping (GraphRAG) to provide comprehensive context on interconnected entities such as pricing tiers, product feature dependencies, and organization hierarchies.
- **Adaptive HyDE Answer Enhancement**: Dynamically generates hypothetical answer passages for abstract user questions, significantly boosting document retrieval accuracy.
- **Self-Correcting Quality Assurance**: Employs an automated self-critique review process that verifies answer candidates against source context before delivering the final response to customers.

### Tech Focus
The application follows a microservices architecture separating an API Gateway proxy (`src.theme_based_rag_gateway`) from the core RAG backend engine (`src.theme_based_rag_backend`). The stateful multi-agent execution loop is built on LangGraph, combining Qdrant hybrid vector search (dense Gemini embeddings + BM25 sparse lexical tokens) with Neo4j Cypher graph queries and FlashRank neural reranking.

#### Technology Stack & Shields.io Badges

* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **Python 3.10+**: Primary programming language and execution environment.
* ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) **FastAPI**: Asynchronous web framework used for API Gateway and backend services.
* ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) **LangGraph**: Orchestration framework for multi-node agent state graphs, conditional routing, and self-critique loops.
* ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) **LangChain**: Text chunking utilities (`RecursiveCharacterTextSplitter`), document model abstractions, and LLM integrations.
* ![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white) **Google Gemini API**: Powers LLM decision-making (`gemini-3.1-flash-lite`) and dense vector embeddings (`gemini-embedding-001`).
* ![Qdrant](https://img.shields.io/badge/Qdrant-DC2626?style=for-the-badge&logo=qdrant&logoColor=white) **Qdrant Vector DB**: Vector database supporting hybrid dense-sparse passage retrieval and metadata filtering.
* ![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white) **Neo4j Graph DB**: Graph database storing extracted entities and 1-hop relationships for GraphRAG context.
* ![FastEmbed](https://img.shields.io/badge/FastEmbed_BM25-FF6F00?style=for-the-badge&logo=python&logoColor=white) **FastEmbed BM25**: Lightweight sparse lexical embedding model (`Qdrant/bm25`).
* ![FlashRank](https://img.shields.io/badge/FlashRank-000000?style=for-the-badge&logo=lightning&logoColor=white) **FlashRank**: Cross-encoder neural reranker used to rank merged vector and graph passages.
* ![LangSmith](https://img.shields.io/badge/LangSmith-FF6F00?style=for-the-badge&logo=langchain&logoColor=white) **LangSmith**: Observability and execution tracing platform for agent steps and LLM prompt calls.
* ![HTTPX](https://img.shields.io/badge/HTTPX-5B60EA?style=for-the-badge&logo=python&logoColor=white) **HTTPX**: Asynchronous HTTP client powering gateway proxy routing.
* ![Uvicorn](https://img.shields.io/badge/Uvicorn-4053D6?style=for-the-badge&logo=python&logoColor=white) **Uvicorn**: Production ASGI server implementation for FastAPI endpoints.
* ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white) **Terraform**: Infrastructure as Code (IaC) tool for Kubernetes namespace, secrets, deployments, and services.
* ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) **Docker**: Containerization infrastructure for microservices, Qdrant, and Neo4j.

---

## Mandatory System Diagrams

### 1. Business Flow Mermaid Diagram

Below is a simplified operational workflow designed for business managers and product stakeholders, illustrating how customer support questions and knowledge base updates flow through the system:

```mermaid
flowchart TD
    %% Styling Node classes
    classDef client fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;
    classDef router fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#b45309;
    classDef kb fill:#f3e8ff,stroke:#7e22ce,stroke-width:2px,color:#6b21a8;
    classDef reply fill:#dcfce7,stroke:#15803d,stroke-width:2px,color:#166534;
    classDef block fill:#fee2e2,stroke:#b91c1c,stroke-width:2px,color:#991b1b;
    classDef process fill:#f9fafb,stroke:#d1d5db,stroke-width:1px,color:#374151;

    Customer(["📱 Customer / App User"]):::client
    
    Customer -->|"1. Submits customer support question"| ScopeCheck{"🤖 Service Scope Verification<br/>(Check if query belongs to Fintech SaaS domain)"}:::router
    
    ScopeCheck -->|"Question matches business domain"| SearchKnowledge["🔍 Search Dual Knowledge Base<br/>(Query Document Text & Entity Graphs)" ]:::process
    ScopeCheck -->|"Question outside business domain"| ScopeRefusal["🛡️ Formulate Polite Refusal Message"]:::block
    
    SearchKnowledge -->|"Fetch matching text passages"| VectorDB[("📚 Company Document Store")]:::kb
    SearchKnowledge -->|"Fetch entity & plan relationships"| GraphDB[("🕸️ Enterprise Knowledge Graph")]:::kb
    
    VectorDB -->|"Document passage results"| SynthesizeAnswer["✍️ Draft Answer Using Retrieved Knowledge"]:::process
    GraphDB -->|"Entity relationship results"| SynthesizeAnswer
    
    SynthesizeAnswer -->|"2. Draft response ready"| QualityCheck{"🔎 Quality & Groundedness Checker<br/>(Verify accuracy and zero hallucination)"}:::router
    ScopeRefusal -->|"Refusal message ready"| QualityCheck
    
    QualityCheck -->|"Passes verification check"| FinalAnswer["✅ Verified Helpful Customer Response"]:::reply
    QualityCheck -->|"Fails verification check"| ScopeCheck
    
    FinalAnswer -->|"3. Deliver final answer to user"| Customer
    
    subgraph DocumentIngestion ["Document & Knowledge Base Update Workflow (Offline)"]
        style DocumentIngestion fill:#f9fafb,stroke:#d1d5db,stroke-width:1px;
        OpsAdmin(["👤 Operations / Admin Team"]):::client -->|"Uploads user guides & product documentation"| DocumentProcessor["✂️ Break Documents into Small Passages & Extract Entity Nodes"]:::process
        DocumentProcessor -->|"Generate and store text embeddings"| VectorDB
        DocumentProcessor -->|"Create and connect entity nodes"| GraphDB
    end
```

---

### 2. Technical Architecture Mermaid Diagram

Below is the technical architecture diagram showing component structures, class implementations, module dependencies, state graph nodes, and database connection drivers:

```mermaid
flowchart TD
    %% Styling
    classDef gateway fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e40af;
    classDef backend fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#166534;
    classDef graphNode fill:#fdf4ff,stroke:#c026d3,stroke-width:2px,color:#86198f;
    classDef dbNode fill:#fff7ed,stroke:#ea580c,stroke-width:2px,color:#9a3412;
    classDef neoNode fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1;

    subgraph GatewayModule ["API Gateway Service (src.theme_based_rag_gateway)"]
        style GatewayModule fill:#f8fafc,stroke:#94a3b8,stroke-width:1px;
        GatewayMain["main.py (FastAPI App)"]:::gateway
        RouteQuery["route_query(QueryRequest)"]:::gateway
        RouteIngest["route_ingest(IngestRequest)"]:::gateway
        HTTPXClient["httpx.AsyncClient"]:::gateway
        
        GatewayMain --> RouteQuery
        GatewayMain --> RouteIngest
        RouteQuery --> HTTPXClient
        RouteIngest --> HTTPXClient
    end

    subgraph BackendModule ["Core RAG Backend Service (src.theme_based_rag_backend)"]
        style BackendModule fill:#f8fafc,stroke:#94a3b8,stroke-width:1px;
        BackendMain["main.py (FastAPI App)"]:::backend
        RunQuery["run_query(QueryRequest)"]:::backend
        IngestDoc["ingest_document(IngestRequest)"]:::backend
        
        BackendMain --> RunQuery
        BackendMain --> IngestDoc
        
        subgraph VectorStoreModule ["Vector Database Pipeline (vector_db.py)"]
            style VectorStoreModule fill:#fff7ed,stroke:#fdba74,stroke-width:1px;
            GetVS["get_vector_store()"]:::dbNode
            AddDocText["add_document_text(text, metadata)"]:::dbNode
            Splitter["RecursiveCharacterTextSplitter"]:::dbNode
            DenseEmbed["GoogleGenerativeAIEmbeddings<br/>(gemini-embedding-001)"]:::dbNode
            SparseEmbed["FastEmbedSparse<br/>(Qdrant/bm25)"]:::dbNode
            QdrantStore[("QdrantVectorStore<br/>collection: local_rag_documents")]:::dbNode
            
            AddDocText --> Splitter
            Splitter --> QdrantStore
            GetVS --> DenseEmbed
            GetVS --> SparseEmbed
            GetVS --> QdrantStore
        end

        subgraph GraphDBModule ["Neo4j Graph Engine (graph_db.py)"]
            style GraphDBModule fill:#e0f2fe,stroke:#38bdf8,stroke-width:1px;
            GetDriver["get_driver()"]:::neoNode
            ExtractEntities["extract_entities_and_relations(text)"]:::neoNode
            AddGraph["add_graph_relations(entities, relationships)"]:::neoNode
            ExtractQueryEntities["extract_query_entities(query)"]:::neoNode
            RetrieveGraph["retrieve_graph_relations(query_entities)"]:::neoNode
            Neo4jDriver[("GraphDatabase.driver<br/>Bolt Protocol")]:::neoNode

            AddGraph --> GetDriver
            RetrieveGraph --> GetDriver
            GetDriver --> Neo4jDriver
        end
        
        subgraph LangGraphAgent ["Agent Execution Graph (agent_flow/graph.py)"]
            style LangGraphAgent fill:#fdf4ff,stroke:#f0abfc,stroke-width:2px;
            AgentState["AgentState (TypedDict)"]:::graphNode
            CompiledGraph["agent_graph (Compiled StateGraph)"]:::graphNode
            
            ClassifierNode["node_classifier(AgentState)"]:::graphNode
            HyDEDecisionNode["node_hyde_decision(AgentState)"]:::graphNode
            HyDEGenNode["node_hyde_generator(AgentState)"]:::graphNode
            RAGQANode["node_rag_qa(AgentState)"]:::graphNode
            RefuseNode["node_refuse(AgentState)"]:::graphNode
            CritiqueNode["node_critique(AgentState)"]:::graphNode
            
            EdgeCategory["edge_category(AgentState)"]:::graphNode
            EdgeHyDE["edge_hyde(AgentState)"]:::graphNode
            EdgeCritique["edge_critique(AgentState)"]:::graphNode
            
            RetrieveTool["tools.retrieve_local_documents"]:::graphNode
            Ranker["FlashrankRerank"]:::graphNode

            CompiledGraph --> ClassifierNode
            ClassifierNode --> EdgeCategory
            EdgeCategory -->|"rag"| HyDEDecisionNode
            EdgeCategory -->|"refuse"| RefuseNode
            
            HyDEDecisionNode --> EdgeHyDE
            EdgeHyDE -->|"enable"| HyDEGenNode
            EdgeHyDE -->|"skip"| RAGQANode
            HyDEGenNode --> RAGQANode
            
            RAGQANode --> RetrieveTool
            RetrieveTool --> GetVS
            RetrieveTool --> Ranker
            RetrieveTool --> ExtractQueryEntities
            RetrieveTool --> RetrieveGraph
            
            RAGQANode --> CritiqueNode
            RefuseNode --> CritiqueNode
            CritiqueNode --> EdgeCritique
            EdgeCritique -->|"approved"| ENDNode([END]):::graphNode
            EdgeCritique -->|"rejected"| ClassifierNode
        end
    end

    HTTPXClient -->|"POST /query"| RunQuery
    HTTPXClient -->|"POST /ingest"| IngestDoc
    RunQuery --> CompiledGraph
    IngestDoc --> AddDocText
    IngestDoc --> ExtractEntities
    ExtractEntities --> AddGraph
```

---

### 3. Technical & Business Logic Sequence Diagram

Below is the technical sequence diagram illustrating exact execution flows, class method calls, data payloads, and conditional routing logic highlighted with colorized alternative blocks:

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client / Mobile App
    participant Gateway as src.theme_based_rag_gateway.main
    participant Backend as src.theme_based_rag_backend.main
    participant Graph as agent_flow.graph.agent_graph
    participant Classifier as agent_flow.nodes.node_classifier
    participant HyDEDecision as agent_flow.nodes.node_hyde_decision
    participant HyDEGen as agent_flow.nodes.node_hyde_generator
    participant QA as agent_flow.nodes.node_rag_qa
    participant Tool as tools.retrieve_local_documents
    participant Qdrant as vector_db.get_vector_store
    participant Neo4j as graph_db.retrieve_graph_relations
    participant Critique as agent_flow.nodes.node_critique
    participant Edges as agent_flow.edges

    Client->>Gateway: POST /query (QueryRequest)
    Gateway->>Backend: httpx.AsyncClient.post("/query", QueryRequest)
    Backend->>Graph: agent_graph.ainvoke(AgentState)
    
    loop Execution Loop (Max 3 attempts)
        Graph->>Classifier: node_classifier(AgentState)
        Note over Classifier: Evaluates cosine similarity of query against CHATBOT_THEME
        Classifier-->>Graph: returns {"category": "rag" | "refuse"}
        
        Graph->>Edges: edge_category(AgentState)
        
        alt Path A: Category is 'rag' (Domain-related query)
            rect rgb(224, 242, 254)
                Edges-->>Graph: returns "rag"
                Graph->>HyDEDecision: node_hyde_decision(AgentState)
                Note over HyDEDecision: Evaluates query length and error code patterns
                HyDEDecision-->>Graph: returns {"use_hyde": true | false}
                
                Graph->>Edges: edge_hyde(AgentState)
                
                alt Branch A1: HyDE Enabled (Abstract / Non-technical query)
                    rect rgb(238, 242, 255)
                        Edges-->>Graph: returns "enable"
                        Graph->>HyDEGen: node_hyde_generator(AgentState)
                        Note over HyDEGen: ChatGoogleGenerativeAI generates hypothetical passage
                        HyDEGen-->>Graph: returns {"hypothetical_document": doc}
                    end
                else Branch A2: HyDE Skipped (Exact query)
                    rect rgb(243, 244, 246)
                        Edges-->>Graph: returns "skip"
                    end
                end
                
                Graph->>QA: node_rag_qa(AgentState)
                QA->>Tool: retrieve_local_documents(query)
                
                par Vector Hybrid Search
                    Tool->>Qdrant: QdrantVectorStore.similarity_search(query, k=5)
                    Qdrant-->>Tool: Raw doc passages
                    Note over Tool: FlashrankRerank.compress_documents() reranks passages
                and GraphRAG Neo4j Query
                    Tool->>Neo4j: extract_query_entities(query)
                    Tool->>Neo4j: retrieve_graph_relations(query_entities)
                    Neo4j-->>Tool: Cypher entity nodes & 1-hop relationships
                end
                
                Tool-->>QA: Combined Vector + Neo4j Graph Context string
                Note over QA: ChatGoogleGenerativeAI synthesizes grounded response
                QA-->>Graph: returns {"agent_response": content}
            end
        else Path B: Category is 'refuse' (Off-theme query)
            rect rgb(254, 226, 226)
                Edges-->>Graph: returns "refuse"
                Graph->>QA: node_refuse(AgentState)
                Note over QA: ChatGoogleGenerativeAI generates polite refusal response
                QA-->>Graph: returns {"agent_response": refusal_content}
            end
        end

        Graph->>Critique: node_critique(AgentState)
        Note over Critique: Evaluates agent_response for groundedness & compliance
        
        Graph->>Edges: edge_critique(AgentState)
        
        alt Validation Status: PASS
            rect rgb(220, 252, 231)
                Critique-->>Graph: returns {"critique_feedback": "PASS"}
                Edges-->>Graph: returns "approved" -> Exit Loop to END
            end
        else Validation Status: FAIL (And attempts < 3)
            rect rgb(254, 243, 199)
                Critique-->>Graph: returns {"critique_feedback": reason, "attempts": attempts + 1}
                Edges-->>Graph: returns "rejected" -> Loop back to node_classifier
            end
        end
    end

    Graph-->>Backend: Final AgentState result
    Backend-->>Gateway: QueryResponse JSON
    Gateway-->>Client: HTTP 200 OK (QueryResponse)
```

---

## System Configuration & Environment Variables

The application is configured using environment variables (stored in `.env`):

| Environment Variable | Description | Default Value |
| :--- | :--- | :--- |
| `GEMINI_API_KEY` | Google Gemini API credentials | *(Required)* |
| `GEMINI_MODEL` | Gemini LLM model for routing, HyDE, QA, and critique | `gemini-3.1-flash-lite` |
| `GEMINI_EMBED_MODEL` | Google Generative AI embeddings model | `gemini-embedding-001` |
| `GEMINI_TEMPERATURE` | Generation temperature (0.0 for deterministic RAG) | `0.0` |
| `PORT` | FastAPI server port for Backend | `8000` |
| `HOST` | FastAPI server bind address | `0.0.0.0` |
| `QDRANT_URL` | URL to access Qdrant instance | `http://localhost:6333` |
| `QDRANT_API_KEY` | Optional API Key if using Qdrant Cloud | `None` |
| `NEO4J_URI` | Neo4j Bolt connection URI for GraphRAG | `bolt://localhost:7687` |
| `NEO4J_USERNAME` | Neo4j authentication username | `neo4j` |
| `NEO4J_PASSWORD` | Neo4j authentication password | `password123` |
| `CHATBOT_THEME` | The primary theme boundary for retrieval routing | `Fintech SaaS platform` |

---