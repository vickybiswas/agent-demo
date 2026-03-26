#!/usr/bin/env python3
"""
GitHub Issue Fixer - Orchestrates the complete issue resolution workflow.

Usage:
    python issue_fixer.py <issue_identifier>

Examples:
    python issue_fixer.py "#42"
    python issue_fixer.py "42"
    python issue_fixer.py "https://github.com/owner/repo/issues/123"
"""

import re
import sys
import json
import subprocess
from pathlib import Path

def parse_issue_id(identifier):
    """Extract issue number from various formats."""
    # Handle full URL
    match = re.search(r'/issues/(\d+)', identifier)
    if match:
        return int(match.group(1))

    # Handle #123 or just 123
    match = re.search(r'#?(\d+)', identifier)
    if match:
        return int(match.group(1))

    raise ValueError(f"Invalid issue identifier: {identifier}")

def get_repo_context():
    """Get repo owner and name from git remote."""
    try:
        result = subprocess.run(
            ['git', 'config', '--get', 'remote.origin.url'],
            capture_output=True,
            text=True,
            check=True
        )
        url = result.stdout.strip()

        # Handle both https and ssh URLs
        match = re.search(r'(?:https://github\.com/|git@github\.com:)([^/]+)/([^/]+?)(?:\.git)?$', url)
        if match:
            return match.group(1), match.group(2)

        raise ValueError(f"Could not parse GitHub URL: {url}")
    except subprocess.CalledProcessError:
        raise RuntimeError("Not a git repository or no remote origin set")

def validate_claude_md():
    """Check that CLAUDE.md exists in repo root."""
    if not Path('CLAUDE.md').exists():
        raise FileNotFoundError("CLAUDE.md not found in repository root")
    print("✓ CLAUDE.md found")

def log_phase(phase_num, title):
    """Log the start of a workflow phase."""
    print(f"\n{'='*60}")
    print(f"Phase {phase_num}: {title}")
    print('='*60)

# Main entry point
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python issue_fixer.py <issue_identifier>")
        sys.exit(1)

    issue_id = parse_issue_id(sys.argv[1])
    owner, repo = get_repo_context()

    print(f"📋 Issue: #{issue_id}")
    print(f"📦 Repo: {owner}/{repo}")

    validate_claude_md()

    # Output configuration for Claude to use
    config = {
        "issue_number": issue_id,
        "owner": owner,
        "repo": repo,
        "branch_name": f"fix/issue-{issue_id}",
        "pr_base": "main"
    }

    print(json.dumps(config, indent=2))
