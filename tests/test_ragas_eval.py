#region Imports & Fixtures
import os
import sys
import json
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from eval.ragas_evaluator import RagasEvalSample, RagasEvalResult
from eval.scripts.dataset_generator import generate_eval_dataset_from_chunks
#endregion

#region Unit Tests for RAGAS Data Models
def test_ragas_eval_sample_and_result_formatting():
    """Validates RagasEvalSample instantiation and Markdown report rendering."""
    sample = RagasEvalSample(
        question="What is Kanzi?",
        answer="Kanzi is a UI creation tool.",
        contexts=["Kanzi is a 3D UI framework for automotive engine."],
        ground_truth="Kanzi is a UI software."
    )
    assert sample.question == "What is Kanzi?"
    assert len(sample.contexts) == 1

    scores = {
        "faithfulness": 0.95,
        "answer_relevancy": 0.88,
        "context_precision": 0.90,
        "context_recall": 0.85
    }
    result = RagasEvalResult(scores=scores, detailed_df=None)
    md = result.to_markdown()
    
    assert "RAGAS Evaluation Summary" in md
    assert "**faithfulness**" in md
    assert "`0.9500`" in md
#endregion

#region Integration Test for Dataset Generator
def test_dataset_generator_output(tmp_path: Path):
    """Tests synthetic evaluation dataset generation from mock chunk structure."""
    mock_chunks = {
        "chunks": [
            {
                "id": "chunk-1",
                "content": "Kanzi Studio enables high performance graphics.",
                "metadata": {
                    "questions": ["How does Kanzi Studio perform?"],
                    "parent_content": "Kanzi Studio enables high performance 3D graphics rendering.",
                    "page_title": "Performance Guide"
                }
            }
        ]
    }
    
    input_file = tmp_path / "mock_chunks.json"
    output_file = tmp_path / "eval_dataset.json"

    with open(input_file, "w", encoding="utf-8") as f:
        json.dump(mock_chunks, f)

    generated = generate_eval_dataset_from_chunks(input_file, output_file, max_samples=5)
    
    assert len(generated) == 1
    assert generated[0]["question"] == "How does Kanzi Studio perform?"
    assert output_file.exists()
#endregion
