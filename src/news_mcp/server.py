import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from news_mcp.news_retriever import cna, straits_times, business_times

load_dotenv()

HOST: str = os.environ["MCP_HOST"]
PORT: str = os.environ["MCP_PORT"]
LOG_LEVEL: str = os.getenv("LOG_LEVEL") or "INFO"


mcp: FastMCP = FastMCP(name="news_mcp", host=HOST, port=int(PORT), log_level=LOG_LEVEL)


mcp.add_tool(straits_times, title="Straits Times (ST)")
mcp.add_tool(cna, title="Channel News Asia (CNA)")
mcp.add_tool(business_times, title="Business Times SG")


def main() -> None:
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
