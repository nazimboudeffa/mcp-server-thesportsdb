from mcp.server.fastmcp import FastMCP
import httpx

# Create an MCP
mcp = FastMCP("thesportsdb")

# Define the API endpoint
# TheSportsDB API endpoint
API_END_POINT = "https://www.thesportsdb.com"

# Define an API call tool
@mcp.tool()
async def list_all_teams_in_a_league(sport, country):
    """
    List all teams in a league
    :param s: The name of the league
    :param c: The country of the league
    :return: A list of teams in the league
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"/api/v1/json/3/search_all_teams.php",
            params={
                "s": sport,
                "c": country,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response.raise_for_status()
        data = response.json()
        return [team["strTeam"] for team in data.get("teams", [])]