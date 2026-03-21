"""API tests for /multiply endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestMultiplyAPI:
    """API tests for /multiply endpoint."""

    def test_multiply_endpoint_success(self) -> None:
        """Test /multiply endpoint with valid inputs."""
        response = client.get("/multiply?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 15}

    def test_multiply_endpoint_decimals(self) -> None:
        """Test /multiply endpoint with decimals."""
        response = client.get("/multiply?num1=5.5&num2=2.0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(11.0)

    def test_multiply_endpoint_by_zero(self) -> None:
        """Test /multiply endpoint with zero."""
        response = client.get("/multiply?num1=5&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_multiply_endpoint_negative(self) -> None:
        """Test /multiply endpoint with negative numbers."""
        response = client.get("/multiply?num1=-5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -15}

    def test_multiply_endpoint_by_one(self) -> None:
        """Test /multiply endpoint with one."""
        response = client.get("/multiply?num1=5&num2=1")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_multiply_endpoint_missing_params(self) -> None:
        """Test /multiply endpoint with missing parameters."""
        response = client.get("/multiply")
        assert response.status_code == 422

    def test_multiply_endpoint_invalid_type(self) -> None:
        """Test /multiply endpoint with invalid input type."""
        response = client.get("/multiply?num1=abc&num2=3")
        assert response.status_code == 422
