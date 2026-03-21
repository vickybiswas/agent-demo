"""
API tests for /power endpoint.

Tests HTTP communication and response format for exponentiation.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestPowerAPI:
    """Test cases for /power API endpoint."""

    def test_power_api_positive_exponent(self):
        """Test /power with positive exponent."""
        response = client.get("/power?num1=2&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_power_api_zero_exponent(self):
        """Test /power with zero exponent."""
        response = client.get("/power?num1=5&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1}

    def test_power_api_negative_exponent(self):
        """Test /power with negative exponent."""
        response = client.get("/power?num1=2&num2=-2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.25)

    def test_power_api_fractional_exponent(self):
        """Test /power with fractional exponent."""
        response = client.get("/power?num1=4&num2=0.5")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.0)

    def test_power_api_float_base(self):
        """Test /power with float base."""
        response = client.get("/power?num1=2.5&num2=2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(6.25)

    def test_power_api_negative_base(self):
        """Test /power with negative base."""
        response = client.get("/power?num1=-2&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -8}

    def test_power_api_missing_num1(self):
        """Test /power missing num1 parameter."""
        response = client.get("/power?num2=3")
        assert response.status_code == 422

    def test_power_api_missing_num2(self):
        """Test /power missing num2 parameter."""
        response = client.get("/power?num1=2")
        assert response.status_code == 422

    def test_power_api_invalid_input_type(self):
        """Test /power with invalid input type."""
        response = client.get("/power?num1=abc&num2=3")
        assert response.status_code == 422
