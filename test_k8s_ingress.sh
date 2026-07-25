#!/bin/bash

# Define log_step function for beautiful ANSI output
log_step() {
    echo -e "\n\033[1;96m========================================================\033[0m"
    echo -e "\033[1;92m>>> $1 [$(basename "$0")] $2\033[0m"
    echo -e "\033[1;96m========================================================\033[0m\n"
}

log_step "[1/1]" "Testing Directly via Kubernetes Ingress Endpoint"

# Resolve Ingress IP/Host or Minikube IP / Localhost
INGRESS_HOST=$(kubectl get ingress theme-based-rag-ingress -n theme-based-rag-workflow -o jsonpath='{.status.loadBalancer.ingress[0].ip}' 2>/dev/null)
if [ -z "$INGRESS_HOST" ]; then
    INGRESS_HOST=$(kubectl get ingress theme-based-rag-ingress -n theme-based-rag-workflow -o jsonpath='{.status.loadBalancer.ingress[0].hostname}' 2>/dev/null)
fi
if [ -z "$INGRESS_HOST" ] && command -v minikube >/dev/null 2>&1; then
    INGRESS_HOST=$(minikube ip 2>/dev/null)
fi
if [ -z "$INGRESS_HOST" ]; then
    INGRESS_URL="http://localhost"
else
    INGRESS_URL="http://${INGRESS_HOST}"
fi

echo -e "\033[1;92mIngress Endpoint Resolved: ${INGRESS_URL}\033[0m"
echo "Executing E2E integration tests directly against Ingress..."

# Use virtual environment python binary
if [ -f "./venv/Scripts/python.exe" ]; then
    PYTHON_BIN="./venv/Scripts/python.exe"
elif [ -f "./venv/bin/python" ]; then
    PYTHON_BIN="./venv/bin/python"
else
    PYTHON_BIN="python"
fi

K8S_GATEWAY_URL="${INGRESS_URL}" "$PYTHON_BIN" -m pytest tests/test_k8s_e2e.py -v -s

