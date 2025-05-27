# Gen3 MCP Client

A Python client application that leverages the Model Context Protocol (MCP) to interact with Gen3 data services. This client enables AI-powered analysis of research studies and data using either Anthropic's Claude or Ollama models.

## Features

- Connects to Gen3 data services through MCP
- Supports multiple LLM backends:
  - Anthropic Claude (claude-3-5-sonnet)
  - Ollama (qwen3:14b)
- Environment variable configuration
- Asynchronous operation
- Flexible MCP server configuration

## Prerequisites

- Python 3.12 or higher
- uv package manager
- Access to either Anthropic API or Ollama

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd gen3-mcp-client
```

2. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with your credentials:
```env
ANTHROPIC_API_KEY=your_api_key_here  # If using Claude
```

2. Configure MCP servers in `mcp_servers/mds_mcp.json`:
```json
{
    "mcpServers": {
        "gen3": {
            "command": "uv",
            "args": [
                "--directory",
                "/path/to/gen3-mcp-server",
                "run",
                "gen3.py"
            ]
        }
    }
}
```

## Usage

Run the client:

```bash
python client.py
```

The client will:
1. Connect to the configured Gen3 MCP server
2. Initialize the specified LLM (Claude or Ollama)
3. Process queries about research studies and data
4. Output analysis results

## Dependencies

- anthropic>=0.51.0
- langchain-anthropic>=0.3.13
- langchain-ollama>=0.3.3
- mcp>=1.8.0
- mcp-use>=1.2.13
- python-dotenv>=1.1.0

## Development

To switch between LLM backends, modify the LLM initialization in `client.py`:

For Claude:
```python
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
```

For Ollama:
```python
llm = ChatOllama(model="qwen3:14b")
```

## License

[Add your license information here]
