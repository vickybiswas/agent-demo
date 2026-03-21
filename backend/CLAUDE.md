# Backend Development Guide (backend/CLAUDE.md)

## Overview
This document guides the FastAPI Specialist agent through building the Python backend.

**Framework**: FastAPI with Uvicorn (ONLY dependencies)
**Language**: Python 3.11+
**Database**: None (stateless calculations)
**Testing**: pytest (unit + API tests)
**Code Quality**: PEP8, type hints, docstrings

---

## Phase 1: Project Setup (Week 1)

### Objective
Initialize FastAPI project with proper structure and dependencies.

### Directory Structure
Create backend/ directory with:
```
backend/
├── main.py                 # FastAPI app instance, CORS middleware
├── routes/
│   ├── __init__.py
│   ├── add.py             # /add endpoint
│   ├── subtract.py        # /subtract endpoint
│   ├── multiply.py        # /multiply endpoint
│   └── divide.py          # /divide endpoint
├── tests/
│   ├── test_add_unit.py   # 5+ unit tests
│   ├── test_add_api.py    # 5+ API tests
│   ├── test_subtract_unit.py
│   ├── test_subtract_api.py
│   ├── test_multiply_unit.py
│   ├── test_multiply_api.py
│   ├── test_divide_unit.py
│   ├── test_divide_api.py
│   └── test_regression.py # Run all tests
├── requirements.txt        # Only: fastapi, uvicorn
├── Dockerfile             # Python 3.11-slim
└── README.md              # Setup documentation
```

### Requirements Setup
Create `backend/requirements.txt`:
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
```

**NO other dependencies** (no numpy, pandas, SQLAlchemy, etc.)

### Virtual Environment
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Project Initialization
- [ ] Create main.py with FastAPI instance
- [ ] Create routes/ directory
- [ ] Create tests/ directory
- [ ] Create requirements.txt (only fastapi + uvicorn)

### Quality Gate
- ✅ Virtual environment created
- ✅ Dependencies installed
- ✅ main.py exists with FastAPI app
- ✅ Directory structure complete

---

## Phase 2: Main App & CORS Middleware (Week 1)

### Objective
Create FastAPI application with CORS middleware for frontend communication.

### main.py Structure
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routes import add, subtract, multiply, divide

app = FastAPI(title="Stranger Things Calculator", version="1.0.0")

# CORS Middleware Configuration
# Allow frontend origin (both local dev and Docker)
cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:3004,http://frontend:3004"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check Endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Import and include routers
app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
```

### CORS Middleware Details
- **allow_origins**: Include frontend localhost (3004) and Docker service name
- **allow_credentials**: Allow cookies/auth headers
- **allow_methods**: GET, POST, OPTIONS (wildcard OK)
- **allow_headers**: Content-Type, Authorization, etc.

### Health Endpoint
- **Path**: `/health`
- **Method**: GET
- **Response**: `{"status": "ok"}`
- **Purpose**: Docker health checks, startup verification

### Environment Variable Setup
- **CORS_ORIGINS**: Comma-separated list of allowed origins
  - Default: `http://localhost:3004,http://frontend:3004`
  - Can be overridden in docker-compose.yaml

### Startup
```bash
python3 main.py
# or
uvicorn main:app --reload --port 8004
```

**Expected Output**:
```
Uvicorn running on http://0.0.0.0:8004
```

### Quality Gate
- ✅ FastAPI app instantiated
- ✅ CORS middleware configured
- ✅ /health endpoint responds
- ✅ Routes imported from routes/ directory
- ✅ Server starts without errors

---

## Phase 3: Route Implementation (Week 1-2)

### Objective
Create separate route files for each calculator operation.

### Route Structure Pattern
Each route file (add.py, subtract.py, etc.) follows this pattern:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Union

router = APIRouter()

class OperationRequest(BaseModel):
    num1: Union[int, float]
    num2: Union[int, float]

@router.get("/add")
async def add_operation(num1: Union[int, float], num2: Union[int, float]):
    """
    Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        JSON with result: {"result": num1 + num2}
    """
    result = num1 + num2
    return {"result": result}

@router.post("/add")
async def add_operation_post(request: OperationRequest):
    """Add two numbers (POST version)"""
    result = request.num1 + request.num2
    return {"result": result}
