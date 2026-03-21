---
name: fastapi-validator
description: Validate FastAPI backend implementation for PEP8 compliance, endpoint structure, zero external dependencies, and comprehensive test coverage. Use this skill to check that all calculator routes (add, subtract, multiply, divide) are in separate files, imported correctly in main app, handle edge cases, include proper error handling, and have full unit and API test coverage. Run whenever building or reviewing backend logic, adding endpoints, or preparing for testing.
compatibility:
  - code-review-graph (for code analysis)
---

# FastAPI Backend Validator

This skill validates your Python FastAPI backend against the Stranger Things Calculator specifications.

## What This Skill Does

Validates that your FastAPI backend meets these requirements:
- **PEP8 compliance** - proper formatting, naming, structure
- **Zero external dependencies** - only Python stdlib and FastAPI (no numpy, requests, etc.)
- **Endpoint structure** - each operation (add, subtract, multiply, divide) in separate file
- **Proper imports** - routes correctly imported in main app file
- **Error handling** - proper HTTP status codes, meaningful error messages
- **Edge cases** - handles division by zero, non-numeric inputs, boundary cases
- **Input validation** - validates query parameters, type checking
- **Response format** - consistent JSON responses
- **Unit tests** - tests for every function
- **API tests** - positive, negative, edge case test coverage
- **Regression suite** - both unit and API tests run together

## How to Use This Skill

**Check your current implementation:**
```
/fastapi-validator
Validate my FastAPI backend. Check the endpoint structure,
make sure routes are in separate files, validate PEP8 compliance.
```

**After adding a new endpoint:**
```
/fastapi-validator
I just added the division endpoint. Check if it handles edge cases
(divide by zero), has proper error handling, and test coverage.
```

**Before running tests:**
```
/fastapi-validator
Validate the entire backend structure. Ensure it's ready for both
unit tests and API tests. Check the Docker setup on port 8004.
```

## Validation Checklist

The skill will check these items:

### Project Structure
- [ ] Main app file (main.py or app.py)
- [ ] Routes directory (routes/ or endpoints/)
- [ ] Separate file for each operation (add.py, subtract.py, multiply.py, divide.py)
- [ ] Test directory (tests/)
- [ ] Unit tests directory (tests/unit/)
- [ ] API tests directory (tests/api/)
- [ ] requirements.txt or pyproject.toml (should only list fastapi)
- [ ] .env file (if needed) for configuration
- [ ] README with setup instructions

### Code Quality - PEP8
- [ ] Python 3.8+ syntax
- [ ] 4-space indentation (no tabs)
- [ ] Line length ≤ 79 characters (or ≤ 99 with ruff config)
- [ ] Proper function naming (snake_case)
- [ ] Proper class naming (PascalCase)
- [ ] Proper constant naming (UPPER_SNAKE_CASE)
- [ ] No unused imports or variables
- [ ] Proper docstrings on functions ("""...""")
- [ ] Type hints on all functions

### Dependencies Check
- [ ] Only imports: fastapi, python stdlib (json, math, logging, etc.)
- [ ] NO external packages (numpy, pandas, requests, etc.)
- [ ] Verify no hidden dependencies in imports
- [ ] Check for lazy imports that might fail

### Route Structure
- [ ] routes/add.py - handles /add endpoint
- [ ] routes/subtract.py - handles /subtract endpoint
- [ ] routes/multiply.py - handles /multiply endpoint
- [ ] routes/divide.py - handles /divide endpoint
- [ ] Each file has @router decorator
- [ ] Routes properly imported in main.py with include_router()
- [ ] Consistent parameter naming (num1, num2)

### Endpoint Implementation
- [ ] GET /add?num1=X&num2=Y returns {"result": Z}
- [ ] GET /subtract?num1=X&num2=Y returns {"result": Z}
- [ ] GET /multiply?num1=X&num2=Y returns {"result": Z}
- [ ] GET /divide?num1=X&num2=Y returns {"result": Z}
- [ ] Content-Type: application/json
- [ ] Proper HTTP status codes (200, 400, 422)

### Input Validation
- [ ] num1 and num2 are required parameters
- [ ] num1 and num2 are float/int types
- [ ] Non-numeric input returns 400/422 with error message
- [ ] Invalid query returns clear error message
- [ ] Query parameters validated before calculation

### Error Handling
- [ ] Division by zero returns 400 with message: "Cannot divide by zero"
- [ ] Invalid inputs return 422 with validation error details
- [ ] All endpoints have try/except if needed
- [ ] Error responses include error message and type
- [ ] No unhandled exceptions (500 errors are caught)

### Edge Cases Tested
- [ ] Division by zero: /divide?num1=10&num2=0 → error
- [ ] Negative numbers: /add?num1=-5&num2=3 → result: -2
- [ ] Decimal numbers: /multiply?num1=2.5&num2=4 → result: 10.0
- [ ] Very large numbers: /add?num1=999999&num2=1 → result: 1000000
- [ ] Zero operands: /add?num1=0&num2=0 → result: 0
- [ ] Missing parameters: /add?num1=5 → error (num2 missing)

