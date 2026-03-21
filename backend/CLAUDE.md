# Backend Implementation Guide (8 Phases)

Build a FastAPI backend for the Stranger Things calculator with comprehensive testing and PEP8 compliance.

## Phase 1: Project Setup & Dependencies

Initialize FastAPI project with minimal dependencies.

### Deliverables
- `backend/` directory structure created
- `requirements.txt` with ONLY: fastapi, uvicorn
- Python 3.11+ virtual environment
- No external libraries (no pandas, numpy, requests, etc.)
- `Dockerfile` created for containerization

### Directory Structure
```
backend/
├── main.py                 # FastAPI app instance
├── routes/
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
│   ├── test_divide_api.py
│   └── test_coverage.py
├── requirements.txt        # ONLY: fastapi, uvicorn
├── Dockerfile
└── .dockerignore
```

### `requirements.txt`
```
fastapi==0.104.0
uvicorn[standard]==0.24.0
pytest==7.4.0
pytest-cov==4.1.0
httpx==0.25.0
```

### Quality Gate ✅
- `requirements.txt` contains ONLY fastapi + uvicorn (+ testing deps)
- No external math/calculation libraries
- Virtual environment created: `python -m venv venv`
- Dependencies installed: `pip install -r requirements.txt`

---

## Phase 2: FastAPI App Setup & CORS Middleware

Create FastAPI application with proper CORS configuration.

### Deliverables
- `main.py` with FastAPI app instance
- CORS middleware configured (allow all origins for now, can restrict later)
- `/health` or root endpoint for health checks
- Proper app startup/shutdown logging
- All routes imported from separate files

### `main.py` Template
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import add, subtract, multiply, divide

