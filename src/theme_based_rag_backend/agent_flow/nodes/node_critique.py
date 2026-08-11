#region Imports & Node Implementation
import logging
from langchain_core.messages import HumanMessage
from src.theme_based_rag_backend.config import CHATBOT_THEME
from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.llm_client import llm

logger = logging.getLogger(__name__)

def critique_node(state: AgentState) -> dict:
    should_answer = state.get("should_answer")
    draft = state.get("final_response")

    docs = state.get("retrieved_documents")
    query = state["query"]
    attempt_count = state.get("attempt_count", 0)
    hypo_doc = state.get("hyde_content")

    if should_answer == "refuse":
        critique_prompt = (
            f"You are a strict quality control evaluator.\n"
            f"Your task is to verify if the draft response is a polite refusal to answer a query outside the theme: '{CHATBOT_THEME}'.\n"
            f"Make sure the response does NOT attempt to answer the user's query or provide any information related to the query, "
            f"and that it clearly and politely states that it can only assist with questions related to '{CHATBOT_THEME}'.\n\n"
            f"User Query: {query}\n\n"
            f"Draft Response to Evaluate: {draft}\n\n"
            f"If the response is a correct and polite refusal, output exactly: PASS\n"
            f"Otherwise, output a detailed explanation of what is wrong with the response."
        )
    else:
        critique_prompt = (
            f"You are a strict quality control evaluator.\n"
            f"Your task is to verify if the draft response is fully grounded in the retrieved documents context.\n"
            f"STRICT HALLUCINATION CHECK:\n"
            f"- Verify that all facts, numbers, prices, and specifications in the draft response exist EXPLICITLY in the retrieved context.\n"
            f"- If the draft response invents or extrapolates numbers/prices (e.g., guessing a monthly fee when the document only mentions plan names), MARK IT AS FAIL.\n\n"
            f"User Query: {query}\n"
            f"HyDE Hypothetical Query Representation: {hypo_doc or 'N/A'}\n\n"
            f"Retrieved Context:\n{docs}\n\n"
            f"Draft Response to Evaluate: {draft}\n\n"
            f"If the response is fully grounded and contains zero extrapolated numbers/facts, output exactly: PASS\n"
            f"Otherwise, output a detailed explanation of what is wrong, extrapolated, or hallucinated."
        )

    messages = [HumanMessage(content=critique_prompt)]
    response = llm.invoke(messages)
    
    content = response.content
    if isinstance(content, list):
        content = "".join(part if isinstance(part, str) else part.get("text", "") for part in content)
    content = content.strip()
    if "pass" in content.lower():
        status = "PASS"
        reason = None
    else:
        status = "FAIL"
        reason = content
            
    if status == "PASS":
        return {"critique_feedback": "PASS"}
    else:
        return {
            "critique_feedback": reason,
            "attempt_count": attempt_count + 1
        }
#endregion

