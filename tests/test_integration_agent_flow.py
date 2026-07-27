import pytest
from unittest.mock import patch, MagicMock
from src.theme_based_rag_backend.agent_flow import (
    AgentState,
    classifier_node,
    rag_qa_node,
    refuse_node,
    critique_node,
    route_by_category,
    route_after_critique,
    agent_graph
)

# Test classifier_node
@patch("src.theme_based_rag_backend.vector_db.embeddings")
def test_classifier_node_rag(mock_embeddings):
    """Test that classifier_node classifies query as 'rag' when cosine similarity is high (>= 0.65)."""
    import src.theme_based_rag_backend.agent_flow.nodes.node_classifier as classifier_module

    classifier_module.theme_embedding_cached = None
    
    mock_embeddings.embed_query.return_value = [1.0, 0.0]

    state: AgentState = {
        "message": "Relevant Fintech SaaS platform question",
        "history": [],
        "category": "refuse",
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = classifier_node(state)
    assert result == {"category": "rag"}

@patch("src.theme_based_rag_backend.vector_db.embeddings")
def test_classifier_node_refuse(mock_embeddings):
    """Test that classifier_node classifies query as 'refuse' when cosine similarity is low (< 0.65)."""
    import src.theme_based_rag_backend.agent_flow.nodes.node_classifier as classifier_module

    classifier_module.theme_embedding_cached = None
    
    mock_embeddings.embed_query.side_effect = [[1.0, 0.0], [0.0, 1.0]]

    state: AgentState = {
        "message": "Unrelated question",
        "history": [],
        "category": "rag",
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = classifier_node(state)
    assert result == {"category": "refuse"}

@patch("src.theme_based_rag_backend.vector_db.embeddings")
def test_classifier_node_fallback(mock_embeddings):
    """Test that classifier_node falls back to 'refuse' when an embedding exception occurs."""
    mock_embeddings.embed_query.side_effect = Exception("API error")

    state: AgentState = {
        "message": "Query message",
        "history": [],
        "category": "rag",
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = classifier_node(state)
    assert result == {"category": "refuse"}

# Test refuse_node
@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_refuse_node(mock_llm):
    """Test that refuse_node generates a standard refusal/guardrails message for queries classified under the 'refuse' category."""
    mock_response = MagicMock()
    mock_response.content = "I can only assist with Fintech SaaS platform questions."
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "General query",
        "history": [],
        "category": "refuse",
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = refuse_node(state)
    assert result == {"agent_response": "I can only assist with Fintech SaaS platform questions."}

# Test rag_qa_node
@patch("src.theme_based_rag_backend.agent_flow.retrieve_local_documents")
@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_rag_qa_node_with_retrieval(mock_llm, mock_retrieve):
    """Test that rag_qa_node retrieves related documents when none are present in state, and synthesizes a draft response."""
    mock_retrieve.invoke.return_value = "Retrieved doc context"
    mock_response = MagicMock()
    mock_response.content = "Synthesized response"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "rag",
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = rag_qa_node(state)
    
    assert result["agent_response"] == "Synthesized response"
    assert result["retrieved_documents"] == "Retrieved doc context"
    mock_retrieve.invoke.assert_called_once_with("query message")

@patch("src.theme_based_rag_backend.agent_flow.retrieve_local_documents")
@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_rag_qa_node_already_retrieved(mock_llm, mock_retrieve):
    """Test that rag_qa_node uses existing retrieved documents in state without invoking retrieval again to generate a response."""
    mock_response = MagicMock()
    mock_response.content = "Synthesized response"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "rag",
        "retrieved_documents": "Existing documents",
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }
    result = rag_qa_node(state)
    
    assert result["agent_response"] == "Synthesized response"
    assert result["retrieved_documents"] == "Existing documents"
    mock_retrieve.invoke.assert_not_called()

# Test critique_node
@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_critique_node_refuse_pass(mock_llm):
    """Test that critique_node invokes the LLM critique and approves (PASS) a valid refusal response."""
    mock_response = MagicMock()
    mock_response.content = "PASS"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "refuse",
        "retrieved_documents": None,
        "agent_response": "I can only assist with Fintech SaaS platform questions.",
        "critique_feedback": None,
        "attempts": 0
    }
    result = critique_node(state)
    assert result == {"critique_feedback": "PASS"}
    mock_llm.invoke.assert_called_once()

@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_critique_node_refuse_fail(mock_llm):
    """Test that critique_node rejects (FAIL) a refusal response that does not adhere to the guardrails."""
    mock_response = MagicMock()
    mock_response.content = "Accidentally answers the question"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "refuse",
        "retrieved_documents": None,
        "agent_response": "Here is the recipe for chocolate cake...",
        "critique_feedback": None,
        "attempts": 0
    }
    result = critique_node(state)
    assert result == {"critique_feedback": "Accidentally answers the question", "attempts": 1}
    mock_llm.invoke.assert_called_once()

