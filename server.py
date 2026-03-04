from fastmcp import FastMCP


mcp = FastMCP(
    name="Horoscope MCP Server",
    instructions="Provides horoscope tools for astrological signs.",
    version="1.0.0",
)


@mcp.tool
def get_horoscope(sign: str) -> str:
    """Get today's horoscope for an astrological sign."""
    return f"{sign}: Next Tuesday you will befriend a baby otter."


if __name__ == "__main__":
    mcp.run()
