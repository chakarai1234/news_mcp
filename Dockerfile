FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock* .python-version ./

RUN uv sync

COPY . .

CMD [ "uv", "run", "news_mcp" ]