import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools

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

    async with client.session("playwright") as session:
        tools = await load_mcp_tools(session)
        model = ChatOllama(model="llama3.2")
        agent = create_react_agent(
            model, tools
        )
        playwright_response = await agent.ainvoke(
            {"messages": [
                {"role": "user", "content": "open google chrome browser and search for langchain mcp"},
                {"role": "user", "content": "maximize the window of the browser"},]}
        )
        print("Playwright Response:",
              playwright_response['messages'][-1].content)

asyncio.run(main())
