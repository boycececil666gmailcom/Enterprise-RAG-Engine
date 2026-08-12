#region Module Initialization
"""
RAGAS Evaluation Package for Enterprise RAG Engine.
Consolidates evaluator, dataset generator, and evaluation runners.
"""
def __getattr__(name):
    if name in ("evaluate_rag_pipeline", "RagasEvalResult", "RagasEvalSample"):
        from .ragas_evaluator import (
            RagasEvalResult,
            RagasEvalSample,
            evaluate_rag_pipeline,
        )
        return locals()[name]
    elif name == "generate_eval_dataset_from_chunks":
        from .scripts.dataset_generator import generate_eval_dataset_from_chunks
        return generate_eval_dataset_from_chunks
    elif name == "run_agent_evaluation":
        from .scripts.run_ragas_eval import run_agent_evaluation
        return run_agent_evaluation
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "evaluate_rag_pipeline",
    "RagasEvalResult",
    "RagasEvalSample",
    "generate_eval_dataset_from_chunks",
    "run_agent_evaluation"
]
#endregion
