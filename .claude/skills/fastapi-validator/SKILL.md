# FastAPI Validator Skill

## Purpose
Validate Python/FastAPI backend code against INSTRUCTIONS.md and backend/CLAUDE.md requirements.

## Triggered On
- Backend code creation (hooks auto-format via autopep8)
- Manual invocation: `/fastapi-validator`

## Validation Checklist

### Project Structure
- [ ] Separate route files (add.py, subtract.py, multiply.py, divide.py)
- [ ] Routes imported in main.py
- [ ] requirements.txt contains only fastapi + uvicorn
- [ ] No external dependencies (numpy, pandas, etc.)
- [ ] Dockerfile for containerization
- [ ] tests/ directory with unit and API tests

### FastAPI Setup
- [ ] FastAPI() app instance in main.py
- [ ] CORSMiddleware configured with proper origins
- [ ] /health endpoint implemented
- [ ] No hardcoded localhost (docker-ready)
- [ ] Uvicorn configured for hot reload

### CORS Configuration
- [ ] CORSMiddleware imported and configured
- [ ] allow_origins includes http://localhost:3004 (local dev) and frontend service (docker)
- [ ] allow_credentials, allow_methods, allow_headers set correctly
- [ ] CORS headers returned on OPTIONS preflight requests

### Route Implementation
- [ ] /add endpoint (POST or GET with query params)
- [ ] /subtract endpoint
- [ ] /multiply endpoint
- [ ] /divide endpoint (with error handling for div by zero)
- [ ] All routes follow consistent pattern
- [ ] Query parameters: num1, num2
- [ ] JSON response format: {"result": value}
- [ ] Error responses with proper status codes

### Code Quality
- [ ] PEP8 compliant (auto-formatted via autopep8)
- [ ] Type hints on all function parameters and returns
- [ ] Docstrings on all functions
- [ ] No unused imports
- [ ] No hardcoded values (constants extracted)
- [ ] Proper error handling and validation

### Unit Tests
- [ ] 5+ tests per operation (add, subtract, multiply, divide)
- [ ] Edge cases tested (zero, negative, floats, division by zero)
- [ ] pytest fixtures for common test data
- [ ] Clear test names describing what's tested
- [ ] Tests in test_*_unit.py files

### API Tests
- [ ] 5+ tests per endpoint
- [ ] Positive cases (valid inputs)
- [ ] Negative cases (invalid inputs, missing params)
- [ ] Edge cases (boundary values)
- [ ] HTTP status code validation (200, 400, 422)
- [ ] Response format validation (JSON structure)
- [ ] Tests in test_*_api.py files

### Test Coverage
- [ ] `pytest --cov` reports 100% coverage (or near)
- [ ] All code paths tested
- [ ] Regression suite in test_regression.py runs all tests
- [ ] No test skips or xfail marks

### Documentation
- [ ] README.md in backend/ with setup instructions
- [ ] Endpoint documentation (path, params, response)
- [ ] Error codes documented (400, 422, 500)
- [ ] CORS setup documented
- [ ] Testing instructions included

## Pass/Fail Criteria
✅ **PASS**: All checked items pass, 100% test coverage, no blocking errors
❌ **FAIL**: Any unchecked items or test coverage < 95%

## Outputs
- Checklist results (passed/failed items)
- Test coverage report
- PEP8 compliance feedback
- Performance metrics (response times)
