"""Test the webapp using pytest"""
import pytest
from httpx import AsyncClient
from webapp import main


@pytest.mark.anyio
async def test_root():
    """Test root /"""
    async with AsyncClient(app=main.app, base_url="http://test/api") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

    # Root should accept only GET requests
    async with AsyncClient(app=main.app, base_url="http://test/api") as ac:
        response = await ac.post("/")
    assert response.status_code == 405

@pytest.mark.anyio
async def test_items():
    """Test /items"""
    async with AsyncClient(app=main.app, base_url="http://test/api") as ac:
        response_get = await ac.get("/items/5?q=somestring")
        response_post = await ac.post("/items/5?q=somestring")
    assert response_get.status_code == 200
    assert response_get.json() == {'item_id': 5, 'q': 'somestring'}
    assert response_post.status_code == 405
