---
name: repo-setup
description: Generate complete Claude-orchestrated project setup from INSTRUCTIONS.md. Creates agents, skills, hooks, and domain guides automatically. Use when you have a project specification in INSTRUCTIONS.md format and need to generate the full repository infrastructure (agents, validators, skills, hooks, orchestration guides, domain-specific CLAUDE.md files). Outputs reproducible, DRY-compliant setup with no manual file creation needed.
---

# Repo Setup Skill - Automated Infrastructure Generation

## Purpose

Transform a project INSTRUCTIONS.md into a complete, production-ready repository setup with:
- Automated code formatting hooks
- 5 specialized agents
- 3 domain-specific validators (skills)
- issue fetch and solve command
- Orchestration guides (CLAUDE.md files)
- Docker integration guide

## When to Use

✅ You have an INSTRUCTIONS.md file specifying a project
✅ You need to generate agents, skills, and execution guides
✅ You want reproducible, DRY-compliant setup
✅ You plan to use `claude build` workflow
✅ You want to avoid manual file creation

## Input Requirements

**INSTRUCTIONS.md must contain:**

```
# Project structure (Frontend/Backend/Orchestration)
- Agents: 5+ agent names
- Stack: Technology choices (frameworks, languages, ports)
- Requirements: Frontend, Backend, and Docker-specific needs
```

**Example INSTRUCTIONS.md sections:**

```
Frontend (React NextJS):
- Stack: TypeScript, SCSS, port 3004
- Requirements: theme, animations, JSON-driven

Backend (Python FastAPI):
- Stack: FastAPI, zero external deps, port 8004
- Requirements: PEP8, separate route files, 100% coverage

Orchestration (Docker):
- Stack: Docker Compose, hot-reload
- Requirements: Service networking, no localhost hardcoding
```

## What Gets Generated (use subagents and paralliize as much as possible)

### 1. Hooks Configuration (`.claude/settings.local.json`)
Auto-formatting on file creation:
- Python: autopep8 (PEP8 compliance)
- TypeScript: prettier (ES6 compliance)
- SCSS: prettier (style consistency)

### 2. Five Agents (`.claude/agents/`)
1. `1-pr-review.md` - Code review specialist
2. `2-fastapi-specialist.md` - Backend expert (Python)
3. `3-nextjs-specialist.md` - Frontend expert (React/NextJS)
4. `4-devops-specialist.md` - Docker orchestration expert
5. `5-qa-specialist.md` - Testing and coverage expert

### 3. Three Validators (`.claude/skills/*/SKILL.md` configured on run on every file update)
1. **nextjs-validator** - TypeScript strict, SCSS organized, animations smooth, no images, Playwright ready
2. **fastapi-validator** - PEP8, separate routes, zero external deps, 100% coverage, edge cases
3. **docker-validator** - Dockerfiles, compose.yaml, ports, volumes, service networking

### 4. Orchestration Files

**CLAUDE.md** (Root orchestration):
- 3 STEPs to spawn agents in parallel (Frontend + Backend) then sequential (Docker)
- Quality gates for each domain
- Dependencies and timing
- End to End Playwrite based UI testing
- Reference to REGRESSION.md as pre-PR requirement

**CREATE.md** (Docker-specific guide):
- Phase 1: Frontend Dockerfile (node:18-alpine)
- Phase 2: Backend Dockerfile (python:3.11-slim)
- Phase 3: docker-compose.yaml (service networking, hot-reload volumes)
- Phase 4: Integration testing (service communication, environment variables)

**REGRESSION.md** (Pre-PR quality gate):
- Phase 1: Local dev setup (backend, frontend, environment variables)
- Phase 2: CORS & integration testing (verify frontend ↔ backend communication)
- Phase 3: Testing requirements (unit, API, e2e tests per CLAUDE.md phases)
- Phase 4: Docker orchestration (docker compose verification)
- Phase 5: Code quality (PEP8, docstrings, type hints)
- Phase 6: Git & PR preparation (clean commits, no debug code)

**STARTUP.md** (Service startup guide):
- 3 startup options (Docker Compose, local development, automated script)
- Environment variable setup (.env vs .env.local documentation)
- Health check verification commands
- CORS troubleshooting section

### 5. Domain Guides 

