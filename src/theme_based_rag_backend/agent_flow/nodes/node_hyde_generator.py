# region HyDE Generator
from typing import cast

from langchain_core.messages import HumanMessage, SystemMessage

from ...llm_client import hyde_llm
from ...models import HyDESchema
from ..state import AgentState


def generate_hypothetical_document(query: str) -> str:
    """Generates a hypothetical technical document passage for query expansion."""
    system_prompt = (
        "You are an expert technical documentation author and software engineer.\n"
        "Write a concise, realistic 2-3 sentence technical excerpt that directly answers the user's query.\n"
        "Include relevant technical concepts, APIs, and error terminology if applicable. Output only the excerpt."
    )
    try:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query),
        ]
        structured_llm = hyde_llm.with_structured_output(HyDESchema)
        res = cast(HyDESchema, structured_llm.invoke(messages))
        if res and res.passage:
            return res.passage.strip()
    except Exception:
        pass
    return query


def hyde_node(state: AgentState) -> dict:
    """Generates hypothetical document passage and updates agent state."""
    return {"hyde_content": generate_hypothetical_document(state["query"])}


# endregion
