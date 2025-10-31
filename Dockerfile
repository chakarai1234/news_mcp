FROM alpine:latest

RUN apk add --no-cache curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    rm -rf /var/cache/apk/*

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock* .python-version ./

RUN uv sync --no-cache --no-dev

COPY . .

CMD [ "uv", "run", "news_mcp" ]