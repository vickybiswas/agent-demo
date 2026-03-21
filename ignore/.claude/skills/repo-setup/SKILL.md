---
name: repo-setup
description: Generate complete Claude-orchestrated project setup from INSTRUCTIONS.md. Creates agents, skills, hooks, and domain guides automatically. Use when you have a project specification in INSTRUCTIONS.md format and need to generate the full repository infrastructure (agents, validators, orchestration guides, domain-specific CLAUDE.md files). Outputs reproducible, DRY-compliant setup with no manual file creation needed.
---

# Repo Setup Skill - Automated Infrastructure Generation

## Purpose

Transform a project INSTRUCTIONS.md into a complete, production-ready repository setup with:
- Automated code formatting hooks
- 5 specialized agents
- 3 domain-specific validators (skills)
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

## What Gets Generated

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

### 3. Three Validators (`.claude/skills/*/SKILL.md`)
1. **nextjs-validator** - TypeScript strict, SCSS organized, animations smooth, no images, Playwright ready
2. **fastapi-validator** - PEP8, separate routes, zero external deps, 100% coverage, edge cases
3. **docker-validator** - Dockerfiles, compose.yaml, ports, volumes, service networking

### 4. Orchestration Files

**CLAUDE.md** (Root orchestration):
- 3 STEPs to spawn agents in parallel (Frontend + Backend) then sequential (Docker)
- Quality gates for each domain
- Dependencies and timing

**CREATE.md** (Docker-specific guide):
- Phase 1: Frontend Dockerfile (node:18-alpine)
- Phase 2: Backend Dockerfile (python:3.11-slim)
- Phase 3: docker-compose.yaml (service networking, hot-reload volumes)
- Phase 4: Integration testing

### 5. Domain Guides

**frontend/CLAUDE.md** (7 phases):
- Phase 1: Setup (project init, dependencies)
- Phase 2: Theme & Layout (JSON config, SCSS, Stranger Things aesthetic)
- Phase 3: Core Component (calculator logic)
- Phase 4: Animations (framer-motion, sounds, effects, 60fps)
- Phase 5: Backend Integration (API calls to backend:8004)
- Phase 6: Testing (Playwright e2e tests)
- Phase 7: Review (TypeScript strict, build succeeds, tests pass)

**backend/CLAUDE.md** (8 phases):
- Phase 1: Setup (structure, requirements.txt: fastapi, uvicorn ONLY)
- Phase 2: Main App (FastAPI instance, CORS, /health endpoint)
- Phase 3: Routes (add.py, subtract.py, multiply.py, divide.py - separate files)
- Phase 4: Unit Tests (5+ per operation, edge cases)
- Phase 5: API Tests (5+ per endpoint, HTTP validation)
- Phase 6: Regression Suite (all tests + 100% coverage)
- Phase 7: Code Quality (PEP8, docstrings, type hints)
- Phase 8: Documentation (README, endpoint docs)

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
5. Generate CLAUDE.md (root orchestration)
6. Generate CREATE.md (Docker phases)
7. Generate frontend/CLAUDE.md (7-phase guide)
8. Generate backend/CLAUDE.md (8-phase guide)

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
├── CLAUDE.md                     (Root orchestration)
├── CREATE.md                     (Docker guide)
├── frontend/CLAUDE.md            (7 phases)
└── backend/CLAUDE.md             (8 phases)
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

### Agent Autonomy
- Each agent reads ONE file (no cross-file jumps)
- Domain files are self-contained
- No coordination needed between agents (parallel execution)

## Framework Focus

The skill generates guides with **specific framework focus**:

- **Frontend**: Animations via framer-motion, styling via SCSS, testing via Playwright
- **Backend**: FastAPI endpoints, pytest for testing, PEP8 for code quality
- **Docker**: Compose for orchestration, volumes for hot-reload, networking for services

Agents follow these frameworks when building, not generic approaches.

## Quality Gates

Generated setup enforces:
- ✅ `frontend/CLAUDE.md` → `/nextjs-validator` MUST PASS
- ✅ `backend/CLAUDE.md` → `/fastapi-validator` MUST PASS
- ✅ `CREATE.md` → `/docker-validator` MUST PASS

No phase advances without skill validation.

## Example

**Input**: INSTRUCTIONS.md with:
- Agents: PR Review, FastAPI Specialist, NextJS Specialist, DevOps Specialist, QA Specialist
- Stack: NextJS/TypeScript/SCSS (3004), FastAPI/Python (8004), Docker Compose
- Requirements: Stranger Things theme, zero external deps, 100% test coverage

**Output**: Complete 13-file setup ready for agent execution via `claude build`

## Notes

- Skill outputs files to current working directory
- All files are properly formatted (hooks auto-fix on creation)
- Generated agents are ready to spawn immediately
- No manual editing needed unless customizing beyond INSTRUCTIONS.md
