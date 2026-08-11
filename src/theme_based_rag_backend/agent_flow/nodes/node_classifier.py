#region Imports & Node Implementation
from functools import lru_cache
from ...config import CHATBOT_THEME
from ...utils import cosine_similarity
from ..state import AgentState
from ...llm_client import embeddings

@lru_cache(maxsize=1)
def get_theme_embedding(theme: str) -> list:
    """Generates and caches theme embedding using lru_cache to avoid redundant API calls."""
    return embeddings.embed_query(theme)

def classifier_node(state: AgentState) -> dict:
    query = state["query"]
    
    try:
        # Embed theme (cached) and query using shared embeddings client
        theme_vector = get_theme_embedding(CHATBOT_THEME)
        query_vector = embeddings.embed_query(query)
        
        # Calculate similarity
        similarity = cosine_similarity(theme_vector, query_vector)
        
        # Threshold check (0.65 is a good baseline for gemini-embedding-001)
        threshold = 0.65
        should_answer = "pass" if similarity >= threshold else "refuse"
        
    except Exception:
        should_answer = "refuse"
        
    return {"should_answer": should_answer}
#endregion

