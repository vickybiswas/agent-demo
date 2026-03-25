# Stranger Things Calculator - Project Orchestration

## Overview
Complete end-to-end orchestration for building a themed calculator with React NextJS frontend and Python FastAPI backend, running on Docker containers.

**Status**: Ready for agent execution via `claude build`

## Prerequisites
- ✅ INSTRUCTIONS.md specifies project requirements
- ✅ Agents configured in `.claude/agents/`
- ✅ Skills configured in `.claude/skills/*/`
- ✅ Local machine has Docker installed

## Project Structure
```
.
├── frontend/              # NextJS React SPA
├── backend/               # FastAPI Python service
├── compose.yaml          # Docker Compose orchestration
├── .env                  # Docker environment
├── .env.local            # Local dev environment
├── REGRESSION.md         # Pre-PR quality checklist (MANDATORY)
├── STARTUP.md            # Service startup guide
├── CREATE.md             # Docker creation phases
└── CLAUDE.md             # This file
```

## Execution Plan

### Phase 1: Frontend Development (Parallel)
**Agent**: React NextJS Specialist
**Duration**: Reads `frontend/CLAUDE.md`
**Parallelization**: STARTS IMMEDIATELY with Phase 2

**What happens**:
1. Create NextJS project with app router
2. Implement Stranger Things themed calculator UI
3. Design SCSS styling system
4. Add framer-motion animations
5. Integrate with FastAPI backend (localhost:8004)
6. Write Playwright E2E tests
7. Run `/nextjs-validator` before completion

**Output**: frontend/ directory with working SPA

### Phase 2: Backend Development (Parallel with Phase 1)
**Agent**: Python FastAPI Specialist
**Duration**: Reads `backend/CLAUDE.md`
**Parallelization**: STARTS IMMEDIATELY with Phase 1

**What happens**:
1. Create FastAPI project with proper structure
2. Implement /add, /subtract, /multiply, /divide endpoints
3. Configure CORS middleware for frontend
4. Write unit tests (5+ per operation)
5. Write API tests (5+ per endpoint)
6. Achieve 100% code coverage
7. Run `/fastapi-validator` before completion

**Output**: backend/ directory with production-ready API

**Synchronization**: Both Phase 1 & 2 run in parallel. Move to Phase 3 only when BOTH complete.

### Phase 3: Docker Orchestration (Sequential after Phase 1 & 2)
**Agent**: DevOps Specialist
**Duration**: Reads `CREATE.md`
**Prerequisites**: Phase 1 & 2 complete

**What happens**:
1. Create Dockerfile for frontend (node:22-alpine)
2. Create Dockerfile for backend (python:3.13-slim)
3. Create docker-compose.yaml with service networking
4. Configure environment variables (.env, .env.local)
5. Test service startup and communication
6. Run `/docker-validator` before completion

**Output**: Complete Docker setup with working services

**Verification**: Frontend ↔ Backend communication verified

### Phase 4: Quality Assurance (Sequential after Phase 3)
**Agent**: QA Automation Specialist
**Duration**: Comprehensive testing

**What happens**:
1. Run backend unit tests (all together, in parallel)
2. Run backend API tests (all together, in parallel)
3. Run backend coverage (after both test suites complete)
4. Run frontend E2E tests (all together, in parallel)
5. Run CORS communication tests
6. Run Docker Compose full-stack tests
7. Verify REGRESSION.md checklist passes

**Output**: Comprehensive test reports, 100% coverage verification

## Parallelization Strategy

### Why Parallelization Matters
1. **Performance**: Frontend + Backend develop simultaneously → 5-10x speedup
2. **Context Management**: Each agent gets fresh context, outputs don't accumulate
3. **Main Agent Responsive**: Continues work while subagents run independently

### Phase-Level Parallelization

#### Frontend + Backend (Phase 1 & 2)
```
Message 1: Spawn Frontend + Backend agents together
/Agent Frontend Specialist with frontend/CLAUDE.md (run_in_background=true)
/Agent Backend Specialist with backend/CLAUDE.md (run_in_background=true)
# Main agent continues; both agents work in parallel
```

#### Within Testing Phases
**Backend Testing** (all parallel, not sequential):
- Unit tests (5 per operation) → spawn all together
- API tests (5 per endpoint) → spawn all together
- Coverage analysis → runs after both complete

**Frontend Testing** (all parallel):
- TypeScript validation
- Build compilation
- Playwright E2E tests
All three spawn together, results collected when done.

**360° Regression Testing** (all parallel):
- Backend service health
- Frontend service startup
- CORS validation
- End-to-end operation
- Docker Compose orchestration
All spawn together in single message.

### Implementation Pattern
```
✅ Correct: Spawn multiple agents/tasks in single message
/Agent Task1 (background)
/Agent Task2 (background)
/Agent Task3 (background)
# Main continues; agents run parallel

❌ Incorrect: Sequential spawning
/Agent Task1  (wait for completion)
/Agent Task2  (wait for completion)
/Agent Task3  (wait for completion, bloats context)
```

## Quality Gates

### Before Frontend Merge
✅ Run `/nextjs-validator`
- TypeScript strict: no errors
- Build succeeds
- Playwright tests pass
- CORS verified

### Before Backend Merge
✅ Run `/fastapi-validator`
- PEP8 compliant
- 100% coverage
- All tests pass
- Docstrings complete

