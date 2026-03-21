# Backend Development - 8 Phase Checklist

**For**: @Python FastAPI Specialist agent
**Location**: `/backend` | **Port**: 8004 | **Stack**: Python/FastAPI
**Dependencies**: ZERO external (stdlib + FastAPI only) | **Auth**: None | **Coverage**: 100% unit + API tests required

**Hooks Active**: Python auto-format on creation
**Skill**: `/fastapi-validator` (run after each phase)
**Duration**: 2-3 hours | **Must Complete**: All 8 phases sequentially

---

## 🎯 Mission

Build a fully-tested FastAPI backend. 4 endpoints (add/subtract/multiply/divide) in separate files. Zero external dependencies. 100% test coverage. PEP8 compliant.

---

## 📋 Execution: 8 Phases

### Phase 1: Project Setup ✅ Must Complete
- [ ] Create backend directory structure:
  ```
  backend/
  ├── main.py               (FastAPI app entry)
  ├── routes/              (endpoint modules)
  │   ├── add.py
  │   ├── subtract.py
  │   ├── multiply.py
  │   └── divide.py
  ├── tests/               (test suite)
  │   ├── unit/           (function tests)
  │   │   ├── test_add.py
  │   │   ├── test_subtract.py
  │   │   ├── test_multiply.py
  │   │   └── test_divide.py
  │   ├── api/            (endpoint tests)
  │   │   ├── test_add_endpoint.py
  │   │   ├── test_subtract_endpoint.py
  │   │   ├── test_multiply_endpoint.py
  │   │   └── test_divide_endpoint.py
  │   └── conftest.py      (pytest config)
  ├── requirements.txt     (only: fastapi, uvicorn)
  ├── .env                 (env vars if needed)
  └── README.md
  ```
- [ ] Create `requirements.txt`:
  ```
  fastapi==0.104.1
  uvicorn==0.24.0
  ```
- [ ] Run: `pip install -r requirements.txt`
- [ ] Test install: `python main.py` (should start on 8004)

**Validation**: Use `/fastapi-validator` after setup

---

### Phase 2: Main App Setup ✅ Must Complete
- [ ] Create `main.py`:
  ```python
  from fastapi import FastAPI
  from fastapi.middleware.cors import CORSMiddleware
  from routes import add, subtract, multiply, divide

  app = FastAPI(title="Calculator API", version="1.0.0")

  # Enable CORS for frontend
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],  # In production, use ["http://localhost:3004"]
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  # Include routers
  app.include_router(add.router)
  app.include_router(subtract.router)
  app.include_router(multiply.router)
  app.include_router(divide.router)

  @app.get("/health")
  async def health():
      return {"status": "ok"}

  @app.get("/")
  async def root():
      return {"message": "Calculator API", "endpoints": ["/add", "/subtract", "/multiply", "/divide"]}

  if __name__ == "__main__":
      import uvicorn
      uvicorn.run(app, host="0.0.0.0", port=8004)
  ```
- [ ] Create `routes/__init__.py` (empty file)
- [ ] Run: `python main.py` (verify starts on 8004)
- [ ] Test: `curl http://localhost:8004/health`

**Validation**: Use `/fastapi-validator` after setup

---

### Phase 3: Create Routes ✅ Must Complete

#### Add Endpoint (`routes/add.py`)
- [ ] Create endpoint: `GET /add?num1=X&num2=Y`
- [ ] Return: `{"result": Z}`
- [ ] Handle: decimal numbers, negative numbers
- [ ] Error: missing parameters return 422

#### Subtract Endpoint (`routes/subtract.py`)
- [ ] Create endpoint: `GET /subtract?num1=X&num2=Y`
- [ ] Return: `{"result": Z}`
- [ ] Handle: decimal numbers, negative numbers
- [ ] Error: missing parameters return 422

#### Multiply Endpoint (`routes/multiply.py`)
- [ ] Create endpoint: `GET /multiply?num1=X&num2=Y`
- [ ] Return: `{"result": Z}`
- [ ] Handle: decimal numbers, very large numbers
- [ ] Error: missing parameters return 422

#### Divide Endpoint (`routes/divide.py`)
- [ ] Create endpoint: `GET /divide?num1=X&num2=Y`
- [ ] Return: `{"result": Z}` OR error if dividing by zero
- [ ] Handle: decimal numbers, return float result
- [ ] Error: missing parameters return 422
- [ ] Error: division by zero return 400 with message

