FROM python:3.12-slim AS base
WORKDIR /app
COPY pyproject.toml .
COPY src/ src/
RUN pip install --no-cache-dir -e ".[ast,dev]"

FROM base AS test
COPY tests/ tests/
COPY fixtures/ fixtures/
CMD ["pytest", "--cov=wiki_mos_audit", "--cov-report=term-missing", "-v"]
