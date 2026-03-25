# Backend Development Guide (8 Phases)

## Agent
**Python FastAPI Specialist**

## Overview
Build a production-ready FastAPI backend with zero external dependencies for calculations, comprehensive testing, and CORS support.

**Stack**: FastAPI | Uvicorn | Python 3.13 | pytest | PEP8 compliance

---

## Phase 1: Project Setup

### Create Directory Structure
```bash
mkdir -p backend/operations backend/tests
cd backend
```

### Create requirements.txt
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pytest==7.4.3
pytest-cov==4.1.0
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### File Structure
```
backend/
├── main.py              # FastAPI app, CORS, health endpoint
├── operations/
│   ├── __init__.py
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   └── divide.py
├── tests/
│   ├── test_add_unit.py
│   ├── test_subtract_unit.py
│   ├── test_multiply_unit.py
│   ├── test_divide_unit.py
│   ├── test_add_api.py
│   ├── test_subtract_api.py
│   ├── test_multiply_api.py
│   └── test_divide_api.py
└── requirements.txt
```

### ✅ Phase 1 Complete
- [x] Project structure created
- [x] Only fastapi & uvicorn dependencies
- [x] requirements.txt defined
- [x] Directory structure established

---

## Phase 2: Main App & CORS Middleware

### Create main.py
```python
"""
Stranger Things Calculator API
FastAPI backend with CORS support for add, subtract, multiply, divide operations.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from operations.add import add_numbers
from operations.subtract import subtract_numbers
from operations.multiply import multiply_numbers
from operations.divide import divide_numbers

app = FastAPI(
    title="Stranger Things Calculator API",
    description="A themed calculator API with add, subtract, multiply, divide operations",
    version="1.0.0"
)

# Add CORS middleware - allows all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict:
    """
    Health check endpoint to verify API is running.

    Returns:
        dict: Status response
    """
    return {"status": "ok"}


@app.get("/add")
def add(num1: float, num2: float) -> dict:
    """
    Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        dict: Result of addition
    """
    result = add_numbers(num1, num2)
    return {"result": result}


@app.get("/subtract")
def subtract(num1: float, num2: float) -> dict:
    """
    Subtract two numbers.

    Args:
        num1: First number
        num2: Second number to subtract

    Returns:
        dict: Result of subtraction
    """
    result = subtract_numbers(num1, num2)
    return {"result": result}


@app.get("/multiply")
def multiply(num1: float, num2: float) -> dict:
    """
    Multiply two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        dict: Result of multiplication
    """
    result = multiply_numbers(num1, num2)
    return {"result": result}


@app.get("/divide")
def divide(num1: float, num2: float) -> dict:
    """
    Divide two numbers.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        dict: Result of division (0 if dividing by zero)
    """
    result = divide_numbers(num1, num2)
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
```

### ✅ Phase 2 Complete
- [x] FastAPI app created
- [x] CORS middleware configured
- [x] /health endpoint implemented
- [x] Endpoints created (add, subtract, multiply, divide)
- [x] All functions typed with docstrings

---

## Phase 3: Route Implementation

### Create operations/__init__.py
```python
"""
Operations module for calculator functions.
"""
```

### Create operations/add.py
```python
"""
Addition operation module.
"""


def add_numbers(num1: float, num2: float) -> float:
    """
    Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        float: Sum of num1 and num2
    """
    return num1 + num2
```

### Create operations/subtract.py
```python
"""
Subtraction operation module.
"""


def subtract_numbers(num1: float, num2: float) -> float:
    """
    Subtract two numbers.

    Args:
        num1: First number
        num2: Second number to subtract

    Returns:
        float: Difference (num1 - num2)
    """
    return num1 - num2
```

### Create operations/multiply.py
```python
"""
Multiplication operation module.
"""


def multiply_numbers(num1: float, num2: float) -> float:
    """
    Multiply two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        float: Product of num1 and num2
    """
    return num1 * num2
```

### Create operations/divide.py
```python
"""
Division operation module.
"""


def divide_numbers(num1: float, num2: float) -> float:
    """
    Divide two numbers.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        float: Quotient (returns 0 if dividing by zero)
    """
    if num2 == 0:
        return 0.0
    return num1 / num2
```

### ✅ Phase 3 Complete
- [x] Separate file for each operation
- [x] All functions typed
- [x] All docstrings complete
- [x] Zero external dependencies for calculations
- [x] Edge cases handled (division by zero)

---

## Phase 4: Unit Tests

