#!/usr/bin/env bash
# ==============================================================================
# Vector Database JSON Chunks Ingestion Script
# ==============================================================================

set -e

SCRIPT_NAME="$(basename "$0")"

echo -e "\n\033[1;96m========================================================\033[0m"
echo -e "\033[1;92m>>> [1/2] [${SCRIPT_NAME}] Checking Environment & Python Executable\033[0m"
echo -e "\033[1;96m========================================================\033[0m\n"

INPUT_FILE="${1:-preprocessing-pipeline/rag_chunks.json}"
ENDPOINT_URL="${2:-${INGEST_ENDPOINT:-http://localhost:8080/ingest/vector}}"
BATCH_SIZE="${3:-50}"

if [ -f "./venv/Scripts/python.exe" ]; then
    PYTHON_EXEC="./venv/Scripts/python.exe"
elif [ -f "./venv/bin/python" ]; then
    PYTHON_EXEC="./venv/bin/python"
else
    PYTHON_EXEC="python"
fi

echo "Input dataset: ${INPUT_FILE}"
echo "Target endpoint: ${ENDPOINT_URL}"
echo "Batch size: ${BATCH_SIZE}"

echo -e "\n\033[1;96m========================================================\033[0m"
echo -e "\033[1;92m>>> [2/2] [${SCRIPT_NAME}] Triggering Ingestion Process\033[0m"
echo -e "\033[1;96m========================================================\033[0m\n"

"${PYTHON_EXEC}" -m src.theme_based_rag_backend.script.ingest_json_to_vdb \
    --input "${INPUT_FILE}" \
    --endpoint "${ENDPOINT_URL}" \
    --batch-size "${BATCH_SIZE}"

echo -e "\033[1;92m✔ Vector DB Ingestion task finished successfully.\033[0m\n"
