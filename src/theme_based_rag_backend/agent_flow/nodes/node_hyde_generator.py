#region Imports & Node Implementation
import logging
from langchain_core.messages import SystemMessage, HumanMessage
from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.llm_client import hyde_llm

logger = logging.getLogger(__name__)

def generate_hypothetical_document(query: str) -> str:
    """Generates a hypothetical document passage for the given user query.
    Falls back to original query if generation fails or LLM is unavailable."""
    try:
        system_prompt = (
            "You are a helpful assistant. Please write a short, plausible excerpt or passage "
            "from an internal documentation document that directly answers the user's query. "
            "Do not include conversational intros or filler. Output only the hypothetical document excerpt."
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        response = hyde_llm.invoke(messages)
        content = response.content
        return content.strip()
    except Exception as e:
        logger.warning(f"HyDE generation failed ({e})")
    
    return query

def hyde_node(state: AgentState) -> dict:
    """Standalone LangGraph node that generates a hypothetical document and saves it into AgentState."""
    query = state["query"]
    hypo_doc = generate_hypothetical_document(query)
    return {"hyde_content": hypo_doc}
#endregion
