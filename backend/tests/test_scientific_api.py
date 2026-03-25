"""
API tests for scientific operation endpoints.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestScientificAPI:
    """API tests for scientific endpoints."""

    def test_sqrt_endpoint(self) -> None:
        """Test /sqrt endpoint."""
        response = client.get("/sqrt?num=16")
        assert response.status_code == 200
        assert response.json() == {"result": 4.0}

    def test_sqrt_float_endpoint(self) -> None:
        """Test /sqrt with float."""
        response = client.get("/sqrt?num=2.25")
        assert response.status_code == 200
        assert response.json() == {"result": 1.5}

    def test_power_endpoint(self) -> None:
        """Test /power endpoint."""
        response = client.get("/power?base=2&exp=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8.0}

    def test_power_zero_exponent(self) -> None:
        """Test /power with zero exponent."""
        response = client.get("/power?base=5&exp=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1.0}

    def test_sin_endpoint(self) -> None:
        """Test /sin endpoint."""
        response = client.get("/sin?angle=0")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 0.0) < 0.001

    def test_sin_90_degrees(self) -> None:
        """Test sin(90 degrees)."""
        response = client.get("/sin?angle=90")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 1.0) < 0.001

    def test_cos_endpoint(self) -> None:
        """Test /cos endpoint."""
        response = client.get("/cos?angle=0")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 1.0) < 0.001

    def test_tan_endpoint(self) -> None:
        """Test /tan endpoint."""
        response = client.get("/tan?angle=0")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 0.0) < 0.001

    def test_log_endpoint(self) -> None:
        """Test /log endpoint."""
        response = client.get("/log?num=100&base=10")
        assert response.status_code == 200
        assert response.json() == {"result": 2.0}

    def test_log_default_base(self) -> None:
        """Test /log with default base 10."""
        response = client.get("/log?num=1000")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 3.0) < 0.001

    def test_factorial_endpoint(self) -> None:
        """Test /factorial endpoint."""
        response = client.get("/factorial?num=5")
        assert response.status_code == 200
        assert response.json() == {"result": 120.0}

    def test_factorial_zero(self) -> None:
        """Test 0!."""
        response = client.get("/factorial?num=0")
        assert response.status_code == 200
        assert response.json() == {"result": 1.0}

    def test_reciprocal_endpoint(self) -> None:
        """Test /reciprocal endpoint."""
        response = client.get("/reciprocal?num=4")
        assert response.status_code == 200
        assert response.json() == {"result": 0.25}

    def test_percentage_endpoint(self) -> None:
        """Test /percentage endpoint."""
        response = client.get("/percentage?num=100&percent_val=10")
        assert response.status_code == 200
        assert response.json() == {"result": 10.0}

    def test_pi_endpoint(self) -> None:
        """Test /pi endpoint."""
        response = client.get("/pi")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 3.14159) < 0.01

    def test_e_endpoint(self) -> None:
        """Test /e endpoint (Euler's number)."""
        response = client.get("/e")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 2.71828) < 0.01

    def test_sqrt_missing_parameter(self) -> None:
        """Test /sqrt with missing parameter."""
        response = client.get("/sqrt")
        assert response.status_code == 422

    def test_power_missing_parameter(self) -> None:
        """Test /power with missing parameter."""
        response = client.get("/power?base=2")
        assert response.status_code == 422

    def test_log_invalid_number(self) -> None:
        """Test /log with invalid number."""
        response = client.get("/log?num=abc&base=10")
        assert response.status_code == 422
