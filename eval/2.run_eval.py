#region Imports & Setup
import argparse
import json
import os
import warnings
from pathlib import Path
import httpx
import pandas as pd
from datasets import Dataset
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas import evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import answer_relevancy, context_precision, context_recall, faithfulness
from ragas.run_config import RunConfig

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
#endregion

#region Model Init
def get_eval_models(temperature: float = 0.0):
    """Initializes LLM and Embeddings configured for OpenRouter evaluation."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("[EvalRunner-init] OPENROUTER_API_KEY is not set in environment.")

    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    model = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-chat")
    embed_model = os.getenv("OPENROUTER_EMBED_MODEL", "text-embedding-3-small")
    provider = os.getenv("OPENROUTER_PROVIDER")
    extra_body = {"provider": {"order": [provider], "allow_fallbacks": False}} if provider else None

    llm = ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=temperature, extra_body=extra_body)
    embeddings = OpenAIEmbeddings(model=embed_model, api_key=api_key, base_url=base_url, check_embedding_ctx_length=False, model_kwargs={"encoding_format": "float"})
    return LangchainLLMWrapper(llm), LangchainEmbeddingsWrapper(embeddings)
#endregion

#region RAG Fetcher
def fetch_rag_responses(dataset_path: Path, endpoint_url: str, limit: int = 0) -> list[dict]:
    """Queries the running RAG endpoint for each test question in the dataset."""
    if not dataset_path.exists():
        raise FileNotFoundError(f"[EvalRunner-fetch] Dataset file not found: {dataset_path}")

    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
    dataset = dataset[:limit] if limit > 0 else dataset
    print(f"[EvalRunner-fetch] Querying RAG endpoint ({endpoint_url}) for {len(dataset)} questions...")

    samples = []
    with httpx.Client(timeout=90.0) as client:
        for idx, item in enumerate(dataset, 1):
            q = item.get("question", "").strip()
            if not q:
                continue

            print(f"[EvalRunner-fetch] [{idx}/{len(dataset)}] Query: '{q[:60]}...'")
            try:
                resp = client.post(endpoint_url, json={"query": q, "history": []})
                resp.raise_for_status()
                data = resp.json()
                answer = data.get("final_response") or data.get("response") or ""
                raw_ctx = data.get("retrieved_documents") or data.get("contexts") or []
                contexts = [str(c) for c in raw_ctx] if isinstance(raw_ctx, list) else [str(raw_ctx)]
            except Exception as err:
                print(f"[EvalRunner-fetch] Error querying '{q[:40]}': {err}")
                answer, contexts = "Error querying RAG endpoint.", ["Error"]

            samples.append({
                "question": q,
                "answer": answer,
                "contexts": contexts,
                "ground_truth": item.get("ground_truth", ""),
                "reference_contexts": item.get("ground_truth_contexts", []),
            })

    return samples
#endregion

#region Metric Evaluation
def run_ragas_evaluation(samples: list[dict], output_dir: Path):
    """Executes RAGAS evaluation on collected samples and exports CSV & Markdown reports."""
    if not samples:
        raise ValueError("[EvalRunner-eval] No samples to evaluate.")

    eval_llm, eval_embeddings = get_eval_models()
    eval_dataset = Dataset.from_dict({
        "question": [s["question"] for s in samples],
        "answer": [s["answer"] for s in samples],
        "contexts": [s["contexts"] for s in samples],
        "ground_truth": [s["ground_truth"] for s in samples],
        "reference_contexts": [s["reference_contexts"] for s in samples],
    })

    metrics = [faithfulness, answer_relevancy, context_precision, context_recall]
    print(f"[EvalRunner-eval] Evaluating {len(samples)} samples with RAGAS metrics...")
    result = evaluate(
        dataset=eval_dataset,
        metrics=metrics,
        llm=eval_llm,
        embeddings=eval_embeddings,
        run_config=RunConfig(max_workers=2, max_retries=5, timeout=120),
    )

    df: pd.DataFrame = result.to_pandas()
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "2.run_eval.csv"
    report_path = output_dir / "2.run_eval.md"

    df.to_csv(csv_path, index=False)
    summary_rows = [f"| **{m.name}** | `{df[m.name].mean():.4f}` |" for m in metrics if m.name in df.columns]
    report_content = (
        "# 📊 RAGAS Pipeline Evaluation Report (2.run_eval)\n\n"
        "| Metric | Average Score |\n"
        "| :--- | :--- |\n"
        + "\n".join(summary_rows)
        + "\n\n## Detailed Sample Results\n\n"
        + df.to_markdown(index=False)
    )

    report_path.write_text(report_content, encoding="utf-8")
    print(f"[EvalRunner-save] Report saved to: {report_path}")
    print(f"[EvalRunner-save] CSV saved to: {csv_path}\n\n{report_content}\n")
#endregion

#region CLI Interface
def main():
    default_dataset = Path(__file__).resolve().parent / "1.eval_dataset.json"
    default_output = Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(description="Run RAGAS evaluation on RAG pipeline.")
    parser.add_argument("--dataset", "-d", type=str, default=str(default_dataset), help="Dataset JSON path")
    parser.add_argument("--output-dir", "-o", type=str, default=str(default_output), help="Output directory (default: eval folder)")
    parser.add_argument("--endpoint", "-e", type=str, default=os.getenv("RAG_ENDPOINT", "http://localhost:8000/query"), help="RAG API Endpoint")
    parser.add_argument("--limit", "-l", type=int, default=0, help="Limit sample count (0 for all)")
    parser.add_argument(
        "--enable",
        action="store_true",
        default=os.getenv("ENABLE_RAGAS_EVAL", "false").lower() in ("true", "1", "yes"),
        help="Safety switch to execute RAGAS API evaluation",
    )
    args = parser.parse_args()

    if not args.enable:
        print("[EvalRunner-skip] Evaluation skipped to prevent unintended API costs. Use --enable to run.")
        return

    samples = fetch_rag_responses(
        dataset_path=Path(args.dataset).resolve(),
        endpoint_url=args.endpoint,
        limit=args.limit,
    )
    run_ragas_evaluation(samples=samples, output_dir=Path(args.output_dir).resolve())

if __name__ == "__main__":
    main()
#endregion
