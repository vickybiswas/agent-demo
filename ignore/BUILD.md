# BUILD.md - Automated Repository Setup & Agent Execution

**Purpose**: Execute complete project setup from INSTRUCTIONS.md and build the application.

---

## 🔄 Complete Workflow

```
1. User provides INSTRUCTIONS.md
         ↓
2. Run: repo-setup skill
         ↓
3. Generated: 13 files (agents, skills, hooks, guides)
         ↓
4. Verify setup (optional)
         ↓
5. Run: claude build
         ↓
6. Result: Full application with all components
```

---

## 📋 Step 1: Prepare INSTRUCTIONS.md

Your INSTRUCTIONS.md must contain:

```markdown
# Project Overview
- Frontend: NextJS/TypeScript/SCSS on port 3004
- Backend: FastAPI/Python on port 8004
- Orchestration: Docker Compose with hot-reload

## Setup Requirements
- Agents: [list of 5 agents]
- Stack: [technologies]
- Validation: [test requirements]

## Frontend Details
- Theme: Stranger Things aesthetic
- Requirements: no images, JSON-driven, animations
- Libraries: framer-motion, shadcn-ui, lucide-react, three.js

## Backend Details
- Stack: FastAPI (zero external deps)
- Routes: separate files (add, subtract, multiply, divide)
- Testing: unit + API + regression, 100% coverage
- Code: PEP8 compliant

## Docker Details
- Compose orchestration
- Hot-reload volumes
- Service-to-service networking (no localhost)
```

---

## 🚀 Step 2: Run Setup Skill

Execute the repo-setup skill to generate all infrastructure:

```bash
As repo-setup specialist, generate complete repository setup from INSTRUCTIONS.md.

Follow the skill definition in: .claude/skills/repo-setup/SKILL.md

Output:
1. .claude/settings.local.json (hooks for auto-formatting)
2. 5 agent definitions (.claude/agents/*)
3. 3 skill validators (.claude/skills/*/SKILL.md)
4. CLAUDE.md (root orchestration guide)
5. CREATE.md (Docker phase guide)
6. frontend/CLAUDE.md (7-phase frontend guide)
7. backend/CLAUDE.md (8-phase backend guide)

All files must follow DRY and SRP principles:
- No duplication across files
- Each file has single responsibility
- Agents can execute independently
```

---

## ✅ Step 3: Verify Setup (Optional)

After skill generates all files:

```bash
# Check all files exist
ls -la .claude/agents/
ls -la .claude/skills/*/
ls -la *.md
ls -la frontend/CLAUDE.md backend/CLAUDE.md

# Verify structure
grep -c "Phase" frontend/CLAUDE.md  # Should show ~7
grep -c "Phase" backend/CLAUDE.md   # Should show ~8

# Verify no major duplication
grep -r "Phase 1: Setup" . --include="*.md" | wc -l  # Should be low

# Test hooks are configured
cat .claude/settings.local.json | grep autopep8  # Python formatting
cat .claude/settings.local.json | grep prettier   # TypeScript/SCSS formatting
```

---

## 🏗️ Step 4: Understand Generated Files

### Agents (`.claude/agents/`)
- `1-pr-review.md` - Code quality review
- `2-fastapi-specialist.md` - Backend development
- `3-nextjs-specialist.md` - Frontend development
- `4-devops-specialist.md` - Docker orchestration
- `5-qa-specialist.md` - Testing and coverage

### Skills (`.claude/skills/*/SKILL.md`)
- `nextjs-validator/` - Validates frontend (TypeScript strict, SCSS, animations, no images)
- `fastapi-validator/` - Validates backend (PEP8, routes, zero deps, 100% coverage)
- `docker-validator/` - Validates Docker (compose.yaml, Dockerfiles, networking)

### Guides (`.md` files)
- `CLAUDE.md` - Root orchestration (3 agent spawn steps)
- `CREATE.md` - Docker phase details
- `frontend/CLAUDE.md` - Frontend execution (7 phases with checklists)
- `backend/CLAUDE.md` - Backend execution (8 phases with checklists)

---

## 🎯 Step 5: Run Build

Execute all agents according to generated orchestration:

```bash
claude build
```

This will:

### Phase 1A & 1B (Parallel)

**Frontend Agent** executes `frontend/CLAUDE.md`:
```
As @React NextJS Specialist, execute frontend development.
Reference: frontend/CLAUDE.md (7 phases)
Skill: /nextjs-validator (run after each phase)
Timeline: 2-3 hours
```

**Backend Agent** executes `backend/CLAUDE.md`:
```
As @Python FastAPI Specialist, execute backend development.
Reference: backend/CLAUDE.md (8 phases)
Skill: /fastapi-validator (run after each phase)
Timeline: 2-3 hours
CRITICAL: Complete Phase 3 (Routes) before Frontend Phase 5
```

### Phase 2 (Sequential - After Phase 1A & 1B)

**DevOps Agent** executes `CREATE.md`:
```
As @DevOps Specialist, execute Docker orchestration.
Reference: CREATE.md (4 Docker phases)
Skill: /docker-validator (run after each phase)
Timeline: 1 hour
Prerequisites: Frontend + Backend complete
```

