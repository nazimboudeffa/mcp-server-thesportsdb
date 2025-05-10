# MCP Server for The Sports DB

An MCP Server for The Sports DB

# Prerequisites

- Python 3.12+
- uv package manager
- MCP-compatible client (e.g., Claude for Desktop)

# Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/nazimboudeffa/mcp-server-thesportsdb.git
   cd mcp-server-thesportsdb
   ```

2. Install dependencies
    ```bash
    pip install uv
    uv add "mcp[cli]"
    ```

# Usage

Run

`uv run mcp install server.py`

Then check the Claude for Desktop config file

```json
{
  "mcpServers": {
    "alphavantage": {
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