**frontend/CLAUDE.md** (7 phases):
- Phase 1: Setup (project init, dependencies)
- Phase 2: Theme & Layout (JSON config, SCSS aesthetic)
- Phase 3: Core Component (calculator logic)
- Phase 4: Animations (framer-motion, sounds, effects, 60fps)
- Phase 5: Backend Integration (**NEW**: CORS testing with curl, env var validation, .env vs .env.local setup)
- Phase 6: Testing (Playwright e2e tests)
- Phase 7: Review (TypeScript strict, build succeeds, tests pass)

**backend/CLAUDE.md** (8 phases):
- Phase 1: Setup (structure, requirements.txt: fastapi, uvicorn ONLY)
- Phase 2: Main App (FastAPI instance, CORS middleware with allowed origins, /health endpoint, **NEW**: CORS header validation)
- Phase 3: Routes (separate files per operation)
- Phase 4: Unit Tests (5+ per operation, edge cases)
- Phase 5: API Tests (5+ per endpoint, HTTP validation)
- Phase 6: Regression Suite (all tests + 100% coverage)
- Phase 7: Code Quality (PEP8, docstrings, type hints)
- Phase 8: Documentation (README, endpoint docs)

### 6. Environment & PR Configuration

**.env.example** and **.env.local.example** (with documentation):
- Shows difference between .env (Docker) and .env.local (local dev)
- Lists all required environment variables
- Explains why each is needed (e.g., NEXT_PUBLIC_API_URL points to different URLs depending on environment)

**GitHub PR Template** (.github/pull_request_template.md):
- Links to REGRESSION.md
- Checklist: All regression checks passed before this PR
- Forces developers to verify locally before pushing

## Parallelization Strategy

**CRITICAL**: All generated CLAUDE.md files must include parallelization guidance to prevent slow sequential execution and context bloat.

### Why Parallelization Matters
1. **Performance**: Independent tasks execute simultaneously → 5-10x speedup
2. **Context Management**: Each subagent gets fresh context window; outputs don't accumulate in main agent
3. **Prevents Context Explosion**: Sequential operation outputs bloat context; parallel avoids this

### Phase-Level Parallelization
- **Phase 1 & 2** (Frontend + Backend): Both spawn simultaneously, run in parallel
- **Phase 3** (Docker): Starts only after Phase 1 & 2 complete (sequential dependency)

### Within-Phase Parallelization
- **Backend Testing**: Unit tests, API tests, coverage → spawn all in parallel
- **Frontend Testing**: TypeScript, build, Playwright → spawn all in parallel
- **360° Testing** (Issue Resolution): Backend service, frontend service, CORS, integration, Docker → spawn all in parallel

### Implementation Pattern
```
✅ Correct: Spawn multiple subagents (hiaku) in single message
/Agent task-1 (background)
/Agent task-2 (background)
/Agent task-3 (background)
# Main agent continues; subagents run in parallel

❌ Incorrect: Sequential subagent spawning
/Agent task-1        (wait for completion)
/Agent task-2        (wait for completion)
/Agent task-3        (wait for completion, bloats context)
```

**Benefits**: 5-10x faster, context stays manageable, main agent stays responsive.

## Execution

### Step 1: Provide INSTRUCTIONS.md
Ensure your INSTRUCTIONS.md contains:
- Clear frontend stack and requirements
- Clear backend stack and requirements
- Clear Docker orchestration requirements
- 5 agent names

### Step 2: Run This Skill
```bash
As repo-setup specialist, analyze INSTRUCTIONS.md and generate complete repo setup:
1. Extract agents, stack, requirements
2. Generate .claude/settings.local.json (hooks)
3. Generate 5 agent files (.claude/agents/)
4. Generate 3 skill validators (.claude/skills/*/SKILL.md)
5. Generate CLAUDE.md (root orchestration + PARALLELIZATION STRATEGY section)
6. Generate CREATE.md (Docker phases)
7. Generate REGRESSION.md (pre-PR checklist - REQUIRED before any PR)
8. Generate STARTUP.md (service startup guide with env var documentation)
9. Generate frontend/CLAUDE.md (7-phase guide with CORS/env testing + parallelization guidance)
10. Generate backend/CLAUDE.md (8-phase guide with CORS middleware + parallelization guidance)
11. Generate .env.example and .env.local.example (with documentation)
12. Generate .github/pull_request_template.md (links to REGRESSION.md)

CRITICAL: CLAUDE.md MUST include "Parallelization Strategy" section (see template below).
Every generated CLAUDE.md shows HOW to parallelize Phase 1 & 2, and within testing phases.

Output all files with proper formatting and structure.
```

