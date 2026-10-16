import asyncio

from mcp_server_weather import server


def test_get_current_weather_returns_data(monkeypatch):
    expected = {"current": {"temperature_2m": 18.5}}
    requested_urls = []

    async def mock_request(url):
        requested_urls.append(url)
        return expected

    monkeypatch.setattr(server, "make_openmeteo_request", mock_request)

    result = asyncio.run(
        server.mcp.call_tool(
            "get_current_weather",
            {"latitude": 51.5, "longitude": -0.1},
        )
    )

    assert not result.is_error
    assert result.structured_content == expected
    assert "latitude=51.5" in requested_urls[0]
    assert "longitude=-0.1" in requested_urls[0]


def test_get_current_weather_reports_unavailable_data(monkeypatch):
    async def mock_request(url):
        return None

    monkeypatch.setattr(server, "make_openmeteo_request", mock_request)

    result = asyncio.run(
        server.mcp.call_tool(
            "get_current_weather",
            {"latitude": 51.5, "longitude": -0.1},
        )
    )

    assert not result.is_error
    assert result.structured_content == {
        "error": "Unable to fetch the current weather data"
    }


def test_get_forecast_returns_structured_data(monkeypatch):
    expected = {"hourly": {"temperature_2m": [18.5]}}
    requested_urls = []

    async def mock_request(url):
        requested_urls.append(url)
        return expected

    monkeypatch.setattr(server, "make_openmeteo_request", mock_request)

    result = asyncio.run(
        server.mcp.call_tool(
            "get_forecast",
            {"latitude": 51.5, "longitude": -0.1},
        )
    )

    assert not result.is_error
    assert result.structured_content == expected
    assert "longitude=-0.1" in requested_urls[0]
