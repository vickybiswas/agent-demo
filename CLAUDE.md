# Stranger Things Calculator - Root Orchestration Guide

A Stranger Things-themed calculator with React/NextJS frontend (3004) and Python FastAPI backend (8004), orchestrated with Docker Compose.

## Project Overview

- **Frontend**: TypeScript React/NextJS with framer-motion animations, SCSS, JSON-driven theme (port 3004)
- **Backend**: Python FastAPI with PEP8 code, separate route files, 100% test coverage (port 8004)
- **Orchestration**: Docker Compose for local dev and CI/CD with hot-reload volumes
- **Quality Gate**: REGRESSION.md checklist required before any PR

## 3-Step Orchestration (Parallelization Strategy)

### ⭐ Key Principle: Parallel Execution
Frontend and Backend agents work **simultaneously**, not sequentially. This prevents context bloat and ensures 5-10x faster execution.

### Step 1: Frontend + Backend (PARALLEL)
Spawn BOTH agents in SAME message with `run_in_background=true`:

1. **Frontend Agent** (reads `frontend/CLAUDE.md`):
   - Phase 1: NextJS setup, TypeScript strict mode
   - Phase 2: JSON-driven theme, SCSS styling
   - Phase 3: Calculator component with interactions
   - Phase 4: Animations (framer-motion, sounds, effects)
   - Phase 5: **CORS Testing** - validate frontend ↔ backend communication
   - Phase 6: Playwright e2e tests
   - Phase 7: TypeScript strict validation, build succeeds

2. **Backend Agent** (reads `backend/CLAUDE.md`):
   - Phase 1: FastAPI project setup, requirements.txt (fastapi + uvicorn)
   - Phase 2: FastAPI app with CORS middleware
   - Phase 3: Separate route files (add.py, subtract.py, multiply.py, divide.py)
   - Phase 4: Unit tests (5+ per function, edge cases)
   - Phase 5: API tests (5+ per endpoint, CORS headers validation)
   - Phase 6: Regression test suite (100% coverage)
   - Phase 7: PEP8 compliance, docstrings, type hints
   - Phase 8: Documentation and edge case handling

**Both agents execute independently and in parallel. Main agent continues while they run.**

### Step 2: Docker Orchestration (SEQUENTIAL - after Step 1 completes)
Once both Frontend and Backend agents complete, spawn **DevOps agent** (reads `CREATE.md`):

1. **DevOps Agent** (reads `CREATE.md`):
   - Phase 1: Frontend Dockerfile (node:18-alpine)
   - Phase 2: Backend Dockerfile (python:3.11-slim)
   - Phase 3: docker-compose.yaml with service networking
   - Phase 4: Integration testing (services communicate, CORS works, calculator operates)
   - Phase 5: Environment variables (.env.example, .env.local.example)

**No parallelization here—Docker depends on working frontend and backend code.**

### Step 3: Quality Gate (REGRESSION.md)
After all agents complete:

1. **QA Agent** (or manual): Run REGRESSION.md checklist
   - Phase 1: Local dev setup (backend, frontend, env vars)
   - Phase 2: CORS & integration testing (frontend ↔ backend communication)
   - Phase 3: Unit & API tests passing (100% coverage)
   - Phase 4: Frontend tests passing (TypeScript, build, Playwright)
   - Phase 5: Docker orchestration verified
   - Phase 6: Code quality checks (PEP8, docstrings, no debug code)

**REGRESSION.md is MANDATORY before PR. Failing this blocks PR creation.**

## File Structure

```
.
├── CLAUDE.md                      # Root orchestration (this file)
├── CREATE.md                      # Docker phases guide
├── REGRESSION.md                  # Pre-PR checklist (MANDATORY)
├── STARTUP.md                     # Service startup & troubleshooting
├── .env.example                   # Docker Compose env vars
├── .env.local.example             # Local dev env vars
├── .github/
│   └── pull_request_template.md   # Links to REGRESSION.md
├── .claude/
│   ├── agents/
│   │   ├── 1-pr-review.md
│   │   ├── 2-fastapi-specialist.md
│   │   ├── 3-nextjs-specialist.md
│   │   ├── 4-devops-specialist.md
│   │   └── 5-qa-specialist.md
│   └── skills/
│       ├── fastapi-validator/SKILL.md
│       ├── nextjs-validator/SKILL.md
│       └── docker-validator/SKILL.md
├── frontend/
│   ├── CLAUDE.md                  # 7-phase frontend guide
│   ├── Dockerfile
│   ├── pages/, components/, styles/
│   ├── __tests__/                 # Playwright tests
│   └── tsconfig.json (strict mode)
└── backend/
    ├── CLAUDE.md                  # 8-phase backend guide
    ├── Dockerfile
    ├── main.py                    # FastAPI app + CORS
    ├── routes/                    # Separate route files
    ├── tests/                     # Unit + API tests
    └── requirements.txt           # fastapi, uvicorn ONLY
```

## Parallelization Strategy Details

### Why Parallel Execution Matters

1. **Performance**: Frontend + Backend execute simultaneously → ~5-10x faster
2. **Context Management**: Each subagent gets fresh context; outputs don't accumulate in main agent
3. **Main Agent Responsive**: Continues work while subagents run in background

### Implementation Pattern (DO THIS)

