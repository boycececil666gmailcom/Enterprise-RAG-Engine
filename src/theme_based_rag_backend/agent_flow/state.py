#region Imports & TypedDict Definitions
from typing import TypedDict, List, Literal, Optional
from typing_extensions import NotRequired

# Input schema visible in LangGraph Studio / LangSmith testing UI
class InputState(TypedDict):
    """User input payload schema required for workflow execution."""
    query: str  # Raw user query input text
    history: NotRequired[List[dict]]  # Prior conversation history list of messages

# Internal state graph schema across workflow nodes
class AgentState(TypedDict):
    """State graph schema passed between LangGraph workflow nodes."""
    query: str  # Primary user query string passed across nodes
    history: NotRequired[List[dict]]  # Chat history messages for conversational context
    should_answer: NotRequired[Literal["rag", "refuse"]]  # Query theme classification result ('rag' or 'refuse')
    should_hyde: NotRequired[bool]  # Flag indicating whether HyDE expansion is enabled
    hyde_reason: NotRequired[Optional[str]]  # Rationale for enabling or skipping HyDE expansion
    hyde_content: NotRequired[Optional[str]]  # Generated hypothetical document passage for vector search
    retrieved_documents: NotRequired[Optional[str]]  # Retrieved document context string from vector and graph DBs
    final_response: NotRequired[str]  # Generated or refined draft response from LLM
    critique_feedback: NotRequired[Optional[str]]  # Feedback from critique node when draft is rejected
    attempt_count: NotRequired[int]  # Count of refinement loop attempts to prevent infinite retries
#endregion
