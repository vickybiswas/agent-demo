# Backend Development Guide - Stranger Things Calculator

8-phase guide for building the FastAPI Python backend.

## Overview
- **Tech Stack**: FastAPI, Python 3.11+, Uvicorn
- **Port**: 8004 (Docker)
- **Endpoints**: /add, /subtract, /multiply, /divide (no external libraries)
- **Testing**: pytest (unit + API tests)
- **Standards**: PEP8, type hints, 100% coverage

## Phase 1: Setup

**Duration**: ~30 mins
**Deliverables**: Project structure, dependencies, Python environment

### Tasks

1. Create project structure
   ```
   backend/
   ├── main.py               # FastAPI app initialization
   ├── requirements.txt      # Dependencies (fastapi, uvicorn ONLY)
   ├── routes/
   │   ├── __init__.py
   │   ├── add.py           # Addition endpoint
   │   ├── subtract.py      # Subtraction endpoint
   │   ├── multiply.py      # Multiplication endpoint
   │   └── divide.py        # Division endpoint
   ├── tests/
   │   ├── __init__.py
   │   ├── test_units.py    # Unit tests
   │   └── test_api.py      # API tests
   └── .env                 # Environment variables
   ```

2. Create `requirements.txt`
   ```
   fastapi==0.104.1
   uvicorn[standard]==0.24.0
   ```

3. Create Python virtual environment
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install pytest httpx  # for testing
   ```

4. Create `.env`
   ```
   DEBUG=True
   PORT=8004
   ```

5. Create `main.py` (empty FastAPI app, will fill in Phase 2)
   ```python
   from fastapi import FastAPI

   app = FastAPI()
   ```

**Quality Gate**: Dependencies installed, project structure created, Python 3.11+

---

## Phase 2: Main App

**Duration**: ~30 mins
**Deliverables**: FastAPI instance, CORS, health endpoint, app structure

### Tasks

1. **Create main.py** (Complete)
   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   from routes import add, subtract, multiply, divide

   app = FastAPI(
       title="Stranger Things Calculator",
       description="A simple calculator API for the Stranger Things theme",
       version="1.0.0"
   )

   # Add CORS middleware
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:3004", "http://frontend:3004"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

   # Health check endpoint
   @app.get("/health")
   async def health():
       """Health check endpoint for Docker container."""
       return {"status": "ok"}

   # Include route handlers
   app.include_router(add.router)
   app.include_router(subtract.router)
   app.include_router(multiply.router)
   app.include_router(divide.router)

   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8004)
   ```

2. **Configure CORS properly**
   - Allow frontend URL (localhost:3004 for dev, frontend:3004 for Docker)
   - Allow credentials if needed
   - Allow all standard HTTP methods

3. **Add type hints everywhere**
   - Function parameters and return types
   - Docstrings for all functions

**Quality Gate**: `uvicorn main:app --reload` starts on port 8004, /health returns 200

---

## Phase 3: Routes

**Duration**: ~1 hour
**Deliverables**: Four separate route files, each implementing one operation

### Tasks

1. **Create routes/__init__.py**
   ```python
   from . import add, subtract, multiply, divide
   ```

2. **Create routes/add.py**
   ```python
   from fastapi import APIRouter
   from typing import Union

   router = APIRouter()

   @router.get("/add")
   async def add_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
       """
       Add two numbers.

       Args:
           num1: First number
           num2: Second number

       Returns:
           Dictionary with result
       """
       result = num1 + num2
       return {"result": result, "operation": "add"}
   ```

3. **Create routes/subtract.py**
   ```python
   from fastapi import APIRouter
   from typing import Union

   router = APIRouter()

   @router.get("/subtract")
   async def subtract_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
       """Subtract two numbers."""
       result = num1 - num2
       return {"result": result, "operation": "subtract"}
   ```

4. **Create routes/multiply.py**
   ```python
   from fastapi import APIRouter
   from typing import Union

   router = APIRouter()

   @router.get("/multiply")
   async def multiply_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
       """Multiply two numbers."""
       result = num1 * num2
       return {"result": result, "operation": "multiply"}
   ```

5. **Create routes/divide.py**
   ```python
   from fastapi import APIRouter, HTTPException
   from typing import Union

   router = APIRouter()

   @router.get("/divide")
   async def divide_numbers(num1: Union[int, float], num2: Union[int, float]) -> dict:
       """Divide two numbers. Raises error if dividing by zero."""
       if num2 == 0:
           raise HTTPException(status_code=400, detail="Cannot divide by zero")
       result = num1 / num2
       return {"result": result, "operation": "divide"}
   ```

