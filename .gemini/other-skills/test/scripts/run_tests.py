#!/usr/bin/env python3
"""
Bangsamoro Development Platform - Test Runner

Runs unit tests, integration tests, and E2E tests for frontend and backend.
Detects changed files and runs appropriate test suites.

Usage:
    python run_tests.py                    # Run all tests
    python run_tests.py --frontend-only    # Frontend tests only
    python run_tests.py --backend-only     # Backend tests only
    python run_tests.py --unit-only        # Unit tests only
    python run_tests.py --e2e-only         # E2E tests only
    python run_tests.py --changed          # Only test changed files
    python run_tests.py --coverage         # Include coverage report
"""

import subprocess
import sys
import time
import os
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

@dataclass
class TestResult:
    name: str
    passed: bool
    duration: float
    passed_count: int = 0
    failed_count: int = 0
    skipped: bool = False
    error_message: str = ""

def get_project_root() -> Path:
    """Get the CSEA project root directory."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "frontend").exists() and (parent / "backend").exists():
            return parent
    return Path.cwd()

def run_command(cmd: List[str], cwd: Optional[Path] = None, timeout: int = 300) -> tuple:
    """Run a command and return (success, output, duration)."""
    start = time.time()
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        duration = time.time() - start
        success = result.returncode == 0
        output = result.stdout + result.stderr
        return success, output, duration
    except subprocess.TimeoutExpired:
        return False, f"Command timed out after {timeout}s", time.time() - start
    except Exception as e:
        return False, str(e), time.time() - start

def get_changed_files() -> List[str]:
    """Get list of changed files from git."""
    project_root = get_project_root()

    # Get staged + unstaged changes
    success, output, _ = run_command(
        ["git", "diff", "--name-only", "HEAD"],
        cwd=project_root
    )
    if not success:
        return []

    files = output.strip().split("\n") if output.strip() else []

    # Also check untracked files
    success, output, _ = run_command(
        ["git", "ls-files", "--others", "--exclude-standard"],
        cwd=project_root
    )
    if success and output.strip():
        files.extend(output.strip().split("\n"))

    return [f for f in files if f]

def should_run_frontend_tests(changed_files: List[str]) -> bool:
    """Check if frontend tests should run based on changed files."""
    frontend_patterns = ["frontend/", "package.json", "tsconfig.json"]
    return any(
        any(pattern in f for pattern in frontend_patterns)
        for f in changed_files
    )

def should_run_backend_tests(changed_files: List[str]) -> bool:
    """Check if backend tests should run based on changed files."""
    backend_patterns = ["backend/", "requirements.txt", "conftest.py"]
    return any(
        any(pattern in f for pattern in backend_patterns)
        for f in changed_files
    )

def run_frontend_unit_tests(project_root: Path, coverage: bool = False) -> TestResult:
    """Run frontend Jest unit tests."""
    frontend_dir = project_root / "frontend"

    if not (frontend_dir / "package.json").exists():
        return TestResult("Frontend Unit", True, 0, skipped=True)

    cmd = ["npm", "run", "test", "--", "--passWithNoTests"]
    if coverage:
        cmd.extend(["--coverage"])

    success, output, duration = run_command(cmd, cwd=frontend_dir, timeout=300)

    # Parse test results from output
    passed_count = 0
    failed_count = 0

    if "Tests:" in output:
        for line in output.split("\n"):
            if "passed" in line.lower():
                try:
                    parts = line.split()
                    for i, part in enumerate(parts):
                        if "passed" in part.lower() and i > 0:
                            passed_count = int(parts[i-1])
                        if "failed" in part.lower() and i > 0:
                            failed_count = int(parts[i-1])
                except (ValueError, IndexError):
                    pass

    return TestResult(
        name="Frontend Unit",
        passed=success,
        duration=duration,
        passed_count=passed_count,
        failed_count=failed_count,
        error_message="" if success else output[-500:]
    )

def run_backend_unit_tests(project_root: Path, coverage: bool = False) -> TestResult:
    """Run backend pytest unit tests."""
    backend_dir = project_root / "backend"

    if not (backend_dir / "manage.py").exists():
        return TestResult("Backend Unit", True, 0, skipped=True)

    cmd = ["pytest", "-v"]
    if coverage:
        cmd.extend(["--cov=apps", "--cov-report=term-missing"])

    success, output, duration = run_command(cmd, cwd=backend_dir, timeout=300)

    # Parse test results
    passed_count = 0
    failed_count = 0

    for line in output.split("\n"):
        if " passed" in line or " failed" in line:
            try:
                parts = line.split()
                for i, part in enumerate(parts):
                    if part == "passed" and i > 0:
                        passed_count = int(parts[i-1])
                    if part == "failed" and i > 0:
                        failed_count = int(parts[i-1])
            except (ValueError, IndexError):
                pass

    return TestResult(
        name="Backend Unit",
        passed=success,
        duration=duration,
        passed_count=passed_count,
        failed_count=failed_count,
        error_message="" if success else output[-500:]
    )

def run_frontend_integration_tests(project_root: Path) -> TestResult:
    """Run frontend integration tests."""
    frontend_dir = project_root / "frontend"

    if not (frontend_dir / "package.json").exists():
        return TestResult("Frontend Integration", True, 0, skipped=True)

    cmd = ["npm", "run", "test", "--", "--testPathPattern=integration", "--passWithNoTests"]
    success, output, duration = run_command(cmd, cwd=frontend_dir, timeout=300)

    return TestResult(
        name="Frontend Integration",
        passed=success,
        duration=duration,
        error_message="" if success else output[-500:]
    )

def run_backend_integration_tests(project_root: Path) -> TestResult:
    """Run backend integration tests."""
    backend_dir = project_root / "backend"

    if not (backend_dir / "manage.py").exists():
        return TestResult("Backend Integration", True, 0, skipped=True)

    cmd = ["pytest", "-v", "-m", "integration"]
    success, output, duration = run_command(cmd, cwd=backend_dir, timeout=300)

    return TestResult(
        name="Backend Integration",
        passed=success,
        duration=duration,
        error_message="" if success else output[-500:]
    )

def run_e2e_tests(project_root: Path) -> TestResult:
    """Run Playwright E2E tests."""
    frontend_dir = project_root / "frontend"

    # Check if playwright is configured
    playwright_config = frontend_dir / "playwright.config.ts"
    if not playwright_config.exists():
        return TestResult("E2E Tests", True, 0, skipped=True)

    cmd = ["npx", "playwright", "test"]
    success, output, duration = run_command(cmd, cwd=frontend_dir, timeout=600)

    return TestResult(
        name="E2E Tests",
        passed=success,
        duration=duration,
        error_message="" if success else output[-500:]
    )

def verify_migrations(project_root: Path) -> TestResult:
    """Verify database migrations."""
    backend_dir = project_root / "backend"

    if not (backend_dir / "manage.py").exists():
        return TestResult("Migration Verification", True, 0, skipped=True)

    # Check for migration verification script
    verify_script = project_root / ".claude" / "skills" / "database" / "scripts" / "verify_migrations.py"

    if verify_script.exists():
        cmd = ["python", str(verify_script), "."]
        success, output, duration = run_command(cmd, cwd=backend_dir, timeout=60)
    else:
        # Fallback: just check for pending migrations
        cmd = ["python", "manage.py", "makemigrations", "--check", "--dry-run"]
        success, output, duration = run_command(cmd, cwd=backend_dir, timeout=60)

    return TestResult(
        name="Migration Verification",
        passed=success,
        duration=duration,
        error_message="" if success else output[-300:]
    )

def print_header():
    """Print test run header."""
    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}TEST RESULTS{RESET}")
    print(f"{'='*50}\n")

def print_section(title: str):
    """Print a section header."""
    print(f"{BOLD}{title}:{RESET}")
    print("-" * 40)

def print_result(result: TestResult):
    """Print a single test result."""
    if result.skipped:
        status = f"{YELLOW}[SKIP]{RESET}"
    elif result.passed:
        status = f"{GREEN}[PASS]{RESET}"
    else:
        status = f"{RED}[FAIL]{RESET}"

    duration_str = f"{result.duration:.1f}s"

    if result.passed_count or result.failed_count:
        counts = f"({result.passed_count} passed, {result.failed_count} failed)"
        print(f"  {status} {result.name} {counts} - {duration_str}")
    else:
        print(f"  {status} {result.name} - {duration_str}")

    if not result.passed and result.error_message:
        print(f"\n{RED}    Error:{RESET}")
        for line in result.error_message.split("\n")[:10]:
            print(f"    {line}")
        print()

def print_summary(results: List[TestResult]):
    """Print final summary."""
    print(f"\n{'='*50}")

    passed = sum(1 for r in results if r.passed and not r.skipped)
    failed = sum(1 for r in results if not r.passed and not r.skipped)
    skipped = sum(1 for r in results if r.skipped)

    if failed == 0:
        print(f"{GREEN}ALL TESTS PASSED{RESET} - Ready for /gitops")
    else:
        print(f"{RED}TESTS FAILED{RESET} - {failed} check(s) failed")

    print(f"\nSummary: {passed} passed, {failed} failed, {skipped} skipped")
    print(f"{'='*50}\n")

def main():
    parser = argparse.ArgumentParser(description="CSEA Test Runner")
    parser.add_argument("--frontend-only", action="store_true", help="Run frontend tests only")
    parser.add_argument("--backend-only", action="store_true", help="Run backend tests only")
    parser.add_argument("--unit-only", action="store_true", help="Run unit tests only")
    parser.add_argument("--integration-only", action="store_true", help="Run integration tests only")
    parser.add_argument("--e2e-only", action="store_true", help="Run E2E tests only")
    parser.add_argument("--changed", action="store_true", help="Only test based on changed files")
    parser.add_argument("--coverage", action="store_true", help="Include coverage report")
    args = parser.parse_args()

    project_root = get_project_root()
    results: List[TestResult] = []

    # Determine what to test
    run_frontend = not args.backend_only
    run_backend = not args.frontend_only
    run_unit = not args.integration_only and not args.e2e_only
    run_integration = not args.unit_only and not args.e2e_only
    run_e2e = not args.unit_only and not args.integration_only

    # Filter by changed files if requested
    if args.changed:
        changed_files = get_changed_files()
        if changed_files:
            run_frontend = run_frontend and should_run_frontend_tests(changed_files)
            run_backend = run_backend and should_run_backend_tests(changed_files)
        else:
            print(f"{YELLOW}No changed files detected{RESET}")

    print_header()

    # Frontend Tests
    if run_frontend:
        print_section("Frontend")
        if run_unit:
            result = run_frontend_unit_tests(project_root, coverage=args.coverage)
            results.append(result)
            print_result(result)
        if run_integration:
            result = run_frontend_integration_tests(project_root)
            results.append(result)
            print_result(result)
        if run_e2e:
            result = run_e2e_tests(project_root)
            results.append(result)
            print_result(result)
        print()

    # Backend Tests
    if run_backend:
        print_section("Backend")
        if run_unit:
            result = run_backend_unit_tests(project_root, coverage=args.coverage)
            results.append(result)
            print_result(result)
        if run_integration:
            result = run_backend_integration_tests(project_root)
            results.append(result)
            print_result(result)

        # Migration verification
        result = verify_migrations(project_root)
        results.append(result)
        print_result(result)
        print()

    print_summary(results)

    # Exit with error code if any tests failed
    if any(not r.passed and not r.skipped for r in results):
        sys.exit(1)

if __name__ == "__main__":
    main()
