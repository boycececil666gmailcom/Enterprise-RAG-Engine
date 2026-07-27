from unittest.mock import MagicMock, patch
import pytest
from src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator import (
    generate_hypothetical_document,
    hyde_node
)
from src.theme_based_rag_backend.agent_flow.state import AgentState

def test_generate_hypothetical_document_mock_llm():
    """Test HyDE document generation with mocked LLM."""
    mock_llm = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "To request a refund on Supernova, navigate to Settings > Billing and click Refund."
    mock_llm.invoke.return_value = mock_response

    with patch("src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator.get_hyde_llm", return_value=mock_llm):
        res = generate_hypothetical_document("How to refund?")
        assert "Settings > Billing" in res
        assert mock_llm.invoke.called

def test_generate_hypothetical_document_fallback_on_error():
    """Test that if LLM raises an exception, HyDE gracefully falls back to the original query."""
    mock_llm = MagicMock()
    mock_llm.invoke.side_effect = RuntimeError("API Rate Limit")

    with patch("src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator.get_hyde_llm", return_value=mock_llm):
        res = generate_hypothetical_document("How to refund?")
        assert res == "How to refund?"

def test_hyde_node_execution():
    """Test standalone hyde_node execution."""
    mock_llm = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "Hypothetical document excerpt"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "User query",
        "history": [],
        "category": "rag",
        "use_hyde": True,
        "hyde_reason": None,
        "hypothetical_document": None,
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }

    with patch("src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator.get_hyde_llm", return_value=mock_llm):
        result = hyde_node(state)
        assert result["hypothetical_document"] == "Hypothetical document excerpt"
