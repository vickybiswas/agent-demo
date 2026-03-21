"""API tests for /divide endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestDivideAPI:
    """API tests for /divide endpoint."""

    def test_divide_endpoint_success(self) -> None:
        """Test /divide endpoint with valid inputs."""
        response = client.get("/divide?num1=6&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 2.0}

    def test_divide_endpoint_by_zero(self) -> None:
        """Test /divide endpoint with zero divisor."""
        response = client.get("/divide?num1=5&num2=0")
        assert response.status_code == 422
        assert "Division by zero" in response.json()["detail"]

    def test_divide_endpoint_negative(self) -> None:
        """Test /divide endpoint with negative numbers."""
        response = client.get("/divide?num1=-6&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2.0}

    def test_divide_endpoint_with_remainder(self) -> None:
        """Test /divide endpoint with remainder."""
        response = client.get("/divide?num1=5&num2=2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.5)

    def test_divide_endpoint_invalid_type(self) -> None:
        """Test /divide endpoint with invalid input type."""
        response = client.get("/divide?num1=abc&num2=3")
        assert response.status_code == 422

    def test_divide_endpoint_decimals(self) -> None:
        """Test /divide endpoint with decimals."""
        response = client.get("/divide?num1=7.5&num2=2.5")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(3.0)

    def test_divide_endpoint_missing_params(self) -> None:
        """Test /divide endpoint with missing parameters."""
        response = client.get("/divide")
        assert response.status_code == 422
