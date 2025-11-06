#! /bin/bash
docker compose down -v
docker compose up --build -d
docker logs -f news_mcp