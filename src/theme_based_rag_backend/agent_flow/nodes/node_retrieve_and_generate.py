#region Imports & Node Implementation
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from ...llm_client import llm
from ...models import RAGResponseSchema
from ...tools import retrieve_VDB
from ..state import AgentState

#endregion

#region Retrieve and Generate Node Implementation
def retrieve_and_generate_node(state: AgentState) -> dict:
    query = state["query"]
    history = state.get("history", [])
    hypo_doc = state.get("hyde_content")

    retrieved_documents = state.get("retrieved_documents")
    if not retrieved_documents:
        search_target = hypo_doc if hypo_doc else query
        retrieved_documents = retrieve_VDB.invoke(search_target)

    system_prompt = (
        f"Retrieved Document Context:\n{retrieved_documents}\n\n"
        f"CRITICAL RULES:\n"
        f"1. Your answer must be strictly grounded in the retrieved document context.\n"
        f"2. If the context does not contain the answer or specific details (such as prices, plans, dates, or figures), "
        f"explicitly state 'Information not available in documentation'. \n"
        f"3. NEVER extrapolate, guess, or invent numbers, prices, or missing facts to fill in gaps (Anti-Hallucination Amplification).\n"
    )

    messages = [SystemMessage(content=system_prompt)]
    
    # Hydrate messages using history
    for msg in history:
        role = msg.get("role")
        content = msg.get("content")
        if role == "user":
            messages.append(HumanMessage(content=content))
        elif role == "assistant":
            messages.append(AIMessage(content=content))
            
    messages.append(HumanMessage(content=query))
    
    # Include critique feedback if any
    feedback = state.get("critique_feedback")
    prev_draft = state.get("final_response")
    if feedback and prev_draft:
        messages.append(AIMessage(content=prev_draft))
        refine_msg = (
            f"CRITIQUE FEEDBACK: Your previous draft answer was rejected because: {feedback}\n"
            f"Please revise your answer to address this feedback. Make sure the response is "
            f"fully grounded in the retrieved document context."
        )
        messages.append(HumanMessage(content=refine_msg))
        
    structured_llm = llm.with_structured_output(RAGResponseSchema)
    response = structured_llm.invoke(messages)
    
    if not response or not getattr(response, "answer", None):
        raise ValueError(f"Failed to generate valid structured RAG response from LLM. Received: {response}")
    
    answer_text = response.answer
    
    updated_history = list(history) + [
        {"role": "user", "content": query},
        {"role": "assistant", "content": answer_text}
    ]
    
    return {
        "final_response": answer_text,
        "retrieved_documents": retrieved_documents,
        "history": updated_history
    }
#endregion

