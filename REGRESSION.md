# Pre-PR Regression Checklist

**Every feature branch must pass ALL checks before creating a PR.**

This checklist should be completed BEFORE pushing code to remote or opening a pull request.

## Phase 1: Local Development Setup

### Backend
- [ ] `cd backend && python3 main.py` starts without errors
- [ ] `curl http://localhost:8004/health` returns `{"status":"ok"}`
- [ ] `curl http://localhost:8004/add?num1=5&num2=3` returns `{"result":8}`
- [ ] All backend routes respond (/add, /subtract, /multiply, /divide)
- [ ] Backend logs show no errors

### Frontend
- [ ] `cd frontend && npm install` completes
- [ ] `npm run dev` starts without errors
- [ ] `curl http://localhost:3004/` returns HTML (calculator page loads)
- [ ] Browser shows no console errors
- [ ] All UI components render (buttons, display, animations)

### Environment Variables
- [ ] Frontend `.env.local` exists with `NEXT_PUBLIC_API_URL=http://localhost:8004`
- [ ] Frontend `.env` has `NEXT_PUBLIC_API_URL=http://backend:8004` (for Docker)
- [ ] Backend `.env` configured correctly (DEBUG=True, PORT=8004)

## Phase 2: CORS & Integration Testing

### CORS Headers
```bash
# Backend must send CORS headers for localhost origin
curl -H "Origin: http://localhost:3004" -v http://localhost:8004/health
```
- [ ] Response includes: `Access-Control-Allow-Origin: http://localhost:3004`
- [ ] Response includes: `Access-Control-Allow-Methods: *`
- [ ] Response includes: `Access-Control-Allow-Headers: *`

### Frontend→Backend Communication
With both services running:
- [ ] Open browser DevTools → Network tab
- [ ] Click calculator button (e.g., "5")
- [ ] Perform operation (e.g., "+" then "3")
- [ ] Click "="
- [ ] Network tab shows XHR request to `http://localhost:8004/add`
- [ ] Response is `{"result":8,...}` (no CORS error)
- [ ] Display shows result: `8`

### End-to-End Operations
- [ ] 5 + 3 = 8 ✓
- [ ] 10 - 4 = 6 ✓
- [ ] 6 × 7 = 42 ✓
- [ ] 20 ÷ 4 = 5 ✓
- [ ] 10 ÷ 0 = E (error) ✓
- [ ] Clear (AC) button resets to 0 ✓
- [ ] Delete (DEL) removes last digit ✓

## Phase 3: Testing Requirements

### Backend Tests (per `backend/CLAUDE.md` Phase 4-6)
```bash
cd backend
pip install -r requirements.txt
pytest tests/test_units.py -v    # Unit tests
pytest tests/test_api.py -v      # API tests
pytest tests/ --cov -v           # Coverage check
```
- [ ] All unit tests pass
- [ ] All API tests pass
- [ ] Coverage is 100%
- [ ] No deprecation warnings

### Frontend Tests (per `frontend/CLAUDE.md` Phase 6-7)
```bash
cd frontend
npm run type-check    # TypeScript strict mode
npm run build         # Build succeeds
npm run test          # Playwright tests pass
```
- [ ] TypeScript: 0 errors, 0 warnings
- [ ] Build: Completes without errors
- [ ] Playwright: All tests pass
- [ ] No console errors during test run

## Phase 4: Docker Orchestration (per `CREATE.md`)

### Docker Compose
```bash
docker compose up -d
docker compose ps
docker compose logs
```
- [ ] `docker compose up` starts without errors
- [ ] All services show "Up" status: `docker compose ps`
- [ ] No critical errors in logs: `docker compose logs`

### Service Communication in Docker
```bash
curl http://localhost:3004/          # Frontend via proxy
curl http://localhost:8004/health    # Backend directly
docker compose exec frontend sh -c 'echo $NEXT_PUBLIC_API_URL'
```
- [ ] Frontend loads at http://localhost:3004
- [ ] Backend health at http://localhost:8004
- [ ] Frontend env var shows `http://backend:8004`
- [ ] Both ports mapped correctly in docker-compose.yaml

### End-to-End in Docker
- [ ] Open http://localhost:3004 in browser
- [ ] Calculator loads with Stranger Things theme
- [ ] Click calculator: 7 + 8 = 15 ✓
- [ ] Result displays correctly
- [ ] No network errors in DevTools
- [ ] Browser console: 0 errors

## Phase 5: Code Quality (per `CLAUDE.md`)

### Backend
- [ ] `autopep8 --check -r backend/` - PEP8 compliant
- [ ] All functions have docstrings
- [ ] Type hints on all parameters and returns

### Frontend
- [ ] No `any` types in TypeScript
- [ ] All components properly typed
- [ ] No hardcoded URLs (use NEXT_PUBLIC_API_URL)
- [ ] Animations smooth (60fps, no jank)

## Phase 6: Git & PR Preparation

### Branch & Commit
- [ ] Branch name: `fix/issue-<number>` or `feature/<name>`
- [ ] Commits reference CLAUDE.md phases: "Per Phase X..."
- [ ] No merge commits (rebase before pushing)
- [ ] Commit messages follow format: `fix: description\n\nFixes #<number>`

### Before Push
```bash
git status                    # No uncommitted changes
git log --oneline -5          # Commit messages clear
git diff origin/main...HEAD   # Review all changes
```
- [ ] All changes staged and committed
- [ ] No debug code (console.log, print statements)
- [ ] No commented-out code
- [ ] No .env.local or secrets committed

## Sign-Off

When ALL checks pass:

```
✅ Local dev: backend + frontend working
✅ Integration: CORS working, frontend↔backend communicating
✅ Tests: unit + API + Playwright all passing
✅ Docker: services running and communicating
✅ Code: typed, documented, PEP8/linted
✅ Git: commits clean, branch ready for PR
```

**Only then**: Create PR and link to this checklist in the description.

## Troubleshooting

If any check fails, do NOT create PR. Debug on the feature branch first:

| Issue | Solution |
|-------|----------|
| Backend won't start | Check requirements.txt, python3 version, port 8004 in use |
| Frontend won't load | Check npm dependencies, .env.local, port 3004 in use |
| CORS error | Verify backend CORS middleware allows frontend origin |
| API call fails | Check NEXT_PUBLIC_API_URL in .env.local, curl test endpoint |
| Docker fail | Run `docker compose config`, check docker-compose.yaml syntax |
| Test failures | Review test output, check CLAUDE.md Phase for fix |

## Reference

- **CLAUDE.md** - Project overview and phases
- **frontend/CLAUDE.md** - Frontend development phases
- **backend/CLAUDE.md** - Backend development phases
- **CREATE.md** - Docker orchestration phases
- **STARTUP.md** - Service startup guide

---

**Last Updated**: 2026-03-21
**Purpose**: Prevent integration issues from reaching GitHub
**Ownership**: Every developer before creating PR
