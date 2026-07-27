from src.theme_based_rag_backend.agent_flow.state import AgentState

def route_after_critique(state: AgentState) -> str:
    """Routes to 'approved' (END) or 'rejected' (loop back) based on critique feedback."""
    feedback = state.get("critique_feedback")
    attempts = state.get("attempts", 0)
    
    if feedback == "PASS" or attempts >= 3:
        if attempts >= 3 and feedback != "PASS":
            print("Max refinement attempts reached. Proceeding with best effort response.")
        return "approved"
    return "rejected"