```

### Individual Route Files

#### routes/add.py
- Endpoint: `/add?num1=xxx&num2=yyy`
- Operation: `num1 + num2`
- Return: `{"result": num1 + num2}`

#### routes/subtract.py
- Endpoint: `/subtract?num1=xxx&num2=yyy`
- Operation: `num1 - num2`
- Return: `{"result": num1 - num2}`

#### routes/multiply.py
- Endpoint: `/multiply?num1=xxx&num2=yyy`
- Operation: `num1 * num2`
- Return: `{"result": num1 * num2}`

#### routes/divide.py
- Endpoint: `/divide?num1=xxx&num2=yyy`
- Operation: `num1 / num2` (with error handling)
- Return: `{"result": num1 / num2}`
- **Error Handling**: Division by zero → HTTP 400 with error message

### Common Requirements
- [ ] All routes typed with type hints
- [ ] All routes documented with docstrings
- [ ] All routes return JSON with `"result"` field
- [ ] Error handling for invalid inputs (400 Bad Request)
- [ ] Division by zero handled (400 Bad Request)

### Testing Routes Manually
```bash
# Test /add
curl "http://localhost:8004/add?num1=5&num2=3"
# Expected: {"result": 8}

# Test /divide (error case)
curl "http://localhost:8004/divide?num1=5&num2=0"
# Expected: 400 error with message
```

### Quality Gate
- ✅ All 4 routes implemented (/add, /subtract, /multiply, /divide)
- ✅ Routes return correct results
- ✅ Error handling for division by zero
- ✅ Type hints on all parameters
- ✅ Docstrings on all functions

---

## Phase 4: Unit Tests (Week 2)

### Objective
Create unit tests for each operation (5+ per operation, 20+ total).

### Unit Test Requirements
- **Test framework**: pytest
- **Location**: tests/test_*_unit.py
- **Tests per operation**: 5+ (covering positive, negative, edge cases)
- **Coverage**: 100% of business logic

### Example Unit Tests (tests/test_add_unit.py)
```python
import pytest

def add(num1, num2):
    """Helper function to test"""
    return num1 + num2

class TestAdd:
    def test_add_positive_integers(self):
        assert add(5, 3) == 8

    def test_add_negative_integers(self):
        assert add(-5, -3) == -8

    def test_add_mixed_signs(self):
        assert add(5, -3) == 2

    def test_add_floats(self):
        assert add(5.5, 3.2) == 8.7

    def test_add_zero(self):
        assert add(5, 0) == 5
```

### Unit Test Structure
For each operation (add, subtract, multiply, divide):
- [ ] Test positive numbers
- [ ] Test negative numbers
- [ ] Test mixed signs (positive + negative)
- [ ] Test floats/decimals
- [ ] Test edge cases:
  - [ ] Zero values
  - [ ] Large numbers
  - [ ] Very small decimals
  - [ ] Division by zero (divide operation only)

### Running Unit Tests
```bash
python3 -m pytest tests/test_*_unit.py -v --tb=short
```

**Expected Output**:
```
tests/test_add_unit.py::TestAdd::test_add_positive_integers PASSED
tests/test_add_unit.py::TestAdd::test_add_negative_integers PASSED
...
======================== 20+ passed in 0.50s ========================
```

### Quality Gate
- ✅ 5+ unit tests per operation
- ✅ Tests pass: `pytest tests/test_*_unit.py -v`
- ✅ All test names descriptive
- ✅ Edge cases covered

---

## Phase 5: API Tests (Week 2-3)

### Objective
Create API endpoint tests using TestClient (5+ per endpoint, 20+ total).

### API Test Requirements
- **Framework**: pytest + FastAPI TestClient
- **Location**: tests/test_*_api.py
- **Tests per endpoint**: 5+
- **Coverage**: Positive, negative, edge cases, HTTP status codes

### API Test Structure (tests/test_add_api.py)
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAddAPI:
    def test_add_api_positive(self):
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_api_negative(self):
        response = client.get("/add?num1=-5&num2=-3")
        assert response.status_code == 200
        assert response.json() == {"result": -8}

    def test_add_api_missing_params(self):
        response = client.get("/add?num1=5")
        assert response.status_code == 422  # Unprocessable Entity

    def test_add_api_invalid_input(self):
        response = client.get("/add?num1=abc&num2=3")
        assert response.status_code == 422

    def test_add_api_floats(self):
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(8.7)
```

