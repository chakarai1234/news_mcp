#!/bin/bash

set -e

is_docker_running() {
    docker info >/dev/null 2>&1
}

if is_docker_running; then
    echo "✅ Docker Desktop is already running."
else
    echo "🚀 Starting Docker Desktop..."
    open -ga Docker

    echo "⏳ Waiting for Docker daemon to start..."
    while ! is_docker_running; do
        sleep 2
        echo "Still waiting..."
    done
    echo "✅ Docker daemon is now running."
fi

echo "📦 Rebuilding and starting containers..."
docker compose down -v
docker compose up --build -d

echo "✅ All containers are up and running."