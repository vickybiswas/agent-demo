# Regression Testing Checklist

## ⚠️ MANDATORY PRE-PR VALIDATION

**This checklist MUST be completed before creating any pull request.**

Incomplete regressions have caused integration failures in the past (Issue #3). This guide prevents those issues by requiring developers to test:
1. Backend service starts
2. Frontend service starts
3. CORS headers correct
4. End-to-end operation works
5. Docker Compose setup works
6. Code quality passes

**Estimated Time**: 15-20 minutes
**All steps MUST pass before PR creation**

---

## Phase 1: Local Backend Setup

### Step 1: Navigate to Backend
```bash
cd backend
```

### Step 2: Install Dependencies
```bash
pip install fastapi uvicorn pytest pytest-cov
```

### Step 3: Start Backend Service
```bash
python3 main.py
```

### Step 4: Verify Backend Starts
Expected output:
```
Uvicorn running on http://0.0.0.0:8004
```

### Step 5: Test Health Endpoint (New Terminal)
```bash
curl http://localhost:8004/health
```

Expected response:
```json
{"status": "ok"}
```

### ✅ Checklist Item 1
- [x] Backend service starts without errors
- [x] Health endpoint returns 200 OK
- [x] Port 8004 is listening

**Keep backend running for Phase 2**

---

## Phase 2: Local Frontend Setup

### Step 1: Navigate to Frontend (New Terminal)
```bash
cd frontend
```

### Step 2: Install Dependencies
```bash
npm install
```

### Step 3: Create Environment File
Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8004
```

### Step 4: Start Frontend Service
```bash
npm run dev
```

### Step 5: Verify Frontend Starts
Expected output:
```
> next dev
  ▲ Next.js 14.x.x
  - Local:        http://localhost:3004
```

### ✅ Checklist Item 2
- [x] Frontend service starts without errors
- [x] Development server running on :3004
- [x] Next.js build succeeds

**Both services now running in separate terminals**

---

## Phase 3: CORS & Integration Testing

### Step 1: Verify CORS Headers
```bash
curl -v http://localhost:8004/add?num1=5&num2=3
```

### Step 2: Check for CORS Headers
Look for these headers in the response:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

### Step 3: Test with Frontend Origin
```bash
curl -H "Origin: http://localhost:3004" \
     -H "Access-Control-Request-Method: GET" \
     http://localhost:8004/add?num1=5&num2=3
```

Expected: CORS headers present

### Step 4: Test Frontend → Backend Communication
Open browser: `http://localhost:3004`

Perform calculation: **5 + 3**

Expected result: **8**

### Step 5: Verify in Browser Console
Open Developer Tools (F12):
- Check Network tab: GET to http://localhost:8004/add should return 200
- Check Console: No CORS errors
- Check Response: Should show `{"result": 8}`

### ✅ Checklist Item 3
- [x] CORS headers present in responses
- [x] Frontend can call backend endpoints
- [x] End-to-end operation works (5 + 3 = 8)
- [x] No CORS errors in browser console

---

## Phase 4: Testing Requirements

### Backend Unit Tests (Run in backend terminal)
Stop the backend server (Ctrl+C) and run:
```bash
python3 -m pytest tests/test_*_unit.py -v
```

Expected:
- All tests pass (5+ per operation)
- No failures

### Backend API Tests
```bash
python3 -m pytest tests/test_*_api.py -v
```

Expected:
- All tests pass (5+ per endpoint)
- No failures

### Backend Coverage
```bash
python3 -m pytest tests/ -v --cov=backend/operations --cov-report=term-missing
```

Expected:
- 100% coverage on operations/
- No missing lines

### Frontend Tests (Run in frontend terminal)
```bash
npm test
```

Expected:
- All Playwright E2E tests pass
- Responsive design tests pass
- CORS communication tests pass

### ✅ Checklist Item 4
- [x] Backend unit tests: all pass, 100% coverage
- [x] Backend API tests: all pass
- [x] Frontend E2E tests: all pass
- [x] No test failures

---

## Phase 5: Docker Compose Verification

### Step 1: Stop Local Services
Stop both backend and frontend (Ctrl+C in both terminals)

### Step 2: Start Docker Compose
```bash
docker compose up -d
```

Wait 10-15 seconds for services to fully start.

### Step 3: Verify Frontend in Docker
```bash
curl http://localhost:3004/
```

Expected: HTML response (NextJS page)

### Step 4: Verify Backend Health in Docker
```bash
curl http://localhost:8004/health
```

Expected:
```json
{"status": "ok"}
```

### Step 5: Test Endpoint in Docker
```bash
curl "http://localhost:8004/add?num1=5&num2=3"
```

Expected:
```json
{"result": 8}
```

### Step 6: View Docker Logs
```bash
docker compose logs -f
```

Expected: No error messages, both services running

### Step 7: Cleanup
```bash
docker compose down
```

### ✅ Checklist Item 5
- [x] Docker Compose starts both services
- [x] Frontend accessible on :3004
- [x] Backend accessible on :8004
- [x] Health check passes
- [x] CORS headers present
- [x] End-to-end operation works

---

## Phase 6: Code Quality

### Backend Code Quality
```bash
cd backend

# PEP8 compliance
autopep8 --diff *.py operations/*.py

# Type checking
python3 -m mypy main.py operations/ --ignore-missing-imports

# No debug code
grep -r "print(" *.py operations/*.py  # Should show no print statements

# Docstrings present
grep -c "def " main.py operations/*.py
grep -c '"""' main.py operations/*.py  # Should have docstrings
```

### Frontend Code Quality
```bash
cd frontend

# TypeScript strict mode
npm run type-check

# Linting
npm run lint

# Build succeeds
npm run build

# No console errors
npm run build 2>&1 | grep -i error
```

### ✅ Checklist Item 6
- [x] Backend: PEP8 compliant
- [x] Backend: Type hints complete
- [x] Backend: Docstrings present
- [x] Frontend: TypeScript strict mode passes
- [x] Frontend: Build succeeds
- [x] Frontend: No console errors
- [x] Frontend: Prettier formatted

---

## Final Checklist Before PR

- [x] **Phase 1**: Backend service starts and health check passes
- [x] **Phase 2**: Frontend service starts and builds successfully
- [x] **Phase 3**: CORS headers verified, end-to-end operation works (5 + 3 = 8)
- [x] **Phase 4**: All unit tests pass (100% coverage), all API tests pass, E2E tests pass
- [x] **Phase 5**: Docker Compose starts both services, CORS verified in Docker, operation works
- [x] **Phase 6**: Code quality passes (PEP8, type hints, docstrings, no build errors)

---

## PR Submission

### Before Creating PR
1. Make sure all items above are checked ✅
2. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: Add calculator operations"
   ```
3. Push to feature branch:
   ```bash
   git push origin feature/calculator-operations
   ```

### When Creating PR
1. GitHub PR template includes this checklist
2. Verify all items completed
3. Provide evidence (test screenshots, curl outputs)
4. Request code review

### During Review
- Reviewer verifies REGRESSION.md checklist
- Reviewer checks all tests pass
- Reviewer validates CORS communication
- Reviewer approves merge

---

## Troubleshooting

### Backend Fails to Start
```bash
# Check if port 8004 is in use
lsof -i :8004

# Kill process using port
kill -9 <PID>

# Restart
python3 main.py
```

### Frontend Fails to Build
```bash
# Clear cache
rm -rf .next node_modules package-lock.json

# Reinstall
npm install
npm run build
```

### CORS Errors
```bash
# Check backend CORS middleware
grep -n "CORSMiddleware" backend/main.py

# Verify allowed origins include localhost:3004
grep -A5 "CORSMiddleware" backend/main.py
```

### Docker Services Won't Start
```bash
# Clean up and rebuild
docker compose down -v
docker compose build --no-cache
docker compose up -d
```

---

## Success = Ready to PR ✅

When all 6 phases are complete, you're ready to create a PR:
- Backend and frontend both working
- All tests passing with 100% coverage
- CORS communication verified
- Docker setup validated
- Code quality standards met

**Do NOT create PR without completing this checklist.**

---

## References

- **CLAUDE.md**: Full project orchestration
- **CREATE.md**: Docker setup phases
- **STARTUP.md**: Service startup options
- **.env.example**: Example environment variables
- **.env.local.example**: Local development setup

---

**⏱️ Estimated Time**: 15-20 minutes
**📋 Required**: Yes, for every PR
**🎯 Goal**: Catch integration issues before PR, not after
