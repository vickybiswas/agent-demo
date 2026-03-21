"""
Regression test suite.

Runs all unit and API tests to verify comprehensive coverage.
"""

import subprocess
import sys


def test_regression_all_unit_tests():
    """Run all unit tests."""
    import os
    import glob
    backend_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unit_tests = glob.glob(os.path.join(backend_path, "tests/test_*_unit.py"))
    result = subprocess.run(
        [sys.executable, "-m", "pytest"] + unit_tests + ["-v"],
        capture_output=True,
        cwd=backend_path
    )
    assert result.returncode == 0, f"Unit tests failed:\n{result.stdout.decode()}"


def test_regression_all_api_tests():
    """Run all API tests."""
    import os
    import glob
    backend_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_tests = glob.glob(os.path.join(backend_path, "tests/test_*_api.py"))
    result = subprocess.run(
        [sys.executable, "-m", "pytest"] + api_tests + ["-v"],
        capture_output=True,
        cwd=backend_path
    )
    assert result.returncode == 0, f"API tests failed:\n{result.stdout.decode()}"


def test_regression_coverage():
    """Run coverage check."""
    import os
    backend_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            os.path.join(backend_path, "tests"),
            "--cov=.", "--cov-report=term-missing"
        ],
        capture_output=True,
        text=True,
        cwd=backend_path
    )
    assert result.returncode == 0, f"Coverage check failed:\n{result.stdout}"
