"""
API tests for /add endpoint.

Tests HTTP communication and response format for addition.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAddAPI:
    """Test cases for /add API endpoint."""

    def test_add_api_positive_integers(self):
        """Test /add with positive integers."""
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_api_negative_integers(self):
        """Test /add with negative integers."""
        response = client.get("/add?num1=-5&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": -8}

    def test_add_api_floats(self):
        """Test /add with floating point numbers."""
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(8.7)

    def test_add_api_missing_param_num1(self):
        """Test /add missing num1 parameter."""
        response = client.get("/add?num2=3")
        assert response.status_code == 422

    def test_add_api_missing_param_num2(self):
        """Test /add missing num2 parameter."""
        response = client.get("/add?num1=5")
        assert response.status_code == 422

    def test_add_api_invalid_input_type(self):
        """Test /add with invalid input type."""
        response = client.get("/add?num1=abc&num2=3")
        assert response.status_code == 422

    def test_add_api_with_zero(self):
        """Test /add with zero value."""
        response = client.get("/add?num1=5&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_add_api_large_numbers(self):
        """Test /add with large numbers."""
        response = client.get("/add?num1=1000000&num2=2000000")
        assert response.status_code == 200
        assert response.json() == {"result": 3000000}
