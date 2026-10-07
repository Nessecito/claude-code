#!/usr/bin/env python3
"""
MCP Server Example: Reports
===========================
A minimal MCP server exposing a single tool that Claude Code can call.

Read more about MCP here: https://docs.anthropic.com/en/docs/claude-code/mcp

Install the SDK, then register the server with Claude Code:

    pip install mcp
    claude mcp add reports -- python3 /path/to/claude-code/examples/mcp/reports_server.py

Make sure to change the path to your actual script.

Requires mcp 2.x. In 1.x this class was named FastMCP and lived in
mcp.server.fastmcp; see https://py.sdk.modelcontextprotocol.io/v2/migration/
"""

import logging

from mcp.server import MCPServer

logger = logging.getLogger(__name__)

mcp = MCPServer("reports")


@mcp.tool()
async def fetch_report(report_id: str) -> str:
    """Fetch a report by id."""
    logger.info("Fetching report %s", report_id)
    return f"Report {report_id} is ready."


if __name__ == "__main__":
    # run() defaults to the stdio transport, which is what `claude mcp add` expects.
    mcp.run()
