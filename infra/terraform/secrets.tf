resource "kubernetes_secret" "gemini_secrets" {
  metadata {
    name      = "gemini-secrets"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
  }

  type = "Opaque"

  data = {
    "gemini-api-key" = var.gemini_api_key
  }
}

resource "kubernetes_secret" "langchain_secrets" {
  metadata {
    name      = "langchain-secrets"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
  }

  type = "Opaque"

  data = {
    "langchain-api-key" = var.langsmith_api_key
  }

}
