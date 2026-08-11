# ==============================================================================
# Lightweight Dockerfile for Theme-Based RAG Workflow Gateway
# ==============================================================================
FROM python:3.12-slim

WORKDIR /app

# Install only minimal packages required for gateway execution
# This avoids compiling native C modules like flashrank on the gateway container
COPY src/theme_based_rag_gateway/requirements.txt /app/src/theme_based_rag_gateway/requirements.txt
RUN pip install --no-cache-dir -r /app/src/theme_based_rag_gateway/requirements.txt

# Create a non-root user for production security compliance
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash appuser

# Copy application files (specifically including core config & models)
COPY --chown=appuser:appgroup src/theme_based_rag_gateway/ /app/src/theme_based_rag_gateway/

ENV PYTHONUNBUFFERED=1
ENV PATH=/home/appuser/.local/bin:$PATH

# Expose API Gateway port
EXPOSE 8080

# Switch to non-root user
USER appuser

# Run API Gateway using python module entry point (reads GATEWAY_HOST & GATEWAY_PORT dynamically)
CMD ["python", "-m", "src.theme_based_rag_gateway.main"]
