---
name: fix-github-issue
description: |
  End-to-end GitHub issue resolution for Docker-based projects with FULL REGRESSION
  TESTING before any action. Fetch issue, perform comprehensive 360° RCA with actual
  testing, fix code, verify all components work together, create PR, and close issue.

  Use this skill when user asks to "fix issue #N", "resolve this GitHub issue",
  "do an RCA and fix it", etc. Performs complete integration testing across:
  - Backend service startup and health
  - Frontend service startup and asset loading
  - Frontend↔Backend CORS communication
  - End-to-end calculator operations
  - Docker Compose orchestration

  Only posts RCA AFTER comprehensive testing proves what's actually broken.
---

# Fix GitHub Issue - Docker-First with Full Regression Testing

Automated issue resolution with complete application testing before any changes.

## Core Principle

**Test EVERYTHING before posting RCA** — Don't assume the problem. Prove it through actual testing:
- Does backend service start?
- Does frontend load?
- Can frontend reach backend? (CORS working?)
- Do end-to-end operations work?
- What actually fails?

## Workflow Overview

1. **Fetch Issue** - Get details from GitHub
2. **360° Regression Testing** - Test entire application stack
3. **Root Cause Analysis** - Post CONCISE findings only after testing
4. **Implement Fix** - Focused change based on proven problem
5. **Verify Fix** - Re-test to confirm resolution
6. **Create PR** - Push with test evidence
7. **Close Issue** - Link PR with brief summary

## Prerequisites

- Git repo with GitHub remote
- CLAUDE.md exists (defines architecture)
- docker-compose.yaml for orchestration
- Project structure: frontend/, backend/, etc.
- GitHub CLI configured

## Usage

```bash
/fix-github-issue #3
/fix-github-issue https://github.com/owner/repo/issues/3
```

---

## Phase 1: Fetch Issue

**Input:** Issue number/URL

**Steps:**
1. Parse issue identifier
2. Fetch from GitHub (title, body, state)
3. Note the claimed problem

**Output:** Issue data

---

## Phase 2: 360° Regression Testing (BEFORE RCA)

**Input:** Issue details

**CRITICAL**: Test the entire application stack to find the ACTUAL problem.

**PERFORMANCE**: All testing below is INDEPENDENT → spawn all test tasks in parallel for 5-10x speedup.

```
Spawn in parallel:
- Backend service test
- Frontend service test
- CORS header test
- Integration test
- Docker test

Collect results when all complete (NOT sequentially).
```

### Backend Testing
```bash
# Try to start backend
cd backend && python3 main.py

# Check 1: Does service start?
curl http://localhost:8004/health
# Expected: {"status":"ok"} or connection refused?

# Check 2: Do endpoints respond?
curl "http://localhost:8004/add?num1=5&num2=3"
# Expected: {"result":8} or error?

# Check 3: Review code for issues
# - main.py CORS configuration correct?
# - routes/__init__.py importing all routes?
# - requirements.txt has all dependencies?
```

### Frontend Testing
```bash
# Check 1: Can frontend start?
cd frontend && npm run dev

# Check 2: Does it load?
curl http://localhost:3004/

# Check 3: Check environment
# - .env has correct NEXT_PUBLIC_API_URL?
# - .env.local exists for local dev?

# Check 4: Are dependencies installed?
npm list | grep -E "react|next|framer"
```

### Integration Testing
```bash
# With both services running:

# Check 1: Can frontend reach backend?
# (Open browser, check Network tab)
# Click calculator button → check XHR to backend

# Check 2: CORS headers present?
curl -H "Origin: http://localhost:3004" -v http://localhost:8004/health
# Look for Access-Control-Allow-Origin header

# Check 3: End-to-end operation
# In browser: 5 + 3 = ? Should show 8
# If shows error or no result → integration broken
```

### Docker Testing
```bash
# If using Docker:
docker compose up -d

# Check 1: Services started?
docker compose ps

# Check 2: Both ports listening?
curl http://localhost:3004/
curl http://localhost:8004/health

# Check 3: Frontend env correct?
docker compose exec frontend sh -c 'echo $NEXT_PUBLIC_API_URL'
# Should be: http://backend:8004
```

**Output:** Test results showing exactly what fails

---

## Phase 3: Root Cause Analysis (AFTER testing)

**Input:** Test results from Phase 2

**Steps:**
1. Only now analyze based on PROVEN failures
2. Review relevant code
3. Reference CLAUDE.md phases
4. Document findings

**Post to GitHub as ONE concise comment:**

```markdown
## Root Cause

**Issue:** [problem statement from tests]

**Component:** Backend | Frontend | Integration | Docker

**Finding:** [What actually fails, proven by testing]

**CLAUDE.md Phase:** [Reference to relevant phase]

**Fix:**
- [specific change 1]
- [specific change 2]
```

**Key**: Keep it SHORT. Only include what testing proved. No speculation.

---

## Phase 4: Implement Fix

**Input:** Tested root cause

**Steps:**
1. Create branch: `fix/issue-<number>`
2. Make focused change based on RCA
3. Commit with issue reference

**Output:** Changes committed

---

## Phase 5: Verify Fix

**Input:** Fixed code on branch

**Steps:**
1. Run the SAME tests from Phase 2
2. Confirm all tests now PASS
3. Document test results

**Output:** Test evidence showing fix works

---

## Phase 6: Create PR

**Input:** Verified fix

**Steps:**
1. Push branch
2. Create PR with:
   - Title: "Fix: [issue title]"
   - Body: RCA + test evidence (concise)
   - Base: main, Head: fix/issue-N

**Output:** PR created

---

## Phase 7: Close Issue

**Input:** PR number

**Steps:**
1. Comment on issue: "Fixed in PR #X"
2. Close issue

**Output:** Issue linked and closed

---

## Success Criteria

✅ Comprehensive testing BEFORE RCA
✅ RCA proves actual problem (not assumed)
✅ Fix is focused on proven issue
✅ Post-fix testing confirms resolution
✅ GitHub updates are CONCISE (no speculation)
✅ All components tested together:
  - Backend alone ✅
  - Frontend alone ✅
  - Frontend ↔ Backend ✅
  - Docker orchestration ✅
  - End-to-end operations ✅

## Key Rules

1. **Don't post RCA until testing is done** - Test first, analyze second
2. **Test the whole stack** - Not just the broken component
3. **Prove the problem** - Use actual test commands/output
4. **Keep RCA brief** - Only include what testing proved
5. **Show evidence in PR** - Include test results showing fix works
6. **Reference CLAUDE.md** - Connect to project phases
7. **One test → One fix** - Don't bundle unrelated changes

## Testing Checklist (Use Before Posting RCA)

- [ ] Backend service starts? (python3 main.py)
- [ ] Backend health endpoint works? (curl /health)
- [ ] Backend endpoints respond? (curl /add, /subtract, etc.)
- [ ] Frontend assets load? (npm run dev, curl localhost:3004)
- [ ] Frontend environment correct? (echo $NEXT_PUBLIC_API_URL)
- [ ] CORS headers present? (curl -H Origin...)
- [ ] Frontend→Backend communication works? (browser Network tab)
- [ ] End-to-end calculation works? (click calculator in browser)
- [ ] Docker Compose works? (docker compose up, all services running)
- [ ] All CLAUDE.md phases referenced? (which phase has the fix?)

**Only after ALL checkboxes**: Post RCA and fix code.
