resource "kubernetes_service" "qdrant_service" {
  metadata {
    name      = "qdrant-service"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "qdrant"
    }
  }

  spec {
    cluster_ip = "None"
    selector = {
      app = "qdrant"
    }

    port {
      name        = "http"
      port        = 6333
      target_port = 6333
    }

    port {
      name        = "grpc"
      port        = 6334
      target_port = 6334
    }
  }
}

resource "kubernetes_stateful_set" "qdrant" {
  wait_for_rollout = true

  metadata {
    name = "qdrant"

    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "qdrant"
    }
  }

  spec {
    service_name = kubernetes_service.qdrant_service.metadata[0].name
    replicas     = 1

    selector {
      match_labels = {
        app = "qdrant"
      }
    }

    template {
      metadata {
        labels = {
          app = "qdrant"
        }
      }

      spec {
        container {
          name              = "qdrant"
          image             = "qdrant/qdrant:latest"
          image_pull_policy = "IfNotPresent"

          port {
            name           = "http"
            container_port = 6333
          }

          port {
            name           = "grpc"
            container_port = 6334
          }

          volume_mount {
            name       = "qdrant-storage"
            mount_path = "/qdrant/storage"
          }

          resources {
            requests = {
              memory = "256Mi"
              cpu    = "100m"
            }
            limits = {
              memory = "512Mi"
              cpu    = "500m"
            }
          }
        }
      }
    }

    volume_claim_template {
      metadata {
        name = "qdrant-storage"
      }

      spec {
        access_modes = ["ReadWriteOnce"]

        resources {
          requests = {
            storage = "5Gi"
          }
        }
      }
    }
  }
}
