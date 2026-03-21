# CREATE.md - Build Orchestration & Docker Phase

**Purpose**: Defines how Docker phase executes (after frontend & backend complete).

**Prerequisite**: Frontend agent + Backend agent must finish all phases first
**Duration**: ~1 hour (Docker orchestration only)
**Parallel Strategy**: See `CLAUDE.md` for agent spawning instructions

---

## 🔄 Execution Phases

**PHASES 1A & 1B**: Frontend + Backend (execute in parallel)
- **Frontend Agent**: Go to `frontend/CLAUDE.md` (7 phases)
- **Backend Agent**: Go to `backend/CLAUDE.md` (8 phases)
- **These phases are detailed in their respective CLAUDE.md files**
- **Do NOT duplicate here** - refer agents to those files

**PHASE 2**: Docker orchestration (execute AFTER 1A & 1B complete)
- **DevOps Agent**: Follow tables below (4 phases)
- **Detailed execution** shown in this file only

---

## ⚠️ PHASE 1A & 1B: Frontend & Backend (See Their CLAUDE.md Files)

**Frontend**: `frontend/CLAUDE.md` → 7 phases (NextJS agent)
**Backend**: `backend/CLAUDE.md` → 8 phases (FastAPI agent)

**Do NOT duplicate here.** All detailed instructions are in those files.
All validation checks are in their respective skill validators.

---

## 📋 PHASE 2: DOCKER (4 phases)

**Assigned To**: `@DevOps Specialist`
**Prerequisite**: Frontend (1A) + Backend (1B) complete
**Skill**: `/docker-validator` (run after each phase)

| Phase | Task | Validation |
|-------|------|------------|
| 1 | Frontend Dockerfile (node:18-alpine, .dockerignore) | `docker build ./frontend` ✅ |
| 2 | Backend Dockerfile (python:3.11-slim, .dockerignore) | `docker build ./backend` ✅ |
| 3 | docker-compose.yaml (2 services, volumes, networking) | YAML valid, no localhost hardcoding |
| 4 | Integration (docker compose build/up/down/test) | Both services accessible, hot-reload works ✅ |

**Final Check**:
```bash
/docker-validator              # Must pass
docker compose up              # Starts successfully
```

---

## ✅ Quality Gates (No Exceptions)

Each phase must pass its skill before advancing:
- **Frontend phases** → `/nextjs-validator` ✅
- **Backend phases** → `/fastapi-validator` ✅
- **Docker phases** → `/docker-validator` ✅

---

## ✨ Project Complete When

- [ ] Frontend agent: 7 phases + skill passes
- [ ] Backend agent: 8 phases + skill passes
- [ ] DevOps agent: 4 phases + skill passes
- [ ] `docker compose up` → both services start
- [ ] http://localhost:3004 → Frontend loads
- [ ] http://localhost:8004 → Backend responds
- [ ] End-to-end calculator works
- [ ] All tests pass (100% coverage)

---

## 📚 Document Map (No Duplication)

| File | Purpose | For Whom |
|------|---------|----------|
| `CLAUDE.md` | Agent spawning guide | Humans |
| `frontend/CLAUDE.md` | 7-phase detailed execution | Frontend agent |
| `backend/CLAUDE.md` | 8-phase detailed execution | Backend agent |
| `CREATE.md` | Docker phase + orchestration | DevOps agent |
| `INSTRUCTIONS.md` | Raw requirements spec | Reference |

---

**→ Go to `CLAUDE.md` to spawn agents**
