# Regression Testing Checklist (REGRESSION.md)

## Critical Requirement
**EVERY developer must complete ALL sections of this checklist before creating a PR.**

This checklist prevents integration issues like GitHub Issue #3 (CORS/env var failures) from reaching the repository. Run it locally in your development environment.

---

## Phase 1: Local Development Setup

### Backend Service
- [ ] Create virtual environment: `cd backend && python3 -m venv venv && source venv/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt` (only fastapi + uvicorn)
- [ ] Start backend: `python3 main.py` or `uvicorn main:app --reload --port 8004`
- [ ] Backend logs show: "Application startup complete"
- [ ] Backend responds: `curl http://localhost:8004/health` (or test any endpoint)
- [ ] Backend responds to calculations: `curl "http://localhost:8004/add?num1=5&num2=3"` returns `{"result": 8}`

### Frontend Service
- [ ] Navigate to frontend: `cd frontend`
- [ ] Install dependencies: `npm install`
- [ ] Create .env.local with: `NEXT_PUBLIC_API_URL=http://localhost:8004`
- [ ] Start frontend: `npm run dev`
- [ ] Frontend logs show: "ready - started server on 0.0.0.0:3004" (or similar)
- [ ] Frontend loads: `curl http://localhost:3004` returns HTML
- [ ] Browser opens http://localhost:3004 and shows calculator UI

### Environment Variables
- [ ] Backend .env variables set (if needed, per backend requirements)
- [ ] Frontend .env.local exists with `NEXT_PUBLIC_API_URL=http://localhost:8004`
- [ ] No hardcoded localhost/ports in code (should come from env)
- [ ] .env files are in .gitignore (never commit secrets)

---

## Phase 2: CORS & Integration Testing

### CORS Header Validation
```bash
# Backend should return CORS headers on OPTIONS request
curl -i -X OPTIONS \
  -H "Origin: http://localhost:3004" \
  -H "Access-Control-Request-Method: GET" \
  http://localhost:8004/add

# Expected response headers:
# Access-Control-Allow-Origin: http://localhost:3004
# Access-Control-Allow-Methods: GET, POST, OPTIONS
# Access-Control-Allow-Headers: content-type
```

- [ ] Backend responds with CORS headers
- [ ] `Access-Control-Allow-Origin` includes frontend URL
- [ ] `Access-Control-Allow-Methods` includes GET/POST
- [ ] No CORS errors in browser console

### Backend → Frontend (Frontend Calling Backend)
```bash
# From browser console or Playwright:
fetch('http://localhost:8004/add?num1=5&num2=3', {
  headers: { 'Origin': 'http://localhost:3004' }
})
.then(r => r.json())
.then(d => console.log(d))  // Should log {"result": 8}
```

- [ ] Frontend can fetch from backend without CORS errors
- [ ] Response is valid JSON with `result` field
- [ ] Browser Network tab shows CORS headers in response

### End-to-End Manual Test
1. [ ] Open http://localhost:3004 in browser
2. [ ] Calculator UI displays (Stranger Things theme visible)
3. [ ] Click calculator buttons: 5 + 3 (or similar operation)
4. [ ] Result displays: 8 (or correct calculation)
5. [ ] Browser console has NO errors (including no CORS errors)
6. [ ] Network tab shows successful request to http://localhost:8004/...

---

## Phase 3: Testing Requirements

### Backend Unit Tests
```bash
cd backend
python3 -m pytest tests/test_*_unit.py -v --tb=short
```

- [ ] All unit tests PASS (green)
- [ ] Coverage report shows 100% or near 100%
- [ ] No test skips or xfails
- [ ] Edge cases tested (division by zero, negative numbers, floats)

### Backend API Tests
```bash
cd backend
python3 -m pytest tests/test_*_api.py -v --tb=short
```

- [ ] All API tests PASS
- [ ] HTTP status codes correct (200 OK, 400 Bad Request, etc.)
- [ ] Response format is valid JSON
- [ ] Error messages are clear

### Backend Regression Suite
```bash
cd backend
python3 -m pytest tests/test_regression.py -v --tb=short
```

- [ ] All tests pass
- [ ] Coverage: 100% of functions tested

### Frontend TypeScript Compilation
```bash
cd frontend
npm run build
```

- [ ] Build succeeds (no errors)
- [ ] No TypeScript strict mode violations
- [ ] No warnings about unused imports or variables

### Frontend Playwright E2E Tests
```bash
cd frontend
npx playwright test
# or
npm run test:e2e
```

- [ ] All tests PASS (green)
- [ ] Tests verify calculator operations (5+3=8, 10-2=8, etc.)
- [ ] Tests verify backend integration (no CORS errors)
- [ ] Tests verify animations (if applicable)

### Summary
```bash
# Quick regression check:
cd backend && python3 -m pytest tests/ -v --cov=. --cov-report=term && cd ../frontend && npm run build && npx playwright test
```

- [ ] Backend tests pass + coverage 100%
- [ ] Frontend builds with no errors
- [ ] Playwright tests pass

---

## Phase 4: Docker Orchestration

### Build Services
```bash
docker compose build
```

- [ ] Frontend service builds successfully
- [ ] Backend service builds successfully
- [ ] No build errors or warnings
- [ ] Build completes in < 5 minutes

### Start Services
```bash
docker compose up
```

