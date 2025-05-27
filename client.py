import asyncio
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic
from mcp_use import MCPAgent, MCPClient
import json
import re

def get_mcp_config(file_path):
    load_dotenv()
    with open(file_path, 'r') as f:
        content = f.read()

    content = re.sub(r'\$\{([^}]+)\}', lambda m: os.getenv(m.group(1), m.group(0)), content)
    return json.loads(content)

async def main():
    # Load environment variables
    load_dotenv()

    print(os.getenv("GEN3_ACCESS_TOKEN"))

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(get_mcp_config(os.path.join("mcp_servers", "mds_mcp.json")))

    print(client.config)

    # Create LLM
    # llm = ChatOllama(model="qwen3:14b")
    llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Analyze a few studies and tell me what this data is all about, like what kind of research can be done on it?",
        max_steps=50
    )
    print(f"\nResult: {result}")
    for item in result:
        if item.get('type') == 'text' and 'text' in item:
            # Get the text content
            text_content = item['text']
            
            # Print with proper line breaks
            print(text_content)
            print()

if __name__ == "__main__":
    asyncio.run(main())