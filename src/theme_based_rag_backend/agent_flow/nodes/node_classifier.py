#region Imports & Node Implementation
import logging
from functools import lru_cache
from src.theme_based_rag_backend.config import CHATBOT_THEME
from src.theme_based_rag_backend.utils import cosine_similarity
from src.theme_based_rag_backend.agent_flow.state import AgentState
from src.theme_based_rag_backend.llm_client import embeddings

logger = logging.getLogger(__name__)

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
        
    except Exception as e:
        logger.error(f"Error during vector similarity classification: {e}. Falling back to 'refuse'.")
        should_answer = "refuse"
        
    return {"should_answer": should_answer}
#endregion

