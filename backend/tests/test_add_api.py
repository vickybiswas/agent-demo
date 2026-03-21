"""API tests for /add endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAddAPI:
    """API tests for /add endpoint."""

    def test_add_endpoint_success(self) -> None:
        """Test /add endpoint with valid inputs."""
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_endpoint_decimals(self) -> None:
        """Test /add endpoint with decimals."""
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(8.7)

    def test_add_endpoint_negative(self) -> None:
        """Test /add endpoint with negative numbers."""
        response = client.get("/add?num1=-5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_add_endpoint_zero(self) -> None:
        """Test /add endpoint with zero."""
        response = client.get("/add?num1=0&num2=5")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_add_endpoint_missing_params(self) -> None:
        """Test /add endpoint with missing parameters."""
        response = client.get("/add")
        assert response.status_code == 422

    def test_add_endpoint_invalid_type(self) -> None:
        """Test /add endpoint with invalid input type."""
        response = client.get("/add?num1=abc&num2=3")
        assert response.status_code == 422

    def test_add_endpoint_large_numbers(self) -> None:
        """Test /add endpoint with large numbers."""
        response = client.get("/add?num1=1e10&num2=1e10")
        assert response.status_code == 200
        assert response.json() == {"result": 2e10}
