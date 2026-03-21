# fix-github-issue Skill

**End-to-end GitHub issue resolution with FULL REGRESSION TESTING before any action.**

## What it does

Automates the complete workflow for fixing a GitHub issue with emphasis on testing everything FIRST:

1. **Fetch Issue** - Get issue details from GitHub
2. **360° Regression Testing** - Comprehensive testing BEFORE RCA (backend, frontend, CORS, integration)
3. **RCA** - Concise analysis ONLY of proven findings from testing
4. **Fix Code** - Focused implementation based on tested root cause
5. **Verify Fix** - Re-test to confirm all components work
6. **Create PR** - Push with test evidence
7. **Close Issue** - Link PR with brief summary

## File Structure

```
fix-github-issue/
├── SKILL.md                    # Main skill instructions (7 phases)
├── README.md                   # This file
└── scripts/
    └── issue_fixer.py         # Helper script for issue parsing & validation
```

## Usage

```bash
# Any of these work:
/fix-github-issue #42
/fix-github-issue Fix issue #1
/fix-github-issue https://github.com/owner/repo/issues/123
/fix-github-issue Resolve this: #99 and push the PR
```

## Requirements

- Git repository with remote origin set to GitHub
- `CLAUDE.md` in repository root (for test directions)
- Current working directory is the repo to fix
- GitHub CLI configured (for API access)

## Key Design Decisions

1. **Test FIRST, RCA SECOND** - Comprehensive 360° testing BEFORE posting analysis (no speculation)
2. **Whole-stack testing** - Tests backend alone, frontend alone, CORS, integration, Docker
3. **Concise updates** - Only post RCA AFTER testing proves the issue (brief, no assumptions)
4. **Focused fixes** - Single, proven root cause per issue (no bundling unrelated changes)
5. **Verify everything** - Post-fix testing confirms all components work together
6. **Evidence in PR** - Include test results showing the fix works

## Output

- **GitHub issue comment** with RCA findings and fix strategy
- **Git branch** with committed fix
- **Pull request** against main with fix
- **Issue** linked and closed
- **Local test results** showing all tests passing

## Notes

- The skill requires real GitHub API access and git operations
- It's safe to test since it creates a new branch (doesn't touch main)
- User can manually review the issue comment before code changes execute
- If something fails (tests don't pass), user can debug on the branch and retry
