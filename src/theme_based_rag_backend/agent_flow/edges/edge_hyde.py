from src.theme_based_rag_backend.agent_flow.state import AgentState

def route_by_hyde_decision(state: AgentState) -> str:
    """Routes to 'enable' (hyde_node) or 'skip' (rag_qa_node) based on HyDE decision state."""
    use_hyde = state.get("use_hyde", True)
    return "enable" if use_hyde else "skip"
