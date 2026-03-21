"""API tests for square root endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSqrtAPI:
    """API tests for /sqrt endpoint."""

    def test_sqrt_endpoint_success(self):
        """Test /sqrt endpoint with valid input."""
        response = client.get("/sqrt?num=4")
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_sqrt_endpoint_decimal(self):
        """Test /sqrt endpoint with decimal."""
        response = client.get("/sqrt?num=2.25")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.5)

    def test_sqrt_endpoint_zero(self):
        """Test /sqrt endpoint with zero."""
        response = client.get("/sqrt?num=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_sqrt_endpoint_negative(self):
        """Test /sqrt endpoint with negative number."""
        response = client.get("/sqrt?num=-4")
        assert response.status_code == 422
        assert "Cannot take square root" in response.json()["detail"]

    def test_sqrt_endpoint_large_number(self):
        """Test /sqrt endpoint with large number."""
        response = client.get("/sqrt?num=1000000")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1000)
