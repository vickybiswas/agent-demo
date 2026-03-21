"""
API tests for /divide endpoint.

Tests HTTP communication and response format for division.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestDivideAPI:
    """Test cases for /divide API endpoint."""

    def test_divide_api_positive_integers(self):
        """Test /divide with positive integers."""
        response = client.get("/divide?num1=6&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_divide_api_negative_integers(self):
        """Test /divide with negative integers."""
        response = client.get("/divide?num1=-6&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": 2}

    def test_divide_api_floats(self):
        """Test /divide with floating point numbers."""
        response = client.get("/divide?num1=5.5&num2=2.0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.75)

    def test_divide_api_by_zero(self):
        """Test /divide by zero returns 400 error."""
        response = client.get("/divide?num1=5&num2=0")
        assert response.status_code == 400
        assert "Division by zero" in response.json()["detail"]

    def test_divide_api_missing_param_num1(self):
        """Test /divide missing num1 parameter."""
        response = client.get("/divide?num2=3")
        assert response.status_code == 422

    def test_divide_api_missing_param_num2(self):
        """Test /divide missing num2 parameter."""
        response = client.get("/divide?num1=5")
        assert response.status_code == 422

    def test_divide_api_invalid_input_type(self):
        """Test /divide with invalid input type."""
        response = client.get("/divide?num1=abc&num2=3")
        assert response.status_code == 422

    def test_divide_api_zero_dividend(self):
        """Test /divide with zero as dividend."""
        response = client.get("/divide?num1=0&num2=5")
        assert response.status_code == 200
        assert response.json() == {"result": 0}
