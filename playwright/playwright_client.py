import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "playwright": {
                "url": "http://localhost:8931/mcp/",
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatOllama(model="llama3.2")
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages": [
            {"role": "user", "content": "open google.com and search for langchain mcp"}]}
    )

    print("Playwright Response:", math_response['messages'][-1].content)

asyncio.run(main())
