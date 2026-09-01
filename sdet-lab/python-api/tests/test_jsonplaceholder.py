import httpx
import pytest

BASE = "https://jsonplaceholder.typicode.com"


@pytest.mark.smoke
def test_get_post_returns_expected_resource():
    response = httpx.get(f"{BASE}/posts/1", timeout=20.0)
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == 1
    assert payload["userId"] == 1
    assert payload["title"]


def test_list_posts_returns_a_collection():
    response = httpx.get(f"{BASE}/posts", timeout=20.0)
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_create_post_returns_created_payload():
    response = httpx.post(
        f"{BASE}/posts",
        json={"title": "sdet-lab", "body": "week-5", "userId": 1},
        timeout=20.0,
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == "sdet-lab"
    assert payload["id"] is not None
