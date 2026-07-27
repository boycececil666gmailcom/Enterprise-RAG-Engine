from typing import TypedDict, List, Literal, Optional

class AgentState(TypedDict):
    message: str
    history: List[dict]
    category: Literal["rag", "refuse"]
    use_hyde: bool
    hyde_reason: Optional[str]
    hypothetical_document: Optional[str]
    retrieved_documents: Optional[str]
    agent_response: str

    critique_feedback: Optional[str]
    attempts: int