```
✅ Correct: Spawn in SAME message
Agent 1 (background)
Agent 2 (background)
Agent 3 (background)
# Main agent continues; all 3 execute in parallel

❌ Incorrect: Sequential spawning
Agent 1 (wait for completion) ← Blocks
Agent 2 (wait for completion) ← Waits for #1
Agent 3 (wait for completion) ← Waits for #2
# Slow + context bloat
```

### Phase-Level Parallelization

**Step 1 (Frontend + Backend PARALLEL)**:
- Frontend builds components, animations, tests
- Backend builds routes, tests, coverage
- Both independent → run together

**Step 1 Within-Phase Testing (PARALLEL)**:

**Backend Testing Phase**:
- Unit tests for add (all together)
- Unit tests for subtract (all together)
- Unit tests for multiply (all together)
- Unit tests for divide (all together)
- All four spawn together, collect results when done

**Frontend Testing Phase**:
- TypeScript validation
- NextJS build
- Playwright tests
- All three spawn together, collect results

**Step 2 (Docker SEQUENTIAL)**:
- Must wait for Step 1 completion
- Docker needs working code to build
- No parallelization here

**Step 3 (Regression SEQUENTIAL)**:
- Must wait for Step 2 completion
- Tests Docker orchestration
- Blocks PR until all checks pass

## Quality Gates by Phase

### Frontend Quality Gate (Phase 7)
- ✅ TypeScript strict mode: `npm run type-check` passes
- ✅ Build succeeds: `npm run build` (no warnings/errors)
- ✅ Playwright tests pass: `npx playwright test`
- ✅ CORS integration: frontend ↔ backend works
- ✅ Animations: smooth (60fps, no jank)

### Backend Quality Gate (Phase 8)
- ✅ PEP8 compliant: `autopep8 --check backend/`
- ✅ 100% test coverage: `pytest --cov=routes`
- ✅ All tests pass: `pytest tests/`
- ✅ CORS headers: validated in API tests
- ✅ All endpoints: responding with correct JSON

### Docker Quality Gate (Phase 5)
- ✅ Services start: `docker compose up` (no errors)
- ✅ Frontend accessible: `curl http://localhost:3004`
- ✅ Backend accessible: `curl http://localhost:8004`
- ✅ Frontend ↔ Backend: CORS working
- ✅ Calculator operation: 5 + 3 = 8 succeeds

### Regression Quality Gate (Phase 6)
- ✅ All REGRESSION.md checks pass
- ✅ Local dev setup works
- ✅ CORS integration confirmed
- ✅ All unit/API/e2e tests passing
- ✅ Docker orchestration verified
- ✅ Code quality checks passed

## Commands

### Build (Spawn Agents)

```bash
# Step 1: Spawn Frontend + Backend TOGETHER (parallel)
# In Claude Code:
# /Agent @frontend-specialist frontend/CLAUDE.md (background)
# /Agent @backend-specialist backend/CLAUDE.md (background)
# Then wait ~15-20 mins for both to complete

# Step 2: Spawn Docker orchestration (sequential, after Step 1)
# /Agent @devops-specialist CREATE.md (background)
# Wait ~5-10 mins

# Step 3: Verify with REGRESSION.md
# Complete all checks manually or spawn QA agent
# /Agent @qa-specialist REGRESSION.md
```

### Start Services (Development)

```bash
# Local development (without Docker)
cd backend && python main.py     # Terminal 1: http://localhost:8004
cd frontend && npm run dev       # Terminal 2: http://localhost:3004
# Or use STARTUP.md for detailed instructions

# Docker Compose (complete stack)
docker compose up
# Frontend: http://localhost:3004
# Backend: http://localhost:8004
```

### Test

```bash
# Backend tests
cd backend && pytest tests/ --cov=routes

# Frontend tests
cd frontend && npx playwright test

# Integration tests
./tests/integration.sh    # If exists

# Docker health check
docker compose ps         # All services Up
curl http://localhost:8004/health
curl http://localhost:3004
```

## Before Creating a PR

**MANDATORY: Complete REGRESSION.md checklist**

✅ Phase 1: Local setup verified
✅ Phase 2: CORS & integration tested
✅ Phase 3: All tests passing (100% coverage)
✅ Phase 4: Frontend validation complete
✅ Phase 5: Docker orchestration working
✅ Phase 6: Code quality checks passed

**Only after ALL checks pass, create PR.**

## References

- **Frontend Setup**: `frontend/CLAUDE.md` (7 phases)
- **Backend Setup**: `backend/CLAUDE.md` (8 phases)
- **Docker Setup**: `CREATE.md` (5 phases)
- **Pre-PR Checklist**: `REGRESSION.md` (6 phases, MANDATORY)
- **Service Startup**: `STARTUP.md` (3 options + troubleshooting)
- **Validators**:
  - `/fastapi-validator` - Backend code quality
  - `/nextjs-validator` - Frontend code quality
  - `/docker-validator` - Docker orchestration

## Notes

- Parallelization is CRITICAL for performance—spawn independent work together, not sequentially
- Each agent reads ONE file (no cross-file coordination needed)
- REGRESSION.md is MANDATORY—failing it blocks PR
- Environment variables differ between .env (Docker) and .env.local (local dev)
- All tests must pass before PR—this is enforced by PR template linking to REGRESSION.md
