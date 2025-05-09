# MCP Server for The Sports DB
[![smithery badge](https://smithery.ai/badge/@nazimboudeffa/mcp-server-thesportsdb)](https://smithery.ai/server/@nazimboudeffa/mcp-server-thesportsdb)

An MCP Server for The Sports DB

# Quick Start

## 1 - Installation

### Installing via Smithery

To install mcp-server-thesportsdb for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@nazimboudeffa/mcp-server-thesportsdb):

```bash
npx -y @smithery/cli install @nazimboudeffa/mcp-server-thesportsdb --client claude
```

### Manual Installation
Clone locally and cd the folder

`uv run mcp install server.py`

## 2 - Check Claude

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
