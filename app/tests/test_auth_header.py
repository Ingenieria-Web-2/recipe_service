import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_recipe_requires_user_header():
    # No X-User-ID header -> dependency should raise 401
    r = client.post("/api/recipe/create", json={
        "name": "Test Recipe",
        "description": "Tasty",
        "difficulty": "beginner",
        "prep_time_minutes": 10
    })
    assert r.status_code == 401


def test_recipe_with_user_header():
    # Simulate gateway by adding X-User-ID
    headers = {"X-User-ID": "1"}
    r = client.post("/api/recipe/create", json={
        "name": "Test Recipe",
        "description": "Tasty",
        "difficulty": "beginner",
        "prep_time_minutes": 10
    }, headers=headers)
    assert r.status_code == 200
    body = r.json()
    assert body["name"] == "Test Recipe"
