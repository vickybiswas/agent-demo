"""
API tests for /sqrt endpoint.

Tests HTTP communication and response format for square root.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSqrtAPI:
    """Test cases for /sqrt API endpoint."""

    def test_sqrt_api_positive_integer(self):
        """Test /sqrt with positive integer."""
        response = client.get("/sqrt?num1=9")
        assert response.status_code == 200
        assert response.json() == {"result": 3.0}

    def test_sqrt_api_zero(self):
        """Test /sqrt with zero."""
        response = client.get("/sqrt?num1=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0.0}

    def test_sqrt_api_float(self):
        """Test /sqrt with float."""
        response = client.get("/sqrt?num1=2.25")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.5)

    def test_sqrt_api_large_number(self):
        """Test /sqrt with large number."""
        response = client.get("/sqrt?num1=1000000")
        assert response.status_code == 200
        assert response.json() == {"result": 1000.0}

    def test_sqrt_api_negative_number(self):
        """Test /sqrt with negative number returns 400."""
        response = client.get("/sqrt?num1=-4")
        assert response.status_code == 400
        assert "Square root of negative" in response.json()["detail"]

    def test_sqrt_api_missing_param(self):
        """Test /sqrt missing num1 parameter."""
        response = client.get("/sqrt")
        assert response.status_code == 422

    def test_sqrt_api_invalid_input_type(self):
        """Test /sqrt with invalid input type."""
        response = client.get("/sqrt?num1=abc")
        assert response.status_code == 422

    def test_sqrt_api_decimal_result(self):
        """Test /sqrt resulting in decimal."""
        response = client.get("/sqrt?num1=2")
        assert response.status_code == 200
        result = response.json()["result"]
        assert result == pytest.approx(1.41421356, rel=1e-5)
