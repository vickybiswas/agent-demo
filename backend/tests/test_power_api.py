"""API tests for power endpoint."""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestPowerAPI:
    """API tests for /power endpoint."""

    def test_power_endpoint_success(self):
        """Test /power endpoint with valid inputs."""
        response = client.get("/power?base=2&exponent=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_power_endpoint_zero_exponent(self):
        """Test /power endpoint with zero exponent."""
        response = client.get("/power?base=5&exponent=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1}

    def test_power_endpoint_negative_exponent(self):
        """Test /power endpoint with negative exponent."""
        response = client.get("/power?base=2&exponent=-1")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0.5)

    def test_power_endpoint_decimal(self):
        """Test /power endpoint with decimal base."""
        response = client.get("/power?base=2.5&exponent=2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(6.25)

    def test_power_endpoint_fractional_exponent(self):
        """Test /power endpoint with fractional exponent."""
        response = client.get("/power?base=4&exponent=0.5")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.0)
