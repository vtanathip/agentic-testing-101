from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
import asyncio
from langchain_ollama import ChatOllama
from phoenix.otel import register

# Recommended: Enable automatic instrumentation
tracer_provider = register(
    project_name="my-llm-app",
    auto_instrument=True,  # Automatically instruments AI/ML libraries
    batch=True  # Recommended for production - exports spans in background
)


async def main():
    # Create configuration dictionary
    config = {
        "mcpServers": {
            "playwright": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"],
                "env": {
                    "DISPLAY": ":1"
                }
            }
        }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)
    model = ChatOllama(model="gpt-oss", temperature=0.1)
    # Create agent with the client
    agent = MCPAgent(llm=model, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        """ Navigate to https://practicetestautomation.com/practice-test-login/.
        Fill username 'student' and password 'Password123'.
        Click the 'Submit' button.
        Verify that the login is successful by checking for a confirmation message.""",
    )
    print(f"\nResult: {result}")

asyncio.run(main())
