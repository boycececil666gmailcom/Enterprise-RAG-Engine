#region Imports & Node Implementation
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.theme_based_rag_backend.config import CHATBOT_THEME
from src.theme_based_rag_backend.models import RAGResponseSchema
from src.theme_based_rag_backend.agent_flow.state import AgentState
#endregion

#region RAG QA Node Implementation
def rag_qa_node(state: AgentState) -> dict:
    from src.theme_based_rag_backend.agent_flow import llm, retrieve_local_documents
    query = state["message"]
    history = state.get("history", [])
    hypo_doc = state.get("hypothetical_document")
    
    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [Agent Flow] Executing RAG QA retrieval & synthesis\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    # Retrieve local documents using HyDE hypothetical document if present, otherwise raw query
    retrieved_docs = state.get("retrieved_documents")
    if not retrieved_docs:
        search_target = hypo_doc if hypo_doc else query
        print(f"Invoking retrieve_local_documents tool with target: '{search_target[:60]}...'")
        retrieved_docs = retrieve_local_documents.invoke(search_target)
    
    system_prompt = (
        f"You are a customer service assistant. Your primary theme is: {CHATBOT_THEME}.\n"
        f"Answer the user's question using ONLY the provided retrieved document context below.\n\n"
        f"Retrieved Document Context:\n{retrieved_docs}\n\n"
        f"CRITICAL RULES:\n"
        f"1. Your answer must be strictly grounded in the retrieved document context.\n"
        f"2. If the context does not contain the answer or specific details (such as prices, plans, dates, or figures), "
        f"explicitly state 'ドキュメントに該当情報が記載されていません' (Information not available in documentation).\n"
        f"3. NEVER extrapolate, guess, or invent numbers, prices, or missing facts to fill in gaps (Anti-Hallucination Amplification).\n"
        f"4. Do not make up facts or use pre-trained general knowledge."
    )

    messages = [SystemMessage(content=system_prompt)]
    
    # Hydrate history
    for msg in history:
        role = msg.get("role")
        content = msg.get("content")
        if role == "user":
            messages.append(HumanMessage(content=content))
        elif role == "assistant":
            messages.append(AIMessage(content=content))
            
    messages.append(HumanMessage(content=query))
    
    # Include critique feedback
    feedback = state.get("critique_feedback")
    prev_draft = state.get("agent_response")
    if feedback and prev_draft:
        print(f"Refinement attempt: applying critique feedback: {feedback}")
        messages.append(AIMessage(content=prev_draft))
        refine_msg = (
            f"CRITIQUE FEEDBACK: Your previous draft answer was rejected because: {feedback}\n"
            f"Please revise your answer to address this feedback. Make sure the response is "
            f"fully grounded in the retrieved document context."
        )
        messages.append(HumanMessage(content=refine_msg))
        
    structured_llm = llm.with_structured_output(RAGResponseSchema)
    response: RAGResponseSchema = structured_llm.invoke(messages)
    return {
        "agent_response": response.answer,
        "retrieved_documents": retrieved_docs
    }
#endregion