### Create tests/test_add_unit.py
```python
"""
Unit tests for add operation.
"""

import pytest
from operations.add import add_numbers


class TestAddUnit:
    """Unit tests for add_numbers function."""

    def test_add_positive_numbers(self) -> None:
        """Test adding two positive numbers."""
        result = add_numbers(5, 3)
        assert result == 8

    def test_add_negative_numbers(self) -> None:
        """Test adding two negative numbers."""
        result = add_numbers(-5, -3)
        assert result == -8

    def test_add_mixed_signs(self) -> None:
        """Test adding numbers with mixed signs."""
        result = add_numbers(10, -3)
        assert result == 7

    def test_add_floats(self) -> None:
        """Test adding floating point numbers."""
        result = add_numbers(5.5, 3.2)
        assert abs(result - 8.7) < 0.01

    def test_add_zero(self) -> None:
        """Test adding with zero."""
        result = add_numbers(5, 0)
        assert result == 5
```

### Create tests/test_subtract_unit.py
```python
"""
Unit tests for subtract operation.
"""

import pytest
from operations.subtract import subtract_numbers


class TestSubtractUnit:
    """Unit tests for subtract_numbers function."""

    def test_subtract_positive_numbers(self) -> None:
        """Test subtracting two positive numbers."""
        result = subtract_numbers(10, 3)
        assert result == 7

    def test_subtract_negative_numbers(self) -> None:
        """Test subtracting negative numbers."""
        result = subtract_numbers(-5, -3)
        assert result == -2

    def test_subtract_mixed_signs(self) -> None:
        """Test subtracting with mixed signs."""
        result = subtract_numbers(10, -3)
        assert result == 13

    def test_subtract_floats(self) -> None:
        """Test subtracting floating point numbers."""
        result = subtract_numbers(10.5, 3.2)
        assert abs(result - 7.3) < 0.01

    def test_subtract_zero(self) -> None:
        """Test subtracting with zero."""
        result = subtract_numbers(5, 0)
        assert result == 5
```

### Create tests/test_multiply_unit.py
```python
"""
Unit tests for multiply operation.
"""

import pytest
from operations.multiply import multiply_numbers


class TestMultiplyUnit:
    """Unit tests for multiply_numbers function."""

    def test_multiply_positive_numbers(self) -> None:
        """Test multiplying two positive numbers."""
        result = multiply_numbers(4, 5)
        assert result == 20

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplying negative numbers."""
        result = multiply_numbers(-4, -5)
        assert result == 20

    def test_multiply_mixed_signs(self) -> None:
        """Test multiplying with mixed signs."""
        result = multiply_numbers(4, -5)
        assert result == -20

    def test_multiply_floats(self) -> None:
        """Test multiplying floating point numbers."""
        result = multiply_numbers(2.5, 4.0)
        assert result == 10.0

    def test_multiply_by_zero(self) -> None:
        """Test multiplying by zero."""
        result = multiply_numbers(5, 0)
        assert result == 0
```

### Create tests/test_divide_unit.py
```python
"""
Unit tests for divide operation.
"""

import pytest
from operations.divide import divide_numbers


class TestDivideUnit:
    """Unit tests for divide_numbers function."""

    def test_divide_positive_numbers(self) -> None:
        """Test dividing two positive numbers."""
        result = divide_numbers(20, 4)
        assert result == 5

    def test_divide_negative_numbers(self) -> None:
        """Test dividing negative numbers."""
        result = divide_numbers(-20, -4)
        assert result == 5

    def test_divide_mixed_signs(self) -> None:
        """Test dividing with mixed signs."""
        result = divide_numbers(20, -4)
        assert result == -5

    def test_divide_floats(self) -> None:
        """Test dividing floating point numbers."""
        result = divide_numbers(10.0, 2.5)
        assert abs(result - 4.0) < 0.01

    def test_divide_by_zero(self) -> None:
        """Test dividing by zero returns 0."""
        result = divide_numbers(10, 0)
        assert result == 0
```

### Run Unit Tests
```bash
python3 -m pytest tests/test_*_unit.py -v
```

### ✅ Phase 4 Complete
- [x] Unit tests created (5+ per operation)
- [x] Positive cases tested
- [x] Negative cases tested
- [x] Edge cases tested (zero, division by zero)
- [x] All tests passing

---

## Phase 5: API Tests

### Create tests/test_add_api.py
```python
"""
API tests for /add endpoint.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAddAPI:
    """API tests for /add endpoint."""

    def test_add_valid_numbers(self) -> None:
        """Test adding valid numbers via API."""
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_floats_via_api(self) -> None:
        """Test adding floats via API."""
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        data = response.json()
        assert abs(data["result"] - 8.7) < 0.01

    def test_add_negative_via_api(self) -> None:
        """Test adding negative numbers via API."""
        response = client.get("/add?num1=-5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_add_missing_parameter(self) -> None:
        """Test missing parameter returns error."""
        response = client.get("/add?num1=5")
        assert response.status_code == 422

    def test_add_invalid_parameter(self) -> None:
        """Test invalid parameter returns error."""
        response = client.get("/add?num1=abc&num2=3")
        assert response.status_code == 422
```

### Create tests/test_subtract_api.py
```python
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
```

