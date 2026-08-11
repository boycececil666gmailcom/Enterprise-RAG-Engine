#region Imports & Setup
import os
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any
import httpx

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.theme_based_rag_backend.eval.ragas_evaluator import (
    evaluate_rag_pipeline,
    RagasEvalSample,
    RagasEvalResult
)

logger = logging.getLogger(__name__)
#endregion

#region Pipeline Execution Harness
def run_agent_evaluation(
    dataset_path: Path,
    endpoint_url: str = None
) -> List[RagasEvalSample]:
    """
    Runs evaluation over all questions in dataset using either HTTP API Endpoint (K8s/Docker)
    or local direct agent_graph.invoke.
    """
    if not dataset_path.exists():
        raise FileNotFoundError(f"Evaluation dataset file not found: {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        raw_dataset = json.load(f)

    is_remote_http = bool(endpoint_url and endpoint_url.lower() != "local")
    mode_str = f"HTTP Endpoint ({endpoint_url})" if is_remote_http else "Local Direct agent_graph.invoke"

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/2] Executing Evaluation Pipeline over {len(raw_dataset)} Questions [{mode_str}]\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    samples: List[RagasEvalSample] = []

    agent_graph = None
    if not is_remote_http:
        from src.theme_based_rag_backend.agent_flow.graph import agent_graph as local_graph
        agent_graph = local_graph

    with httpx.Client(timeout=90.0) if is_remote_http else sys.modules[__name__] as http_client:
        for idx, item in enumerate(raw_dataset, start=1):
            question = item.get("question")
            ground_truth = item.get("ground_truth")

            if not question:
                continue

            print(f"[{idx}/{len(raw_dataset)}] Processing Query: '{question}'")

            try:
                if is_remote_http:
                    resp = http_client.post(endpoint_url, json={"query": question, "history": []})
                    if resp.status_code != 200:
                        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text}")
                    data = resp.json()
                    answer = data.get("final_response", "") or data.get("response", "")
                    raw_contexts = data.get("retrieved_documents", "") or data.get("contexts", "")
                else:
                    initial_state = {"query": question, "history": []}
                    final_state = agent_graph.invoke(initial_state)
                    answer = final_state.get("final_response", "")
                    raw_contexts = final_state.get("retrieved_documents", "")

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
                logger.error(f"Error executing pipeline on question '{question}': {err}")
                samples.append(RagasEvalSample(
                    question=question,
                    answer="Error executing RAG pipeline.",
                    contexts=["Error"],
                    ground_truth=ground_truth
                ))

    return samples
#endregion

#region CLI Entry Point & Report Output
def main():
    default_dataset = Path(__file__).resolve().parent / "eval_dataset.json"
    if not default_dataset.exists():
        default_dataset = Path(__file__).resolve().parents[1] / "eval_dataset.json"

    default_output = Path(__file__).resolve().parent / "output"
    if not default_output.exists():
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
        default=os.getenv("RAG_ENDPOINT", "local"),
        help="HTTP API Endpoint URL for container/K8s evaluation (e.g. http://localhost:8000/query or http://localhost:8080/query). Pass 'local' for in-memory direct invocation."
    )

    args = parser.parse_args()
    dataset_path = Path(args.dataset).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    samples = run_agent_evaluation(dataset_path, endpoint_url=args.endpoint)
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
