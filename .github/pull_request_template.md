# Pull Request: Stranger Things Calculator

## Description
<!-- Briefly describe what this PR adds or fixes -->

## Changes
<!-- List the main changes in this PR -->
- 
- 
- 

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Code refactoring
- [ ] Documentation
- [ ] Docker/Infrastructure

## REGRESSION.md Checklist
**⚠️ MANDATORY: All items must be checked before merge**

### Phase 1: Local Backend Setup
- [ ] Backend service starts without errors
- [ ] Health endpoint returns 200 OK
- [ ] Port 8004 is listening

### Phase 2: Local Frontend Setup
- [ ] Frontend service starts without errors
- [ ] Development server running on :3004
- [ ] Next.js build succeeds

### Phase 3: CORS & Integration Testing
- [ ] CORS headers present in responses
- [ ] Frontend can call backend endpoints
- [ ] End-to-end operation works (5 + 3 = 8)
- [ ] No CORS errors in browser console

### Phase 4: Testing Requirements
- [ ] Backend unit tests: all pass, 100% coverage
- [ ] Backend API tests: all pass
- [ ] Frontend E2E tests: all pass
- [ ] No test failures

### Phase 5: Docker Compose Verification
- [ ] Docker Compose starts both services
- [ ] Frontend accessible on :3004
- [ ] Backend accessible on :8004
- [ ] Health check passes
- [ ] CORS headers present
- [ ] End-to-end operation works

### Phase 6: Code Quality
- [ ] Backend: PEP8 compliant
- [ ] Backend: Type hints complete
- [ ] Backend: Docstrings present
- [ ] Frontend: TypeScript strict mode passes
- [ ] Frontend: Build succeeds
- [ ] Frontend: No console errors
- [ ] Frontend: Prettier formatted

## Testing Evidence
<!-- Provide screenshots or output showing tests pass -->

### Backend Tests
```
<paste output from: python3 -m pytest tests/ -v>
```

### Frontend Tests
```
<paste output from: npm test>
```

### Docker Verification
```
<paste output from: docker compose up -d && curl http://localhost:8004/health>
```

## Screenshots (If Applicable)
<!-- Show calculator UI, CORS headers, etc. -->

## Related Issues
<!-- Link to GitHub issues: Closes #123 -->

## Additional Notes
<!-- Any other information reviewers should know -->

---

## Review Checklist

### Code Reviewer
- [ ] All REGRESSION.md items are checked
- [ ] No merge conflicts
- [ ] Code follows project conventions
- [ ] TypeScript strict mode passes (frontend)
- [ ] PEP8 compliant (backend)
- [ ] Tests passing with full coverage
- [ ] CORS configuration correct

### Quality Gates
- [ ] Frontend validator passed: `/nextjs-validator`
- [ ] Backend validator passed: `/fastapi-validator`
- [ ] Docker validator passed: `/docker-validator`

### Before Merge
- [ ] Squash or rebase commits (as per project standards)
- [ ] Delete feature branch
- [ ] Update documentation if needed

---

**See REGRESSION.md for the complete testing checklist.**
**See CLAUDE.md for project orchestration details.**
**See STARTUP.md for service startup options.**
