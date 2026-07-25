import logging
from langchain_core.messages import SystemMessage, HumanMessage
from src.theme_based_rag_backend.config import GEMINI_API_KEY, GEMINI_MODEL
from src.theme_based_rag_backend.agent_flow.state import AgentState

logger = logging.getLogger(__name__)

_hyde_llm = None

def get_hyde_llm():
    """Lazily initialize LLM instance for HyDE generation."""
    global _hyde_llm
    if _hyde_llm is None:
        if not GEMINI_API_KEY or GEMINI_API_KEY == "dummy_key_for_testing":
            return None
        from langchain_google_genai import ChatGoogleGenerativeAI
        _hyde_llm = ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GEMINI_API_KEY,
            temperature=0.3
        )
    return _hyde_llm

def generate_hypothetical_document(query: str) -> str:
    """Generates a hypothetical document passage for the given user query.
    Falls back to original query if generation fails or LLM is unavailable."""
    try:
        llm = get_hyde_llm()
        if not llm:
            return query

        system_prompt = (
            "You are a helpful assistant. Please write a short, plausible excerpt or passage "
            "from an internal documentation document that directly answers the user's query. "
            "Do not include conversational intros or filler. Output only the hypothetical document excerpt."
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        response = llm.invoke(messages)
        content = response.content
        if isinstance(content, list):
            content = "".join(part if isinstance(part, str) else part.get("text", "") for part in content)
        
        if content and content.strip():
            logger.info(f"HyDE generated hypothetical document for query '{query}': {content[:100]}...")
            return content.strip()
    except Exception as e:
        logger.warning(f"HyDE generation failed ({e}), falling back to original query.")
    
    return query

def hyde_node(state: AgentState) -> dict:
    """Standalone LangGraph node that generates a hypothetical document and saves it into AgentState."""
    query = state["message"]
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [Agent Flow] Executing Standalone HyDE Generation Node\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    hypo_doc = generate_hypothetical_document(query)
    print(f"Generated HyDE Hypothetical Document: '{hypo_doc[:100]}...'")
    return {"hypothetical_document": hypo_doc}
