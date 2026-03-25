"""
API tests for /subtract endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestSubtractAPI:
    """API tests for /subtract endpoint."""

    def test_subtract_valid_numbers(self) -> None:
        """Test subtracting valid numbers via API."""
        response = client.get("/subtract?num1=10&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 7}

    def test_subtract_floats_via_api(self) -> None:
        """Test subtracting floats via API."""
        response = client.get("/subtract?num1=10.5&num2=3.2")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 7.3) < 0.01

    def test_subtract_negative_via_api(self) -> None:
        """Test subtracting with negative numbers via API."""
        response = client.get("/subtract?num1=10&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": 13}

    def test_subtract_missing_parameter(self) -> None:
        """Test missing parameter returns error."""
        response = client.get("/subtract?num1=10")
        assert response.status_code == 422

    def test_subtract_invalid_parameter(self) -> None:
        """Test invalid parameter returns error."""
        response = client.get("/subtract?num1=abc&num2=3")
        assert response.status_code == 422
