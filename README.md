# Medical_calculator_MCP
MCP server for medical calculations

## If you haven't installed Calude Desktop, please install it first. 

## Installation
Adding MCP to your python project
We recommend using uv to manage your Python projects. In a uv managed python project, add mcp to dependencies by:
```
uv add "mcp[cli]"
```


Alternatively, for projects using pip for dependencies:
```
pip install mcp
```

Running the standalone MCP development tools

To run the mcp command with uv:
```
uv run mcp
```
## Running the server

You can install this server in Claude Desktop and interact with it right away by running:
```
mcp install server.py
```
Alternatively, you can test it with the MCP Inspector:
```
mcp dev server.py
```
