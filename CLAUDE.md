# Stranger Things Calculator - Root Orchestration Guide

## Overview
This document orchestrates the development of a Stranger Things-themed calculator web application with:
- **Frontend**: React NextJS (port 3004) - HIGHLY ANIMATED, JSON-driven theme
- **Backend**: Python FastAPI (port 8004) - Zero external deps, 100% test coverage
- **Orchestration**: Docker Compose - Hot-reload volumes, service networking

## Critical Requirement: REGRESSION.md
**Before creating any PR**, developers must complete ALL sections of [REGRESSION.md](./REGRESSION.md):
- Phase 1: Local dev setup (backend + frontend running locally)
- Phase 2: CORS & integration testing (frontend → backend communication)
- Phase 3: Testing (unit + API + e2e tests pass)
- Phase 4: Docker orchestration (docker compose up works)
- Phase 5: Code quality (PEP8, TypeScript strict, SCSS)
- Phase 6: Git preparation (clean commits, no debug code)

**FAIL to run REGRESSION.md = risk of GitHub issues like #3 (CORS/env var failures).**

## Execution Strategy: 3 Phases

### Phase 1 & 2: Frontend + Backend (PARALLEL)
Spawn two agents simultaneously:
1. **Frontend Agent** (NextJS Specialist) → reads `frontend/CLAUDE.md` (7 phases)
2. **Backend Agent** (FastAPI Specialist) → reads `backend/CLAUDE.md` (8 phases)

**Why parallel?** Independent codebases, no cross-dependencies.
**Time**: Both run simultaneously (not sequential) → 5-10x faster.

### Phase 3: Docker (SEQUENTIAL after Phase 1 & 2)
Once Frontend + Backend agents complete:
1. **DevOps Agent** → reads `CREATE.md` (4 phases)

**Why sequential?** Docker needs working frontend/backend code.

## Phase 1 & 2 Execution (Parallel)

### Frontend Agent (NextJS Specialist)
**Command** (in main agent):
```
Spawn Frontend Agent to read frontend/CLAUDE.md and execute 7 phases:
1. Setup (NextJS project init)
2. Theme & Layout (Stranger Things JSON config + SCSS)
3. Core Component (Calculator UI)
4. Animations (framer-motion, 60fps)
5. Backend Integration (CORS testing, .env setup)
6. Testing (Playwright e2e tests)
7. Review (TypeScript strict, build succeeds)
```

**Deliverables**:
- ✅ frontend/ directory with NextJS project
- ✅ Stranger Things theme fully animated
- ✅ JSON-driven configuration
- ✅ CORS integration tested
- ✅ Playwright e2e tests passing
- ✅ Build succeeds

### Backend Agent (FastAPI Specialist)
**Command** (in main agent):
```
Spawn Backend Agent to read backend/CLAUDE.md and execute 8 phases:
1. Setup (FastAPI project init)
2. Main App (FastAPI instance + CORS middleware)
3. Routes (separate files: add.py, subtract.py, multiply.py, divide.py)
4. Unit Tests (5+ per operation)
5. API Tests (5+ per endpoint)
6. Regression Suite (all tests + 100% coverage)
7. Code Quality (PEP8, docstrings, type hints)
8. Documentation (README, endpoint docs)
```

**Deliverables**:
- ✅ backend/ directory with FastAPI project
- ✅ 4 separate route files imported in main.py
- ✅ CORS middleware configured
- ✅ Unit tests (100% coverage)
- ✅ API tests (all endpoints)
- ✅ PEP8-compliant code with type hints

## Phase 3 Execution (Sequential after Phase 1 & 2)

### DevOps Agent (Docker Specialist)
**Command** (after Frontend + Backend complete):
```
Spawn DevOps Agent to read CREATE.md and execute 4 phases:
1. Frontend Dockerfile (node:18-alpine, hot-reload)
2. Backend Dockerfile (python:3.11-slim, hot-reload)
3. docker-compose.yaml (service networking, env setup)
4. Integration Testing (verify docker compose up works)
```

**Deliverables**:
- ✅ frontend/Dockerfile (Node 18-alpine)
- ✅ backend/Dockerfile (Python 3.11-slim)
- ✅ docker-compose.yaml (service network, volumes)
- ✅ .env and .env.local documented
- ✅ docker compose up succeeds
- ✅ Services communicate (frontend → backend)

## Parallelization Strategy

### Why Parallelization?
1. **Performance**: Independent tasks run simultaneously → 5-10x faster than sequential
2. **Context Management**: Each subagent gets fresh context; outputs don't bloat main agent
3. **Responsiveness**: Main agent continues work while subagents run