### Step 3: Verify Generation
```bash
# Check all files created
ls -la .claude/agents/
ls -la .claude/skills/*/
ls -la *.md
ls -la frontend/ backend/

# Verify no duplication (DRY)
grep -r "Phase 1" frontend/CLAUDE.md backend/CLAUDE.md CLAUDE.md | wc -l
# Should show low count, no major duplication

# Verify each file has single responsibility (SRP)
wc -l .claude/agents/*.md frontend/CLAUDE.md backend/CLAUDE.md CLAUDE.md CREATE.md
# Each should be focused, not bloated
```

### Step 4: Run Build
After setup generation completes:
```bash
claude build
```

This will spawn agents following the generated orchestration guides.

## Output Structure

```
.claude/
├── settings.local.json          (Hooks: auto-format Python/TS/SCSS)
├── agents/
│   ├── 1-pr-review.md
│   ├── 2-fastapi-specialist.md
│   ├── 3-nextjs-specialist.md
│   ├── 4-devops-specialist.md
│   └── 5-qa-specialist.md
├── skills/
│   ├── nextjs-validator/SKILL.md
│   ├── fastapi-validator/SKILL.md
│   └── docker-validator/SKILL.md

Root directory:
├── CLAUDE.md                     (Root orchestration + REGRESSION.md reference)
├── CREATE.md                     (Docker guide with integration testing)
├── REGRESSION.md                 (Pre-PR checklist - REQUIRED before any PR)
├── STARTUP.md                    (Service startup guide)
├── .env.example                  (Environment variables for Docker)
├── .env.local.example            (Environment variables for local dev)
├── .github/
│   └── pull_request_template.md (Links to REGRESSION.md checklist)

Domain guides:
├── frontend/CLAUDE.md            (7 phases including CORS testing)
└── backend/CLAUDE.md             (8 phases including CORS middleware validation)
```

## Key Principles Applied

### DRY (Don't Repeat Yourself)
- Each piece of information exists once
- No phase description appears in multiple files
- CLAUDE.md only orchestrates, doesn't duplicate domain details

### SRP (Single Responsibility Principle)
- Each file has ONE clear purpose:
  - Agent files: Define agent role only
  - Skill files: Validate one domain only
  - CLAUDE.md: Orchestrate agents only
  - frontend/CLAUDE.md: 7 phases for frontend only
  - backend/CLAUDE.md: 8 phases for backend only
  - CREATE.md: Docker phases only

### Agent Autonomy & Parallelization
- Each agent reads ONE file (no cross-file jumps)
- Domain files are self-contained
- **CRITICAL**: No coordination needed between agents → enables parallel execution
- Frontend + Backend agents MUST spawn together (not sequentially)
- Within each phase, independent tasks (tests, validations) spawn together
- ALWAYS use SubAgents where possible and wnsure the Claude file and CREATE.ms you create propose the same for max parallization
- **Result**: 5-10x speedup from parallelization vs sequential execution recommended in all CLAUDE.md files

## Framework Focus

The skill generates guides with **specific framework focus**:

- **Frontend**: Animations via framer-motion, styling via SCSS, testing via Playwright
- **Backend**: FastAPI endpoints, pytest for testing, PEP8 for code quality
- **Docker**: Compose for orchestration, volumes for hot-reload, networking for services, End to End automated testing, frontend connected to backend and working together 

Agents follow these frameworks when building, not generic approaches.

## Quality Gates

Generated setup enforces:
- ✅ `frontend/CLAUDE.md` → `/nextjs-validator` MUST PASS
- ✅ `backend/CLAUDE.md` → `/fastapi-validator` MUST PASS
- ✅ `CREATE.md` → `/docker-validator` MUST PASS

No phase advances without skill validation.

## Parallelization Template (Generate in CLAUDE.md)

Every generated CLAUDE.md MUST include this section:

