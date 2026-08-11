# ==============================================================================
# RAGAS Evaluation Harness Service Dockerfile
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

#region Install Evaluation Dependencies
ENV UV_PROJECT_ENVIRONMENT=/usr/local
COPY --chown=appuser:appgroup eval_ragas/pyproject.toml eval_ragas/uv.lock /app/eval_ragas/
RUN cd /app/eval_ragas && uv sync --frozen --no-install-project
#endregion

#region Application Setup
COPY --chown=appuser:appgroup eval_ragas/ /app/eval_ragas/
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
#endregion

USER appuser

CMD ["python", "-m", "eval_ragas.scripts.run_ragas_eval"]
