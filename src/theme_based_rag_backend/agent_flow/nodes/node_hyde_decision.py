#region Imports & Node Implementation
import re
from ..state import AgentState

def hyde_decision_node(state: AgentState) -> dict:
    """Analyzes the user query dynamically to decide whether HyDE expansion should be enabled or skipped."""
    query = state["query"].strip()

    # 1. Check for specific error codes, UUIDs, model/version patterns or numeric identifiers
    error_pattern = r'(error|err|code|uuid|v\d+\.\d+|\b[A-Z]{2,}-\d+\b|\b\d{3,5}\b)'
    if re.search(error_pattern, query, re.IGNORECASE):
        reason = "Query contains exact technical identifier, code, or error number pattern"
        return {"should_hyde": False, "hyde_reason": reason}

    # 2. Check for overly detailed / long queries
    if len(query) > 80 or len(query.split()) >= 12:
        reason = "Query is already specific, detailed, and keyword-rich"
        return {"should_hyde": False, "hyde_reason": reason}

    # 3. Default for abstract / non-technical / short queries -> Enable HyDE
    reason = "Abstract or non-technical query benefits from HyDE hypothetical expansion"
    return {"should_hyde": True, "hyde_reason": reason}
#endregion
