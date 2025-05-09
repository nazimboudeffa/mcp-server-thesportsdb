# MCP Server for The Sports DB

An MCP Server for The Sports DB

## Installation

Clone locally and cd the folder

`uv run mcp install server.py`

## Claude

Edit the config file

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
        "C:\\Users\\YOUR_USERNAME\\Documents\\GitHub\\thesportsdb-mcp-server\\server.py"
      ]
    }
  }
}
```