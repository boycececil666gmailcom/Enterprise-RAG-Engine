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
