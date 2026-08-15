#region Utility
import math


def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    """Calculates cosine similarity between two numerical vectors."""
    dot = sum(x * y for x, y in zip(v1, v2))
    norm_v1 = math.sqrt(sum(x * x for x in v1))
    norm_v2 = math.sqrt(sum(x * x for x in v2))
    if not norm_v1 or not norm_v2:
        return 0.0
    return dot / (norm_v1 * norm_v2)
#endregion