**Each route file template**:
```python
from fastapi import APIRouter, HTTPException, Query
from typing import Union

router = APIRouter()

def operation(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Perform operation on two numbers."""
    return num1 + num2  # Replace with actual operation

@router.get("/add")
async def add_numbers(num1: float = Query(...), num2: float = Query(...)):
    """Add two numbers."""
    try:
        result = operation(num1, num2)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

**Validation**: Use `/fastapi-validator` after routes

---

### Phase 4: Write Unit Tests ✅ Must Complete

Create `tests/unit/test_*.py` files testing each operation function directly.

**Template for `tests/unit/test_add.py`**:
```python
import pytest
from routes.add import operation

def test_add_positive_integers():
    assert operation(5, 3) == 8

def test_add_negative_numbers():
    assert operation(-5, 3) == -2

def test_add_decimals():
    assert operation(2.5, 1.5) == 4.0

def test_add_zero():
    assert operation(0, 0) == 0

def test_add_large_numbers():
    assert operation(999999, 1) == 1000000

# Create 3+ tests per function covering normal, edge, and error cases
```

**Requirements**:
- [ ] Each operation has `test_add.py`, `test_subtract.py`, `test_multiply.py`, `test_divide.py`
- [ ] Each test file has minimum 5 test cases
- [ ] Cover: positive, negative, zero, decimal, large numbers
- [ ] Run: `pytest tests/unit/` (all pass)
- [ ] Coverage: 100% of functions

**Validation**: Use `/fastapi-validator` after unit tests

---

### Phase 5: Write API Tests ✅ Must Complete

Create `tests/api/test_*_endpoint.py` files testing each endpoint via HTTP.

**Template for `tests/api/test_add_endpoint.py`**:
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_endpoint_valid():
    response = client.get("/add?num1=5&num2=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_add_endpoint_missing_param():
    response = client.get("/add?num1=5")
    assert response.status_code == 422  # Unprocessable entity

def test_add_endpoint_invalid_type():
    response = client.get("/add?num1=abc&num2=5")
    assert response.status_code == 422

def test_add_endpoint_decimals():
    response = client.get("/add?num1=2.5&num2=1.5")
    assert response.status_code == 200
    assert response.json()["result"] == 4.0

# Add tests for edge cases and error scenarios
```

**Requirements**:
- [ ] Each endpoint has test file: `test_add_endpoint.py`, etc.
- [ ] Test files in `tests/api/`
- [ ] Each test file has minimum 5 test cases
- [ ] Cover: valid inputs, missing params, invalid types, decimals, edge cases
- [ ] For divide: test division by zero (expect 400 error)
- [ ] Run: `pytest tests/api/` (all pass)
- [ ] Response format validated: `{"result": number}`

**Validation**: Use `/fastapi-validator` after API tests

---

