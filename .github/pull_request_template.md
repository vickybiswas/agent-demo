# Pull Request

## Description
Brief description of what this PR does.

## Related Issue
Closes #(issue number)

## Changes
- [ ] Backend changes (FastAPI routes, tests, CORS)
- [ ] Frontend changes (React components, styling, animations)
- [ ] Docker changes (Dockerfile, docker-compose.yaml)
- [ ] Documentation changes (CLAUDE.md, STARTUP.md, etc.)

## Testing

### REGRESSION.md Checklist (MANDATORY)
**This PR cannot be merged until ALL items below are complete.**

- [ ] **Phase 1**: Local development setup verified (backend, frontend, .env.local)
- [ ] **Phase 2**: CORS & integration testing passed (frontend ↔ backend communication works)
- [ ] **Phase 3**: Unit & API tests passing (100% coverage for backend)
- [ ] **Phase 4**: Frontend tests passing (TypeScript strict, build succeeds, Playwright tests pass)
- [ ] **Phase 5**: Docker orchestration verified (`docker compose up` works, services communicate)
- [ ] **Phase 6**: Code quality checks passed (PEP8, no debug code, docstrings present)

**See REGRESSION.md for detailed checklist and troubleshooting.**

### Manual Testing
- [ ] Tested locally without Docker
- [ ] Tested with `docker compose up`
- [ ] Calculator operations work: 5 + 3 = 8
- [ ] Animations smooth and responsive
- [ ] No console errors or warnings
- [ ] CORS headers present in Network tab

## Code Quality
- [ ] Code follows project conventions
- [ ] No hardcoded `localhost` (uses environment variables)
- [ ] All functions have docstrings
- [ ] Type hints present (Python and TypeScript)
- [ ] No debug `print()` or `console.log()` statements
- [ ] Tests pass locally and in Docker

## Documentation
- [ ] Updated README if needed
- [ ] Updated CLAUDE.md if architecture changed
- [ ] Commit messages are clear and descriptive

## Reviewer Notes
Any additional context for reviewers:
- Design decisions and trade-offs
- Known limitations or future improvements
- Specific areas that need extra review

---

**Remember**: All REGRESSION.md checks must pass before this PR can be merged. This ensures integration issues are caught during development, not in production.
