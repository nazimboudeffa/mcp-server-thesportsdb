[![smithery badge](https://smithery.ai/badge/@nazimboudeffa/mcp-server-thesportsdb)](https://smithery.ai/server/@nazimboudeffa/mcp-server-thesportsdb)

# MCP Server for The Sports DB

An MCP Server for The Sports DB

# Installing via Smithery

To install this MCP Server for Claude Desktop automatically via Smithery:

`npx -y @smithery/cli install @nazimboudeffa/mcp-server-thesportsdb --client claude`

# Manual installation

## Prerequisites

- Python 3.12+
- uv package manager
- MCP-compatible client (e.g., Claude for Desktop)
- Follow this tutorial https://github.com/modelcontextprotocol/python-sdk

## Installation

Install Python

`pip install uv`

`uv add "mcp[cli]"`

Clone locally and cd the folder

`uv run mcp install server.py`

## Check Claude

Verify the config file

```
{
  "mcpServers": {
    "thesportsdb": {
      "command": "C:\\Users\\YOU_USERNAME\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\uv.EXE",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\Users\\YOUR_USERNAME\\Documents\\GitHub\\mcp-server-thesportsdb\\server.py"
      ]
    }
  }
}
```
