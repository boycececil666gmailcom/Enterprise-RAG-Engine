#region Imports & Node Implementation
from langchain_core.messages import SystemMessage, HumanMessage
from ...config import CHATBOT_THEME
from ...models import RAGResponseSchema
from ..state import AgentState
from ...llm_client import llm

def refuse_node(state: AgentState) -> dict:
    refusal_prompt = (
        f"You are a customer service assistant bound to the theme '{CHATBOT_THEME}'.\n"
        f"Politely explain to the user that you are only configured to assist with questions "
        f"related to '{CHATBOT_THEME}', and decline to answer this query."
    )
    messages = [
        SystemMessage(content=refusal_prompt),
        HumanMessage(content=state["query"])
    ]
    structured_llm = llm.with_structured_output(RAGResponseSchema)
    response: RAGResponseSchema = structured_llm.invoke(messages)
    return {"final_response": response.answer}
#endregion