**Requirements**:
- Each route in separate file
- Type hints on all parameters
- Docstrings for all functions
- Error handling (divide by zero)
- Consistent response format

**Quality Gate**: All endpoints work, curl http://localhost:8004/add?num1=5&num2=3 returns {"result": 8}

---

## Phase 4: Unit Tests

**Duration**: ~1 hour
**Deliverables**: pytest unit tests for all operations

### Tasks

1. **Create tests/test_units.py**
   ```python
   import pytest

   # Test addition
   def test_add_positive():
       """Test addition of positive numbers."""
       assert 5 + 3 == 8

   def test_add_negative():
       """Test addition with negative numbers."""
       assert -5 + 3 == -2

   def test_add_zero():
       """Test addition with zero."""
       assert 5 + 0 == 5

   def test_add_floats():
       """Test addition with decimal numbers."""
       assert 5.5 + 3.2 == 8.7

   def test_add_large_numbers():
       """Test addition with large numbers."""
       assert 999999 + 1 == 1000000

   # Test subtraction (5+ tests)
   def test_subtract_positive():
       assert 5 - 3 == 2

   def test_subtract_negative():
       assert 5 - (-3) == 8

   def test_subtract_zero():
       assert 5 - 0 == 5

   def test_subtract_floats():
       assert 5.5 - 3.2 == 2.3

   def test_subtract_large():
       assert 1000000 - 1 == 999999

   # Test multiplication (5+ tests)
   def test_multiply_positive():
       assert 5 * 3 == 15

   def test_multiply_negative():
       assert -5 * 3 == -15

   def test_multiply_zero():
       assert 5 * 0 == 0

   def test_multiply_floats():
       assert 2.5 * 4 == 10.0

   def test_multiply_large():
       assert 1000 * 1000 == 1000000

   # Test division (5+ tests)
   def test_divide_positive():
       assert 6 / 2 == 3

   def test_divide_negative():
       assert -6 / 2 == -3

   def test_divide_floats():
       assert 7.5 / 2.5 == 3

   def test_divide_by_zero():
       with pytest.raises(ZeroDivisionError):
           6 / 0

   def test_divide_remainder():
       assert 7 / 2 == 3.5
   ```

2. Run tests
   ```bash
   pytest tests/test_units.py -v
   ```

**Requirements**:
- Minimum 5 tests per operation
- Cover: positive, negative, zero, edge cases
- Use pytest assertions
- Document each test with docstring

**Quality Gate**: All unit tests pass (`pytest tests/test_units.py` returns 0 failures)

---

## Phase 5: API Tests

**Duration**: ~1 hour
**Deliverables**: pytest API tests for endpoint behavior

### Tasks

1. **Create tests/test_api.py**
   ```python
   import pytest
   from fastapi.testclient import TestClient
   from main import app

   client = TestClient(app)

   # Test health endpoint
   def test_health():
       response = client.get("/health")
       assert response.status_code == 200
       assert response.json() == {"status": "ok"}

   # Test add endpoint (5+ scenarios)
   def test_add_success():
       response = client.get("/add?num1=5&num2=3")
       assert response.status_code == 200
       assert response.json()["result"] == 8

   def test_add_floats():
       response = client.get("/add?num1=5.5&num2=3.2")
       assert response.status_code == 200
       assert response.json()["result"] == 8.7

   def test_add_negative():
       response = client.get("/add?num1=-5&num2=3")
       assert response.status_code == 200
       assert response.json()["result"] == -2

   def test_add_missing_param():
       response = client.get("/add?num1=5")
       assert response.status_code == 422  # Unprocessable Entity

   def test_add_invalid_param():
       response = client.get("/add?num1=abc&num2=3")
       assert response.status_code == 422

   # Test subtract endpoint (5+ scenarios)
   def test_subtract_success():
       response = client.get("/subtract?num1=5&num2=3")
       assert response.status_code == 200
       assert response.json()["result"] == 2

   # ... more subtract tests

   # Test multiply endpoint (5+ scenarios)
   def test_multiply_success():
       response = client.get("/multiply?num1=5&num2=3")
       assert response.status_code == 200
       assert response.json()["result"] == 15

   # ... more multiply tests

   # Test divide endpoint (5+ scenarios)
   def test_divide_success():
       response = client.get("/divide?num1=6&num2=2")
       assert response.status_code == 200
       assert response.json()["result"] == 3

   def test_divide_by_zero():
       response = client.get("/divide?num1=6&num2=0")
       assert response.status_code == 400
       assert "Cannot divide by zero" in response.json()["detail"]

   # ... more divide tests

   # Test response schema
   def test_response_schema():
       response = client.get("/add?num1=5&num2=3")
       data = response.json()
       assert "result" in data
       assert "operation" in data
   ```

