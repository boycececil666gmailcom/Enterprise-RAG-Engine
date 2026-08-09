import pytest
from unittest.mock import patch, MagicMock
from src.theme_based_rag_backend.graph_db import (
    sanitize_rel_type,
    clean_json_response,
    extract_entities_and_relations,
    add_graph_relations,
    extract_query_entities,
    retrieve_graph_relations
)

def test_sanitize_rel_type():
    assert sanitize_rel_type("has-plan") == "HAS_PLAN"
    assert sanitize_rel_type("part_of") == "PART_OF"
    assert sanitize_rel_type("!@#abc_123$%^") == "ABC_123"
    assert sanitize_rel_type("") == "RELATED_TO"

def test_clean_json_response():
    raw_response = "```json\n{\n  \"entities\": []\n}\n```"
    cleaned = clean_json_response(raw_response)
    assert cleaned == "{\n  \"entities\": []\n}"

    simple_response = "{\n  \"entities\": []\n}"
    assert clean_json_response(simple_response) == simple_response

@patch("src.theme_based_rag_backend.graph_db.get_llm")
def test_extract_entities_and_relations(mock_get_llm):
    mock_llm = MagicMock()
    mock_response = MagicMock()
    mock_response.content = '{"entities": [{"name": "Supernova", "type": "Product", "description": "SaaS Platform"}], "relationships": [{"source": "Supernova", "type": "HAS", "target": "Premium Plan"}]}'
    mock_llm.invoke.return_value = mock_response
    mock_get_llm.return_value = mock_llm

    result = extract_entities_and_relations("Some text")
    assert len(result["entities"]) == 1
    assert result["entities"][0]["name"] == "Supernova"
    assert len(result["relationships"]) == 1
    assert result["relationships"][0]["source"] == "Supernova"

@patch("src.theme_based_rag_backend.graph_db.get_driver")
def test_add_graph_relations(mock_get_driver):
    mock_driver = MagicMock()
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session
    mock_get_driver.return_value = mock_driver

    entities = [{"name": "A", "type": "T", "description": "D"}]
    relationships = [{"source": "A", "type": "REL", "target": "B"}]

    add_graph_relations(entities, relationships)

    assert mock_session.run.call_count >= 3 # MERGE A, MERGE B, MERGE RELATION

@patch("src.theme_based_rag_backend.graph_db.get_llm")
def test_extract_query_entities(mock_get_llm):
    mock_llm = MagicMock()
    mock_response = MagicMock()
    mock_response.content = '["Supernova", "Premium Plan"]'
    mock_llm.invoke.return_value = mock_response
    mock_get_llm.return_value = mock_llm

    result = extract_query_entities("Show me Supernova Premium Plan")
    assert result == ["Supernova", "Premium Plan"]

@patch("src.theme_based_rag_backend.graph_db.get_driver")
def test_retrieve_graph_relations(mock_get_driver):
    mock_driver = MagicMock()
    mock_session = MagicMock()
    mock_result = MagicMock()
    
    # Mock records returned by session.run
    record = {
        "name": "Supernova",
        "type": "Product",
        "description": "SaaS platform",
        "rel_type": "HAS_PLAN",
        "neighbor_name": "Premium Plan",
        "is_source": True
    }
    mock_result.__iter__.return_value = [record]
    mock_session.run.return_value = mock_result
    mock_driver.session.return_value.__enter__.return_value = mock_session
    mock_get_driver.return_value = mock_driver

    context = retrieve_graph_relations(["Supernova"])
    assert "Entity: Supernova" in context
    assert "- (Supernova) -[HAS_PLAN]-> (Premium Plan)" in context

@patch("src.theme_based_rag_backend.graph_db.get_llm")
@patch("src.theme_based_rag_backend.graph_db.get_driver")
@patch("src.theme_based_rag_backend.vector_db.get_vector_store")
def test_graph_rag_integration_flow(mock_get_vector_store, mock_get_driver, mock_get_llm):
    """Integration test verifying that document ingestion writes to both Qdrant and Neo4j,
    and query retrieval fetches and merges context from both databases."""
    # Mock vector store
    mock_vector_store = MagicMock()
    mock_get_vector_store.return_value = mock_vector_store
    
    # Mock Neo4j session & driver
    mock_driver = MagicMock()
    mock_session = MagicMock()
    mock_driver.session.return_value.__enter__.return_value = mock_session
    mock_get_driver.return_value = mock_driver
    
    # Mock LLM responses
    mock_llm = MagicMock()
    mock_get_llm.return_value = mock_llm
    
    # Mock 1: Ingestion entity extraction
    mock_ingest_response = MagicMock()
    mock_ingest_response.content = '{"entities": [{"name": "Zenith", "type": "Company", "description": "Fintech platform operator"}], "relationships": []}'
    
    # Mock 2: Query entity extraction
    mock_query_response = MagicMock()
    mock_query_response.content = '["Zenith"]'
    
    mock_llm.invoke.side_effect = [mock_ingest_response, mock_query_response]
    
    # Mock Neo4j retrieve records
    mock_record = {
        "name": "Zenith",
        "type": "Company",
        "description": "Fintech platform operator",
        "rel_type": "OPERATES",
        "neighbor_name": "Supernova",
        "is_source": True
    }
    mock_result = MagicMock()
    mock_result.__iter__.return_value = [mock_record]
    mock_session.run.return_value = mock_result
    
    # 1. Trigger Ingestion
    from src.theme_based_rag_backend.vector_db import add_document_text
    from src.theme_based_rag_backend.graph_db import ingest_graph_document
    chunk_count = add_document_text("Zenith operates Supernova platform.")
    ingest_graph_document("Zenith operates Supernova platform.")
    
    assert chunk_count > 0
    # Verify that add_graph_relations was called (indicated by session.run calls)
    assert mock_session.run.call_count >= 1
    
    # 2. Trigger Retrieval
    from src.theme_based_rag_backend.tools import retrieve_local_documents
    # Mock similarity search in Qdrant
    mock_doc = MagicMock()
    mock_doc.page_content = "Zenith operates Supernova platform."
    mock_doc.metadata = {"relevance_score": 0.9}
    mock_vector_store.similarity_search.return_value = [mock_doc]
    
    # Run retrieve tool
    context = retrieve_local_documents.invoke("Tell me about Zenith")
    
    # Verify both Vector and Graph contexts are merged
    assert "=== VECTOR DATABASE CONTEXT ===" in context
    assert "=== KNOWLEDGE GRAPH CONTEXT ===" in context
    assert "Entity: Zenith" in context
    assert "- (Zenith) -[OPERATES]-> (Supernova)" in context
