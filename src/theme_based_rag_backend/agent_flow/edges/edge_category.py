from src.theme_based_rag_backend.agent_flow.state import AgentState

def route_by_category(state: AgentState) -> str:
    """Routes state based on classification category ('rag' vs 'refuse')."""
    return state["category"]
