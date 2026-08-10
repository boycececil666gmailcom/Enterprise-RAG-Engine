resource "kubernetes_service" "gateway_service" {
  metadata {
    name      = "theme-based-rag-gateway-service"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "theme-based-rag-gateway"
    }
  }

  spec {
    type = "NodePort"

    selector = {
      app = "theme-based-rag-gateway"
    }

    port {
      name        = "http"
      port        = 8080
      target_port = 8080
      node_port   = 30080
    }
  }
}

resource "kubernetes_deployment" "gateway" {
  wait_for_rollout = true

  metadata {
    name = "theme-based-rag-gateway"

    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "theme-based-rag-gateway"
    }
  }

  spec {
    replicas = var.gateway_replicas

    selector {
      match_labels = {
        app = "theme-based-rag-gateway"
      }
    }

    template {
      metadata {
        labels = {
          app = "theme-based-rag-gateway"
        }
      }

      spec {
        container {
          name              = "theme-based-rag-gateway"
          image             = var.gateway_image
          image_pull_policy = "Always"

          port {
            name           = "http"
            container_port = 8080
          }

          env {
            name  = "RAG_BACKEND_URL"
            value = var.rag_backend_url
          }


          liveness_probe {
            http_get {
              path = "/health"
              port = 8080
            }
            initial_delay_seconds = 10
            period_seconds        = 10
          }

          readiness_probe {
            http_get {
              path = "/health"
              port = 8080
            }
            initial_delay_seconds = 5
            period_seconds        = 5
          }

          resources {
            requests = {
              memory = "128Mi"
              cpu    = "50m"
            }
            limits = {
              memory = "256Mi"
              cpu    = "200m"
            }
          }
        }
      }
    }
  }
}
