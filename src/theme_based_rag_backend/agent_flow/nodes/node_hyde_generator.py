#region Imports & Node Implementation
from langchain_core.messages import SystemMessage, HumanMessage
from ..state import AgentState
from ...llm_client import hyde_llm
from ...models import HyDESchema

def generate_hypothetical_document(query: str) -> str:
    """Generates a hypothetical document passage for the given user query with Pydantic type safety."""
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
        structured_llm = hyde_llm.with_structured_output(HyDESchema)
        res: HyDESchema = structured_llm.invoke(messages)
        if res and res.passage:
            return res.passage.strip()
    except Exception:
        pass
    
    return query

def hyde_node(state: AgentState) -> dict:
    """Standalone LangGraph node that generates a hypothetical document and saves it into AgentState."""
    query = state["query"]
    hypo_doc = generate_hypothetical_document(query)
    return {"hyde_content": hypo_doc}
#endregion
