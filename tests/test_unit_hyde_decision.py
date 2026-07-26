import pytest
from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.agent_flow.nodes.node_hyde_decision import hyde_decision_node

def test_hyde_decision_disabled_for_error_code():
    """Test that hyde_decision_node disables HyDE for queries containing error codes/IDs."""
    state: AgentState = {
        "message": "Encountered ERR-500 connection refused on server",
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
    result = hyde_decision_node(state)
    assert result["use_hyde"] is False
    assert "error" in result["hyde_reason"].lower() or "code" in result["hyde_reason"].lower()

def test_hyde_decision_disabled_for_detailed_query():
    """Test that hyde_decision_node disables HyDE for long, highly detailed queries."""
    state: AgentState = {
        "message": "Supernova SaaS platform refund policy clause 4 section B regarding monthly subscriptions for enterprise clients in region US-East",
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
    result = hyde_decision_node(state)
    assert result["use_hyde"] is False
    assert "detailed" in result["hyde_reason"].lower() or "specific" in result["hyde_reason"].lower()

def test_hyde_decision_enabled_for_abstract_query():
    """Test that hyde_decision_node enables HyDE for short, non-technical colloquial queries."""
    state: AgentState = {
        "message": "How do I get my money back?",
        "history": [],
        "category": "rag",
        "use_hyde": False,
        "hyde_reason": None,
        "hypothetical_document": None,
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = hyde_decision_node(state)
    assert result["use_hyde"] is True
    assert "abstract" in result["hyde_reason"].lower() or "colloquial" in result["hyde_reason"].lower()
