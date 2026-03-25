"""
API tests for /add endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAddAPI:
    """API tests for /add endpoint."""

    def test_add_valid_numbers(self) -> None:
        """Test adding valid numbers via API."""
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_floats_via_api(self) -> None:
        """Test adding floats via API."""
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 8.7) < 0.01

    def test_add_negative_via_api(self) -> None:
        """Test adding negative numbers via API."""
        response = client.get("/add?num1=-5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_add_missing_parameter(self) -> None:
        """Test missing parameter returns error."""
        response = client.get("/add?num1=5")
        assert response.status_code == 422

    def test_add_invalid_parameter(self) -> None:
        """Test invalid parameter returns error."""
        response = client.get("/add?num1=abc&num2=3")
        assert response.status_code == 422
