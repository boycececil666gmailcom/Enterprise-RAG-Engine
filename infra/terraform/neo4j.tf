resource "kubernetes_service" "neo4j_service" {
  metadata {
    name      = "neo4j-service"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "neo4j"
    }
  }

  spec {
    cluster_ip = "None"
    selector = {
      app = "neo4j"
    }

    port {
      name        = "http"
      port        = 7474
      target_port = 7474
    }

    port {
      name        = "bolt"
      port        = 7687
      target_port = 7687
    }
  }
}

resource "kubernetes_stateful_set" "neo4j" {
  wait_for_rollout = true

  metadata {
    name      = "neo4j"
    namespace = kubernetes_namespace.rag_namespace.metadata[0].name
    labels = {
      app = "neo4j"
    }
  }

  spec {
    service_name = kubernetes_service.neo4j_service.metadata[0].name
    replicas     = 1

    selector {
      match_labels = {
        app = "neo4j"
      }
    }

    template {
      metadata {
        labels = {
          app = "neo4j"
        }
      }

      spec {
        container {
          name              = "neo4j"
          image             = "neo4j:latest"
          image_pull_policy = "IfNotPresent"

          port {
            name           = "http"
            container_port = 7474
          }

          port {
            name           = "bolt"
            container_port = 7687
          }

          env {
            name = "NEO4J_AUTH"
            value_from {
              secret_key_ref {
                name = kubernetes_secret.neo4j_secrets.metadata[0].name
                key  = "neo4j-auth"
              }
            }
          }

          volume_mount {
            name       = "neo4j-data"
            mount_path = "/data"
          }

          resources {
            requests = {
              memory = "512Mi"
              cpu    = "200m"
            }
            limits = {
              memory = "1Gi"
              cpu    = "1000m"
            }
          }
        }
      }
    }

    volume_claim_template {
      metadata {
        name = "neo4j-data"
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
