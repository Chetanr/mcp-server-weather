import asyncio

from mcp_server_weather import server


def test_get_current_weather_returns_data(monkeypatch):
    expected = {"current": {"temperature_2m": 18.5}}
    requested_urls = []

    async def mock_request(url):
        requested_urls.append(url)
        return expected

    monkeypatch.setattr(server, "make_openmeteo_request", mock_request)

    result = asyncio.run(server.get_current_weather(51.5, -0.1))

    assert result == expected
    assert "latitude=51.5" in requested_urls[0]
    assert "longitude=-0.1" in requested_urls[0]


def test_get_current_weather_reports_unavailable_data(monkeypatch):
    async def mock_request(url):
        return None

    monkeypatch.setattr(server, "make_openmeteo_request", mock_request)

    result = asyncio.run(server.get_current_weather(51.5, -0.1))

    assert result == "Unable to fetch the current weather data"
