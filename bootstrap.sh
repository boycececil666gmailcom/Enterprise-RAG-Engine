#!/bin/bash

# Define log_step function for beautiful ANSI output
log_step() {
    echo -e "\n\033[1;96m========================================================\033[0m"
    echo -e "\033[1;92m>>> $1 [$(basename "$0")] $2\033[0m"
    echo -e "\033[1;96m========================================================\033[0m\n"
}

# Step 1: Initialize local python environment
log_step "[1/4]" "Setting Up Python Virtual Environment & Dependencies"
source ./setup_env.sh

# Step 2: Build Docker images locally
log_step "[2/4]" "Building Local Docker Images"
docker info >/dev/null 2>&1 || { echo -e "\033[1;31mError: Docker daemon is not running. Please start Docker and try again.\033[0m"; exit 1; }

echo "Building core chatbot backend image..."
docker build -t theme-based-rag-backend:latest -f src/theme_based_rag_backend/Dockerfile . || exit 1

echo "Building API gateway image..."
docker build -t theme-based-rag-gateway:latest -f src/theme_based_rag_gateway/Dockerfile . || exit 1

# Step 3: Deploy Infrastructure via Terraform
log_step "[3/4]" "Deploying Kubernetes Infrastructure via Terraform"
./deploy_terraform.sh || exit 1

