from langchain_google_genai import ChatGoogleGenerativeAI
from src.theme_based_rag_backend.config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_TEMPERATURE
from src.theme_based_rag_backend.tools import retrieve_local_documents

#region LLM Initialization
api_key = GEMINI_API_KEY or "DUMMY_KEY_FOR_STARTUP"

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=api_key,
    temperature=GEMINI_TEMPERATURE
)
#endregion

from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.agent_flow.nodes import (
    classifier_node,
    rag_qa_node,
    refuse_node,
    critique_node
)
from src.theme_based_rag_backend.agent_flow.edges import (
    route_by_category,
    route_after_critique
)
from src.theme_based_rag_backend.agent_flow.graph import agent_graph
