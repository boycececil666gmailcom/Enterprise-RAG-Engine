#region Imports & Configuration
import os
import sys
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# Directly load .env file from project root without depending on backend modules
ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# Apply compatibility shim for ragas vertexai import
try:
    import langchain_community.chat_models.vertexai
except ModuleNotFoundError:
    import types
    mod = types.ModuleType("langchain_community.chat_models.vertexai")
    try:
        from langchain_google_vertexai import ChatVertexAI
        mod.ChatVertexAI = ChatVertexAI
    except ImportError:
        mod.ChatVertexAI = None
    import sys
    sys.modules["langchain_community.chat_models.vertexai"] = mod

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

logger = logging.getLogger(__name__)
#endregion

#region Data Models
@dataclass
class RagasEvalSample:
    """Represents a single query-answer evaluation sample."""
    question: str
    answer: str
    contexts: List[str]
    ground_truth: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class RagasEvalResult:
    """Container for RAGAS evaluation scores and summary metrics."""
    scores: Dict[str, float]
    detailed_df: pd.DataFrame

    def to_markdown(self) -> str:
        """Renders summary metrics table in GitHub Flavored Markdown."""
        lines = ["### 📊 RAGAS Evaluation Summary", "", "| Metric | Score |", "| :--- | :--- |"]
        for metric, score in self.scores.items():
            lines.append(f"| **{metric}** | `{score:.4f}` |")
        return "\n".join(lines)
#endregion

#region RAGAS Client Initialization
def create_ragas_llm_and_embeddings():
    """Instantiates and wraps Gemini LLM and Embeddings independently for RAGAS evaluation."""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key and "pytest" in sys.modules:
        gemini_api_key = "dummy_key_for_testing"

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment variables.")

    gemini_model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
    gemini_embed_model = os.getenv("GEMINI_EMBED_MODEL", "models/text-embedding-004")
    if not gemini_embed_model.startswith("models/") and not gemini_embed_model.startswith("tunedModels/"):
        gemini_embed_model = f"models/{gemini_embed_model}"

    llm = ChatGoogleGenerativeAI(
        model=gemini_model,
        google_api_key=gemini_api_key,
        temperature=0.0
    )
    embeddings = GoogleGenerativeAIEmbeddings(
        model=gemini_embed_model,
        google_api_key=gemini_api_key
    )

    ragas_llm = LangchainLLMWrapper(llm)
    ragas_embeddings = LangchainEmbeddingsWrapper(embeddings)

    return ragas_llm, ragas_embeddings
#endregion

#region RAGAS Evaluation Core Engine
def evaluate_rag_pipeline(
    samples: List[RagasEvalSample],
    metrics_to_run: Optional[List[str]] = None
) -> RagasEvalResult:
    """
    Evaluates a batch of RAG execution samples using RAGAS framework and Gemini models.

    Args:
        samples: List of RagasEvalSample containing question, answer, contexts, and optional ground_truth.
        metrics_to_run: Optional list of metric names to evaluate ('faithfulness', 'answer_relevancy', 'context_precision', 'context_recall').

    Returns:
        RagasEvalResult containing aggregated metric scores and detailed sample DataFrame.
    """
    if not samples:
        raise ValueError("No evaluation samples provided for RAGAS evaluation.")

    try:
        try:
            import langchain_community.chat_models.vertexai
        except ModuleNotFoundError:
            import types
            mod = types.ModuleType("langchain_community.chat_models.vertexai")
            try:
                from langchain_google_vertexai import ChatVertexAI
                mod.ChatVertexAI = ChatVertexAI
            except ImportError:
                mod.ChatVertexAI = None
            import sys
            sys.modules["langchain_community.chat_models.vertexai"] = mod

        from ragas import evaluate
        from ragas.metrics import (
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall
        )
        from datasets import Dataset
    except ImportError as e:
        logger.error(f"RAGAS or datasets package not available: {e}")
        raise RuntimeError("RAGAS dependency missing. Please run `pip install ragas datasets pandas`.") from e

    ragas_llm, ragas_embeddings = create_ragas_llm_and_embeddings()

    # Prepare dataset payload dictionary
    dataset_dict: Dict[str, List[Any]] = {
        "question": [s.question for s in samples],
        "answer": [s.answer for s in samples],
        "contexts": [s.contexts for s in samples],
    }

    # Determine if ground_truth is available across samples
    has_ground_truth = any(s.ground_truth is not None for s in samples)
    if has_ground_truth:
        dataset_dict["ground_truth"] = [s.ground_truth or "" for s in samples]

    eval_dataset = Dataset.from_dict(dataset_dict)

    # Select metrics
    all_metrics = {
        "faithfulness": faithfulness,
        "answer_relevancy": answer_relevancy,
    }
    if has_ground_truth:
        all_metrics["context_precision"] = context_precision
        all_metrics["context_recall"] = context_recall

    if metrics_to_run:
        selected_metrics = [all_metrics[m] for m in metrics_to_run if m in all_metrics]
    else:
        selected_metrics = list(all_metrics.values())

    # Configure metrics with custom LLM & Embeddings
    for m in selected_metrics:
        if hasattr(m, "llm"):
            m.llm = ragas_llm
        if hasattr(m, "embeddings"):
            m.embeddings = ragas_embeddings

    logger.info(f"Running RAGAS evaluation on {len(samples)} samples using {len(selected_metrics)} metrics...")
    
    result = evaluate(
        dataset=eval_dataset,
        metrics=selected_metrics,
        llm=ragas_llm,
        embeddings=ragas_embeddings
    )

    detailed_df = result.to_pandas()
    
    # Calculate summary mean scores
    scores: Dict[str, float] = {}
    for m in selected_metrics:
        metric_name = getattr(m, "name", str(m))
        if metric_name in detailed_df.columns:
            scores[metric_name] = float(detailed_df[metric_name].mean())

    return RagasEvalResult(scores=scores, detailed_df=detailed_df)
#endregion
