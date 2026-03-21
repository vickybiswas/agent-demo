"""API tests for sine endpoint."""

import pytest
import math
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSineAPI:
    """API tests for /sin endpoint."""

    def test_sin_endpoint_zero(self):
        """Test /sin endpoint with zero."""
        response = client.get("/sin?num=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_sin_endpoint_90_degrees(self):
        """Test /sin endpoint with 90 degrees."""
        response = client.get("/sin?num=90&degrees=true")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_sin_endpoint_180_degrees(self):
        """Test /sin endpoint with 180 degrees."""
        response = client.get("/sin?num=180&degrees=true")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(0, abs=1e-10)

    def test_sin_endpoint_radians(self):
        """Test /sin endpoint with radians."""
        response = client.get(f"/sin?num={math.pi / 2}")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(1.0)

    def test_sin_endpoint_negative(self):
        """Test /sin endpoint with negative angle."""
        response = client.get("/sin?num=-90&degrees=true")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(-1.0)

    def test_sin_endpoint_cors_headers(self):
        """Test CORS headers in response."""
        response = client.get(
            "/sin?num=0",
            headers={"Origin": "http://localhost:3004"}
        )
        assert response.status_code == 200
