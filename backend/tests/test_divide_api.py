"""
API tests for /divide endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestDivideAPI:
    """API tests for /divide endpoint."""

    def test_divide_valid_numbers(self) -> None:
        """Test dividing valid numbers via API."""
        response = client.get("/divide?num1=20&num2=4")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_divide_floats_via_api(self) -> None:
        """Test dividing floats via API."""
        response = client.get("/divide?num1=10.0&num2=2.5")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 4.0) < 0.01

    def test_divide_negative_via_api(self) -> None:
        """Test dividing negative numbers via API."""
        response = client.get("/divide?num1=20&num2=-4")
        assert response.status_code == 200
        assert response.json() == {"result": -5}

    def test_divide_by_zero_via_api(self) -> None:
        """Test dividing by zero returns 0."""
        response = client.get("/divide?num1=10&num2=0")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

    def test_divide_missing_parameter(self) -> None:
        """Test missing parameter returns error."""
        response = client.get("/divide?num1=20")
        assert response.status_code == 422

    def test_divide_invalid_parameter(self) -> None:
        """Test invalid parameter returns error."""
        response = client.get("/divide?num1=20&num2=abc")
        assert response.status_code == 422
