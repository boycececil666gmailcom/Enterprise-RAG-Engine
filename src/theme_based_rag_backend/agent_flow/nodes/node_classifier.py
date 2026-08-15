#region Classifier Node
from functools import lru_cache

from ...config import CHATBOT_THEME
from ...llm_client import embeddings
from ...utils import cosine_similarity
from ..state import AgentState


@lru_cache(maxsize=1)
def get_theme_embedding(theme: str) -> list[float]:
    """Generates and caches theme embedding."""
    return embeddings.embed_query(theme)


def classifier_node(state: AgentState) -> dict:
    """Classifies if query aligns with configured chatbot theme."""
    try:
        theme_vector = get_theme_embedding(CHATBOT_THEME)
        query_vector = embeddings.embed_query(state["query"])
        similarity = cosine_similarity(theme_vector, query_vector)
        should_answer = "pass" if similarity >= 0.65 else "refuse"
    except Exception:
        should_answer = "refuse"

    return {"should_answer": should_answer}
#endregion