### Unit Tests (tests/unit/)
- [ ] test_add.py tests add function directly
- [ ] test_subtract.py tests subtract function directly
- [ ] test_multiply.py tests multiply function directly
- [ ] test_divide.py tests divide function directly
- [ ] Each test function named test_*
- [ ] Each function has 3+ test cases (normal, edge, error)
- [ ] Tests cover: positive, negative, zero, decimal inputs
- [ ] 100% function coverage

### API Tests (tests/api/)
- [ ] test_add_endpoint.py tests /add route
- [ ] test_subtract_endpoint.py tests /subtract route
- [ ] test_multiply_endpoint.py tests /multiply route
- [ ] test_divide_endpoint.py tests /divide route
- [ ] Positive cases: valid inputs return 200 with correct result
- [ ] Negative cases: invalid inputs return 400/422
- [ ] Edge cases: division by zero, boundary values
- [ ] Response format: {"result": number} or {"error": "message"}
- [ ] Content-Type validation
- [ ] Query parameter validation

### Regression Suite
- [ ] Can run all unit tests: `pytest tests/unit/`
- [ ] Can run all API tests: `pytest tests/api/`
- [ ] Can run both: `pytest tests/`
- [ ] All tests pass before deployment
- [ ] CI would catch regressions

### Main App File (main.py)
- [ ] FastAPI instance created
- [ ] CORS enabled for frontend (http://localhost:3004)
- [ ] All routes imported and registered
- [ ] Root endpoint available (GET /)
- [ ] Health check available (GET /health or similar)
- [ ] Documentation available (Swagger /docs)
- [ ] Proper logging setup

### Docker Readiness
- [ ] Requirements.txt includes only fastapi
- [ ] Can start with: `python main.py` or `uvicorn main:app --host 0.0.0.0 --port 8004`
- [ ] Listens on port 8004
- [ ] Frontend can reach backend at http://backend:8004 (in Docker)
- [ ] No hardcoded localhost (use 0.0.0.0)

## How the Skill Works

1. **Structure Analysis**: Checks directory layout and file organization
2. **Dependency Audit**: Verifies only stdlib and FastAPI are used
3. **Code Quality**: Reviews PEP8 compliance, type hints, docstrings
4. **Route Validation**: Checks endpoint structure and implementation
5. **Test Coverage**: Verifies unit and API test completeness
6. **Edge Case Review**: Checks special case handling (division by zero, etc.)
7. **Docker Compatibility**: Ensures port configuration and startup setup
8. **Report**: Generates checklist with pass/fail and action items

## Output Format

The skill produces a validation report with:
- **Status**: ✅ Pass, ⚠️ Warnings, ❌ Failures
- **Category**: which area was checked
- **Finding**: what was found
- **Action**: how to fix if needed
- **Severity**: Critical, High, Medium, Low

### Example Report
```
FASTAPI BACKEND VALIDATION REPORT
==================================

✅ Project Structure (5/5)
  ✅ Main app file present
  ✅ Routes directory with separate files
  ✅ Test directories organized
  ✅ requirements.txt only has fastapi

⚠️ Code Quality - PEP8 (3/4)
  ✅ Proper function naming (snake_case)
  ✅ Type hints on functions
  ❌ Line length exceeds 79 chars in divide.py:15
    Action: Break line or increase limit to 99
    Severity: Low

❌ Edge Cases (3/4)
  ✅ Division by zero handled
  ✅ Negative numbers work
  ❌ Missing test for very large numbers
    Action: Add test for num1=999999999, num2=1
    Severity: Medium
```

## When to Run This

- **Initial setup**: After creating the project structure
- **After implementing endpoints**: Check each new route
- **Before writing tests**: Validate structure is correct
- **Code review**: Check PEP8 and best practices
- **Docker prep**: Before containerizing the backend

## Pro Tips

1. **Use pydantic for validation** - FastAPI includes pydantic, use it for query params
2. **Organize constants** - math operations in one file, validation in another
3. **Add logging** - log requests and calculations for debugging
4. **Type hints everywhere** - helps catch bugs early
5. **Separate logic from routes** - define calculation functions separately from endpoints

## Troubleshooting

**"Can't import route X"**: Check file path in include_router(), use correct relative imports

**"Division by zero not handled"**: Add `if num2 == 0: return error_response`

**"Tests not finding app"**: Ensure pytest can import from package, use conftest.py if needed

**"CORS errors"**: Add `CORSMiddleware` in main.py for http://localhost:3004

**"Port 8004 already in use"**: Change port in main.py or stop other services

**"FastAPI not imported"**: Run `pip install fastapi uvicorn`
