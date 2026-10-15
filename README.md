# Weather MCP Server Powered by the Open-Meteo API

This MCP server interfaces with the [Open-Meteo API](https://open-meteo.com/en/docs) and offers tools to fetch current weather conditions and weather forecasts for any location worldwide.

## Installation

```bash
uv run
```

## Development

1. Start the virtual environment

   ```bash
   source .venv/bin/activate
   ```

   NOTE: To stop the virtual environment:

   ```bash
   deactivate
   ```

2. Run MCP server in dev mode with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

   ```bash
   mcp dev server.py
   ```

## Run MCP server in Claude Desktop

1. Open `claude_desktop_config.js` in an editor:

   File location:
   - MacOS / Linux `~/Library/Application/Support/Claude/claude_desktop_config.json`
   - Windows `AppData\Claude\claude_desktop_config.json`

2. Find the full path to `uv`:
   - MacOS / Linux:

   ```bash
   which uv
   ```

   - Windows:

   ```bash
   where uv
   ```

3. In `claude_desktop_config.js`

   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "/absolute/path/to/uv",
         "args": [
           "run",
           "--with",
           "mcp[cli]",
           "mcp",
           "run",
           "/absolute/path/to/open-meteo-weather/server.py"
         ]
       }
     }
   }
   ```

4. Reboot Claude Desktop and use a prompt that will trigger your MCP.

## Usage

In Claude Desktop:

- request current weather information for a specified location
- request a weather forecast for a specified location and time
- ask if it's going to rain tomorrow
- ask if you need to put on sunscreen if you're going for a walk later

## Run MCP server in other AI agents

To run the MCP in any AI agent, refer to the official documentations.