### Create tests/test_multiply_api.py
```python
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
```

### Create tests/test_divide_api.py
```python
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
```

### Run API Tests
```bash
python3 -m pytest tests/test_*_api.py -v
```

### ✅ Phase 5 Complete
- [x] API tests created (5+ per endpoint)
- [x] Valid input tested
- [x] Invalid input tested
- [x] Edge cases tested (divide by zero)
- [x] HTTP status codes verified
- [x] All tests passing

---

## Phase 6: Coverage & Regression Suite

### Run All Tests with Coverage
```bash
python3 -m pytest tests/ -v --cov=operations --cov-report=term-missing
```

Expected output:
```
======================== test session starts =========================
...
----- coverage: platform linux -- Python 3.13.x -----
Name                    Stmts   Miss  Cover
-----------------------------------------------
operations/__init__.py      0      0   100%
operations/add.py           2      0   100%
operations/divide.py        4      0   100%
operations/multiply.py      2      0   100%
operations/subtract.py      2      0   100%
-----------------------------------------------
TOTAL                      12      0   100%
```

### Regression Test Suite
All tests should pass (unit + API):
```bash
python3 -m pytest tests/ -v
```

### ✅ Phase 6 Complete
- [x] 100% code coverage on operations/
- [x] All unit tests passing
- [x] All API tests passing
- [x] Regression suite complete
- [x] No missing coverage

---

## Phase 7: Code Quality

### PEP8 Compliance
```bash
python3 -m autopep8 --diff main.py operations/*.py

# Auto-fix (if needed)
autopep8 --in-place --aggressive --aggressive main.py operations/*.py
```

### Check for Docstrings
```bash
# All functions should have docstrings
grep -c "def " main.py operations/*.py
grep -c '"""' main.py operations/*.py
```

Expected: Each function has a docstring

### Type Hints
All functions should be fully typed:
```bash
# Verify type hints present
grep "def " main.py operations/*.py | grep -v "->"
# Should return empty (no untyped functions)
```

### No Debug Code
```bash
# Check for print statements
grep "print(" main.py operations/*.py
# Should return empty
```

### ✅ Phase 7 Complete
- [x] PEP8 compliant
- [x] Type hints complete
- [x] Docstrings present
- [x] No debug code
- [x] Code quality verified

---

## Phase 8: Documentation

### Create API Documentation
FastAPI automatically generates OpenAPI docs:
```bash
python3 main.py
# Visit http://localhost:8004/docs for Swagger UI
```

### README (Optional but Recommended)
Create `README.md`:
```markdown
# Stranger Things Calculator API

## Endpoints

- `GET /health` - Health check
- `GET /add?num1=x&num2=y` - Addition
- `GET /subtract?num1=x&num2=y` - Subtraction
- `GET /multiply?num1=x&num2=y` - Multiplication
- `GET /divide?num1=x&num2=y` - Division

## Example

```bash
curl http://localhost:8004/add?num1=5&num2=3
# {"result":8}
```

## Testing

```bash
# Unit tests
python3 -m pytest tests/test_*_unit.py -v

# API tests
python3 -m pytest tests/test_*_api.py -v

# Coverage
python3 -m pytest tests/ --cov=operations --cov-report=term-missing
```
```

### ✅ Phase 8 Complete
- [x] API documentation available (/docs endpoint)
- [x] Code well-documented with docstrings
- [x] Endpoints clearly defined
- [x] Testing procedures documented

---

## Parallelization Strategy

**Independent tests spawn together, not sequentially:**

### Testing Phases (All Parallel)
```
Unit Tests (5 per operation)   → spawn all together
API Tests (5 per endpoint)     → spawn all together
Coverage Analysis              → runs after both complete
```

### Result
**5-10x faster** than sequential testing.

---

## Quick Commands

| Command | Purpose |
|---------|---------|
| `python3 main.py` | Start server on :8004 |
| `python3 -m pytest tests/test_*_unit.py -v` | Run unit tests |
| `python3 -m pytest tests/test_*_api.py -v` | Run API tests |
| `python3 -m pytest tests/ -v --cov=operations` | Run all + coverage |
| `curl http://localhost:8004/health` | Check health |
| `curl "http://localhost:8004/add?num1=5&num2=3"` | Test add endpoint |

---

## References
- **CLAUDE.md**: Full project orchestration
- **frontend/CLAUDE.md**: Frontend phases
- **REGRESSION.md**: Pre-PR checklist (mandatory)
- **STARTUP.md**: Service startup options

---

## Success Criteria
✅ FastAPI backend created
✅ Zero external dependencies for calculations
✅ Separate route files (operations/)
✅ 100% test coverage
✅ All tests passing (unit + API)
✅ PEP8 compliant
✅ Full type hints
✅ Complete docstrings
✅ CORS middleware configured
✅ Ready for Docker & PR