2. Run tests
   ```bash
   pytest tests/test_api.py -v
   ```

**Requirements**:
- Minimum 5 tests per endpoint
- Test success cases (HTTP 200)
- Test error cases (HTTP 400, 422)
- Verify response schema
- Use TestClient for HTTP testing

**Quality Gate**: All API tests pass (`pytest tests/test_api.py` returns 0 failures)

---

## Phase 6: Regression Suite

**Duration**: ~30 mins
**Deliverables**: Full test suite with coverage report

### Tasks

1. **Run all tests**
   ```bash
   pytest tests/ -v --cov=. --cov-report=html
   ```

2. **Check coverage**
   ```bash
   # Coverage should be 100%
   # All routes, all operations, all edge cases covered
   ```

3. **Create pytest.ini**
   ```ini
   [pytest]
   testpaths = tests
   python_files = test_*.py
   python_classes = Test*
   python_functions = test_*
   ```

**Quality Gate**: 100% code coverage, all tests passing

---

## Phase 7: Code Quality

**Duration**: ~30 mins
**Deliverables**: PEP8 compliance, type hints, docstrings

### Tasks

1. **PEP8 check**
   ```bash
   pip install autopep8
   autopep8 --check -r .
   # Fix with: autopep8 --in-place -r .
   ```

2. **Add type hints**
   - All function parameters
   - All return types
   - Use Union, Optional from typing

3. **Add docstrings**
   - All functions
   - All classes
   - Module-level docstring in main.py

4. **Run static type checking** (optional)
   ```bash
   pip install mypy
   mypy .
   ```

**Quality Gate**: PEP8 compliant, no type issues, docstrings on all functions

---

## Phase 8: Documentation

**Duration**: ~30 mins
**Deliverables**: README, API docs, endpoint reference

### Tasks

1. **Create README.md**
   ```markdown
   # Stranger Things Calculator API

   FastAPI backend for calculator operations.

   ## Setup
   ```bash
   pip install -r requirements.txt
   ```

   ## Running
   ```bash
   uvicorn main:app --reload
   ```

   ## Endpoints
   - GET /add?num1=X&num2=Y
   - GET /subtract?num1=X&num2=Y
   - GET /multiply?num1=X&num2=Y
   - GET /divide?num1=X&num2=Y

   ## Testing
   ```bash
   pytest tests/ -v
   ```
   ```

2. **API Documentation** (Auto-generated by FastAPI)
   - Available at http://localhost:8004/docs (Swagger UI)
   - Available at http://localhost:8004/redoc (ReDoc)

3. **Create ENDPOINTS.md**
   ```markdown
   ## /add
   - Parameters: num1 (float), num2 (float)
   - Returns: {"result": float, "operation": "add"}
   - Example: /add?num1=5&num2=3 → {"result": 8}

   ## /subtract
   - Parameters: num1 (float), num2 (float)
   - Returns: {"result": float, "operation": "subtract"}

   ## /multiply
   - Parameters: num1 (float), num2 (float)
   - Returns: {"result": float, "operation": "multiply"}

   ## /divide
   - Parameters: num1 (float), num2 (float)
   - Returns: {"result": float, "operation": "divide"}
   - Error: HTTP 400 if num2 == 0
   ```

**Quality Gate**: README complete, API docs available, endpoints documented

---

## Success Checklist
- ✅ FastAPI app created (main.py)
- ✅ CORS configured for frontend
- ✅ Routes in separate files
- ✅ All endpoints working
- ✅ Unit tests: 5+ per operation (20+ total)
- ✅ API tests: 5+ per endpoint (20+ total)
- ✅ Regression suite: 100% coverage
- ✅ PEP8 compliant
- ✅ Type hints on all functions
- ✅ Docstrings on all functions
- ✅ No external dependencies (only fastapi, uvicorn)
- ✅ fastapi-validator approves
- ✅ Ready for Docker Phase 3

## Notes
- Zero external dependencies: Only fastapi and uvicorn
- Type hints: Use Union for int/float, Optional for nullable
- Error handling: Divide by zero → HTTP 400
- CORS: Allow frontend to call backend
- Testing: 100% coverage mandatory
