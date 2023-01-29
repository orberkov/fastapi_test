import pytest
from unittest import mock

import pytest_asyncio
from httpx import AsyncClient

from src.api_services.cache_service import CacheService
from src.config_source import ConfigSource
from src.main import app


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_index(client):
    print(client)
    print(type(client))
    config_source_mock = mock.Mock(spec=ConfigSource)
    config_source_mock.get.return_value = [
            {
                "name": "ip-api",
                "protocol": "http",
                "host": "ip-api.com",
                "path": "/json/<ip_address>"
            }
        ]

    cache_service_mock = mock.Mock(spec=CacheService)
    cache_service_mock.get.return_value = None

    with app.container.config_source.override(config_source_mock):
        with app.container.cache_service.override(cache_service_mock):
            response = await client.get("/24.148.0.123")

    assert response.status_code == 200
    data = response.json()
    print('Getting the data and analysing. TBD: replace http services with Mocks')
    print(data)
    assert data["metrics"] is not None
    assert data["raw_data"] is not None


