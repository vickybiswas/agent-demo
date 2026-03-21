# Stranger Things Calculator - Build Orchestration

Project: Full-stack calculator app with React NextJS frontend and Python FastAPI backend, themed after the Netflix series "Stranger Things", running on Docker.

## Overview
- **Frontend**: NextJS + TypeScript + SCSS (port 3004)
- **Backend**: FastAPI + Python (port 8004)
- **Orchestration**: Docker Compose with hot-reload volumes
- **Theme**: Stranger Things (dark, neon, retro 80s)

## Build Phases

### Phase 1: Frontend Development (Parallel with Phase 2)
**Agent**: React NextJS Specialist
**Guide**: `frontend/CLAUDE.md`
**Completion**: All 7 phases in frontend/CLAUDE.md complete

```
├─ Phase 1: Setup (project init, dependencies)
├─ Phase 2: Theme & Layout (JSON config, SCSS)
├─ Phase 3: Core Component (calculator logic)
├─ Phase 4: Animations (framer-motion, effects)
├─ Phase 5: Backend Integration (API calls)
├─ Phase 6: Testing (Playwright e2e)
└─ Phase 7: Review (TypeScript strict, build succeeds)
```

**Quality Gate**: `/nextjs-validator` MUST PASS

### Phase 2: Backend Development (Parallel with Phase 1)
**Agent**: Python FastAPI Specialist
**Guide**: `backend/CLAUDE.md`
**Completion**: All 8 phases in backend/CLAUDE.md complete

```
├─ Phase 1: Setup (structure, requirements.txt)
├─ Phase 2: Main App (FastAPI instance, CORS)
├─ Phase 3: Routes (separate files per operation)
├─ Phase 4: Unit Tests (5+ per operation)
├─ Phase 5: API Tests (5+ per endpoint)
├─ Phase 6: Regression Suite (100% coverage)
├─ Phase 7: Code Quality (PEP8, docstrings)
└─ Phase 8: Documentation (README, endpoint docs)
```

**Quality Gate**: `/fastapi-validator` MUST PASS

### Phase 3: Docker Orchestration (Sequential after Phases 1 & 2)
**Agent**: DevOps Specialist
**Guide**: `CREATE.md`
**Completion**: All phases in CREATE.md complete

**Prerequisite**: Phases 1 & 2 COMPLETE

```
├─ Phase 1: Frontend Dockerfile (node:18-alpine)
├─ Phase 2: Backend Dockerfile (python:3.11-slim)
├─ Phase 3: docker-compose.yaml (networking, volumes)
└─ Phase 4: Integration Testing (service communication)
```

**Quality Gate**: `/docker-validator` MUST PASS

### Phase 4: Quality Assurance (Final)
**Agent**: QA Automation Specialist

- Verify `docker compose up` works immediately
- Test all calculator operations (add, subtract, multiply, divide)
- Verify Stranger Things theme implementation
- Validate animations and sound effects
- Check responsive design
- Ensure zero errors in production build

## Success Criteria

✅ **Frontend**
- NextJS build succeeds (TypeScript strict)
- All Playwright tests pass
- nextjs-validator approved
- No hardcoded images
- Animations smooth (60fps)

✅ **Backend**
- All unit tests pass
- All API tests pass
- 100% code coverage
- fastapi-validator approved
- PEP8 compliant
- Zero external dependencies

✅ **Docker**
- `docker compose up` works
- Frontend accessible at http://localhost:3004
- Backend accessible at http://localhost:8004
- Services communicate correctly
- Hot-reload functional
- docker-validator approved

✅ **Integration**
- Calculator works end-to-end
- All operations functional
- Theme implemented correctly
- No console errors
- Lighthouse > 80

## Execution
1. **Start Phase 1 & 2 in parallel** → FastAPI Specialist & NextJS Specialist
2. **Monitor**: Both complete their 7-8 phases respectively
3. **Gate**: Both pass their validators
4. **Start Phase 3**: DevOps Specialist (only after 1 & 2 complete)
5. **Gate**: Docker validator passes
6. **Final Validation**: QA Specialist verifies end-to-end

## Notes
- DRY Principle: Each phase documented in its own file (no duplication)
- Parallel Execution: Frontend & Backend develop independently
- Quality Gates: Validators block merge if not passing
- No manual file creation: All infrastructure auto-generated
