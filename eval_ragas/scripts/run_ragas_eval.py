#region Imports & Setup
import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any
import httpx

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from eval_ragas.ragas_evaluator import (
    evaluate_rag_pipeline,
    RagasEvalSample,
    RagasEvalResult
)
#endregion

#region Pipeline Execution Harness
def run_agent_evaluation(
    dataset_path: Path,
    endpoint_url: str,
    limit: int = 0
) -> List[RagasEvalSample]:
    """
    Runs evaluation over all questions in dataset by querying the running HTTP API Endpoint.
    """
    if not dataset_path.exists():
        raise FileNotFoundError(f"Evaluation dataset file not found: {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        raw_dataset = json.load(f)

    if limit > 0:
        raw_dataset = raw_dataset[:limit]

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/2] Executing Evaluation Pipeline via HTTP Endpoint: {endpoint_url}\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    samples: List[RagasEvalSample] = []

    with httpx.Client(timeout=90.0) as http_client:
        for idx, item in enumerate(raw_dataset, start=1):
            question = item.get("question")
            ground_truth = item.get("ground_truth")

            if not question:
                continue

            print(f"[{idx}/{len(raw_dataset)}] Processing Query: '{question}'")

            try:
                resp = http_client.post(endpoint_url, json={"query": question, "history": []})
                if resp.status_code != 200:
                    raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
                
                data = resp.json()
                answer = data.get("final_response", "") or data.get("response", "")
                raw_contexts = data.get("retrieved_documents", "") or data.get("contexts", "")

                # Extract retrieved contexts
                if isinstance(raw_contexts, list):
                    contexts = [str(c) for c in raw_contexts]
                elif isinstance(raw_contexts, str):
                    contexts = [raw_contexts] if raw_contexts else ["No documents retrieved."]
                else:
                    contexts = ["No documents retrieved."]

                samples.append(RagasEvalSample(
                    question=question,
                    answer=answer,
                    contexts=contexts,
                    ground_truth=ground_truth,
                    metadata={"id": item.get("id", str(idx))}
                ))
            except Exception as err:
                print(f"Error executing pipeline on question '{question}': {err}")
                samples.append(RagasEvalSample(
                    question=question,
                    answer="Error executing RAG pipeline via HTTP API.",
                    contexts=["Error"],
                    ground_truth=ground_truth
                ))

    return samples
#endregion

#region CLI Entry Point & Report Output
def main():
    default_dataset = Path(__file__).resolve().parents[1] / "eval_dataset.json"
    default_output = Path(__file__).resolve().parents[1] / "output"
    
    parser = argparse.ArgumentParser(description="Run RAGAS evaluation on Enterprise RAG Backend Engine.")
    parser.add_argument(
        "--dataset", "-d",
        type=str,
        default=str(default_dataset),
        help=f"Path to evaluation dataset JSON file (default: {default_dataset})"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=str,
        default=str(default_output),
        help=f"Directory to save evaluation report and CSV (default: {default_output})"
    )
    parser.add_argument(
        "--endpoint", "-e",
        type=str,
        default=os.getenv("RAG_ENDPOINT", "http://localhost:8000/query"),
        help="HTTP API Endpoint URL for container/K8s evaluation (default: http://localhost:8000/query)"
    )
    parser.add_argument(
        "--enable",
        action="store_true",
        default=os.getenv("ENABLE_RAGAS_EVAL", "false").lower() in ("true", "1", "yes"),
        help="Safety switch to enable RAGAS evaluation execution (default: false)"
    )
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=0,
        help="Limit number of dataset samples to evaluate (0 for all, default: 0)"
    )

    args = parser.parse_args()
    if not args.enable:
        print("\n\033[1;93m[SKIP] RAGAS Evaluation is disabled by default to prevent API costs.\033[0m")
        print("\033[1;93mTo run evaluation, set environment variable 'ENABLE_RAGAS_EVAL=true' or pass '--enable'.\033[0m\n")
        return

    dataset_path = Path(args.dataset).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    samples = run_agent_evaluation(dataset_path, endpoint_url=args.endpoint, limit=args.limit)
    if not samples:
        print("No valid evaluation samples collected. Exiting.")
        return

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [2/2] Running RAGAS Metrics Evaluation Backend\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    eval_result: RagasEvalResult = evaluate_rag_pipeline(samples)

    # Output Markdown Summary Report
    markdown_report = eval_result.to_markdown()
    print("\n" + markdown_report + "\n")

    report_path = output_dir / "ragas_evaluation_report.md"
    csv_path = output_dir / "ragas_evaluation_results.csv"

    with open(report_path, "w", encoding="utf-8") as rf:
        rf.write(f"# RAGAS Pipeline Evaluation Report\n\n{markdown_report}\n\n## Detailed Sample Results\n\n```csv\n{eval_result.detailed_df.to_csv(index=False)}\n```\n")

    eval_result.detailed_df.to_csv(csv_path, index=False)

    print(f"✅ RAGAS Evaluation Completed!")
    print(f"📄 Markdown Report saved to: {report_path}")
    print(f"📊 Detailed CSV saved to: {csv_path}")

if __name__ == "__main__":
    main()
#endregion
