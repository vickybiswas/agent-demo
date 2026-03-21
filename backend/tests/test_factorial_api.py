"""API tests for factorial endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestFactorialAPI:
    """API tests for /factorial endpoint."""

    def test_factorial_endpoint_zero(self):
        """Test /factorial endpoint with zero."""
        response = client.get("/factorial?num=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1}

    def test_factorial_endpoint_five(self):
        """Test /factorial endpoint with 5."""
        response = client.get("/factorial?num=5")
        assert response.status_code == 200
        assert response.json() == {"result": 120}

    def test_factorial_endpoint_ten(self):
        """Test /factorial endpoint with 10."""
        response = client.get("/factorial?num=10")
        assert response.status_code == 200
        assert response.json() == {"result": 3628800}

    def test_factorial_endpoint_negative(self):
        """Test /factorial endpoint with negative number."""
        response = client.get("/factorial?num=-5")
        assert response.status_code == 422
        assert "Cannot calculate factorial" in response.json()["detail"]

    def test_factorial_endpoint_decimal(self):
        """Test /factorial endpoint with decimal."""
        response = client.get("/factorial?num=5.5")
        assert response.status_code == 422
        assert "Factorial only works with integers" in response.json()["detail"]
