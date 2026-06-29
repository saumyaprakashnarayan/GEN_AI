from langchain_mcp_adapters import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mcpmathserver.py"], #ensure correct absolute path
                "transport":"stdio"
            },

            "weather":{
                "url":"https://localhost:8000/mcp", #make sure the server is running here
                "transport":"streamable_http"
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools= await client.get_tools()
    model=ChatGroq(model="groq:llama-3.3-70b-versatile")
    agent=create_react_agent(model,tools)


    math_response=await agent.ainvoke({"message":[{"role":"user","content":"whats 2+3 then multiply it with 4"}]})
    weather_response=await agent.ainvoke({"message":[{"role":"user","content":"weather of california"}]})

    print("math_response:",math_response['message'][-1].content)
    print("weather_response:",weather_response['message'][-1].content)



asyncio.run(main())