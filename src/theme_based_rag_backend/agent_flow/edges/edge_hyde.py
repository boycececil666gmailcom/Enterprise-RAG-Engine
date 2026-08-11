from ..state import AgentState

def route_by_hyde_decision(state: AgentState) -> str:
    """Routes to 'enable' (hyde_node) or 'skip' (retrieve_and_generate_node) based on HyDE decision state."""
    should_hyde = state.get("should_hyde", True)
    return "enable" if should_hyde else "skip"
