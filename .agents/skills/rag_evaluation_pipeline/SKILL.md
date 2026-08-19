---
name: rag_evaluation_pipeline
description: Standard operating procedures and automated workflows for synthesizing test datasets, running dynamic RAGAS benchmarks, and auto-synchronizing evaluation metrics with EVALUATION_JOURNAL.md.
---

# Enterprise RAG Evaluation & Dynamic Journaling Pipeline

This skill defines standard operating procedures and workflows for generating synthetic test datasets, running RAGAS benchmarks against active RAG endpoints, and automatically synchronizing evaluation scores into [`eval/EVALUATION_JOURNAL.md`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/EVALUATION_JOURNAL.md).

---

## Pipeline Architecture

```
                      [eval/0.chunks.json]
                               │
                               ▼
             [eval/1.dataset_generator.py] (Ragas KnowledgeGraph)
                               │
                               ▼
                     [eval/1.eval_dataset.json]
                               │
                               ▼
                  [eval/2.run_eval.py] ◄──► [RAG Backend: /query]
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
   [eval/2.run_eval_TIMESTAMP.csv]   [eval/EVALUATION_JOURNAL.md]
     (Detailed sample metrics)       (Auto-appended summary row)
```

- **[`eval/llm_client.py`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/llm_client.py)**: Centralized OpenRouter evaluation client (`max_tokens=16384`, `reasoning: {"effort": "medium"}`).
- **[`eval/1.dataset_generator.py`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/1.dataset_generator.py)**: Synthesizes ground truth test sets using RAGAS KnowledgeGraph extractors.
- **[`eval/2.run_eval.py`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/2.run_eval.py)**: Queries `/query`, runs 4 RAGAS metrics, saves timestamped CSVs, and dynamically updates the summary table in [`eval/EVALUATION_JOURNAL.md`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/EVALUATION_JOURNAL.md).
- **[`eval/EVALUATION_JOURNAL.md`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/EVALUATION_JOURNAL.md)**: Persistent benchmark evolution journal and engineering notes.

---

## Standard Operating Procedures

### 1. Prerequisites Check

Verify that the RAG backend or gateway is up and healthy:

```powershell
# Verify backend service
curl.exe http://localhost:8000/health

# Or verify gateway service
curl.exe http://localhost:8080/health
```

### 2. Generate Synthetic Dataset (Optional)(Normally you don't need this as the test set is already well defined)

Synthesize a fresh test set from raw document chunks:

```powershell
.\.venv\Scripts\python.exe eval\1.dataset_generator.py --chunks eval\0.chunks.json --size 30
```

- **Output**: [`eval/1.eval_dataset.json`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/1.eval_dataset.json)

### 3. Execute Dynamic Evaluation & Journal Sync

Run end-to-end evaluation against the running backend:

```powershell
# Default evaluation (auto-updates eval/EVALUATION_JOURNAL.md upon completion)
.\.venv\Scripts\python.exe eval\2.run_eval.py

# Custom dataset or endpoint URL
.\.venv\Scripts\python.exe eval\2.run_eval.py --dataset eval\1.eval_dataset.json --endpoint http://localhost:8000/query
```

- **Outputs**:
  - `eval/2.run_eval_YYYYMMDD_HHMMSS.csv` (Full per-question breakdown)
  - [`eval/EVALUATION_JOURNAL.md`](file:///c:/Users/boyce/OneDrive/Desktop/Enterprise-RAG-Engine/eval/EVALUATION_JOURNAL.md) (Appended summary row)

### 4. Review Historical Benchmark Evolution

Inspect summary metrics across all historical runs:

```powershell
.\.venv\Scripts\python.exe -c "import glob, pandas as pd; [print(f, pd.read_csv(f, nrows=1)[['user_input','faithfulness','answer_relevancy','context_precision','context_recall']].to_dict(orient='records')) for f in sorted(glob.glob('eval/2.run_eval_*.csv'))]"
```

---

## Target Metrics Reference

| Metric | Target Goal | Focus Area | Optimization Strategy |
| :--- | :---: | :--- | :--- |
| **Faithfulness** | `>= 0.80` | Grounding / Non-hallucination | Node critique loop & strict prompt validation |
| **Answer Relevancy** | `>= 0.75` | Direct response completeness | Direct-first answer format & markdown formatting |
| **Context Precision** | `>= 0.85` | Signal-to-noise in retrieval | Qdrant hybrid retrieval + FlashRank reranker |
| **Context Recall** | `>= 0.80` | Ground truth coverage | Domain-injected HyDE expansion |
