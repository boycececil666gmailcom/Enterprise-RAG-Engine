variable "kubeconfig_path" {
  type        = string
  description = "Path to the kubeconfig file"
  default     = "~/.kube/config"
}

variable "kubeconfig_context" {
  type        = string
  description = "Kubernetes context to use"
  default     = ""
}

variable "namespace" {
  type        = string
  description = "Kubernetes namespace for Theme-Based RAG Workflow"
  default     = "theme-based-rag-workflow"
}

variable "gemini_api_key" {
  type        = string
  description = "Google Gemini API Key"
  sensitive   = true
  default     = "dummy_key_for_testing"
}

variable "langsmith_api_key" {
  type        = string
  description = "LangSmith API Key for tracing"
  sensitive   = true
  default     = ""
}


variable "langsmith_tracing" {
  type        = string
  description = "Enable LangSmith tracing"
  default     = "true"
}

variable "langsmith_project" {
  type        = string
  description = "LangSmith project name"
  default     = "pr-virtual-cork-53"
}


variable "gemini_model" {
  type        = string
  description = "Gemini LLM Model for routing and synthesis"
  default     = "gemini-3.1-flash-lite"
}

variable "gemini_embed_model" {
  type        = string
  description = "Gemini Embeddings Model"
  default     = "gemini-embedding-001"
}

variable "chatbot_theme" {
  type        = string
  description = "Theme boundary for chatbot routing & safeguards"
  default     = "Fintech SaaS platform"
}

variable "backend_replicas" {
  type        = number
  description = "Number of backend deployment replicas"
  default     = 2
}

variable "gateway_replicas" {
  type        = number
  description = "Number of gateway deployment replicas"
  default     = 2
}

variable "backend_image" {
  type        = string
  description = "Docker image for theme-based RAG backend"
  default     = "theme-based-rag-backend:latest"
}

variable "gateway_image" {
  type        = string
  description = "Docker image for theme-based RAG gateway"
  default     = "theme-based-rag-gateway:latest"
}