- [ ] Frontend logs show: "ready - started server on..."
- [ ] Backend logs show: "Application startup complete"
- [ ] Both services start without crashing
- [ ] Services remain running (don't exit after startup)

### Service Health Checks
```bash
# In another terminal, while docker compose up is running

# Check frontend
curl http://localhost:3004

# Check backend
curl http://localhost:8004/health  # or any endpoint
```

- [ ] Frontend responds (returns HTML)
- [ ] Backend responds (returns JSON)
- [ ] No connection refused errors

### Service Communication (Inside Docker Network)
```bash
docker compose exec frontend curl http://backend:8004/add?num1=5&num2=3
```

- [ ] Frontend service can reach backend service
- [ ] Response is valid JSON: `{"result": 8}`

### CORS Validation (Docker)
```bash
curl -i -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
```

- [ ] Backend returns CORS headers inside Docker
- [ ] `Access-Control-Allow-Origin: *` or includes frontend URL

### End-to-End (Browser Test in Docker)
1. [ ] Open http://localhost:3004 in browser (while docker compose up running)
2. [ ] Calculator loads and displays theme
3. [ ] Click buttons to perform operation (5 + 3)
4. [ ] Result appears correctly (8)
5. [ ] Browser console has NO errors
6. [ ] Network tab shows successful backend request

### Cleanup
```bash
docker compose down
```

- [ ] Both services stop cleanly
- [ ] No errors in shutdown logs

---

## Phase 5: Code Quality

### Backend Code Quality
```bash
cd backend
autopep8 --diff --aggressive --aggressive .
python3 -m pylint main.py routes/*.py  # If pylint installed, otherwise skip
```

- [ ] PEP8 style compliance (no long lines, proper spacing)
- [ ] Type hints on all functions: `def add(num1: float, num2: float) -> float:`
- [ ] Docstrings on all functions
- [ ] No hardcoded ports or localhost URLs
- [ ] Error handling for invalid inputs

### Frontend Code Quality
```bash
cd frontend
npx tsc --noEmit  # Check TypeScript strict mode
npx prettier --check .
```

- [ ] TypeScript strict mode: no compilation errors
- [ ] No `any` types without explicit escape hatches
- [ ] Code formatted (prettier)
- [ ] No hardcoded localhost:8004 (use NEXT_PUBLIC_API_URL env)
- [ ] SCSS properly organized (no duplicate styles, consistent variables)

### No Debug Code
- [ ] No `console.log` statements in production code
- [ ] No `print()` statements in backend production code
- [ ] No `debugger` statements
- [ ] No `.only` or `.skip` in tests (would skip tests)

---

## Phase 6: Git Preparation

### Commit History
```bash
git log --oneline -10
```

- [ ] Commits have clear, descriptive messages
- [ ] No "WIP", "debug", "TODO", or random commits
- [ ] Each commit represents a logical change

### Staged Files
```bash
git status
git diff --cached  # See what will be committed
```

- [ ] Only intended files staged
- [ ] No .env or .env.local files committed (check .gitignore)
- [ ] No node_modules/ or venv/ committed
- [ ] No build artifacts committed

### Pre-PR Sync
```bash
git fetch origin
git rebase origin/main  # Or merge, depending on workflow
```

- [ ] No merge conflicts
- [ ] Local branch up to date with main
- [ ] All tests still pass after rebase

---

## Pre-PR Final Checklist

Before clicking "Create PR", verify:

- [ ] **Phase 1**: Both services start and respond locally
- [ ] **Phase 2**: CORS validated, end-to-end operation works in browser
- [ ] **Phase 3**: All tests pass (unit, API, e2e)
- [ ] **Phase 4**: Docker compose starts services, they communicate
- [ ] **Phase 5**: Code quality checks pass, no debug code
- [ ] **Phase 6**: Git history clean, no secrets committed

### Final Verification Command
```bash
# Quick check that everything works:

# 1. Backend tests
cd backend && python3 -m pytest tests/ -v --cov=. --cov-report=term-missing && cd ..

# 2. Frontend build + tests
cd frontend && npm run build && npm run test && cd ..

# 3. Docker check
docker compose up -d && sleep 3 && curl http://localhost:3004 && curl http://localhost:8004/health && docker compose down
```

- [ ] Backend tests pass
- [ ] Frontend builds successfully
- [ ] Docker services start and respond

---

## If Regression Test Fails

### CORS Errors
1. Check backend CORS middleware is configured
2. Verify `CORS_ORIGINS` environment variable includes frontend URL
3. Test CORS with curl (command in Phase 2)
4. Check browser Network tab for CORS error details

### Service Doesn't Start
1. Check docker compose logs: `docker compose logs frontend` / `docker compose logs backend`
2. Check port conflicts: `lsof -i :3004` / `lsof -i :8004`
3. Rebuild with no-cache: `docker compose build --no-cache`

### Tests Fail
1. Run REGRESSION.md Phase 3 locally (not in Docker)
2. Check test output for specific failure details
3. Review test requirements in /nextjs-validator or /fastapi-validator skills

### Git Issues
1. Ensure you're on the correct branch
2. Pull latest from origin/main: `git pull origin main`
3. Resolve merge conflicts manually if needed

---

## Summary
**This is mandatory.** Every PR must have evidence that REGRESSION.md passed. Include test outputs in PR description to prove all phases passed.

Skipping this checklist risks GitHub issues that could have been caught locally.
