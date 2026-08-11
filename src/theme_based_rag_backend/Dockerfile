# ==============================================================================
# Core RAG Backend Engine Service Dockerfile
# ==============================================================================
FROM python:3.12-slim

#region UV CLI Setup
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#endregion

WORKDIR /app

#region Build Tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ python3-dev \
    && rm -rf /var/lib/apt/lists/*
#endregion

#region User Security
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash appuser
#endregion

#region Install Backend Dependencies
ENV UV_PROJECT_ENVIRONMENT=/usr/local
COPY --chown=appuser:appgroup src/theme_based_rag_backend/pyproject.toml src/theme_based_rag_backend/uv.lock /app/src/theme_based_rag_backend/
RUN cd /app/src/theme_based_rag_backend && uv sync --frozen --no-install-project
#endregion

#region Application Setup
COPY --chown=appuser:appgroup src/theme_based_rag_backend/ /app/src/theme_based_rag_backend/
COPY --chown=appuser:appgroup langgraph.json /app/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000 2024
#endregion

USER appuser

CMD ["python", "-m", "src.theme_based_rag_backend.main"]
