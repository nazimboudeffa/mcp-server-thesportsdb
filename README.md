https://www.linkedin.com/posts/nazimboudeffa_mon-premier-mcp-sur-smitheryai-activity-7326760165775454209-wB_u?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAMEPAoBdueet-RrggQFNjvkUv0U_YAaniI

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

## Installation

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
