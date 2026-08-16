#region Critique Node
from typing import cast
from langchain_core.messages import HumanMessage

from ...config import CHATBOT_THEME
from ...llm_client import llm
from ...models import CritiqueResultSchema
from ..state import AgentState


def critique_node(state: AgentState) -> dict:
    """Evaluates draft answer quality and groundedness against retrieved context or refusal rules."""
    should_answer = state.get("should_answer")
    draft = state.get("final_response")
    docs = state.get("compressed_documents")
    query = state["query"]
    attempt_count = state.get("attempt_count", 0)
    hypo_doc = state.get("hyde_content")

    if should_answer == "refuse":
        prompt = (
            f"You are a strict quality control evaluator.\n"
            f"Verify if the draft response is a polite refusal to answer a query outside the theme: '{CHATBOT_THEME}'.\n"
            f"User Query: {query}\n"
            f"Draft Response: {draft}\n"
            f"If polite and correct refusal, output is_passed: True. Otherwise output is_passed: False with detailed feedback."
        )
    else:
        prompt = (
            f"You are a strict quality control evaluator.\n"
            f"Verify if the draft response is fully grounded in the retrieved documents context.\n"
            f"STRICT CHECK: No extrapolated or invented numbers/facts.\n"
            f"User Query: {query}\n"
            f"HyDE Passage: {hypo_doc or 'N/A'}\n"
            f"Retrieved Context:\n{docs}\n"
            f"Draft Response: {draft}\n"
            f"If fully grounded with zero hallucination, output is_passed: True. Otherwise output is_passed: False with feedback."
        )

    structured_llm = llm.with_structured_output(CritiqueResultSchema)
    eval_result = cast(
        CritiqueResultSchema,
        structured_llm.invoke([HumanMessage(content=prompt)]),
    )

    if eval_result.is_passed:
        return {"critique_feedback": "PASS"}

    return {
        "critique_feedback": eval_result.feedback or "Failed groundedness validation",
        "attempt_count": attempt_count + 1,
    }
#endregion
