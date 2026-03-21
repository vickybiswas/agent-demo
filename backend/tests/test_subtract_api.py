"""API tests for /subtract endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSubtractAPI:
    """API tests for /subtract endpoint."""

    def test_subtract_endpoint_success(self) -> None:
        """Test /subtract endpoint with valid inputs."""
        response = client.get("/subtract?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_subtract_endpoint_decimals(self) -> None:
        """Test /subtract endpoint with decimals."""
        response = client.get("/subtract?num1=8.7&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(5.5)

    def test_subtract_endpoint_negative_result(self) -> None:
        """Test /subtract endpoint resulting in negative."""
        response = client.get("/subtract?num1=3&num2=5")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_subtract_endpoint_negative_inputs(self) -> None:
        """Test /subtract endpoint with negative inputs."""
        response = client.get("/subtract?num1=-5&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_subtract_endpoint_zero(self) -> None:
        """Test /subtract endpoint with zero."""
        response = client.get("/subtract?num1=5&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_subtract_endpoint_missing_params(self) -> None:
        """Test /subtract endpoint with missing parameters."""
        response = client.get("/subtract")
        assert response.status_code == 422

    def test_subtract_endpoint_invalid_type(self) -> None:
        """Test /subtract endpoint with invalid input type."""
        response = client.get("/subtract?num1=abc&num2=3")
        assert response.status_code == 422
