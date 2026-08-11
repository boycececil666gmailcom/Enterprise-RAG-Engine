# ==============================================================================
# Multi-stage Dockerfile for Theme-Based RAG Workflow Backend
# ==============================================================================

# --- Stage 1: Build dependencies ---
FROM python:3.12-slim AS builder

WORKDIR /app

# Install compilation tools required for flashrank
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY src/theme_based_rag_backend/requirements.txt /app/src/theme_based_rag_backend/requirements.txt

#region Install Backend Dependencies
RUN pip install --no-cache-dir --user -r /app/src/theme_based_rag_backend/requirements.txt
#endregion


# --- Stage 2: Production runner ---
FROM python:3.12-slim AS runner

WORKDIR /app

# Create a non-root user for security compliance in production Kubernetes
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash appuser

#region User Permissions and Environment Setup
# Copy installed Python packages from the builder stage
COPY --from=builder /root/.local /home/appuser/.local
RUN chown -R appuser:appgroup /home/appuser/.local && chmod -R +x /home/appuser/.local/bin/*
COPY --chown=appuser:appgroup src/theme_based_rag_backend/ /app/src/theme_based_rag_backend/
COPY --chown=appuser:appgroup langgraph.json pyproject.toml README.md /app/

# Update PATH variable to include user's local bin
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
#endregion

#region Exposed Container Ports
# Expose FastAPI default port (8000) and LangGraph Studio dev port (2024)
EXPOSE 8000 2024
#endregion

# Switch to non-root user
USER appuser

# Run Chatbot Backend using python module entry point (reads HOST & PORT dynamically)
CMD ["python", "-m", "src.theme_based_rag_backend.main"]