app = FastAPI(
    title="Stranger Things Calculator",
    description="A retro-themed calculator API",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health():
    """Health check endpoint."""
    return {"status": "ok"}

# Include route modules
app.include_router(add.router)
app.include_router(subtract.router)
app.include_router(multiply.router)
app.include_router(divide.router)

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {"message": "Stranger Things Calculator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004, reload=True)
```

### CORS Headers Validation
When frontend requests from `http://localhost:3004`:
- Request: `Origin: http://localhost:3004`
- Response includes:
  - `Access-Control-Allow-Origin: *` (or specific origin)
  - `Access-Control-Allow-Methods: GET, POST, OPTIONS`
  - `Access-Control-Allow-Credentials: true`

### Health Check
```bash
curl http://localhost:8004/health
# Expected: {"status": "ok"}
```

### Quality Gate ✅
- App starts without errors: `python main.py` listens on 8004
- Health endpoint responds: `curl http://localhost:8004/health` returns 200
- CORS headers present: `curl -H "Origin: http://localhost:3004" ...` shows CORS headers
- Root endpoint responds: `curl http://localhost:8004/` returns 200

---

## Phase 3: Separate Route Files (add, subtract, multiply, divide)

Create route functions in separate files, each imported into main.py.

### Deliverables
- `routes/add.py` - Addition operation
- `routes/subtract.py` - Subtraction operation
- `routes/multiply.py` - Multiplication operation
- `routes/divide.py` - Division operation
- Each route file has: function, endpoint, type hints, docstring
- All routes imported and included in main.py

### `routes/add.py` Template
```python
from fastapi import APIRouter

router = APIRouter()

def add_numbers(num1: float, num2: float) -> float:
    """Add two numbers.

    Args:
        num1: First number
        num2: Second number

    Returns:
        Sum of num1 and num2
    """
    return num1 + num2

@router.get("/add", tags=["Operations"])
async def add(num1: float, num2: float):
    """Add two numbers.

    Args:
        num1: First number (query param)
        num2: Second number (query param)

    Returns:
        JSON object with result key
    """
    result = add_numbers(num1, num2)
    return {"result": result}
```

### `routes/divide.py` (with error handling)
```python
from fastapi import APIRouter, HTTPException

router = APIRouter()

def divide_numbers(num1: float, num2: float) -> float:
    """Divide two numbers.

    Args:
        num1: Numerator
        num2: Denominator

    Returns:
        num1 / num2

    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Division by zero")
    return num1 / num2

@router.get("/divide", tags=["Operations"])
async def divide(num1: float, num2: float):
    """Divide two numbers.

    Args:
        num1: Numerator (query param)
        num2: Denominator (query param)

    Returns:
        JSON object with result key

    Raises:
        HTTPException 422: If num2 is zero
    """
    try:
        result = divide_numbers(num1, num2)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
```

### Endpoint Specifications
- **GET /add?num1=X&num2=Y** → `{"result": X+Y}`
- **GET /subtract?num1=X&num2=Y** → `{"result": X-Y}`
- **GET /multiply?num1=X&num2=Y** → `{"result": X*Y}`
- **GET /divide?num1=X&num2=Y** → `{"result": X/Y}` or 422 error if Y=0

### Testing Routes
```bash
curl "http://localhost:8004/add?num1=5&num2=3"           # {"result": 8}
curl "http://localhost:8004/subtract?num1=5&num2=3"      # {"result": 2}
curl "http://localhost:8004/multiply?num1=5&num2=3"      # {"result": 15}
curl "http://localhost:8004/divide?num1=6&num2=3"        # {"result": 2.0}
curl "http://localhost:8004/divide?num1=5&num2=0"        # 422 error
```

### Quality Gate ✅
- All 4 routes accessible and respond with correct JSON
- Each route in separate file
- All routes imported in main.py
- Error handling for division by zero
- Type hints on all functions
- Docstrings on all functions and endpoints

---

## Phase 4: Unit Tests (5+ per function)

Write comprehensive unit tests for each operation function.

### Deliverables
- `tests/test_add_unit.py` - 5+ tests for add operation
- `tests/test_subtract_unit.py` - 5+ tests for subtract operation
- `tests/test_multiply_unit.py` - 5+ tests for multiply operation
- `tests/test_divide_unit.py` - 5+ tests for divide operation
- All tests passing: `pytest tests/test_*_unit.py`

### `tests/test_add_unit.py` Template
```python
import pytest
from routes.add import add_numbers

class TestAddNumbers:
    """Unit tests for add operation."""

    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add_numbers(5, 3) == 8

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add_numbers(-5, 3) == -2
        assert add_numbers(-5, -3) == -8

    def test_add_decimals(self):
        """Test adding decimal numbers."""
        assert add_numbers(5.5, 3.2) == pytest.approx(8.7)

    def test_add_zero(self):
        """Test adding zero."""
        assert add_numbers(5, 0) == 5
        assert add_numbers(0, 0) == 0

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add_numbers(1e10, 1e10) == 2e10
```

### `tests/test_divide_unit.py` (with error cases)
```python
import pytest
from routes.divide import divide_numbers

class TestDivideNumbers:
    """Unit tests for divide operation."""

    def test_divide_positive_integers(self):
        """Test dividing positive integers."""
        assert divide_numbers(6, 3) == 2

    def test_divide_with_remainder(self):
        """Test division with remainder."""
        assert divide_numbers(5, 2) == pytest.approx(2.5)

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide_numbers(-6, 3) == -2
        assert divide_numbers(6, -3) == -2
        assert divide_numbers(-6, -3) == 2

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Division by zero"):
            divide_numbers(5, 0)

    def test_divide_decimals(self):
        """Test dividing decimal numbers."""
        assert divide_numbers(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_one(self):
        """Test dividing by one."""
        assert divide_numbers(5, 1) == 5
```

### Test Coverage Targets
- ✅ 5+ tests per operation
- ✅ Positive cases (normal inputs)
- ✅ Negative cases (invalid inputs)
- ✅ Edge cases (zero, large numbers, decimals)
- ✅ Error cases (division by zero)
- ✅ Type validation (ensure functions handle numbers)

### Quality Gate ✅
- All unit tests pass: `pytest tests/test_*_unit.py -v`
- 20+ total unit tests (5+ per operation)
- All edge cases covered
- No test skips

---

## Phase 5: API Tests (5+ per endpoint)

Write integration tests for FastAPI endpoints, including CORS header validation.

### Deliverables
- `tests/test_add_api.py` - 5+ API tests for /add endpoint
- `tests/test_subtract_api.py` - 5+ API tests for /subtract endpoint
- `tests/test_multiply_api.py` - 5+ API tests for /multiply endpoint
- `tests/test_divide_api.py` - 5+ API tests for /divide endpoint
- All tests passing: `pytest tests/test_*_api.py`

### `tests/test_add_api.py` Template
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAddAPI:
    """API tests for /add endpoint."""

    def test_add_endpoint_success(self):
        """Test /add endpoint with valid inputs."""
        response = client.get("/add?num1=5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 8}

    def test_add_endpoint_decimals(self):
        """Test /add endpoint with decimals."""
        response = client.get("/add?num1=5.5&num2=3.2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(8.7)

    def test_add_endpoint_negative(self):
        """Test /add endpoint with negative numbers."""
        response = client.get("/add?num1=-5&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}

    def test_add_endpoint_missing_params(self):
        """Test /add endpoint with missing parameters."""
        response = client.get("/add")
        assert response.status_code == 422  # Unprocessable Entity

    def test_add_endpoint_cors_headers(self):
        """Test CORS headers in response."""
        response = client.get(
            "/add?num1=5&num2=3",
            headers={"Origin": "http://localhost:3004"}
        )
        assert response.status_code == 200
        # CORS headers should be present (set by middleware)
        # Note: TestClient may not include CORS headers in tests
        # See full integration tests below
```

### `tests/test_divide_api.py` (with error cases)
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestDivideAPI:
    """API tests for /divide endpoint."""

    def test_divide_endpoint_success(self):
        """Test /divide endpoint with valid inputs."""
        response = client.get("/divide?num1=6&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": 2.0}

    def test_divide_endpoint_by_zero(self):
        """Test /divide endpoint with zero divisor."""
        response = client.get("/divide?num1=5&num2=0")
        assert response.status_code == 422  # Unprocessable Entity
        assert "Division by zero" in response.json()["detail"]

    def test_divide_endpoint_negative(self):
        """Test /divide endpoint with negative numbers."""
        response = client.get("/divide?num1=-6&num2=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2.0}

    def test_divide_endpoint_with_remainder(self):
        """Test /divide endpoint with remainder."""
        response = client.get("/divide?num1=5&num2=2")
        assert response.status_code == 200
        assert response.json()["result"] == pytest.approx(2.5)

    def test_divide_endpoint_invalid_type(self):
        """Test /divide endpoint with invalid input type."""
        response = client.get("/divide?num1=abc&num2=3")
        assert response.status_code == 422  # Type validation error
```

### CORS Testing in Production
```python
# For actual CORS header testing, use curl or httpx
# TestClient bypasses CORS middleware in some cases

# Better: Test with httpx or requests library directly
import httpx

async def test_cors_headers_production():
    """Test CORS headers in real request."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8004/add?num1=5&num2=3",
            headers={"Origin": "http://localhost:3004"}
        )
        assert "access-control-allow-origin" in response.headers
```

### Quality Gate ✅
- All API tests pass: `pytest tests/test_*_api.py -v`
- 20+ total API tests (5+ per endpoint)
- Tests cover success cases, error cases, missing params
- CORS headers validated (in manual testing or via httpx)
- All endpoints respond with correct HTTP status codes

---

## Phase 6: Regression Test Suite (100% Coverage)

Run all tests together and verify 100% code coverage.

### Deliverables
- All unit tests pass (20+ tests)
- All API tests pass (20+ tests)
- Code coverage report: `pytest --cov=routes` shows 100%
- Coverage report shows all lines, all branches covered
- No untested code paths

### Run Full Test Suite
```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=routes --cov-report=html --cov-report=term-missing

# View coverage in browser
open htmlcov/index.html
```

### Expected Coverage Output
```
routes/add.py           10      0   100%
routes/subtract.py      10      0   100%
routes/multiply.py      10      0   100%
routes/divide.py        15      0   100%  (higher due to error handling)
--------------------------------------------------
TOTAL                   45      0   100%
```

### Coverage > 100%?
If coverage report shows > 100%, it's usually due to how statements are counted. Aim for ≥ 100% line coverage and ≥ 95% branch coverage.

### Regression Checklist
Before committing, verify:
```bash
# All tests pass
pytest tests/ --tb=short

# 100% coverage
pytest tests/ --cov=routes --cov-fail-under=100

# No test skips
grep -r "@pytest.mark.skip\|@pytest.mark.xfail\|\.skip\|\.only" tests/

# No debug code
grep -r "print(" routes/ | grep -v "typing"
```

### Quality Gate ✅
- All 40+ tests pass: `pytest tests/`
- Coverage = 100%: `pytest --cov=routes` shows 100%
- No test skips
- No untested code paths

---

## Phase 7: Code Quality (PEP8, Docstrings, Type Hints)

Ensure code follows PEP8 and best practices.

### Deliverables
- PEP8 compliant code: `autopep8 --check backend/`
- Type hints on all functions and parameters
- Docstrings on all functions and endpoints
- No unused imports
- No debug code (no `print()` statements outside of docstrings)
- Clean error handling

### PEP8 Validation
```bash
# Check PEP8 compliance
autopep8 --check backend/

# Auto-fix PEP8 issues
autopep8 --in-place --aggressive --aggressive backend/
```

### Type Hints Example
```python
def add_numbers(num1: float, num2: float) -> float:
    """Add two numbers."""
    return num1 + num2

@router.get("/add")
async def add(num1: float, num2: float) -> dict[str, float]:
    """Add two numbers."""
    result = add_numbers(num1, num2)
    return {"result": result}
```

### Docstring Format (Google Style)
```python
def divide_numbers(num1: float, num2: float) -> float:
    """Divide two numbers.

    Args:
        num1: Numerator
        num2: Denominator

    Returns:
        num1 / num2

    Raises:
        ValueError: If num2 is zero
    """
    if num2 == 0:
        raise ValueError("Division by zero")
    return num1 / num2
```

### Code Quality Checklist
- [ ] PEP8 compliant (autopep8 passes)
- [ ] Type hints on all functions
- [ ] Docstrings on all functions
- [ ] Docstrings on all endpoints
- [ ] No unused imports
- [ ] No debug `print()` statements
- [ ] Error handling is proper (specific exceptions, not bare `except:`)
- [ ] No hardcoded values (use env vars)
- [ ] Comments explain "why", not "what"

### Quality Gate ✅
- PEP8 check passes: `autopep8 --check backend/` (no violations)
- All functions have type hints
- All functions have docstrings
- No console errors when running
- No debug code

---

## Phase 8: Documentation & Edge Cases

Document all endpoints and ensure edge cases are handled.

### Deliverables
- README.md documenting all endpoints
- Endpoint examples and expected responses
- Edge case documentation (division by zero, large numbers, etc.)
- Dockerfile builds successfully
- Production-ready error handling

### README.md Template
```markdown
# Stranger Things Calculator API

FastAPI backend for calculator operations.

## Endpoints

### GET /health
Health check endpoint.

**Response**: `{"status": "ok"}`

### GET /add
Add two numbers.

**Query Parameters**:
- `num1` (float): First number
- `num2` (float): Second number

**Response**: `{"result": 8}`

**Example**: `curl http://localhost:8004/add?num1=5&num2=3`

### GET /subtract
Subtract two numbers.

**Example**: `curl http://localhost:8004/subtract?num1=5&num2=3`

**Response**: `{"result": 2}`

### GET /multiply
Multiply two numbers.

**Example**: `curl http://localhost:8004/multiply?num1=5&num2=3`

**Response**: `{"result": 15}`

### GET /divide
Divide two numbers.

**Example**: `curl http://localhost:8004/divide?num1=6&num2=3`

**Response**: `{"result": 2.0}`

**Error**: Division by zero returns HTTP 422 with error message.

## Running

\`\`\`bash
pip install -r requirements.txt
python main.py
\`\`\`

## Testing

\`\`\`bash
pytest tests/ --cov=routes
\`\`\`

## Edge Cases

- Division by zero: Returns HTTP 422 error
- Large numbers: Handled as floats, no overflow
- Negative numbers: Supported
- Decimal numbers: Fully supported
- Query parameter validation: FastAPI validates types, returns 422 if invalid
```

### Edge Case Handling
- ✅ Division by zero: Raises ValueError, returns 422 HTTP status
- ✅ Large numbers: Use float type, handle appropriately
- ✅ Negative numbers: Support fully tested
- ✅ Decimal numbers: Support fully tested
- ✅ Invalid types: FastAPI validates, returns 422
- ✅ Missing parameters: FastAPI validates, returns 422

### Docker Validation
```bash
# Build image
docker build -t calculator-backend -f Dockerfile .

# Run container
docker run -p 8004:8004 calculator-backend

# Test
curl http://localhost:8004/health
```

### Quality Gate ✅
- README.md documents all endpoints and examples
- Edge cases handled and tested
- Dockerfile builds successfully: `docker build -f Dockerfile .`
- All 8 phases complete
- Code is production-ready

---

## Parallelization Strategy

**Within Phase 4 & 5** (testing phases):

Spawn all test files in parallel:
```bash
pytest tests/test_add_unit.py &
pytest tests/test_subtract_unit.py &
pytest tests/test_multiply_unit.py &
pytest tests/test_divide_unit.py &
# All four run simultaneously, collect results when complete
```

This cuts test time from ~10 seconds (sequential) to ~3 seconds (parallel).

---

## Success Criteria

✅ **Backend is production-ready if ALL 8 phases are complete**:
- ✅ Phase 1: FastAPI + minimal dependencies
- ✅ Phase 2: CORS middleware configured
- ✅ Phase 3: 4 separate route files
- ✅ Phase 4: 20+ unit tests (5+ per operation)
- ✅ Phase 5: 20+ API tests (5+ per endpoint)
- ✅ Phase 6: 100% test coverage verified
- ✅ Phase 7: PEP8 compliant, type hints, docstrings
- ✅ Phase 8: Documentation complete, edge cases handled

---

## Next Steps

Once all 8 phases are complete:
1. Verify REGRESSION.md Phase 3 checks pass
2. Frontend must also be complete (see frontend/CLAUDE.md)
3. Docker orchestration will be built (see CREATE.md)
4. After everything is working, create PR with REGRESSION.md checklist
