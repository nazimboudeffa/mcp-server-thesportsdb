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
    List all teams in a sport
    :param s: The name of the sport
    :param c: The country of the sport
    :return: A list of teams in the sport
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

# Define an API call tool
@mcp.tool()
async def lookup_table_by_league_id_and_season(league_id, season):
    """
    Get the classification of a league
    :param league_id: The id of the league
    :param season: The season of the league
    :return: A list of teams in the league
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"/api/v1/json/3/lookuptable.php",
            params={
                "l": league_id,
                "s": season,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        try:
            response.raise_for_status()
            if not response.text or not response.text.strip():
                return {"error": "Empty response from API"}
            data = response.json()
        except Exception as e:
            return {"error": f"Failed to parse API response: {str(e)}", "raw_response": response.text}
        standings = data.get("table", [])
        return [
            {
                "rank": team.get("intRank"),
                "team": team.get("strTeam"),
                "played": team.get("intPlayed"),
                "win": team.get("intWin"),
                "draw": team.get("intDraw"),
                "loss": team.get("intLoss"),
                "goals_for": team.get("intGoalsFor"),
                "goals_against": team.get("intGoalsAgainst"),
                "goal_difference": team.get("intGoalDifference"),
                "points": team.get("intPoints"),
            }
            for team in standings
        ]

# Define an API call tool
@mcp.tool()
async def search_for_event_by_event_name(event_name):
    """
    Search for an event by name
    :param event_name: The name of the event
    :return: A list of events
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"/api/v1/json/3/searchevents.php",
            params={
                "e": event_name,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response.raise_for_status()
        data = response.json()
        return [
            {
                "event_id": event["idEvent"],
                "event_name": event["strEvent"],
                "event_date": event["dateEvent"],
                "event_time": event["strTime"],
            }
            for event in data.get("event", [])
        ]
    
# Define an API call tool
@mcp.tool()
async def search_for_players_by_name(player_name):
    """
    Search for players by name
    :param player_name: The name of the player
    :return: A list of players
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_END_POINT+"/api/v1/json/3/searchplayers.php",
            params={
                "p": player_name,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response.raise_for_status()
        data = response.json()
        return [
            {
                "player_id": player["idPlayer"],
                "player_name": player["strPlayer"],
                "team_name": player["strTeam"],
            }
            for player in data.get("player", [])
        ]