# SETUP.md - Stranger Things Calculator Repo Setup

**Goal**: Create all repo files from INSTRUCTIONS.md only, following DRY & SOC principles.

---

## 📋 From INSTRUCTIONS.md, Extract These

```
Agents:
  - @React NextJS Specialist (frontend)
  - @Python FastAPI Specialist (backend)
  - @DevOps Specialist (docker)
  - @PR Review Specialist
  - @QA Automation Specialist

Stack:
  - Frontend: NextJS, TypeScript, SCSS (port 3004)
  - Backend: FastAPI, Python, zero external deps (port 8004)
  - Orchestration: Docker Compose, hot-reload volumes

Requirements:
  - Frontend: No images, JSON-driven, animations, Stranger Things theme
  - Backend: PEP8, routes in separate files, 100% test coverage
  - Docker: Hot-reload, service-to-service networking (no localhost)
```

---

## 🔨 Create These 8 Files

### 1. `.claude/settings.local.json` (Hooks)
```json
{
  "hooks": [
    {"event": "file_created", "pattern": "**/*.py", "command": "autopep8 --in-place --aggressive --aggressive {file}"},
    {"event": "file_created", "pattern": "**/*.ts", "command": "prettier --write {file}"},
    {"event": "file_created", "pattern": "**/*.tsx", "command": "prettier --write {file}"},
    {"event": "file_created", "pattern": "**/*.scss", "command": "prettier --write {file}"}
  ]
}
```

### 2. `.claude/agents/1-pr-review.md`
```
Role: Code review specialist
Validates: Code quality, security, test coverage
Run after: Code changes before merge
```

### 3. `.claude/agents/2-fastapi-specialist.md`
```
Role: Backend expert
Reads: backend/CLAUDE.md
Validates with: /fastapi-validator
```

### 4. `.claude/agents/3-nextjs-specialist.md`
```
Role: Frontend expert
Reads: frontend/CLAUDE.md
Validates with: /nextjs-validator
```

### 5. `.claude/agents/4-devops-specialist.md`
```
Role: Docker/orchestration expert
Reads: CREATE.md (Phase 2)
Validates with: /docker-validator
```

### 6. `.claude/agents/5-qa-specialist.md`
```
Role: Testing expert
Validates: Unit tests, API tests, coverage (100%)
Supports: Backend pytest + Frontend Playwright
```

### 7-9. `.claude/skills/`
Create 3 validators (SKILL.md in each):

**nextjs-validator/**
- Validates: TypeScript (no `any`), SCSS organized, animations smooth, Playwright ready, no images, JSON-driven design
- Run: After each frontend phase
- Command: `/nextjs-validator`

**fastapi-validator/**
- Validates: PEP8, routes in separate files, zero external deps, 100% coverage, edge cases handled
- Run: After each backend phase
- Command: `/fastapi-validator`

**docker-validator/**
- Validates: Dockerfiles, compose.yaml, ports (3004, 8004), volumes for hot-reload, service networking (no localhost)
- Run: After each docker phase
- Command: `/docker-validator`

### 10. `CLAUDE.md` (Agent Orchestration)
```
STEP 1: Spawn Frontend Agent
As @React NextJS Specialist, execute frontend development.
Reference: frontend/CLAUDE.md
Skill: /nextjs-validator (run after each phase)
Duration: 2-3 hours

STEP 2: Spawn Backend Agent (parallel with STEP 1)
As @Python FastAPI Specialist, execute backend development.
Reference: backend/CLAUDE.md
Skill: /fastapi-validator (run after each phase)
Duration: 2-3 hours
CRITICAL: Complete Phase 3 (Routes) before Frontend Phase 5 starts

STEP 3: Spawn DevOps Agent (after steps 1 & 2)
As @DevOps Specialist, execute Docker orchestration.
Reference: CREATE.md PHASE 2
Skill: /docker-validator (run after each phase)
Duration: 1 hour

Quality Gates:
- Frontend: /nextjs-validator MUST PASS ✅
- Backend: /fastapi-validator MUST PASS ✅
- Docker: /docker-validator MUST PASS ✅
```

### 11. `CREATE.md` (Docker Orchestration)
```
PHASE 2 (Prerequisites: Frontend + Backend complete)

Assigned: @DevOps Specialist
Duration: 1 hour

| Phase | Task | Validation |
|-------|------|------------|
| 1 | Frontend Dockerfile (node:18-alpine) | docker build ./frontend ✅ |
| 2 | Backend Dockerfile (python:3.11-slim) | docker build ./backend ✅ |
| 3 | docker-compose.yaml | No hardcoded localhost, services networked |
| 4 | Integration test | docker compose up → both services accessible |

Final: /docker-validator MUST PASS
```

### 12. `frontend/CLAUDE.md` (7 Phases)
```
For: @React NextJS Specialist
Port: 3004 | Stack: NextJS/TypeScript/SCSS
Skill: /nextjs-validator

Phase 1: Setup (NextJS + deps + directory structure)
Phase 2: Theme & Layout (JSON config + SCSS + landing page with Stranger Things aesthetic)
Phase 3: Calculator component (React + logic + display)
Phase 4: Animations (framer-motion + sounds + effects, 60fps)
Phase 5: Backend integration (API calls to http://backend:8004)
Phase 6: Testing (Playwright tests for all operations)
Phase 7: Review (TypeScript strict, build succeeds, tests pass)

[Include detailed checklists for each phase]
```

### 13. `backend/CLAUDE.md` (8 Phases)
```
For: @Python FastAPI Specialist
Port: 8004 | Stack: FastAPI/Python
Skill: /fastapi-validator

Phase 1: Setup (structure + requirements.txt: fastapi, uvicorn ONLY)
Phase 2: Main app (FastAPI instance + CORS + /health)
Phase 3: Routes (add.py, subtract.py, multiply.py, divide.py - separate files)
Phase 4: Unit tests (5+ per operation, edge cases)
Phase 5: API tests (5+ per endpoint, HTTP tests)
Phase 6: Regression suite (all tests + 100% coverage)
Phase 7: Code quality (PEP8, docstrings, type hints)
Phase 8: Documentation (README + endpoint docs)

[Include detailed checklists for each phase]
```

---

## ✅ Verification

After creating all 13 items above:

- [ ] No duplication across .md files (grep: 0 matches on repeated phases)
- [ ] Each agent has ONE file to read
- [ ] Each file has ONE clear role
- [ ] All INSTRUCTIONS.md requirements are addressed
- [ ] Agents can execute without cross-file jumps

---

## 🎯 Result

✅ Complete repo setup
✅ Ready for agent execution
✅ DRY & SOC applied
✅ No duplication
