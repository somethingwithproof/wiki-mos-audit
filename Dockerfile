FROM python:3.12-slim AS base
WORKDIR /app
RUN pip install --no-cache-dir --only-binary :all: uv==0.10.6
ENV PATH="/app/.venv/bin:$PATH"
COPY pyproject.toml uv.lock ./
COPY src/ src/
RUN uv sync --frozen --no-cache --extra ast --extra dev \
    && useradd --create-home app \
    && chown -R app:app /app
USER app

FROM base AS test
COPY --chown=app:app tests/ tests/
COPY --chown=app:app fixtures/ fixtures/
CMD ["pytest", "--cov=wiki_mos_audit", "--cov-report=term-missing", "-v"]
