#region Imports & Setup
import os
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.theme_based_rag_backend.agent_flow.graph import agent_graph
from src.theme_based_rag_backend.eval.ragas_evaluator import (
    evaluate_rag_pipeline,
    RagasEvalSample,
    RagasEvalResult
)

logger = logging.getLogger(__name__)
#endregion

#region Pipeline Execution Harness
def run_agent_evaluation(dataset_path: Path) -> List[RagasEvalSample]:
    """Runs agent_graph pipeline over all questions in dataset and collects RAGAS samples."""
    if not dataset_path.exists():
        raise FileNotFoundError(f"Evaluation dataset file not found: {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        raw_dataset = json.load(f)

    print(f"\n\033[1;96m========================================================\033[0m")
    print(f"\033[1;92m>>> [1/2] Executing Agent Graph Pipeline over {len(raw_dataset)} Questions\033[0m")
    print(f"\033[1;96m========================================================\033[0m\n")

    samples: List[RagasEvalSample] = []

    for idx, item in enumerate(raw_dataset, start=1):
        question = item.get("question")
        ground_truth = item.get("ground_truth")

        if not question:
            continue

        print(f"[{idx}/{len(raw_dataset)}] Processing Query: '{question}'")

        # Invoke LangGraph RAG Agent Flow
        initial_state = {
            "message": question,
            "history": []
        }
        
        try:
            final_state = agent_graph.invoke(initial_state)
            answer = final_state.get("agent_response", "")
            
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
            logger.error(f"Error executing agent pipeline on question '{question}': {err}")
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

    args = parser.parse_args()
    dataset_path = Path(args.dataset).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    samples = run_agent_evaluation(dataset_path)
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
