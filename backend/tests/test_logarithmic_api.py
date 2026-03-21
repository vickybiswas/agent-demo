"""
API tests for logarithmic endpoints (/log, /ln).

Tests HTTP communication and response format for base-10 and natural logarithm.
"""

import pytest
import math
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestLogAPI:
    """Test cases for /log API endpoint."""

    def test_log_api_one(self):
        """Test /log with one."""
        response = client.get("/log?num1=1")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0)

    def test_log_api_ten(self):
        """Test /log with ten."""
        response = client.get("/log?num1=10")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_log_api_hundred(self):
        """Test /log with hundred."""
        response = client.get("/log?num1=100")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.0)

    def test_log_api_small_decimal(self):
        """Test /log with small decimal."""
        response = client.get("/log?num1=0.1")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_log_api_fractional(self):
        """Test /log with fractional number."""
        response = client.get("/log?num1=5")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.69897)

    def test_log_api_zero(self):
        """Test /log with zero returns 400."""
        response = client.get("/log?num1=0")
        assert response.status_code == 400
        assert "zero or negative" in response.json()["detail"]

    def test_log_api_negative(self):
        """Test /log with negative number returns 400."""
        response = client.get("/log?num1=-5")
        assert response.status_code == 400
        assert "zero or negative" in response.json()["detail"]

    def test_log_api_missing_param(self):
        """Test /log missing num1 parameter."""
        response = client.get("/log")
        assert response.status_code == 422

    def test_log_api_invalid_input_type(self):
        """Test /log with invalid input type."""
        response = client.get("/log?num1=abc")
        assert response.status_code == 422


class TestLnAPI:
    """Test cases for /ln API endpoint."""

    def test_ln_api_one(self):
        """Test /ln with one."""
        response = client.get("/ln?num1=1")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0)

    def test_ln_api_e(self):
        """Test /ln with e (natural constant)."""
        response = client.get(f"/ln?num1={math.e}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_ln_api_e_squared(self):
        """Test /ln with e^2."""
        response = client.get(f"/ln?num1={math.e ** 2}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.0)

    def test_ln_api_small_number(self):
        """Test /ln with small number."""
        response = client.get("/ln?num1=0.5")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-0.69314718)

    def test_ln_api_large_number(self):
        """Test /ln with large number."""
        response = client.get("/ln?num1=1000")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(6.90775527)

    def test_ln_api_zero(self):
        """Test /ln with zero returns 400."""
        response = client.get("/ln?num1=0")
        assert response.status_code == 400
        assert "zero or negative" in response.json()["detail"]

    def test_ln_api_negative(self):
        """Test /ln with negative number returns 400."""
        response = client.get("/ln?num1=-10")
        assert response.status_code == 400
        assert "zero or negative" in response.json()["detail"]

    def test_ln_api_missing_param(self):
        """Test /ln missing num1 parameter."""
        response = client.get("/ln")
        assert response.status_code == 422

    def test_ln_api_invalid_input_type(self):
        """Test /ln with invalid input type."""
        response = client.get("/ln?num1=notanumber")
        assert response.status_code == 422
