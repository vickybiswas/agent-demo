"""
API tests for /multiply endpoint.

Tests HTTP communication and response format for multiplication.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestMultiplyAPI:
    """Test cases for /multiply API endpoint."""

    def test_multiply_api_positive_integers(self):
        """Test /multiply with positive integers."""
        response = client.get("/multiply?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 15}

    def test_multiply_api_negative_integers(self):
        """Test /multiply with negative integers."""
        response = client.get("/multiply?num1=-5&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": 15}

    def test_multiply_api_floats(self):
        """Test /multiply with floating point numbers."""
        response = client.get("/multiply?num1=5.5&num2=2.0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(11.0)

    def test_multiply_api_missing_param_num1(self):
        """Test /multiply missing num1 parameter."""
        response = client.get("/multiply?num2=3")
        assert response.status_code == 422

    def test_multiply_api_missing_param_num2(self):
        """Test /multiply missing num2 parameter."""
        response = client.get("/multiply?num1=5")
        assert response.status_code == 422

    def test_multiply_api_invalid_input_type(self):
        """Test /multiply with invalid input type."""
        response = client.get("/multiply?num1=abc&num2=3")
        assert response.status_code == 422

    def test_multiply_api_by_zero(self):
        """Test /multiply with zero."""
        response = client.get("/multiply?num1=5&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_multiply_api_by_one(self):
        """Test /multiply by one."""
        response = client.get("/multiply?num1=5&num2=1")
        assert response.status_code == 200
        assert response.json() == {"result": 5}
