# Pull Request: Stranger Things Calculator

## Summary
<!-- Brief description of changes (1-3 sentences) -->

## Changes
<!-- List specific changes made -->
-
-
-

## Related Issues
<!-- Link to GitHub issues, if any -->
Fixes #

## Testing
<!-- Describe testing performed -->

### REGRESSION.md Compliance ✅
<!-- MANDATORY: All PRs must pass REGRESSION.md checklist -->

**Before submitting this PR, complete ALL sections of [REGRESSION.md](../REGRESSION.md):**

- [ ] **Phase 1**: Local development setup (backend + frontend running locally)
- [ ] **Phase 2**: CORS & integration testing (frontend → backend communication verified)
- [ ] **Phase 3**: Testing requirements (all unit, API, and e2e tests pass)
- [ ] **Phase 4**: Docker orchestration (docker compose up works, services communicate)
- [ ] **Phase 5**: Code quality (PEP8, TypeScript strict, SCSS rules pass)
- [ ] **Phase 6**: Git preparation (commits clean, no debug code)

### Test Results
```bash
# Backend tests
python3 -m pytest tests/ -v --cov=. --cov-report=term-missing
# Status: [PASS/FAIL] - Coverage: XX%

# Frontend build
npm run build
# Status: [PASS/FAIL]

# Frontend tests
npm run test
# Status: [PASS/FAIL]

# Docker Compose
docker compose up -d && sleep 3 && curl http://localhost:3004 && curl http://localhost:8004/health && docker compose down
# Status: [PASS/FAIL]
```

## Checklist
- [ ] Code follows PEP8 (Python) and TypeScript strict mode (Frontend)
- [ ] All tests pass (unit + API + e2e)
- [ ] Test coverage: 100% (backend) or 95%+
- [ ] CORS headers validated in browser
- [ ] No hardcoded localhost/ports (use environment variables)
- [ ] No debug code (console.log, print, debugger)
- [ ] Commits have clear messages
- [ ] .env and .env.local are in .gitignore (not committed)
- [ ] REGRESSION.md sections completed before PR

## Screenshots (if applicable)
<!-- Include screenshots for UI changes -->

## Notes
<!-- Any additional notes or context -->

---

**REMEMBER**: This PR must pass REGRESSION.md completely before merge. Run the checklist locally first!

See [REGRESSION.md](../REGRESSION.md) for detailed pre-PR verification steps.
