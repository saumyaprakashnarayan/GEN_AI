from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")
@mcp.tool()
async def weather(location:str)->str:
    """get the weather location"""
    return "its always raining"

if __name__ =="__main__":
    mcp.run(transport="streamable-http")