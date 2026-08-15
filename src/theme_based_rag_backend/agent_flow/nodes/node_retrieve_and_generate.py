#region Retrieval & Generation
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from ...llm_client import llm
from ...models import RAGResponseSchema
from ...tools import retrieve_VDB
from ..state import AgentState


def retrieve_and_generate_node(state: AgentState) -> dict:
    """Retrieves document context and synthesizes strictly grounded answer."""
    query = state["query"]
    history = state.get("history", [])
    hypo_doc = state.get("hyde_content")

    retrieved_documents = state.get("retrieved_documents")
    if not retrieved_documents:
        search_target = hypo_doc if hypo_doc else query
        retrieved_documents = retrieve_VDB.invoke(search_target)

    system_prompt = (
        f"Retrieved Document Context:\n{retrieved_documents}\n\n"
        "CRITICAL RULES:\n"
        "1. Your answer must be strictly grounded in the retrieved document context.\n"
        "2. If context does not contain the answer or specific details, state 'Information not available in documentation'.\n"
        "3. NEVER extrapolate, guess, or invent numbers, prices, or missing facts."
    )

    messages = [SystemMessage(content=system_prompt)]

    # Append conversational history
    for msg in history:
        role, content = msg.get("role"), msg.get("content", "")
        if role == "user":
            messages.append(HumanMessage(content=content))
        elif role == "assistant":
            messages.append(AIMessage(content=content))

    messages.append(HumanMessage(content=query))

    # Append critique feedback for retry loops if present
    feedback = state.get("critique_feedback")
    prev_draft = state.get("final_response")
    if feedback and prev_draft:
        messages.append(AIMessage(content=prev_draft))
        messages.append(HumanMessage(content=(
            f"CRITIQUE FEEDBACK: Previous draft was rejected because: {feedback}\n"
            "Revise your answer to strictly follow retrieved context."
        )))

    structured_llm = llm.with_structured_output(RAGResponseSchema)
    response: RAGResponseSchema = structured_llm.invoke(messages)
    answer_text = response.answer if response else "Information not available in documentation."

    updated_history = list(history) + [
        {"role": "user", "content": query},
        {"role": "assistant", "content": answer_text},
    ]

    return {
        "final_response": answer_text,
        "retrieved_documents": retrieved_documents,
        "history": updated_history,
    }
#endregion