### Implementation Pattern
**Single message with multiple subagent spawns:**
```
Spawn Frontend + Backend agents in SAME message:
- Agent 1: Frontend (run_in_background=true)
- Agent 2: Backend (run_in_background=true)
Main agent continues; subagents run in parallel.
Collect results when both complete.
```

**Do NOT spawn sequentially** (wait, spawn, wait, spawn) — that defeats parallelization.

## Quality Gates

Each phase must pass before advancing:

### Phase 1 & 2 Quality Gates
- ✅ **Frontend**: Build succeeds, Playwright tests pass, CORS validated
- ✅ **Backend**: Pytest 100% coverage, all API tests pass, PEP8 compliant
- ✅ **Both**: /nextjs-validator and /fastapi-validator report PASS

### Phase 3 Quality Gate
- ✅ **Docker**: `/docker-validator` reports PASS
- ✅ **docker compose up** succeeds without errors
- ✅ Services communicate (frontend ↔ backend)
- ✅ Health checks pass

## Pre-PR Checklist (REGRESSION.md)
Before any pull request:
1. ✅ Run REGRESSION.md all sections
2. ✅ All tests pass (unit + API + e2e)
3. ✅ CORS validated (curl + browser)
4. ✅ docker compose up works
5. ✅ No hardcoded localhost/ports
6. ✅ Code quality checks pass
7. ✅ Commits are clean (no debug code)

See [REGRESSION.md](./REGRESSION.md) for detailed checklist.

## Files Generated
- `.claude/agents/` - 5 agent definitions
- `.claude/skills/` - 3 validator skills (nextjs, fastapi, docker)
- `frontend/CLAUDE.md` - Frontend 7-phase guide
- `backend/CLAUDE.md` - Backend 8-phase guide
- `CREATE.md` - Docker 4-phase guide
- `REGRESSION.md` - Pre-PR checklist
- `STARTUP.md` - Service startup guide
- `.env.example` - Production environment template
- `.env.local.example` - Development environment template
- `.github/pull_request_template.md` - PR template with REGRESSION.md reference

## Commands for Development

### Local Development (3 services)
```bash
# Terminal 1: Backend
cd backend && python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 main.py  # Runs on localhost:8004

# Terminal 2: Frontend
cd frontend && npm install && npm run dev  # Runs on localhost:3004

# Terminal 3: Test Backend
cd backend && python3 -m pytest tests/ -v --tb=short

# Terminal 4: Test Frontend
cd frontend && npm run test  # or Playwright
```

### Docker Development (with Compose)
```bash
# Start both services + hot-reload
docker compose up

# In separate terminal, verify services
curl http://localhost:8004/health
curl http://localhost:3004

# Run tests inside containers (optional)
docker compose exec backend pytest tests/ -v
docker compose exec frontend npm run test
```

## Troubleshooting

### CORS Issues
- See [STARTUP.md](./STARTUP.md) CORS troubleshooting section
- Validate CORS headers with: `curl -H "Origin: http://localhost:3004" http://localhost:8004/add?num1=5&num2=3 -v`
- Check backend CORS middleware configuration (fastapi.middleware.cors.CORSMiddleware)
- Check frontend .env.local (NEXT_PUBLIC_API_URL must point to backend)

### Services Not Starting
- Check docker-compose.yaml for typos in service names, ports, volumes
- Verify Dockerfiles build: `docker build -t frontend:latest frontend/`
- Check logs: `docker compose logs frontend` or `docker compose logs backend`

### Tests Failing
- Run REGRESSION.md Phase 1 & 2 locally (outside Docker)
- Verify backend responds: `curl http://localhost:8004/health`
- Verify frontend loads: `curl http://localhost:3004`
- Check environment variables (.env vs .env.local)

## References
- **INSTRUCTIONS.md** - Original project specification
- **REGRESSION.md** - Pre-PR checklist (MANDATORY)
- **STARTUP.md** - Service startup & env var setup
- **frontend/CLAUDE.md** - Frontend 7-phase guide
- **backend/CLAUDE.md** - Backend 8-phase guide
- **CREATE.md** - Docker 4-phase guide

## Next Steps
1. Run REGRESSION.md to verify local setup
2. Review agent definitions in `.claude/agents/`
3. Read domain guides (frontend/CLAUDE.md, backend/CLAUDE.md)
4. Execute Phase 1 & 2 (Frontend + Backend agents in parallel)
5. Execute Phase 3 (Docker agent)
6. Run REGRESSION.md again before creating PR
7. Create PR with confidence that all integration tests pass
