"""
Basic tests for the Kids ABB API.
"""
import pytest
from fastapi.testclient import TestClient
from ..main import app


class TestKidsABB:
    """Test class for the Kids ABB API."""

    def setup_method(self):
        """Set up test client before each test."""
        self.client = TestClient(app)

    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_add_kid(self):
        """Test adding a new kid."""
        kid_data = {"name": "TestKid", "age": 10}
        response = self.client.post("/api/v1/kids/add", json=kid_data)
        assert response.status_code == 200
        assert "message" in response.json()
        assert response.json()["kid"]["name"] == "TestKid"
        assert response.json()["kid"]["age"] == 10

    def test_add_duplicate_kid(self):
        """Test adding a duplicate kid (should fail)."""
        kid_data = {"name": "TestKid2", "age": 12}

        # Add first time
        response1 = self.client.post("/api/v1/kids/add", json=kid_data)
        assert response1.status_code == 200

        # Try to add again (should fail due to hash collision)
        response2 = self.client.post("/api/v1/kids/add", json=kid_data)
        assert response2.status_code == 400

    def test_get_all_kids(self):
        """Test getting all kids."""
        response = self.client.get("/api/v1/kids/list")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_tree_stats(self):
        """Test getting tree statistics."""
        response = self.client.get("/api/v1/kids/stats")
        assert response.status_code == 200
        assert "total_kids" in response.json()
        assert "is_empty" in response.json()