### Before Docker Merge
✅ Run `/docker-validator`
- docker-compose.yaml valid
- Services start
- CORS headers present
- Frontend↔Backend works

### Before ANY PR
✅ Complete REGRESSION.md checklist:
- [ ] Local backend starts (`python3 main.py`)
- [ ] Local frontend starts (`npm run dev`)
- [ ] CORS headers validated (curl)
- [ ] End-to-end operation tested (5 + 3 = 8)
- [ ] Docker Compose starts both services
- [ ] Code quality passes
- [ ] All tests passing

**REGRESSION.md is MANDATORY before PR creation.**

## Directory Structure After Completion
```
.
├── frontend/
│   ├── app/
│   ├── components/
│   ├── styles/
│   ├── tests/
│   ├── config/
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── playwright.config.ts
│   ├── Dockerfile
│   ├── .env.local
│   └── CLAUDE.md

├── backend/
│   ├── main.py
│   ├── operations/
│   │   ├── add.py
│   │   ├── subtract.py
│   │   ├── multiply.py
│   │   └── divide.py
│   ├── tests/
│   │   ├── test_*_unit.py
│   │   └── test_*_api.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── CLAUDE.md

├── compose.yaml
├── .env
├── .env.local
├── .github/
│   └── pull_request_template.md
├── REGRESSION.md
├── STARTUP.md
├── CREATE.md
└── CLAUDE.md
```

## Startup & Deployment

### Local Development
```bash
# Terminal 1: Frontend
cd frontend
npm install
npm run dev
# Accessible on http://localhost:3004

# Terminal 2: Backend
cd backend
pip install -r requirements.txt
python3 main.py
# Accessible on http://localhost:8004/health
```

### Docker (Production)
```bash
# Single command
docker compose up -d

# Monitor services
docker compose logs -f

# Stop
docker compose down
```

**See STARTUP.md for full startup guide.**

## Testing & Validation

### Run All Tests Locally
```bash
# Backend tests (parallel)
python3 -m pytest backend/tests/test_*_unit.py -v &
python3 -m pytest backend/tests/test_*_api.py -v &
wait

# Frontend tests
npm test

# Coverage
python3 -m pytest backend/tests/ --cov=backend/operations
```

### Run Docker Tests
```bash
docker compose up -d
docker compose exec backend python3 -m pytest tests/ -v
npm run test:docker
docker compose down
```

## Integration Testing
Both frontend and backend MUST communicate:
- Frontend calls `http://localhost:8004/add?num1=5&num2=3`
- Returns `{"result": 8}`
- Frontend displays result: "5 + 3 = 8"

**Verified before Docker deploy.**

## Environment Variables

### Docker (.env)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
NEXT_PUBLIC_API_URL=http://localhost:8004
PYTHONUNBUFFERED=1
```

### Local (.env.local)
```
FRONTEND_PORT=3004
BACKEND_PORT=8004
API_URL=http://localhost:8004
API_HOST=localhost
API_PORT=8004
```

## PR Workflow

1. **Create feature branch**: `git checkout -b feature/calculator-operations`
2. **Implement changes**: Follow CLAUDE.md phases
3. **Run REGRESSION.md checklist**: Must pass all items
4. **Commit**: `git add . && git commit -m "feat: Add calculator operations"`
5. **Create PR**: GitHub PR automatically includes REGRESSION.md checklist
6. **Code review**: Reviewers verify all items checked
7. **Merge**: Squash or rebase to main

**See REGRESSION.md before creating any PR.**

## Success Criteria (Final)
- ✅ Frontend: Stranger Things themed, highly animated calculator
- ✅ Backend: FastAPI with add/subtract/multiply/divide endpoints
- ✅ Docker: Both services running on localhost:3004 and :8004
- ✅ Testing: 100% backend coverage, E2E frontend tests
- ✅ CORS: Frontend ↔ Backend communication verified
- ✅ Code Quality: PEP8, TypeScript strict, Prettier formatted
- ✅ Documentation: STARTUP.md, REGRESSION.md, all CLAUDE.md files complete

## References

- **Frontend Details**: See `frontend/CLAUDE.md` (7 phases)
- **Backend Details**: See `backend/CLAUDE.md` (8 phases)
- **Docker Details**: See `CREATE.md` (4 phases)
- **Startup Guide**: See `STARTUP.md` (3 options)
- **Pre-PR Checklist**: See `REGRESSION.md` (6 phases)
- **Agent Guides**: See `.claude/agents/*`
- **Skill Validators**: See `.claude/skills/*/SKILL.md`

## Quick Commands

| Command | Purpose |
|---------|---------|
| `claude build` | Run full orchestration (Phase 1-4) |
| `docker compose up -d` | Start services locally |
| `npm run build` | Frontend build check |
| `python3 -m pytest` | Backend tests |
| `/nextjs-validator` | Validate frontend |
| `/fastapi-validator` | Validate backend |
| `/docker-validator` | Validate Docker setup |

## Notes
- Use localhost:port connections, not container names, for frontend→backend communication
- All code executes in Docker containers, not locally
- REGRESSION.md must be completed before any PR
- Frontend and backend agents MUST run in parallel (Phase 1 & 2)
- Testing within phases should spawn tasks in parallel for 5-10x speedup
