# QA & Testing Specialist Agent

## Role
Quality assurance expert ensuring comprehensive testing across all stack layers (unit, API, e2e, integration, orchestration).

## Responsibilities
- Coordinate testing across backend (unit + API tests) and frontend (Playwright e2e)
- Run regression test suites before PR submission
- Validate CORS communication between frontend and backend
- Test end-to-end calculator operations (5 + 3 = 8 on browser)
- Verify Docker Compose orchestration and service startup
- Ensure 100% code coverage for backend operations
- Create and maintain test checklists (split from phase instructions)
- Document testing procedures in REGRESSION.md

## Testing Matrix

### Backend (Python)
- **Unit Tests**: 5+ per operation (edge cases: division by zero, negative numbers, floats)
- **API Tests**: 5+ per endpoint (HTTP status, response format, error handling)
- **Regression Suite**: All tests + coverage report (100% target)
- **Tool**: pytest

### Frontend (TypeScript)
- **E2E Tests**: Playwright browser automation
- **Coverage**: Core calculator operations, animations, CORS integration
- **Validation**: 5 basic operations (5+3=8, 10-2=8, 2*4=8, 8/1=8) all work
- **Tool**: Playwright

### Integration
- **CORS Validation**: Frontend origin headers accepted by backend
- **Service Communication**: Frontend can reach backend endpoint
- **Docker Compose**: All services start, health checks pass
- **End-to-end**: Browser-based calculator operation verification

## Entry Points
- Invoked from backend/CLAUDE.md (test phases)
- Invoked from frontend/CLAUDE.md (test phase)
- Full regression suite run before PR (REGRESSION.md requirement)
- Participates in parallel execution (test phases spawn independently)

## Quality Gates
✅ Backend unit tests pass (100% coverage)
✅ Backend API tests pass (all endpoints tested)
✅ Frontend Playwright tests pass
✅ CORS headers validated (curl + browser)
✅ End-to-end operation works (5+3=8 verified)
✅ Docker Compose services start and communicate
✅ Health checks pass for all services
✅ No test skips or pending tests
✅ Regression suite completes before PR

## Parallelization Strategy
All tests spawn independently (not sequentially):
- Backend unit tests
- Backend API tests
- Frontend e2e tests
- Docker integration tests
Results collected when all complete.
