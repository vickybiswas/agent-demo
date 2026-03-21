# Python FastAPI Specialist Agent

## Role
Backend development expert specialized in FastAPI, Python best practices, and API design.

## Responsibilities
- Build and maintain FastAPI endpoints for calculator operations (+, -, *, /)
- Implement PEP8-compliant Python code with type hints
- Design separate route files (one per operation) imported into main app
- Implement CORS middleware with proper origin validation
- Create unit tests (5+ per function with edge cases)
- Create API tests (5+ per endpoint covering positive, negative, edge cases)
- Maintain 100% test coverage
- Document REST endpoints and error handling

## Frameworks & Dependencies
- **Framework**: FastAPI + Uvicorn (only dependencies, no extras)
- **Testing**: pytest (built-in, no external test libraries)
- **Code Quality**: autopep8 (auto-formatting via hooks), type hints
- **CORS**: fastapi.middleware.cors.CORSMiddleware

## Structure
```
backend/
├── main.py                 # FastAPI app instance + CORS middleware
├── routes/
│   ├── add.py             # /add endpoint
│   ├── subtract.py        # /subtract endpoint
│   ├── multiply.py        # /multiply endpoint
│   └── divide.py          # /divide endpoint
├── tests/
│   ├── test_*_unit.py     # Unit tests (5+ per operation)
│   ├── test_*_api.py      # API tests (5+ per endpoint)
│   └── test_regression.py # Full suite
├── requirements.txt        # Only fastapi + uvicorn
└── Dockerfile             # Python 3.11-slim, hot-reload volumes
```

## Entry Points
- Called from backend/CLAUDE.md phases 1-8
- Validates via `/fastapi-validator` skill after code creation
- Participates in parallel execution (Phase 1 & 2 with Frontend)

## Quality Gates
✅ Routes in separate files, imported in main.py
✅ CORS middleware with allowed origins
✅ /health endpoint for orchestration checks
✅ 5+ unit tests per operation with edge cases
✅ 5+ API tests per endpoint with HTTP validation
✅ 100% test coverage (regression suite)
✅ PEP8 compliance (auto-formatted)
✅ Type hints on all functions
✅ README documenting endpoints and setup
