# Stranger Things Calculator - Agent Orchestration Guide

**Mission**: Build a Stranger Things themed calculator with NextJS frontend (3004) + FastAPI backend (8004) + Docker orchestration.

**Execution Model**: 3 agents in parallel, using skills + hooks + detailed guides.

---

## 🔄 How to Spawn Agents (Read This First!)

### **STEP 1: Spawn Frontend Agent** (Run this command)
```
As @React NextJS Specialist, execute frontend development.

Reference: frontend/CLAUDE.md (7 phases)
Skill: /nextjs-validator (run after each phase)
Hooks: TypeScript/SCSS auto-format on file creation
Start: Phase 1, follow sequentially through Phase 7

CRITICAL: Do NOT proceed to Phase 5 (Backend Integration)
until Backend agent completes Phase 3.
```

### **STEP 2: Spawn Backend Agent** (Run in parallel with STEP 1)
```
As @Python FastAPI Specialist, execute backend development.

Reference: backend/CLAUDE.md (8 phases)
Skill: /fastapi-validator (run after each phase)
Hooks: Python auto-format on file creation
Start: Phase 1, follow sequentially through Phase 8

CRITICAL: Complete Phase 3 (Create Routes) before Frontend
can proceed with Phase 5 (Backend Integration).
```

### **STEP 3: Spawn DevOps Agent** (Run AFTER steps 1 & 2 complete)
```
As @DevOps Specialist, execute Docker orchestration.

Reference: CREATE.md section "PHASE 2: DOCKER"
Skill: /docker-validator (run after each phase)
Prerequisites: Frontend Phase 1-7 + Backend Phase 1-8 complete

4 phases:
  1. Frontend Dockerfile (node:18-alpine)
  2. Backend Dockerfile (python:3.11-slim)
  3. docker-compose.yaml (service networking)
  4. Integration testing (docker compose up/down)
```

---

## 📋 Document Purpose & Scope

| Document | Purpose | Audience | Scope |
|----------|---------|----------|-------|
| **INSTRUCTIONS.md** | Raw requirements (spec) | All | What to build |
| **CLAUDE.md** | Agent orchestration (THIS FILE) | Humans spawning agents | How to spawn agents |
| **CREATE.md** | High-level execution phases | Agents for reference | What agents execute |
| **frontend/CLAUDE.md** | Frontend development guide | Frontend agent | 7 phases, step-by-step |
| **backend/CLAUDE.md** | Backend development guide | Backend agent | 8 phases, step-by-step |

---

## 🛠️ Tools & Automation (FYI for Agents)

### Hooks (Automatic)
- ✅ TypeScript/SCSS auto-format on file creation (prettier)
- ✅ Python auto-format on file creation (autopep8)
- No manual formatting needed

### Skills (Manual Validation - Must Run)
- ✅ `/nextjs-validator` → After each frontend phase
- ✅ `/fastapi-validator` → After each backend phase
- ✅ `/docker-validator` → After each docker phase

### Agents (For Complex Tasks)
- ✅ `@React NextJS Specialist` → Frontend execution
- ✅ `@Python FastAPI Specialist` → Backend execution
- ✅ `@DevOps Specialist` → Docker execution

### Plugins (Optional Enhancements)
- `frontend-design` plugin (available for frontend agent)
- `security-guidance` plugin (available for backend agent)

---

## 🎯 Quality Gates (Non-Negotiable)

Before moving to next phase, skill must PASS:

```
Frontend Phase → /nextjs-validator MUST PASS ✅
Backend Phase  → /fastapi-validator MUST PASS ✅
Docker Phase   → /docker-validator MUST PASS ✅
```

**No exceptions. No phase advances without skill validation.**

---

## 📚 Detailed Guides (For Agents)

### Frontend Agent
- **Go to**: `frontend/CLAUDE.md`
- **Execute**: Phase 1 through Phase 7 (sequentially)
- **Validate**: `/nextjs-validator` after each phase
- **Duration**: 2-3 hours
- **Completion**: All 7 phases + skill passes

### Backend Agent
- **Go to**: `backend/CLAUDE.md`
- **Execute**: Phase 1 through Phase 8 (sequentially)
- **Validate**: `/fastapi-validator` after each phase
- **Duration**: 2-3 hours
- **Completion**: All 8 phases + skill passes
- **Critical**: Finish Phase 3 before Frontend Phase 5 starts

### DevOps Agent
- **Go to**: `CREATE.md` section "PHASE 2: DOCKER"
- **Execute**: Phase 1 through Phase 4 (sequentially)
- **Validate**: `/docker-validator` after each phase
- **Duration**: 1 hour
- **Completion**: All 4 phases + skill passes
- **Prerequisite**: Frontend & Backend agents must finish first

---

## ✅ Project Complete When

- [ ] Frontend: All 7 phases complete + `/nextjs-validator` pass ✅
- [ ] Backend: All 8 phases complete + `/fastapi-validator` pass ✅
- [ ] Docker: All 4 phases complete + `/docker-validator` pass ✅
- [ ] `docker compose up` works → both services start
- [ ] Frontend accessible at http://localhost:3004
- [ ] Backend accessible at http://localhost:8004
- [ ] End-to-end: all calculator operations work
- [ ] All tests pass (100% coverage for backend)

---

## 🚀 TL;DR - Quick Start

1. **Read this file** ← You are here
2. **Spawn Frontend Agent** with `frontend/CLAUDE.md` reference
3. **Spawn Backend Agent** with `backend/CLAUDE.md` reference (in parallel)
4. **Wait for both** to complete all phases
5. **Spawn DevOps Agent** with Docker phase from `CREATE.md`
6. **Done!** All agents finish → Project complete

---

## 📞 When Agents Get Stuck

1. Check skill output (run `/nextjs-validator`, `/fastapi-validator`, etc.)
2. Read relevant phase in frontend/CLAUDE.md or backend/CLAUDE.md
3. Use `/plan` agent to break down the problem
4. Use `/code-review` agent for code quality feedback
5. Refer back to INSTRUCTIONS.md for original requirements

---

**Key Files**: `frontend/CLAUDE.md`, `backend/CLAUDE.md`, `CREATE.md`
**Automation**: Hooks + Skills + Agents working together
