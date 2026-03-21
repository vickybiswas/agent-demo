# FastAPI Validator Skill

Validates Python FastAPI backend implementation for correctness, testing, and PEP8 compliance.

## Usage

```
/fastapi-validator
```

## What It Validates

### 1. Project Structure
- ✅ `backend/main.py` exists (FastAPI app)
- ✅ `backend/routes/` directory exists with separate files:
  - `add.py`, `subtract.py`, `multiply.py`, `divide.py`
- ✅ All routes imported in `main.py`
- ✅ `backend/tests/` directory with test files
- ✅ `backend/requirements.txt` exists (fastapi + uvicorn only)
- ✅ `Dockerfile` exists in `backend/`

### 2. FastAPI Implementation
- ✅ FastAPI instance created in `main.py`
- ✅ CORS middleware configured:
  - `Access-Control-Allow-Origin: *` (or specific origins)
  - Credentials allowed
  - Methods: GET, POST, OPTIONS
- ✅ `/add?num1=X&num2=Y` endpoint works
- ✅ `/subtract?num1=X&num2=Y` endpoint works
- ✅ `/multiply?num1=X&num2=Y` endpoint works
- ✅ `/divide?num1=X&num2=Y` endpoint works
- ✅ All endpoints return `{"result": value}` JSON
- ✅ Division by zero handled (error response)
- ✅ `/health` or root endpoint for health checks

### 3. Code Quality
- ✅ PEP8 compliant (autopep8 passes)
- ✅ Type hints on all functions
- ✅ Docstrings on all functions
- ✅ No unused imports
- ✅ No debug print statements
- ✅ No hardcoded localhost (use env vars for port)

### 4. Testing
- ✅ Unit tests for each operation (5+ per function)
  - Positive cases (normal math)
  - Negative cases (invalid inputs)
  - Edge cases (division by zero, large numbers, decimals)
  - Type validation
- ✅ API tests for each endpoint (5+ per endpoint)
  - Status codes (200, 422, 500)
  - Response format validation
  - CORS headers present
  - Error handling
- ✅ 100% code coverage
  - No untested lines
  - All branches covered
- ✅ All tests pass: `pytest tests/`

### 5. Dependencies
- ✅ `requirements.txt` contains ONLY:
  - fastapi
  - uvicorn
- ✅ No external libraries (pandas, numpy, etc.)
- ✅ Python 3.11+ compatibility

## Validation Steps

1. Check file structure exists
2. Verify FastAPI instance and CORS middleware
3. Test all 4 endpoints (manual curl or test runner)
4. Run linting: `autopep8 --check backend/`
5. Run type checking: `mypy backend/` (or verify type hints)
6. Run tests: `pytest tests/ --cov=routes`
7. Verify 100% coverage report
8. Check Docker image builds: `docker build -f backend/Dockerfile .`

## Pass Criteria

✅ **PASS** if ALL of the following are true:
- Project structure correct
- All 4 endpoints respond with correct JSON
- 100% test coverage achieved
- All tests pass
- PEP8 compliant
- CORS headers present
- No external dependencies

❌ **FAIL** if ANY of:
- Missing endpoints or wrong response format
- Test coverage < 100%
- Tests failing
- PEP8 violations
- External dependencies in requirements.txt

## Output

```
✅ FastAPI Validator Results

Project Structure:
  ✅ main.py exists
  ✅ routes/ directory with add.py, subtract.py, multiply.py, divide.py
  ✅ tests/ directory with test files
  ✅ requirements.txt (fastapi, uvicorn only)

Implementation:
  ✅ FastAPI instance created
  ✅ CORS middleware configured
  ✅ All 4 endpoints working
  ✅ Correct JSON response format

Code Quality:
  ✅ PEP8 compliant (autopep8 passes)
  ✅ Type hints on all functions
  ✅ Docstrings present

Testing:
  ✅ Unit tests: 20+ total tests
  ✅ API tests: 20+ total tests
  ✅ Code coverage: 100%
  ✅ All tests passing

Docker:
  ✅ Dockerfile builds successfully

Result: ✅ PASS - Backend ready for integration
```
