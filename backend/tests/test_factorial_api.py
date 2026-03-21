"""
API tests for /factorial endpoint.

Tests HTTP communication and response format for factorial.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestFactorialAPI:
    """Test cases for /factorial API endpoint."""

    def test_factorial_api_zero(self):
        """Test /factorial with zero."""
        response = client.get("/factorial?num1=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1}

    def test_factorial_api_one(self):
        """Test /factorial with one."""
        response = client.get("/factorial?num1=1")
        assert response.status_code == 200
        assert response.json() == {"result": 1}

    def test_factorial_api_five(self):
        """Test /factorial with five."""
        response = client.get("/factorial?num1=5")
        assert response.status_code == 200
        assert response.json() == {"result": 120}

    def test_factorial_api_ten(self):
        """Test /factorial with ten."""
        response = client.get("/factorial?num1=10")
        assert response.status_code == 200
        assert response.json() == {"result": 3628800}

    def test_factorial_api_small_number(self):
        """Test /factorial with small number."""
        response = client.get("/factorial?num1=3")
        assert response.status_code == 200
        assert response.json() == {"result": 6}

    def test_factorial_api_float_whole_number(self):
        """Test /factorial with float that is whole number."""
        response = client.get("/factorial?num1=5.0")
        assert response.status_code == 200
        assert response.json() == {"result": 120}

    def test_factorial_api_negative(self):
        """Test /factorial with negative number returns 400."""
        response = client.get("/factorial?num1=-1")
        assert response.status_code == 400
        assert "negative" in response.json()["detail"]

    def test_factorial_api_float_non_integer(self):
        """Test /factorial with non-integer float returns 400."""
        response = client.get("/factorial?num1=5.5")
        assert response.status_code == 400
        assert "non-negative integers" in response.json()["detail"]

    def test_factorial_api_missing_param(self):
        """Test /factorial missing num1 parameter."""
        response = client.get("/factorial")
        assert response.status_code == 422

    def test_factorial_api_invalid_input_type(self):
        """Test /factorial with invalid input type."""
        response = client.get("/factorial?num1=abc")
        assert response.status_code == 422

    def test_factorial_api_large_number(self):
        """Test /factorial with larger number."""
        response = client.get("/factorial?num1=12")
        assert response.status_code == 200
        assert response.json() == {"result": 479001600}