### Phase 6: Regression Test Suite ✅ Must Complete
- [ ] Create `tests/conftest.py` (pytest configuration):
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from main import app

  @pytest.fixture
  def client():
      return TestClient(app)
  ```
- [ ] Run full suite: `pytest tests/` (runs both unit and api tests)
- [ ] All tests pass: ✅
- [ ] Coverage report: `pytest --cov=routes tests/`
- [ ] Target: 100% code coverage

**Validation**: Use `/fastapi-validator` for coverage check

---

### Phase 7: Code Quality & PEP8 ✅ Must Complete
- [ ] Check PEP8: `python -m pycodestyle routes/ main.py`
- [ ] Check imports: All files only import stdlib and fastapi
- [ ] Add docstrings to all functions and endpoints
- [ ] Add type hints to all function parameters and returns
- [ ] Use snake_case for functions and variables
- [ ] Use UPPER_CASE for constants
- [ ] No unused imports or variables
- [ ] Lines ≤ 79 characters (or ≤ 99 with config)
- [ ] Auto-format: `autopep8 --in-place -r routes/ main.py`

**Example function with proper formatting**:
```python
def divide(num1: float, num2: float) -> float:
    """
    Divide num1 by num2.

    Args:
        num1: Dividend
        num2: Divisor

    Returns:
        float: Result of division

    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
```

**Validation**: Use `/fastapi-validator` and `/code-review`

---

### Phase 8: Documentation ✅ Must Complete
- [ ] Create `README.md`:
  ```markdown
  # Backend - Stranger Things Calculator

  ## Setup
  pip install -r requirements.txt

  ## Run
  python main.py

  ## Test
  pytest tests/unit/              # Unit tests
  pytest tests/api/               # API tests
  pytest tests/                   # Full suite

  ## Endpoints
  - GET /add?num1=X&num2=Y
  - GET /subtract?num1=X&num2=Y
  - GET /multiply?num1=X&num2=Y
  - GET /divide?num1=X&num2=Y

  ## Response Format
  {"result": number}

  ## Error Response
  {"detail": "error message"}
  ```
- [ ] Document each endpoint in code
- [ ] Add architecture notes to README

**Validation**: Documentation complete

---

## 🚀 Quick Commands

```bash
# Setup
pip install -r requirements.txt

# Run
python main.py                  # Start on 8004

# Test
pytest tests/                   # Run all tests
pytest tests/unit/              # Run unit tests only
pytest tests/api/               # Run API tests only
pytest --cov=routes tests/      # Coverage report

# Code Quality
python -m pycodestyle routes/ main.py     # Check PEP8
autopep8 --in-place -r routes/ main.py   # Auto-format (via hook)
```

---

## ✅ Work Completion Checklist

Before marking backend as DONE, verify ALL of these:

- [ ] **Phase 1 Complete**: Project setup with proper structure
- [ ] **Phase 2 Complete**: `main.py` runs on port 8004
- [ ] **Phase 3 Complete**: All 4 routes created and working
- [ ] **Phase 4 Complete**: Unit tests written for all functions
- [ ] **Phase 5 Complete**: API tests written for all endpoints
- [ ] **Phase 6 Complete**: Regression suite runs: `pytest tests/` ✅
- [ ] **Phase 7 Complete**: PEP8 compliant, no `any` types
- [ ] **Phase 8 Complete**: README.md and documentation done
- [ ] **Skills**: Passed `/fastapi-validator`
- [ ] **Tests**: `pytest tests/` shows 100% pass rate ✅
- [ ] **Coverage**: `pytest --cov=routes tests/` shows 100% ✅
- [ ] **Code**: No console errors or warnings
- [ ] **Requirements**: Only fastapi and uvicorn in requirements.txt
- [ ] **API**: All endpoints return correct format: `{"result": number}`
- [ ] **Errors**: Division by zero handled (returns 400)

---

## 🛠️ Tools & Skills Available

| Tool | Use Case |
|------|----------|
| `/fastapi-validator` | Validate PEP8, routes, test coverage |
| `/code-review` | Code quality and best practices |
| `autopep8` | Auto-format Python (automatic via hook) |
| `pytest` | Unit and API testing |
| `python -m pycodestyle` | PEP8 compliance checking |

---

## ⚠️ Critical Requirements (DO NOT SKIP)

1. **ZERO EXTERNAL DEPS** - Only FastAPI, no requests/numpy/etc
2. **SEPARATE FILES** - Each operation in its own file in `routes/`
3. **NO AUTH** - Public endpoints, no authentication
4. **FULL TESTING** - Unit + API tests, 100% coverage
5. **PEP8** - Strict compliance, auto-formatted
6. **TYPE HINTS** - Full typing, no `any`
7. **ERROR HANDLING** - Proper HTTP status codes and messages
8. **EDGE CASES** - Division by zero, invalid inputs, decimals
9. **CORS** - Enabled for frontend on port 3004
10. **PORT 8004** - Must listen on 0.0.0.0:8004 for Docker

---

## 🔍 Validation Workflow

```
1. Write/modify code
   ↓
2. Run: python main.py (check starts)
   ↓
3. Use: /fastapi-validator (check compliance)
   ↓
4. Run: pytest tests/ (check all tests pass)
   ↓
5. Use: /code-review (check quality)
   ↓
6. Fix any issues found
   ↓
7. Commit with message: "feat(backend): [description]"
```

---

## 📞 When Stuck

**Use these skills in order**:
1. `/fastapi-validator` - Diagnose what's wrong
2. `/code-review` - Identify code issues
3. `/plan` - Redesign approach if needed

---

**Remember**: Each phase MUST be completed and validated before moving to the next. No skipping!
