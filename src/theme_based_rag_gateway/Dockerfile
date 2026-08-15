# ==============================================================================
# Lightweight Gateway Service Dockerfile
# ==============================================================================
FROM python:3.12-slim

#region UV CLI Setup
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
#endregion

WORKDIR /app

#region User Security
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g appgroup -m -s /bin/bash appuser
#endregion

#region Install Dependencies
ENV UV_PROJECT_ENVIRONMENT=/usr/local
COPY --chown=appuser:appgroup src/theme_based_rag_gateway/pyproject.toml src/theme_based_rag_gateway/uv.lock /app/src/theme_based_rag_gateway/
RUN cd /app/src/theme_based_rag_gateway && uv sync --frozen --no-install-project
#endregion

#region Application Setup
COPY --chown=appuser:appgroup src/theme_based_rag_gateway/ /app/src/theme_based_rag_gateway/
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
#endregion

USER appuser

CMD ["python", "-m", "src.theme_based_rag_gateway.main"]