### API Test Coverage
For each endpoint (/add, /subtract, /multiply, /divide):
- [ ] Positive case (valid inputs, success)
- [ ] Negative numbers
- [ ] Floats/decimals
- [ ] Missing parameters (400 Bad Request)
- [ ] Invalid input types (422 Unprocessable Entity)
- [ ] Special cases (0, very large numbers)
- [ ] Division by zero (divide endpoint only)

### Running API Tests
```bash
python3 -m pytest tests/test_*_api.py -v --tb=short
```

### HTTP Status Codes
- **200 OK**: Valid request, successful calculation
- **400 Bad Request**: Division by zero, missing required parameter
- **422 Unprocessable Entity**: Invalid parameter type (e.g., "abc" for number)
- **500 Internal Server Error**: Unexpected error in calculation

### Quality Gate
- ✅ 5+ API tests per endpoint
- ✅ Tests pass: `pytest tests/test_*_api.py -v`
- ✅ HTTP status codes validated
- ✅ Response format validated (JSON with "result")
- ✅ All test names descriptive

---

## Phase 6: Regression Suite & Coverage (Week 3)

### Objective
Create comprehensive regression test suite with 100% coverage.

### Regression Test Suite (tests/test_regression.py)
```python
import subprocess
import sys

def test_regression_all_unit_tests():
    """Run all unit tests"""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_*_unit.py", "-v"],
        capture_output=True
    )
    assert result.returncode == 0, "Unit tests failed"

def test_regression_all_api_tests():
    """Run all API tests"""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_*_api.py", "-v"],
        capture_output=True
    )
    assert result.returncode == 0, "API tests failed"

def test_regression_coverage():
    """Run coverage check"""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "--cov=.", "--cov-report=term-missing"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Coverage check failed:\n{result.stdout}"
    assert "100%" in result.stdout or "95%" in result.stdout, "Coverage too low"
```

### Running Regression Suite
```bash
python3 -m pytest tests/test_regression.py -v
# or run all tests with coverage
python3 -m pytest tests/ -v --cov=. --cov-report=term-missing
```

**Expected Output**:
```
tests/test_add_unit.py::TestAdd::test_add_positive_integers PASSED
tests/test_add_api.py::TestAddAPI::test_add_api_positive PASSED
...
======================== 25 passed in 1.50s ========================
Name                  Stmts   Miss  Cover
routes/add.py            10      0   100%
routes/subtract.py       10      0   100%
routes/multiply.py       10      0   100%
routes/divide.py         15      0   100%
main.py                  20      0   100%
TOTAL                    65      0   100%
```

