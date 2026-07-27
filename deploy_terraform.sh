#!/bin/bash

# Define log_step function for step output
log_step() {
    echo -e "\n\033[1;96m========================================================\033[0m"
    echo -e "\033[1;92m>>> $1 [$(basename "$0")] $2\033[0m"
    echo -e "\033[1;96m========================================================\033[0m\n"
}

# Step 1: Initialize Terraform
log_step "[1/4]" "Initializing Terraform Providers"
cd "$(dirname "$0")/infra/terraform" || exit 1

terraform init || exit 1

# Step 2: Validate Terraform Configuration
log_step "[2/4]" "Validating Terraform HCL Configuration"
terraform validate || exit 1

# Step 3: Plan Terraform Deployment (Clean legacy namespace if present)
log_step "[3/4]" "Preparing Infrastructure & Generating Deployment Plan"
terraform plan -out=tfplan || exit 1

# Step 4: Apply Terraform Infrastructure
log_step "[4/4]" "Applying Infrastructure to Kubernetes Cluster"
terraform apply -auto-approve tfplan || exit 1

echo -e "\n\033[1;92m>>> [$(basename "$0")] Terraform Infrastructure Provisioning Complete!\033[0m\n"
