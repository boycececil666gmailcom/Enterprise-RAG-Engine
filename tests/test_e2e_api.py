import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
import httpx

from src.theme_based_rag_backend.main import app as backend_app
from src.theme_based_rag_gateway.main import app as gateway_app
from src.theme_based_rag_gateway import main as gateway_module

@pytest.fixture(autouse=True)
def setup_gateway_routing():
    """Fixture to route gateway asynchronous HTTP requests directly to the backend FastAPI ASGI application in-memory."""
    # Route gateway request client in-memory directly to backend ASGI app
    gateway_module.async_client = httpx.AsyncClient(transport=httpx.ASGITransport(app=backend_app), base_url="http://localhost:8000")
    yield

@patch("src.theme_based_rag_backend.graph_db.get_llm")
@patch("src.theme_based_rag_backend.graph_db.get_driver")
@patch("src.theme_based_rag_backend.vector_db.embeddings")
@patch("src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator.get_hyde_llm")
@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_full_e2e_flow(mock_llm, mock_hyde_llm, mock_embeddings, mock_get_driver, mock_get_graph_llm):
    """Test the full end-to-end flow from document ingestion to querying via the API Gateway."""
    # Mock Neo4j driver & session
    mock_driver = MagicMock()
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session
    mock_get_driver.return_value = mock_driver

    # Mock Graph DB LLM calls (Ingestion extraction and query entity extraction)
    mock_graph_llm = MagicMock()
    mock_get_graph_llm.return_value = mock_graph_llm

    mock_ingest_json = MagicMock(content='{"entities": [{"name": "Supernova", "type": "Product", "description": "security scanning system"}], "relationships": [{"source": "Supernova", "type": "DEVELOPED_FOR", "target": "Fintech platforms"}]}')
    mock_query_json = MagicMock(content='["Supernova"]')
    mock_graph_llm.invoke.side_effect = [mock_ingest_json, mock_query_json]

    # Mock graph records for retrieval query
    mock_record = {
        "name": "Supernova",
        "type": "Product",
        "description": "security scanning system",
        "rel_type": "DEVELOPED_FOR",
        "neighbor_name": "Fintech platforms",
        "is_source": True
    }
    mock_result = MagicMock()
    mock_result.__iter__.return_value = [mock_record]
    mock_session.run.return_value = mock_result

    # Setup Vector DB and Agent Flow LLM mocks
    import src.theme_based_rag_backend.agent_flow.nodes.node_classifier as classifier_module
    classifier_module.theme_embedding_cached = None
    mock_embeddings.embed_query.return_value = [1.0, 0.0]
    mock_hyde_llm.return_value = mock_llm

    gateway_client = TestClient(gateway_app)
    
    # 1. Ingest document via API Gateway (Vector and Graph stores)
    ingest_payload = {
        "text": "Supernova project is a next generation security scanning system developed for Fintech platforms.",
        "metadata": {"project": "Supernova"}
    }
    ingest_vector_res = gateway_client.post("/ingest/vector", json=ingest_payload)
    assert ingest_vector_res.status_code == 200
    assert ingest_vector_res.json()["status"] == "success"
    assert ingest_vector_res.json()["chunk_count"] > 0

    ingest_graph_res = gateway_client.post("/ingest/graph", json=ingest_payload)
    assert ingest_graph_res.status_code == 200
    assert ingest_graph_res.json()["status"] == "success"

    # 2. Query chatbot via API Gateway
    mock_resp_hyde = MagicMock(content='Supernova project security scanning system excerpt.')
    mock_resp_qa = MagicMock(content='The Supernova project is a next generation security scanning system.')
    mock_resp_crit = MagicMock(content='PASS')
    
    mock_llm.invoke.side_effect = [mock_resp_hyde, mock_resp_qa, mock_resp_crit]

    query_payload = {
        "message": "What is the Supernova project on the Fintech SaaS platform?"
    }
    query_response = gateway_client.post("/query", json=query_payload)
    
    assert query_response.status_code == 200
    res_json = query_response.json()
    assert "Supernova project" in res_json["response"]
    assert "retrieve_local_documents" in res_json["tool_calls_executed"]

    # Verify both Vector and Graph contexts are merged
    retrieved_docs = res_json["retrieved_documents"]
    assert "=== VECTOR DATABASE CONTEXT ===" in retrieved_docs
    assert "=== KNOWLEDGE GRAPH CONTEXT ===" in retrieved_docs
    assert "Supernova project is a next generation" in retrieved_docs
    assert "Entity: Supernova" in retrieved_docs
    assert "- (Supernova) -[DEVELOPED_FOR]-> (Fintech platforms)" in retrieved_docs
