"""API tests for calculator endpoints."""
import pytest
from starlette.testclient import TestClient
from main import app

client = TestClient(app)


# Test health endpoint
def test_health() -> None:
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Test add endpoint
def test_add_success() -> None:
    """Test successful add operation."""
    response = client.get("/add?num1=5&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8
    assert response.json()["operation"] == "add"


def test_add_floats() -> None:
    """Test add with float numbers."""
    response = client.get("/add?num1=5.5&num2=3.2")
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(8.7)
    assert response.json()["operation"] == "add"


def test_add_negative() -> None:
    """Test add with negative numbers."""
    response = client.get("/add?num1=-5&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == -2


def test_add_missing_param() -> None:
    """Test add with missing parameter."""
    response = client.get("/add?num1=5")
    assert response.status_code == 422


def test_add_invalid_param() -> None:
    """Test add with invalid parameter."""
    response = client.get("/add?num1=abc&num2=3")
    assert response.status_code == 422


# Test subtract endpoint
def test_subtract_success() -> None:
    """Test successful subtract operation."""
    response = client.get("/subtract?num1=5&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == 2
    assert response.json()["operation"] == "subtract"


def test_subtract_floats() -> None:
    """Test subtract with float numbers."""
    response = client.get("/subtract?num1=5.5&num2=3.2")
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(2.3)


def test_subtract_negative() -> None:
    """Test subtract with negative numbers."""
    response = client.get("/subtract?num1=-5&num2=-3")
    assert response.status_code == 200
    assert response.json()["result"] == -2


def test_subtract_missing_param() -> None:
    """Test subtract with missing parameter."""
    response = client.get("/subtract?num1=5")
    assert response.status_code == 422


def test_subtract_invalid_param() -> None:
    """Test subtract with invalid parameter."""
    response = client.get("/subtract?num1=5&num2=xyz")
    assert response.status_code == 422


# Test multiply endpoint
def test_multiply_success() -> None:
    """Test successful multiply operation."""
    response = client.get("/multiply?num1=5&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == 15
    assert response.json()["operation"] == "multiply"


def test_multiply_floats() -> None:
    """Test multiply with float numbers."""
    response = client.get("/multiply?num1=2.5&num2=4")
    assert response.status_code == 200
    assert response.json()["result"] == 10.0


def test_multiply_by_zero() -> None:
    """Test multiply by zero."""
    response = client.get("/multiply?num1=5&num2=0")
    assert response.status_code == 200
    assert response.json()["result"] == 0


def test_multiply_negative() -> None:
    """Test multiply with negative numbers."""
    response = client.get("/multiply?num1=-5&num2=3")
    assert response.status_code == 200
    assert response.json()["result"] == -15


def test_multiply_missing_param() -> None:
    """Test multiply with missing parameter."""
    response = client.get("/multiply?num1=5")
    assert response.status_code == 422


# Test divide endpoint
def test_divide_success() -> None:
    """Test successful divide operation."""
    response = client.get("/divide?num1=6&num2=2")
    assert response.status_code == 200
    assert response.json()["result"] == 3
    assert response.json()["operation"] == "divide"


def test_divide_floats() -> None:
    """Test divide with float numbers."""
    response = client.get("/divide?num1=7.5&num2=2.5")
    assert response.status_code == 200
    assert response.json()["result"] == 3


def test_divide_by_zero() -> None:
    """Test divide by zero returns 400."""
    response = client.get("/divide?num1=6&num2=0")
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json()["detail"]


def test_divide_negative() -> None:
    """Test divide with negative numbers."""
    response = client.get("/divide?num1=-6&num2=2")
    assert response.status_code == 200
    assert response.json()["result"] == -3


def test_divide_missing_param() -> None:
    """Test divide with missing parameter."""
    response = client.get("/divide?num1=6")
    assert response.status_code == 422


# Test response schema consistency
def test_response_schema_add() -> None:
    """Test add response has required fields."""
    response = client.get("/add?num1=5&num2=3")
    data = response.json()
    assert "result" in data
    assert "operation" in data
    assert len(data) == 2


def test_response_schema_subtract() -> None:
    """Test subtract response has required fields."""
    response = client.get("/subtract?num1=5&num2=3")
    data = response.json()
    assert "result" in data
    assert "operation" in data


def test_response_schema_multiply() -> None:
    """Test multiply response has required fields."""
    response = client.get("/multiply?num1=5&num2=3")
    data = response.json()
    assert "result" in data
    assert "operation" in data


def test_response_schema_divide() -> None:
    """Test divide response has required fields."""
    response = client.get("/divide?num1=6&num2=2")
    data = response.json()
    assert "result" in data
    assert "operation" in data
