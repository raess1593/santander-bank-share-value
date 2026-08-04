FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --frozen

FROM python:3.12-slim AS runner

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN useradd -m appuser

WORKDIR /app

COPY --chown=appuser:appuser --from=builder /app/.venv /app/.venv

COPY --chown=appuser:appuser src/ /app/src/

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "src/main.py"]