```markdown
## Parallelization Strategy

**Performance & Context Management**: Spawn independent tasks in parallel to:
- Execute 5-10x faster (parallel vs sequential)
- Keep context manageable (each subagent gets fresh context, outputs don't accumulate)
- Keep main agent responsive (continues work while subagents run)

### Phase 1 & 2: Parallel Execution
Frontend + Backend agents MUST spawn together in SAME message:
- Frontend agent: reads frontend/CLAUDE.md (7 phases)
- Backend agent: reads backend/CLAUDE.md (8 phases)
- Both execute independently, in parallel

### Within Each Phase: Parallel Testing
Independent tasks spawn together (NOT sequentially):

**Backend Testing Phase**:
- Unit tests (all together)
- API tests (all together)
- Coverage analysis (runs after both complete)

**Frontend Testing Phase**:
- TypeScript validation
- Build compilation
- Playwright tests
All three spawn together, results collected when done.

**360° Regression Testing** (Issue Resolution):
- Backend service startup
- Frontend service startup
- CORS header validation
- End-to-end operation - Playwrite
- Frontend should be reaching backend and e2e should be able to prove that by mimicing usage.
- Docker Compose startup
All spawn together in single message.

### Implementation Rule
Spawn independent tasks in SINGLE message with `run_in_background=true`.
Do NOT spawn sequentially (wait for each to complete).
```

## Example

**Input**: INSTRUCTIONS.md with:
- Agents: PR Review, FastAPI Specialist, NextJS Specialist, DevOps Specialist, QA Specialist
- Stack: NextJS/TypeScript/SCSS (3004), FastAPI/Python (8004), Docker Compose
- Requirements: Stranger Things theme, zero external deps, 100% test coverage

**Output**: Complete 13-file setup ready for agent execution via `claude build`
- Includes subagents and parallelization guidance in generated CLAUDE.md
- Frontend & Backend agents spawn together and front end can reach backend on browser
- All testing phases use parallel execution patterns with thrrough testing

## Integration Testing Prevention

**Why REGRESSION.md is Critical:**

Without a pre-PR checklist, integration issues slip through to GitHub. Issue #3 demonstrated how CORS and environment variable misconfigurations can be missed if developers don't test the entire stack locally:

- ❌ **Before**: Backend responded, frontend loaded separately, but frontend→backend communication broke because CORS wasn't tested
- ❌ **Before**: Env vars (.env vs .env.local) weren't documented, causing localhost:8004 vs docker http://backend:8004 mismatches
- ❌ **Before**: No checklist existed to verify all components working together before PR

**With REGRESSION.md:**
- ✅ Developers test backend service starts (`python3 main.py`)
- ✅ Developers test frontend service starts (`npm run dev`)
- ✅ Developers test CORS headers sent correctly (`curl -H "Origin..." ...`)
- ✅ Developers test end-to-end operation (5 + 3 = 8) tested on browser UI to see frontend and backend working together
- ✅ Developers test Docker Compose orchestration
- ✅ All tests passing BEFORE creating PR

**New Files Added to repo-setup:**
1. **REGRESSION.md** - Forces regression testing before ANY PR
2. **STARTUP.md** - Documents service startup and env var setup
3. **Enhanced Phase 5 (Frontend)** - Tests CORS with curl, validates env vars
4. **Enhanced Phase 2 (Backend)** - Tests CORS middleware with actual frontend origins
5. **.env.example & .env.local.example** - Explains environment variable differences
6. **PR template** - Checklist linking to REGRESSION.md

**Performance Note:** REGRESSION.md tests should spawn in PARALLEL:
- Backend health check
- Frontend asset loading
- CORS validation
- End-to-end operation
- Docker Compose startup

All independent → spawn together, not sequentially. Cuts regression testing time 5-10x.

**Result:** Integration issues are caught during development, not after PR submission. Testing is fast.

## Notes

- Skill outputs files to current working directory
- All files are properly formatted (hooks auto-fix on creation)
- Generated agents are ready to spawn immediately
- No manual editing needed unless customizing beyond INSTRUCTIONS.md
- **REGRESSION.md is mandatory** - Every developer must complete it before creating a PR

# Learnings
2026/03/25 - In docker compose use http://localhost instead of http://service_name (eg. backend) to reach backend from frontend when running in local development. The generated documentation and guides must clearly explain this difference and how to set up environment variables accordingly. Add this a a gate for completion before docker compose up is called.
