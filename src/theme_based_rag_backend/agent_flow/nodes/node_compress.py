#region Context Compression
from ...config import LLMLINGUA_RATE
from ...llm_client import compressor
from ..state import AgentState


def compress_node(state: AgentState) -> dict:
    """Compresses retrieved documents using LLMLingua-2 to reduce prompt tokens and latency."""
    query = state["query"]
    docs = state.get("retrieved_documents", "")

    if not docs:
        return {"compressed_documents": docs}

    try:
        result = compressor.compress_prompt(
            context=[docs],
            instruction="",
            question=query,
            rate=LLMLINGUA_RATE,
        )
        compressed_context = result.get("compressed_prompt", docs)
    except Exception:
        compressed_context = docs

    return {"compressed_documents": compressed_context}
#endregion
