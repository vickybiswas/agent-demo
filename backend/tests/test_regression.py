"""
Regression test suite.

Runs all unit and API tests to verify comprehensive coverage.
"""

import subprocess
import sys


def test_regression_all_unit_tests():
    """Run all unit tests."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_*_unit.py", "-v"],
        capture_output=True,
        cwd="/Users/vicky/rani/agent-demo/backend"
    )
    assert result.returncode == 0, f"Unit tests failed:\n{result.stdout.decode()}"


def test_regression_all_api_tests():
    """Run all API tests."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_*_api.py", "-v"],
        capture_output=True,
        cwd="/Users/vicky/rani/agent-demo/backend"
    )
    assert result.returncode == 0, f"API tests failed:\n{result.stdout.decode()}"


def test_regression_coverage():
    """Run coverage check."""
    result = subprocess.run(
        [
            sys.executable, "-m", "pytest", "tests/",
            "--cov=.", "--cov-report=term-missing"
        ],
        capture_output=True,
        text=True,
        cwd="/Users/vicky/rani/agent-demo/backend"
    )
    assert result.returncode == 0, f"Coverage check failed:\n{result.stdout}"
