"""
API tests for /multiply endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestMultiplyAPI:
    """API tests for /multiply endpoint."""

    def test_multiply_valid_numbers(self) -> None:
        """Test multiplying valid numbers via API."""
        response = client.get("/multiply?num1=4&num2=5")
        assert response.status_code == 200
        assert response.json() == {"result": 20}

    def test_multiply_floats_via_api(self) -> None:
        """Test multiplying floats via API."""
        response = client.get("/multiply?num1=2.5&num2=4.0")
        assert response.status_code == 200
        assert response.json() == {"result": 10.0}

    def test_multiply_negative_via_api(self) -> None:
        """Test multiplying negative numbers via API."""
        response = client.get("/multiply?num1=4&num2=-5")
        assert response.status_code == 200
        assert response.json() == {"result": -20}

    def test_multiply_missing_parameter(self) -> None:
        """Test missing parameter returns error."""
        response = client.get("/multiply?num1=4")
        assert response.status_code == 422

    def test_multiply_invalid_parameter(self) -> None:
        """Test invalid parameter returns error."""
        response = client.get("/multiply?num1=abc&num2=5")
        assert response.status_code == 422
