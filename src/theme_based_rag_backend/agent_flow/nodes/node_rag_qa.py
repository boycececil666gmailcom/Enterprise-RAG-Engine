#region Imports & Node Implementation
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.theme_based_rag_backend.config import CHATBOT_THEME
from src.theme_based_rag_backend.models import RAGResponseSchema
from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.llm_client import llm
from src.theme_based_rag_backend.tools import retrieve_local_documents
#endregion

#region RAG QA Node Implementation
def rag_qa_node(state: AgentState) -> dict:
    query = state["query"]
    history = state.get("history", [])
    retrieved_documents = state.get("retrieved_documents")

    system_prompt = (
        f"You are a customer service assistant. Your primary theme is: {CHATBOT_THEME}.\n"
        f"Answer the user's question using ONLY the provided retrieved document context below.\n\n"
        f"Retrieved Document Context:\n{retrieved_documents}\n\n"
        f"CRITICAL RULES:\n"
        f"1. Your answer must be strictly grounded in the retrieved document context.\n"
        f"2. If the context does not contain the answer or specific details (such as prices, plans, dates, or figures), "
        f"explicitly state 'Information not available in documentation'. \n"
        f"3. NEVER extrapolate, guess, or invent numbers, prices, or missing facts to fill in gaps (Anti-Hallucination Amplification).\n"
        f"4. Do not make up facts or use pre-trained general knowledge."
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
    response: RAGResponseSchema = structured_llm.invoke(messages)
    
    updated_history = list(history) + [
        {"role": "user", "content": query},
        {"role": "assistant", "content": response.answer}
    ]
    
    return {
        "final_response": response.answer,
        "retrieved_documents": retrieved_documents,
        "history": updated_history
    }
#endregion

