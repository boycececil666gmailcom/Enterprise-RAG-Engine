#region Imports & TypedDict Definitions
from typing import Literal, NotRequired, TypedDict


# Input schema visible in LangGraph Studio / LangSmith testing UI
class InputState(TypedDict):
    """User input payload schema required for workflow execution."""
    query: str  # Raw user query input text
    history: NotRequired[list[dict]]  # Prior conversation history list of messages

# Internal state graph schema across workflow nodes
class AgentState(TypedDict):
    """State graph schema passed between LangGraph workflow nodes."""
    query: str  # Primary user query string passed across nodes
    history: NotRequired[list[dict]]  # Chat history messages for conversational context
    should_answer: NotRequired[Literal["pass", "refuse"]]  # Query theme classification result ('pass' or 'refuse')
    should_hyde: NotRequired[bool]  # Flag indicating whether HyDE expansion is enabled
    hyde_reason: NotRequired[str | None]  # Rationale for enabling or skipping HyDE expansion
    hyde_content: NotRequired[str | None]  # Generated hypothetical document passage for vector search
    retrieved_documents: NotRequired[str | None]  # Retrieved document context string from vector and graph DBs
    final_response: NotRequired[str]  # Generated or refined draft response from LLM
    critique_feedback: NotRequired[str | None]  # Feedback from critique node when draft is rejected
    attempt_count: NotRequired[int]  # Count of refinement loop attempts to prevent infinite retries
#endregion
