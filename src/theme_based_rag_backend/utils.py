#region Utility Functions
import math

def cosine_similarity(v1: list, v2: list) -> float:
    """Calculates the cosine similarity between two numerical vectors."""
    dot_product = sum(x * y for x, y in zip(v1, v2))
    norm_v1 = math.sqrt(sum(x * x for x in v1))
    norm_v2 = math.sqrt(sum(x * x for x in v2))
    if not norm_v1 or not norm_v2:
        return 0.0
    return dot_product / (norm_v1 * norm_v2)
#endregion