### Coverage Requirements
- **Target**: 100% coverage or minimum 95%
- **Files to cover**: main.py, routes/*.py
- **Exclude**: __init__.py, tests/

### Quality Gate
- ✅ All unit tests pass
- ✅ All API tests pass
- ✅ Coverage: 100% (or minimum 95%)
- ✅ Regression suite: `pytest tests/test_regression.py -v` passes

---

## Phase 7: Code Quality & Documentation (Week 3-4)

### Objective
Ensure PEP8 compliance, type hints, docstrings, and documentation.

### PEP8 Compliance
```bash
autopep8 --diff --aggressive --aggressive .
# or
python3 -m flake8 . --max-line-length=100
```

Requirements:
- [ ] Line length: max 100 characters
- [ ] Proper spacing (2 blank lines between functions)
- [ ] Imports organized (standard lib, third-party, local)
- [ ] Consistent indentation (4 spaces)
- [ ] No trailing whitespace

### Type Hints
Every function must have type hints:
```python
def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Add two numbers"""
    return num1 + num2
```

- [ ] All parameters typed
- [ ] Return type specified
- [ ] Use Union for multiple types
- [ ] Use Optional[Type] for optional parameters

### Docstrings
Every function must have docstrings (Google style):
```python
def add(num1: float, num2: float) -> float:
    """
    Add two numbers.

    Args:
        num1: First number to add.
        num2: Second number to add.

    Returns:
        Sum of num1 and num2.

    Examples:
        >>> add(5, 3)
        8
    """
    return num1 + num2
```

### README Documentation
Create backend/README.md with:
- [ ] Setup instructions (venv, pip install)
- [ ] Startup command (python3 main.py)
- [ ] Endpoint documentation (path, params, response)
- [ ] Error codes (400, 422, 500)
- [ ] Testing instructions (pytest, coverage)
- [ ] Example requests (curl)

### Quality Gate
- ✅ PEP8 compliant (autopep8 --diff clean)
- ✅ Type hints on all functions
- ✅ Docstrings on all functions
- ✅ README.md complete
- ✅ No hardcoded ports/localhost

---

## Phase 8: Orchestration & Final Verification (Week 4)

### Objective
Verify backend works in Docker and complete integration testing.

### Docker Build
```bash
docker build -t backend:latest .
```

- [ ] Dockerfile exists (see CREATE.md)
- [ ] Build succeeds
- [ ] Image size reasonable (< 300MB)

### Docker Run
```bash
docker run -p 8004:8004 -e CORS_ORIGINS="http://localhost:3004" backend:latest
```

- [ ] Container starts
- [ ] Server listens on port 8004
- [ ] Health check responds: `curl http://localhost:8004/health`

### REGRESSION.md Compliance
Before submitting PR, verify:
- [ ] Phase 1: Local dev setup complete
- [ ] Phase 2: CORS validated (curl with Origin header)
- [ ] Phase 3: All tests pass (unit + API)
- [ ] Phase 4: Docker compose works
- [ ] Phase 5: Code quality passes
- [ ] Phase 6: Git history clean

### Final Checklist
- [ ] All phases complete
- [ ] All tests pass: `pytest tests/ -v --cov=. --cov-report=term`
- [ ] Coverage: 100% (or 95%+)
- [ ] PEP8 compliant
- [ ] Type hints on all functions
- [ ] Docstrings on all functions
- [ ] README.md complete
- [ ] No hardcoded ports/localhost
- [ ] CORS middleware configured
- [ ] /health endpoint working

### Quality Gate
- ✅ All tests pass (100% coverage)
- ✅ PEP8 compliant
- ✅ Type hints + docstrings
- ✅ Docker builds successfully
- ✅ REGRESSION.md passes

---

## Parallelization Strategy

### Testing Parallelization
When running tests, spawn independently:
- Unit tests: `pytest tests/test_*_unit.py`
- API tests: `pytest tests/test_*_api.py`
- Coverage: `pytest tests/ --cov=.`

**Do NOT run sequentially** — use pytest-xdist for parallel execution:
```bash
pip install pytest-xdist
pytest tests/ -n auto  # auto-detect CPU count
```

### Development Workflow
Run in parallel:
- Code changes in editor
- Linting: `autopep8 --check .` (background)
- Tests: `pytest tests/ --watch` (background)
- Coverage: `pytest tests/ --cov=.` (background)

---

## Directory Structure

```
backend/
├── main.py                 # FastAPI app + CORS middleware + routers
├── routes/
│   ├── __init__.py
│   ├── add.py             # /add endpoint (5 lines)
│   ├── subtract.py        # /subtract endpoint
│   ├── multiply.py        # /multiply endpoint
│   └── divide.py          # /divide endpoint + error handling
├── tests/
│   ├── test_add_unit.py   # 5+ tests
│   ├── test_add_api.py    # 5+ tests
│   ├── test_subtract_unit.py
│   ├── test_subtract_api.py
│   ├── test_multiply_unit.py
│   ├── test_multiply_api.py
│   ├── test_divide_unit.py
│   ├── test_divide_api.py
│   └── test_regression.py # All tests + coverage
├── requirements.txt        # Only: fastapi, uvicorn
├── Dockerfile             # Python 3.11-slim (see CREATE.md)
├── README.md              # Setup + endpoint documentation
└── .gitignore             # venv/, __pycache__/, .pytest_cache/
```

---

## Environment Variables

### CORS_ORIGINS
```
CORS_ORIGINS=http://localhost:3004,http://frontend:3004
```

Used in main.py to configure CORSMiddleware.

### How It's Used
```python
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3004,http://frontend:3004").split(",")
```

---

## Troubleshooting

### Tests Failing
```bash
pytest tests/ -v --tb=short  # See detailed error
```
- Check division by zero handling
- Verify type hints are correct
- Check test data is valid

### CORS Issues
```bash
curl -i -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
```
- Verify CORS middleware is configured in main.py
- Check CORS_ORIGINS environment variable
- Verify frontend origin is in allowed_origins list

### Import Errors
```bash
python3 -c "from routes import add"  # Test import
```
- Ensure routes/ has __init__.py
- Check route names match imports in main.py

---

## References
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- pytest: https://docs.pytest.org/
- PEP8: https://www.python.org/dev/peps/pep-0008/
- CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
