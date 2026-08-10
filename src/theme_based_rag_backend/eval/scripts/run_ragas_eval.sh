#!/usr/bin/env bash
# ==============================================================================
# RAGAS Evaluation Automation Script (Consolidated in eval/)
# ==============================================================================

set -e

SCRIPT_NAME="$(basename "$0")"

echo -e "\n\033[1;96m========================================================\033[0m"
echo -e "\033[1;92m>>> [1/3] [${SCRIPT_NAME}] Initializing RAGAS Evaluation Environment\033[0m"
echo -e "\033[1;96m========================================================\033[0m\n"

INPUT_CHUNKS="${1:-preprocessing-pipeline/rag_chunks.json}"
EVAL_DATASET="${2:-src/theme_based_rag_backend/eval/eval_dataset.json}"
OUTPUT_DIR="${3:-progress-doc}"
MAX_SAMPLES="${4:-10}"

if [ -f "./venv/Scripts/python.exe" ]; then
    PYTHON_EXEC="./venv/Scripts/python.exe"
elif [ -f "./venv/bin/python" ]; then
    PYTHON_EXEC="./venv/bin/python"
else
    PYTHON_EXEC="python"
fi

echo "Using Python executable: ${PYTHON_EXEC}"

echo -e "\n\033[1;96m========================================================\033[0m"
echo -e "\033[1;92m>>> [2/3] [${SCRIPT_NAME}] Generating Evaluation Dataset from Chunks\033[0m"
echo -e "\033[1;96m========================================================\033[0m\n"

"${PYTHON_EXEC}" -m src.theme_based_rag_backend.eval.dataset_generator \
    --input "${INPUT_CHUNKS}" \
    --output "${EVAL_DATASET}" \
    --max "${MAX_SAMPLES}"

echo -e "\n\033[1;96m========================================================\033[0m"
echo -e "\033[1;92m>>> [3/3] [${SCRIPT_NAME}] Running RAGAS Evaluation Harness\033[0m"
echo -e "\033[1;96m========================================================\033[0m\n"

"${PYTHON_EXEC}" -m src.theme_based_rag_backend.eval.run_ragas_eval \
    --dataset "${EVAL_DATASET}" \
    --output-dir "${OUTPUT_DIR}"

echo -e "\033[1;92m✔ RAGAS Evaluation complete. Reports generated in '${OUTPUT_DIR}' directory.\033[0m\n"
