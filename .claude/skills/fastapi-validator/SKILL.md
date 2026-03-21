# FastAPI Validator Skill

Validates FastAPI Python backend for quality and specification compliance.

## Purpose
Ensures backend meets all project requirements: PEP8, zero external deps, full test coverage.

## Validation Checklist

### Dependencies
- [ ] `requirements.txt` contains ONLY: fastapi, uvicorn
- [ ] No extra libraries imported
- [ ] No unused imports
- [ ] All imports from stdlib or fastapi

### Code Structure
- [ ] Main app file (`main.py` or `app.py`) exists
- [ ] Routes in separate files: `add.py`, `subtract.py`, `multiply.py`, `divide.py`
- [ ] Routes imported into main app
- [ ] CORS enabled for frontend access
- [ ] `/health` endpoint implemented
- [ ] Error handling for all endpoints

### PEP8 Compliance
- [ ] Code runs through autopep8 without issues
- [ ] Type hints on all functions
- [ ] Docstrings on all functions
- [ ] Line length <= 79 characters
- [ ] No trailing whitespace

### Endpoint Validation
- [ ] `/add?num1=X&num2=Y` returns correct sum
- [ ] `/subtract?num1=X&num2=Y` returns correct difference
- [ ] `/multiply?num1=X&num2=Y` returns correct product
- [ ] `/divide?num1=X&num2=Y` returns correct quotient (or error for div by 0)
- [ ] All endpoints return JSON with consistent schema

### Test Coverage
- [ ] **Unit Tests**: 5+ per operation
  - Positive: normal inputs
  - Edge cases: zero, negative, large, decimals
  - Error cases: invalid types
- [ ] **API Tests**: 5+ per endpoint
  - HTTP 200 success cases
  - HTTP 400 validation errors
  - HTTP 422 invalid parameters
  - Response schema validation
- [ ] **Regression Suite**: All tests passing
- [ ] **Coverage**: 100% line coverage

## How to Invoke

```bash
/fastapi-validator
```

Validator will:
1. Check dependencies (fastapi, uvicorn only)
2. Verify PEP8 compliance
3. Run all unit tests
4. Run all API tests
5. Check code coverage
6. Verify endpoints work
7. Test error cases

## Output Format
- ✅ Passing checks
- ⚠️ Warnings
- ❌ Failing checks (blocks merge)

## Pass Criteria
- All ❌ items resolved
- 100% test coverage
- PEP8 compliant
- Zero external dependencies
- All endpoints functional
- All tests passing