@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_critique_node_pass(mock_llm):
    """Test that critique_node returns a 'PASS' status when the LLM critique determines the draft response is accurate and appropriate."""
    mock_response = MagicMock()
    mock_response.content = "PASS"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "rag",
        "retrieved_documents": "Context",
        "agent_response": "Response",
        "critique_feedback": None,
        "attempts": 1
    }
    result = critique_node(state)
    assert result == {"critique_feedback": "PASS"}

@patch("src.theme_based_rag_backend.agent_flow.llm")
def test_critique_node_fail(mock_llm):
    """Test that critique_node returns detailed feedback and increments the attempts counter when the LLM critique finds issues in the draft response."""
    mock_response = MagicMock()
    mock_response.content = "Hallucination of fact X"
    mock_llm.invoke.return_value = mock_response

    state: AgentState = {
        "message": "query message",
        "history": [],
        "category": "rag",
        "retrieved_documents": "Context",
        "agent_response": "Response",
        "critique_feedback": None,
        "attempts": 1
    }
    result = critique_node(state)
    assert result == {"critique_feedback": "Hallucination of fact X", "attempts": 2}

# Test route_by_category
def test_route_by_category():
    """Test that route_by_category correctly routes the flow based on the classification category ('rag' or 'refuse')."""
    state: AgentState = {"category": "rag"}
    assert route_by_category(state) == "rag"
    
    state = {"category": "refuse"}
    assert route_by_category(state) == "refuse"

# Test route_after_critique
def test_route_after_critique():
    """Test that route_after_critique correctly routes the workflow to approved or rejected based on the critique feedback and attempts count."""
    state: AgentState = {"critique_feedback": "PASS", "attempts": 0}
    assert route_after_critique(state) == "approved"
    
    state = {"critique_feedback": "Hallucination detected", "attempts": 1}
    assert route_after_critique(state) == "rejected"
    
    state = {"critique_feedback": "Hallucination detected", "attempts": 3}
    assert route_after_critique(state) == "approved"

# Test compiled graph end-to-end
@patch("src.theme_based_rag_backend.vector_db.embeddings")
@patch("src.theme_based_rag_backend.agent_flow.nodes.node_hyde_generator.get_hyde_llm")
@patch("src.theme_based_rag_backend.agent_flow.retrieve_local_documents")
@patch("src.theme_based_rag_backend.agent_flow.llm")
@pytest.mark.asyncio
async def test_agent_graph_e2e(mock_llm, mock_retrieve, mock_hyde_llm, mock_embeddings):
    """Test that the compiled LangGraph agent workflow functions correctly end-to-end from classification to final approved response."""
    import src.theme_based_rag_backend.agent_flow.nodes.node_classifier as classifier_module
    classifier_module.theme_embedding_cached = None
    mock_embeddings.embed_query.return_value = [1.0, 0.0]
    
    mock_hyde_llm.return_value = mock_llm
    mock_retrieve.invoke.return_value = "Retrieved documents"
    
    # Mock LLM calls: HyDE Generation -> RAG QA -> Critique (Classifier is vector-similarity based)
    mock_resp_hyde = MagicMock(content='Hypothetical document passage')
    mock_resp_qa = MagicMock(content='Draft Response text')
    mock_resp_crit = MagicMock(content="PASS")
    
    mock_llm.invoke.side_effect = [mock_resp_hyde, mock_resp_qa, mock_resp_crit]



    
    inputs = {
        "message": "How does the Fintech SaaS platform process payments?",
        "history": [],
        "category": "refuse",

        "hypothetical_document": None,
        "retrieved_documents": None,
        "agent_response": "",
        "critique_feedback": None,
        "attempts": 0
    }

    
    result = await agent_graph.ainvoke(inputs)
    assert result["category"] == "rag"
    assert result["agent_response"] == "Draft Response text"
    assert result["critique_feedback"] == "PASS"
