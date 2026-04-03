#!/usr/bin/env python3
"""
Build Verification for GitOps

Runs build checks before allowing commits:
- Frontend: lint, build, test
- Backend: Django check, pytest

Usage:
    python build_verify.py [--frontend-only | --backend-only]

    --frontend-only  Run only frontend checks
    --backend-only   Run only backend checks
"""

import subprocess
import sys
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class CheckCategory(Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"


class CheckStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"


@dataclass
class CheckResult:
    name: str
    category: CheckCategory
    status: CheckStatus
    output: str
    duration: float
    command: str


# Check definitions
FRONTEND_CHECKS = [
    {"name": "Lint", "command": "npm run lint", "timeout": 120},
    {"name": "Build", "command": "npm run build", "timeout": 300},
    {"name": "Test", "command": "npm run test -- --passWithNoTests --testPathIgnorePatterns=e2e", "timeout": 300},
]

BACKEND_CHECKS = [
    {"name": "Django Check", "command": "DEBUG=True python3 manage.py check", "timeout": 30},
    {"name": "Test", "command": "DEBUG=True python3 -m pytest -q", "timeout": 300},
]


def find_project_root() -> Path:
    """Find the project root directory."""
    current = Path.cwd()
    while current != current.parent:
        if (current / "frontend").exists() and (current / "backend").exists():
            return current
        current = current.parent
    return Path.cwd()


def run_check(
    name: str,
    command: str,
    category: CheckCategory,
    cwd: Path,
    timeout: int = 120
) -> CheckResult:
    """Run a single check and return the result."""
    start_time = time.time()

    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        duration = time.time() - start_time

        if result.returncode == 0:
            return CheckResult(
                name=name,
                category=category,
                status=CheckStatus.PASS,
                output=result.stdout[:500] if result.stdout else "",
                duration=duration,
                command=command
            )
        else:
            error_output = result.stderr or result.stdout
            return CheckResult(
                name=name,
                category=category,
                status=CheckStatus.FAIL,
                output=error_output[:2000] if error_output else "No error output",
                duration=duration,
                command=command
            )

    except subprocess.TimeoutExpired:
        duration = time.time() - start_time
        return CheckResult(
            name=name,
            category=category,
            status=CheckStatus.FAIL,
            output=f"Timeout after {timeout}s",
            duration=duration,
            command=command
        )
    except Exception as e:
        duration = time.time() - start_time
        return CheckResult(
            name=name,
            category=category,
            status=CheckStatus.FAIL,
            output=str(e),
            duration=duration,
            command=command
        )


def run_frontend_checks(project_root: Path) -> list[CheckResult]:
    """Run all frontend checks."""
    results = []
    frontend_dir = project_root / "frontend"

    if not frontend_dir.exists():
        return [CheckResult(
            name="Frontend",
            category=CheckCategory.FRONTEND,
            status=CheckStatus.SKIP,
            output="frontend/ directory not found",
            duration=0,
            command=""
        )]

    has_failure = False
    for check in FRONTEND_CHECKS:
        if has_failure:
            results.append(CheckResult(
                name=check["name"],
                category=CheckCategory.FRONTEND,
                status=CheckStatus.SKIP,
                output="Skipped due to previous failure",
                duration=0,
                command=check["command"]
            ))
        else:
            result = run_check(
                name=check["name"],
                command=check["command"],
                category=CheckCategory.FRONTEND,
                cwd=frontend_dir,
                timeout=check["timeout"]
            )
            results.append(result)
            if result.status == CheckStatus.FAIL:
                has_failure = True

    return results


def run_backend_checks(project_root: Path) -> list[CheckResult]:
    """Run all backend checks."""
    results = []
    backend_dir = project_root / "backend"

    if not backend_dir.exists():
        return [CheckResult(
            name="Backend",
            category=CheckCategory.BACKEND,
            status=CheckStatus.SKIP,
            output="backend/ directory not found",
            duration=0,
            command=""
        )]

    has_failure = False
    for check in BACKEND_CHECKS:
        if has_failure:
            results.append(CheckResult(
                name=check["name"],
                category=CheckCategory.BACKEND,
                status=CheckStatus.SKIP,
                output="Skipped due to previous failure",
                duration=0,
                command=check["command"]
            ))
        else:
            result = run_check(
                name=check["name"],
                command=check["command"],
                category=CheckCategory.BACKEND,
                cwd=backend_dir,
                timeout=check["timeout"]
            )
            results.append(result)
            if result.status == CheckStatus.FAIL:
                has_failure = True

    return results


def format_results(results: list[CheckResult]) -> str:
    """Format check results for display."""
    output = []
    output.append("BUILD VERIFICATION RESULTS")
    output.append("=" * 50)

    # Group by category
    by_category = {cat: [] for cat in CheckCategory}
    for result in results:
        by_category[result.category].append(result)

    total_passed = 0
    total_failed = 0
    total_skipped = 0

    for category in CheckCategory:
        category_results = by_category[category]
        if not category_results:
            continue

        output.append(f"\n{category.value}:")
        output.append("-" * 40)

        for result in category_results:
            status_icon = {
                CheckStatus.PASS: "[PASS]",
                CheckStatus.FAIL: "[FAIL]",
                CheckStatus.SKIP: "[SKIP]"
            }[result.status]

            duration_str = f"({result.duration:.1f}s)" if result.duration > 0 else ""
            output.append(f"  {status_icon} {result.name} {duration_str}")

            if result.status == CheckStatus.FAIL and result.output:
                # Indent error output
                for line in result.output.strip().split("\n")[:10]:
                    output.append(f"    {line}")
                if result.output.count("\n") > 10:
                    output.append("    ... (truncated)")

            if result.status == CheckStatus.PASS:
                total_passed += 1
            elif result.status == CheckStatus.FAIL:
                total_failed += 1
            else:
                total_skipped += 1

    output.append("\n" + "=" * 50)

    if total_failed > 0:
        output.append(f"BUILD BLOCKED: {total_failed} check(s) failed")
        output.append("Fix all errors before committing.")
        output.append("Run /debugger skill to investigate failures.")
    else:
        output.append(f"BUILD PASSED: {total_passed} check(s) passed")
        if total_skipped > 0:
            output.append(f"({total_skipped} skipped)")

    return "\n".join(output)


def main():
    # Parse arguments
    frontend_only = "--frontend-only" in sys.argv
    backend_only = "--backend-only" in sys.argv

    project_root = find_project_root()
    print(f"Project root: {project_root}")
    print("Running build verification...\n")

    all_results = []

    if not backend_only:
        print("Checking frontend...")
        frontend_results = run_frontend_checks(project_root)
        all_results.extend(frontend_results)

    if not frontend_only:
        print("Checking backend...")
        backend_results = run_backend_checks(project_root)
        all_results.extend(backend_results)

    print("\n" + format_results(all_results))

    # Exit with error if any failures
    has_failures = any(r.status == CheckStatus.FAIL for r in all_results)
    sys.exit(1 if has_failures else 0)


if __name__ == "__main__":
    main()
