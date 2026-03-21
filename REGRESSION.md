# REGRESSION.md - Pre-PR Quality Checklist

**MANDATORY**: Complete ALL phases before creating a PR. This checklist prevents integration issues from reaching GitHub.

## Phase 1: Local Development Setup

Verify your development environment is configured correctly.

- [ ] Backend dependencies installed: `cd backend && pip install -r requirements.txt`
- [ ] Frontend dependencies installed: `cd frontend && npm install`
- [ ] `.env.local` file exists with correct values:
  ```
  API_URL=http://localhost:8004
  NEXT_PUBLIC_API_URL=http://localhost:8004
  NODE_ENV=development
  ```
- [ ] Backend starts successfully: `python main.py` listens on 8004
- [ ] Frontend starts successfully: `npm run dev` listens on 3004
- [ ] No errors in either terminal during startup

## Phase 2: CORS & Integration Testing

Verify frontend and backend can communicate across ports.

**Backend Health Check**:
```bash
curl http://localhost:8004/health
# Expected: {"status": "ok"} or similar 200 response
```

**CORS Header Validation**:
```bash
curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3
# Expected: 200 OK with CORS headers:
# Access-Control-Allow-Origin: http://localhost:3004
# Access-Control-Allow-Credentials: true
```

**API Response Validation**:
```bash
curl http://localhost:8004/add?num1=5&num2=3
# Expected: {"result": 8}
```

- [ ] Backend /health endpoint responds (HTTP 200)
- [ ] Backend /add endpoint responds (HTTP 200)
- [ ] CORS headers present in response
- [ ] Response JSON format correct: `{"result": value}`
- [ ] Frontend loads without CORS errors in browser console (F12 → Console)
- [ ] Calculator operation in browser works: 5 + 3 = 8 displays correctly

## Phase 3: Unit & API Tests (100% Coverage)

Verify all backend code is tested.

**Run Backend Tests**:
```bash
cd backend && pytest tests/ -v
```

**Run Coverage Check**:
```bash
cd backend && pytest tests/ --cov=routes --cov-report=term-missing
```

- [ ] Unit tests pass: `test_*_unit.py` files all green
- [ ] API tests pass: `test_*_api.py` files all green
- [ ] Coverage >= 100%: `pytest --cov=routes` shows 100%
- [ ] No skipped tests (no `.skip`, `.xfail`, `.only` decorators)
- [ ] All edge cases covered:
  - Division by zero handled
  - Negative numbers work
  - Decimal numbers work
  - Large numbers work
- [ ] CORS headers validated in API tests
- [ ] Error responses tested (422 for invalid inputs, 500 for errors)

## Phase 4: Frontend Tests

Verify frontend code quality and functionality.

**TypeScript Strict Mode**:
```bash
cd frontend && npm run type-check
```

**Build Check**:
```bash
cd frontend && npm run build
```

**Playwright Tests**:
```bash
cd frontend && npx playwright test
```

**Browser Console Check**:
- Open http://localhost:3004 in browser
- Open DevTools (F12) → Console tab
- Perform a calculation (5 + 3)
- Verify no errors or warnings in console

- [ ] TypeScript strict mode: `npm run type-check` passes (no errors)
- [ ] Build succeeds: `npm run build` (no warnings/errors in build output)
- [ ] Playwright tests pass: `npx playwright test` (all green)
- [ ] No TypeScript errors in code (strict mode enabled)
- [ ] No console errors when performing calculations
- [ ] Animations smooth: no stuttering during button clicks
- [ ] Sound effects play on interaction
- [ ] Calculator displays result correctly after operation

## Phase 5: Docker Orchestration

Verify the complete stack works in Docker.

**Start Docker Compose**:
```bash
docker compose up -d
sleep 3  # Wait for services to start
```

**Verify Services Running**:
```bash
docker compose ps
# Expected: All services Up (not Exit code X or Exited)
```

**Test Backend Health**:
```bash
curl http://localhost:8004/health
```

**Test Frontend Access**:
```bash
curl http://localhost:3004
# Expected: HTTP 200 with HTML content
```

**Test End-to-End Operation**:
```bash
# Option 1: curl from CLI
curl http://localhost:8004/add?num1=5&num2=3

# Option 2: Open browser and test
# http://localhost:3004 → calculator UI → click 5 + 3 = 8
```

**Cleanup**:
```bash
docker compose down
```

- [ ] All services listed in `docker compose ps` show "Up" status
- [ ] Backend responds to health check (HTTP 200)
- [ ] Frontend responds to HTTP request (HTTP 200)
- [ ] Frontend ↔ Backend communication works (no CORS errors)
- [ ] Calculator operation succeeds in Docker (5 + 3 = 8)
- [ ] No error logs in service output
- [ ] Services start within 10 seconds
- [ ] Port conflicts resolved (3004, 8004 available)
- [ ] Environment variables correctly loaded (.env file used)

