#region Imports & Node Implementation
from langchain_core.messages import SystemMessage, HumanMessage
from ...config import CHATBOT_THEME, FORCE_RAG_KEYWORDS
from ...models import ClassifierSchema
from ..state import AgentState
from ...llm_client import llm

def routing_node(state: AgentState) -> dict:
    query = state["query"]
    
    try:
        keywords_str = ", ".join(f"'{kw}'" for kw in FORCE_RAG_KEYWORDS)
        system_prompt = (
            f"You are a routing agent for a customer service chatbot.\n"
            f"Your task is to classify whether a user query is related to the theme: '{CHATBOT_THEME}'.\n"
            f"Queries referencing the following proprietary or theme-specific keywords should also be routed as relevant: {keywords_str}.\n"
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
        structured_llm = llm.with_structured_output(ClassifierSchema)
        res: ClassifierSchema = structured_llm.invoke(messages)
        should_answer = res.category if (res and res.category) else "refuse"
    except Exception:
        should_answer = "refuse"
        
    return {"should_answer": should_answer}
#endregion
