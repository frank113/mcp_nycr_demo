from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.prompts import base
import httpx
from googlemaps import Client as gmapsclient
from dotenv import load_dotenv
import os

load_dotenv()

gmaps = gmapsclient(key=os.getenv("GOOGLE_MAPS_API_KEY"))

mcp = FastMCP("Tutorial")

def _get_lat_long_helper(place: str) -> dict:
	output = gmaps.geocode(place)
	out_dict = output[0]["navigation_points"][0]["location"]
	return out_dict

@mcp.tool(
	name="get_lat_long",
	title = "Determine Latitude and Longitude"
)
async def get_lat_long(place: str) -> dict:
	return _get_lat_long_helper(place)

async def get_nearby_pizza(place: str):
	location_lat_long: dict = _get_lat_long_helper(place)
	


if __name__ == "__main__":
	mcp.run()