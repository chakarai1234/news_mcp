# Singapore News MCP Server

A server that provides real-time news feeds from major Singapore news sources.

## Features

- Real-time news updates via Server-Sent Events (SSE)
- Supports multiple Singapore news sources:
  - The Straits Times
  - Business Times
  - Channel News Asia (CNA)

## Prerequisites

- Python >=3.12
- [uv](https://github.com/astral/uv) package manager

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd news_mcp

# Install dependencies using uv
uv sync
```

## Usage

### Running with Python

```bash
# Start the MCP server
uv run news_mcp

# Individual news retrievers
uv run straits     # Straits Times
uv run business    # Business Times
uv run cna         # Channel News Asia
```

### Running with Docker

```bash
# Build and run using docker-compose
docker compose up --build
```

or

```bash
# You can run using the run.sh file
# This command is only for MacOS or Linux
# For MacOs required Docker Desktop

# Give permissions for run.sh in unix
chmod +x ./run.sh # (sudo chmod) if super user required
```

## Configuration

1. Create a `.env` file with required environment variables:

```
MCP_PORT=8000
```

2. For Claude Desktop integration, use the provided `claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"news_streamable": {
			"command": "/opt/homebrew/bin/uv",
			"args": [
				"tool",
				"run",
				"mcp-proxy",
				"--transport",
				"streamablehttp",
				"http://127.0.0.1:8080/mcp"
			]
		}
	}
}
```

## Dependencies

- bs4 - Web scraping
- dateparser - Date parsing
- httpx - HTTP client
- mcp-proxy - MCP proxy support
- python-dotenv - Environment variable management

## License

MIT