## Phase 6: Code Quality

Verify code follows best practices.

**Backend PEP8 Check**:
```bash
cd backend && autopep8 --check --aggressive --aggressive . > /dev/null && echo "✅ PEP8 OK" || echo "❌ PEP8 violations"
```

**Backend Code Review**:
- [ ] No debug `print()` statements
- [ ] No commented-out code blocks
- [ ] Docstrings on all functions
- [ ] Type hints on all functions and parameters
- [ ] Error handling is proper (no bare `except:`)
- [ ] No hardcoded `localhost` in code (uses env vars)
- [ ] No sensitive data in logs

**Frontend Code Review**:
- [ ] No `console.log()` in production code (OK in tests)
- [ ] No commented-out code blocks
- [ ] No unused variables or imports
- [ ] Props properly typed in all components
- [ ] SCSS well-organized (no duplicate selectors, uses variables)
- [ ] JSON theme configuration used (not hardcoded colors)

**General**:
- [ ] No API keys or secrets in code
- [ ] No `TODO` or `FIXME` comments without assignee/date
- [ ] Commit messages are clear and descriptive
- [ ] Branch name is descriptive (e.g., `feature/calculator-frontend`)

## Phase 7: Git Preparation

Prepare changes for PR.

**Git Status**:
```bash
git status
# Expected: Clean working tree or staged changes only
```

**Staging Changes**:
```bash
git add -A
git commit -m "feat: implement Stranger Things calculator with backend and frontend"
# Or more specific commits for different components
```

**Check Commits**:
```bash
git log --oneline -5
# Verify commits are descriptive and logically grouped
```

- [ ] All code changes are staged
- [ ] Commits have clear, descriptive messages
- [ ] No uncommitted changes remain (or intentionally left unstaged)
- [ ] No merge conflicts
- [ ] Branch is up-to-date with main: `git rebase origin/main`
- [ ] Commit history is clean (no accidental commits like "fix typo", "debugging", etc.)

## Phase 8: PR Submission

Create PR with confidence.

**Before Creating PR**:
- [ ] All 7 phases above are COMPLETE and PASSING
- [ ] You have completed REGRESSION.md checklist 100%
- [ ] You can confidently say: "I've tested locally, in Docker, and all tests pass"

**Create PR**:
```bash
gh pr create --title "feat: Stranger Things calculator" --body "Implements calculator with frontend and backend"
# Or use GitHub UI to create PR
```

**PR Template Requirement**:
The PR description MUST include:
```markdown
## Regression Checklist
- [x] Phase 1: Local setup verified
- [x] Phase 2: CORS & integration tested
- [x] Phase 3: All tests passing (100% coverage)
- [x] Phase 4: Frontend validation complete
- [x] Phase 5: Docker orchestration working
- [x] Phase 6: Code quality checks passed
- [x] Phase 7: Git history clean
```

## Troubleshooting

### Backend won't start
```bash
# Check if port 8004 is in use
lsof -i :8004
# Kill process if needed: kill -9 <PID>

# Check Python version
python --version  # Should be 3.9+

# Check dependencies
pip list | grep fastapi
```

### Frontend won't start
```bash
# Check if port 3004 is in use
lsof -i :3004
# Kill process if needed

# Check Node version
node --version  # Should be 18+

# Clear cache
rm -rf node_modules package-lock.json
npm install
```

### CORS errors in browser
- Verify backend is running and accessible: `curl http://localhost:8004/health`
- Check that CORS middleware is configured in FastAPI app
- Browser console (F12) should show exact error message
- Verify frontend is making requests to correct URL (check env var)

### Docker services won't communicate
- Check service names: `backend`, not `localhost:8004` from inside frontend container
- Verify docker-compose.yaml has `depends_on: backend` on frontend service
- Check network: `docker network ls` should show compose network
- View logs: `docker compose logs backend` and `docker compose logs frontend`

## Success Criteria

✅ **YOU ARE READY FOR PR IF**:
- ✅ All 7 phases above show complete checks (all boxes ticked)
- ✅ You ran all tests locally and they passed
- ✅ You tested in Docker and services communicate
- ✅ You verified CORS headers and frontend ↔ backend works
- ✅ Code quality checks pass (PEP8, TypeScript strict, no debug code)
- ✅ You are confident the code is production-ready
- ✅ You understand that PR review will also validate this checklist

## Important Notes

**This checklist is MANDATORY**. Skipping steps or ticking boxes without actually performing them will:
1. Fail PR review (reviewer will test same items)
2. Delay merge by 1-2 days while issues are fixed
3. Potentially break production if issues aren't caught

**Invest 30 minutes NOW to prevent 2 hours of PR review later.** This is time well spent and prevents integration issues from reaching GitHub.
