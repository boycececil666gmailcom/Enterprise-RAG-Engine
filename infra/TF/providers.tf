terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.26.0"
    }
  }
}

provider "aws" {
  region                      = var.aws_region
  skip_credentials_validation = !var.use_aws_eks
  skip_requesting_account_id  = !var.use_aws_eks
  access_key                  = !var.use_aws_eks ? "mock_access_key" : null
  secret_key                  = !var.use_aws_eks ? "mock_secret_key" : null
}



# Dynamic lookup for AWS EKS cluster details when deploying to AWS
data "aws_eks_cluster" "cluster" {
  count = var.use_aws_eks ? 1 : 0
  name  = var.eks_cluster_name
}

data "aws_eks_cluster_auth" "cluster" {
  count = var.use_aws_eks ? 1 : 0
  name  = var.eks_cluster_name
}

provider "kubernetes" {
  host                   = var.use_aws_eks ? data.aws_eks_cluster.cluster[0].endpoint : null
  cluster_ca_certificate = var.use_aws_eks ? base64decode(data.aws_eks_cluster.cluster[0].certificate_authority[0].data) : null
  token                  = var.use_aws_eks ? data.aws_eks_cluster_auth.cluster[0].token : null

  config_path = var.use_aws_eks ? null : var.kubeconfig_path
}




