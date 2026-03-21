"""
API tests for /subtract endpoint.

Tests HTTP communication and response format for subtraction.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSubtractAPI:
    """Test cases for /subtract API endpoint."""

    def test_subtract_api_positive_integers(self):
        """Test /subtract with positive integers."""
        response = client.get("/subtract?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_subtract_api_negative_integers(self):
        """Test /subtract with negative integers."""
        response = client.get("/subtract?num1=-5&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_subtract_api_floats(self):
        """Test /subtract with floating point numbers."""
        response = client.get("/subtract?num1=5.5&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.3)

    def test_subtract_api_missing_param_num1(self):
        """Test /subtract missing num1 parameter."""
        response = client.get("/subtract?num2=3")
        assert response.status_code == 422

    def test_subtract_api_missing_param_num2(self):
        """Test /subtract missing num2 parameter."""
        response = client.get("/subtract?num1=5")
        assert response.status_code == 422

    def test_subtract_api_invalid_input_type(self):
        """Test /subtract with invalid input type."""
        response = client.get("/subtract?num1=abc&num2=3")
        assert response.status_code == 422

    def test_subtract_api_same_numbers(self):
        """Test /subtract with same numbers."""
        response = client.get("/subtract?num1=5&num2=5")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_subtract_api_large_numbers(self):
        """Test /subtract with large numbers."""
        response = client.get("/subtract?num1=3000000&num2=2000000")
        assert response.status_code == 200
        assert response.json() == {"result": 1000000}
