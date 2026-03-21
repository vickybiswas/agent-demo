# Project Agents - Stranger Things Calculator

This project has 5 specialized agents configured to help with different aspects of development.

---

## 🎯 The 5 Agents

### 1. **PR Review Specialist** (`1-pr-review.md`)
Reviews code quality, security, and best practices

**Invoke when**:
- Before merging pull requests
- Reviewing code from teammates
- Validating changes against requirements

**Ask**: "As PR Review Specialist, review this PR for..."

---

### 2. **Python FastAPI Specialist** (`2-fastapi-specialist.md`)
Expert in building FastAPI backends with PEP8 compliance and full test coverage

**Invoke when**:
- Building backend endpoints
- Writing unit/API tests
- Checking PEP8 compliance
- Handling edge cases

**Ask**: "As Python FastAPI Specialist, help me..."

---

### 3. **React NextJS Specialist** (`3-nextjs-specialist.md`)
Expert in building React/NextJS applications with Stranger Things theme

**Invoke when**:
- Building frontend components
- Creating animations
- Setting up JSON-driven design
- Writing Playwright tests
- Ensuring TypeScript compliance

**Ask**: "As React NextJS Specialist, help me..."

---

### 4. **DevOps Specialist** (`4-devops-specialist.md`)
Expert in Docker, Docker Compose, and infrastructure setup

**Invoke when**:
- Creating Dockerfiles
- Setting up docker-compose.yaml
- Configuring service networking
- Enabling hot-reload development
- Preparing for deployment

**Ask**: "As DevOps Specialist, help me..."

---

### 5. **QA Automation Specialist** (`5-qa-automation-specialist.md`)
Expert in test strategy, test automation, and quality assurance

**Invoke when**:
- Designing test strategy
- Writing unit tests
- Writing API integration tests
- Writing UI/E2E tests (Playwright)
- Achieving 100% test coverage
- Testing edge cases

**Ask**: "As QA Automation Specialist, help me..."

---

## 📋 How to Use Agents

Each agent has a specific domain and responsibilities. Use them by addressing them directly:

```
As [Agent Name], [your request]
```

**Examples**:

```
As Python FastAPI Specialist, create a unit test for the division endpoint
that covers all edge cases including division by zero.
```

```
As React NextJS Specialist, help me implement the calculator display component
with Stranger Things theme styling and animations.
```

```
As DevOps Specialist, set up a docker-compose.yaml that makes frontend
and backend communicate via service names.
```

```
As QA Automation Specialist, help me create a comprehensive Playwright test
suite for all calculator operations.
```

```
As PR Review Specialist, review this code for security issues and test coverage.
```

---

## 🔄 Typical Development Flow

```
1. Start Frontend
   → Ask React NextJS Specialist for help building components
   → Ask QA Automation Specialist for Playwright tests

2. Start Backend
   → Ask Python FastAPI Specialist for endpoint implementation
   → Ask QA Automation Specialist for unit/API tests

3. Setup Docker
   → Ask DevOps Specialist for Dockerfiles and compose setup

4. Code Review
   → Ask PR Review Specialist to review before merge

5. Iterate
   → Use appropriate specialist for each task
```

---

## 🛠️ Agent Context

Each agent has context about:
- **Project structure** (frontend/backend/docker)
- **Requirements** (specifications from INSTRUCTIONS.md)
- **Tools available** (skills, MCP servers, plugins)
- **Success criteria** (what "done" looks like)
- **Quality standards** (PEP8, TypeScript strict, test coverage)

---

## 📚 Reference Files

- `frontend/CLAUDE.md` - Frontend development phases
- `backend/CLAUDE.md` - Backend development phases
- `/nextjs-validator` - Frontend validation skill
- `/fastapi-validator` - Backend validation skill
- `/docker-validator` - Docker validation skill

---

## ⚡ Quick Selection Guide

| Task | Use This Agent |
|------|---|
| Build frontend component | React NextJS Specialist |
| Create backend endpoint | Python FastAPI Specialist |
| Write unit test | QA Automation Specialist |
| Write API test | QA Automation Specialist |
| Write UI test | QA Automation Specialist |
| Setup Docker | DevOps Specialist |
| Review code quality | PR Review Specialist |
| Optimize animation | React NextJS Specialist |
| Handle edge case | Python FastAPI Specialist |
| Test strategy | QA Automation Specialist |

---

**Remember**: These agents are specialized for this project. Use them to get focused, domain-expert help for each part of development.
