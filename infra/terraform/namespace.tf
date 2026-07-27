resource "kubernetes_namespace" "rag_namespace" {
  metadata {
    name = var.namespace
    labels = {
      name        = var.namespace
      environment = "production"
    }
  }
}
