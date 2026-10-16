from typing import Any

import httpx
from mcp.server.mcpserver import MCPServer


mcp = MCPServer("weather")

OPENMETEO_API_BASE = "https://api.open-meteo.com/v1"
USER_AGENT = "weather-app/1.0"


async def make_openmeteo_request(url: str) -> dict[str, Any] | None:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_current_weather(latitude: float, longitude: float) -> dict[str, Any]:
    url = f"{OPENMETEO_API_BASE}/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto"
    data = await make_openmeteo_request(url)

    if not data:
        return {"error": "Unable to fetch the current weather data"}
    return data


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> dict[str, Any]:
    url = f"{OPENMETEO_API_BASE}/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation,weathercode&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode&timezone=auto"
    data = await make_openmeteo_request(url)

    if not data:
        return {"error": "Unable to fetch the current forecast data"}
    return data


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