---

## 🔄 Execution Flow

```
Start
  ↓
Frontend Agent (Phase 1: Setup) ←→ Backend Agent (Phase 1: Setup)
  ↓                                    ↓
Frontend Phase 2-4                  Backend Phase 2-3
  ↓                                    ↓
Frontend WAITS ←─── CRITICAL SYNC ───→ Backend Phase 3 COMPLETE
  ↓                                    ↓
Frontend Phase 5 (Backend Integration) Backend Phase 4-8
  ↓                                    ↓
Frontend Phase 6-7                  Backend tests & docs
  ↓                                    ↓
Frontend COMPLETE                   Backend COMPLETE
  ↓
DevOps Agent Phase 1-4 (Docker)
  ↓
Final: docker compose up
  ↓
http://localhost:3004 (Frontend)
http://localhost:8004 (Backend)
  ↓
Success ✅
```

---

## ✨ Quality Gates (Non-Negotiable)

Each phase must pass validation before advancing:

```
Frontend Phase → /nextjs-validator MUST PASS ✅
Backend Phase  → /fastapi-validator MUST PASS ✅
Docker Phase   → /docker-validator MUST PASS ✅
```

No exceptions. Skills enforce code quality.

---

## 📊 Expected Results After Build

### Frontend (localhost:3004)
- ✅ NextJS SPA with Stranger Things theme
- ✅ Calculator with animations and sound effects
- ✅ JSON-driven design, no images
- ✅ SCSS styling, responsive layout
- ✅ All Playwright tests passing
- ✅ TypeScript strict mode, no `any` types

### Backend (localhost:8004)
- ✅ FastAPI with 4 endpoints (/add, /subtract, /multiply, /divide)
- ✅ Each operation in separate route file
- ✅ Zero external dependencies (fastapi + uvicorn only)
- ✅ 100% test coverage (unit + API tests)
- ✅ PEP8 compliant code
- ✅ Proper error handling (division by zero, invalid inputs)

### Docker
- ✅ Frontend container running on port 3004
- ✅ Backend container running on port 8004
- ✅ Services communicate via service names (no localhost)
- ✅ Hot-reload volumes mounted (/code in containers)
- ✅ docker compose up/down works seamlessly

### Repository
- ✅ All 13 setup files generated
- ✅ No duplication (DRY principle)
- ✅ Each file has single responsibility (SRP)
- ✅ Agents ready to execute
- ✅ All tests passing

---

## 🛠️ Commands Summary

```bash
# Generate setup from INSTRUCTIONS.md
As repo-setup specialist, [generate all files]

# Verify everything was created
ls -la .claude/agents/ .claude/skills/ *.md

# Run full build
claude build

# After build completes
docker compose up
curl http://localhost:3004
curl http://localhost:8004

# Run tests
pytest backend/tests/                    # Backend tests
npx playwright test                      # Frontend tests
```

---

## 📞 When Build Fails

**Check skill validation output:**
```bash
/nextjs-validator     # Frontend compliance
/fastapi-validator    # Backend compliance
/docker-validator     # Docker compliance
```

**Check phase checklists:**
- Read: frontend/CLAUDE.md (for frontend issues)
- Read: backend/CLAUDE.md (for backend issues)
- Read: CREATE.md (for Docker issues)

**Check logs:**
```bash
docker compose logs frontend     # Frontend container logs
docker compose logs backend      # Backend container logs
```

---

## 🎯 Success Criteria

- [ ] INSTRUCTIONS.md provided
- [ ] repo-setup skill executed
- [ ] All 13 files generated with no errors
- [ ] Hooks configured (autopep8, prettier)
- [ ] 5 agents created
- [ ] 3 skills created
- [ ] CLAUDE.md, CREATE.md generated
- [ ] frontend/CLAUDE.md generated (7 phases)
- [ ] backend/CLAUDE.md generated (8 phases)
- [ ] `claude build` spawns agents
- [ ] Frontend agent completes all 7 phases
- [ ] Backend agent completes all 8 phases
- [ ] DevOps agent completes all 4 Docker phases
- [ ] All skills pass validation ✅
- [ ] docker compose up works
- [ ] http://localhost:3004 loads
- [ ] http://localhost:8004 responds
- [ ] End-to-end calculator works
- [ ] All tests pass (100% coverage)

---

## 📚 File Reference

| File | Purpose | Owner |
|------|---------|-------|
| INSTRUCTIONS.md | Raw requirements | You |
| BUILD.md | Execution orchestration | You (reading this) |
| .claude/settings.local.json | Auto-formatting hooks | repo-setup skill |
| .claude/agents/* | Agent definitions | repo-setup skill |
| .claude/skills/*/ | Validators | repo-setup skill |
| CLAUDE.md | Agent spawning guide | repo-setup skill |
| CREATE.md | Docker phases | repo-setup skill |
| frontend/CLAUDE.md | Frontend execution | repo-setup skill |
| backend/CLAUDE.md | Backend execution | repo-setup skill |

---

**Start here**: Provide INSTRUCTIONS.md → Run repo-setup skill → Run `claude build` → Success! 🚀
