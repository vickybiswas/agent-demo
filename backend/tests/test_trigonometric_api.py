"""
API tests for trigonometric endpoints (/sin, /cos, /tan).

Tests HTTP communication and response format for sine, cosine, and tangent.
"""

import pytest
import math
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSinAPI:
    """Test cases for /sin API endpoint."""

    def test_sin_api_zero(self):
        """Test /sin with zero."""
        response = client.get("/sin?num1=0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0)

    def test_sin_api_pi_half(self):
        """Test /sin with pi/2."""
        response = client.get(f"/sin?num1={math.pi / 2}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_sin_api_pi(self):
        """Test /sin with pi."""
        response = client.get(f"/sin?num1={math.pi}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0, abs=1e-10)

    def test_sin_api_negative_angle(self):
        """Test /sin with negative angle."""
        response = client.get(f"/sin?num1={-math.pi / 2}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_sin_api_missing_param(self):
        """Test /sin missing num1 parameter."""
        response = client.get("/sin")
        assert response.status_code == 422

    def test_sin_api_invalid_input_type(self):
        """Test /sin with invalid input type."""
        response = client.get("/sin?num1=abc")
        assert response.status_code == 422


class TestCosAPI:
    """Test cases for /cos API endpoint."""

    def test_cos_api_zero(self):
        """Test /cos with zero."""
        response = client.get("/cos?num1=0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_cos_api_pi_half(self):
        """Test /cos with pi/2."""
        response = client.get(f"/cos?num1={math.pi / 2}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0, abs=1e-10)

    def test_cos_api_pi(self):
        """Test /cos with pi."""
        response = client.get(f"/cos?num1={math.pi}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_cos_api_negative_angle(self):
        """Test /cos with negative angle."""
        response = client.get(f"/cos?num1={-math.pi}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_cos_api_missing_param(self):
        """Test /cos missing num1 parameter."""
        response = client.get("/cos")
        assert response.status_code == 422

    def test_cos_api_invalid_input_type(self):
        """Test /cos with invalid input type."""
        response = client.get("/cos?num1=xyz")
        assert response.status_code == 422


class TestTanAPI:
    """Test cases for /tan API endpoint."""

    def test_tan_api_zero(self):
        """Test /tan with zero."""
        response = client.get("/tan?num1=0")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.0)

    def test_tan_api_pi_fourth(self):
        """Test /tan with pi/4."""
        response = client.get(f"/tan?num1={math.pi / 4}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_tan_api_negative_angle(self):
        """Test /tan with negative angle."""
        response = client.get(f"/tan?num1={-math.pi / 4}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_tan_api_small_angle(self):
        """Test /tan with small angle."""
        response = client.get("/tan?num1=0.1")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.10033467)

    def test_tan_api_missing_param(self):
        """Test /tan missing num1 parameter."""
        response = client.get("/tan")
        assert response.status_code == 422

    def test_tan_api_invalid_input_type(self):
        """Test /tan with invalid input type."""
        response = client.get("/tan?num1=invalid")
        assert response.status_code == 422
