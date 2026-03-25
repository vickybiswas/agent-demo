# FastAPI Validator Skill

## Purpose
Validate Python FastAPI backend code against project standards before merging.

## Validation Rules

### Code Style (PEP8)
- ✅ autopep8 applied
- ✅ No trailing whitespace
- ✅ 4-space indentation
- ✅ Max line length: 99 characters
- ✅ Two blank lines between functions
- ✅ One blank line between methods

### Type Hints
- ✅ All function parameters typed
- ✅ All function returns typed
- ✅ Pydantic models for request/response
- ✅ Type hints for variables where ambiguous
- ✅ No `Any` without justification

### Docstrings
- ✅ Module docstring present
- ✅ Function docstrings (Args, Returns)
- ✅ Class docstrings
- ✅ Complex logic explained
- ✅ Docstring format: Google style

### Project Structure
- ✅ operations/ directory with separate files
- ✅ Each operation in own file (add.py, subtract.py, etc.)
- ✅ main.py imports from operations/
- ✅ No circular imports
- ✅ __init__.py files where needed

### Endpoints
- ✅ /health endpoint present
- ✅ /add endpoint GET query params
- ✅ /subtract endpoint GET query params
- ✅ /multiply endpoint GET query params
- ✅ /divide endpoint GET query params
- ✅ Proper HTTP status codes (200, 400, 422)
- ✅ Error responses descriptive

### Calculations
- ✅ No external dependencies (fastapi, uvicorn only)
- ✅ Pure Python calculation logic
- ✅ Handles edge cases (division by zero)
- ✅ Correct mathematical results
- ✅ Type validation (int/float inputs)

### CORS
- ✅ CORS middleware configured
- ✅ allowed_origins includes frontend
- ✅ CORS headers in responses
- ✅ Pre-flight requests handled
- ✅ Credentials allowed if needed

### Testing
- ✅ Unit tests: 5+ per operation
- ✅ API tests: 5+ per endpoint
- ✅ Positive cases tested
- ✅ Negative cases tested
- ✅ Edge cases tested
- ✅ 100% code coverage
- ✅ All tests pass

### Code Quality
- ✅ No unused imports
- ✅ No debug print statements
- ✅ No hardcoded values (use config)
- ✅ Error handling for all edge cases
- ✅ Logging for important events
- ✅ Comments for non-obvious logic

### Dependencies
- ✅ requirements.txt only: fastapi, uvicorn
- ✅ No extra dependencies
- ✅ Pinned versions
- ✅ Python 3.13 compatible

## Validation Checklist

### Pre-Merge Validation
Run before creating PR:
```bash
# 1. PEP8 check
autopep8 --diff backend/*.py backend/operations/*.py

# 2. Type check
python3 -m mypy backend/ --ignore-missing-imports

# 3. Unit tests (all together)
python3 -m pytest backend/tests/test_*_unit.py -v

# 4. API tests (all together)
python3 -m pytest backend/tests/test_*_api.py -v

# 5. Coverage
python3 -m pytest backend/tests/ -v --cov=backend/operations --cov-report=term-missing

# 6. Review checklist
- [ ] PEP8 compliant
- [ ] Type hints complete
- [ ] Unit tests: 100% coverage
- [ ] API tests: all pass
- [ ] CORS verified
- [ ] Edge cases handled
- [ ] Docstrings present
```

## Failure Cases
Validation fails if:
- PEP8 violations
- Type hints missing
- Unit test coverage < 100%
- API tests fail
- CORS not configured
- External dependencies used
- Edge cases not handled
- Docstrings missing

## Success Criteria
- PEP8 compliant ✅
- Type hints complete ✅
- 100% test coverage ✅
- All tests pass ✅
- CORS configured ✅
- No external deps ✅
- Edge cases handled ✅
- Docstrings present ✅

## Test Execution Strategy
**Parallelization**: Spawn all independent tests together:
```
Unit Tests (5+ per op) → all spawn together
API Tests (5+ per ep)  → all spawn together
Coverage              → runs after both complete
```

## Integration with CLAUDE.md
This validator runs at the end of backend/CLAUDE.md Phase 7 (Code Quality).

## Usage
```bash
claude run fastapi-validator
```

Or invoke from CLAUDE.md:
```markdown
## Phase 7: Code Quality
Run `/fastapi-validator` before committing:
- [ ] PEP8 compliant
- [ ] 100% coverage
- [ ] All tests pass
- [ ] Docstrings present
```
