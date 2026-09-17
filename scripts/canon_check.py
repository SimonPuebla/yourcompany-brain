#!/usr/bin/env python3
"""Verificación mínima del canon sin dependencias externas."""

from datetime import date
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def report(path, line_number, message):
    print(f"{path.relative_to(ROOT)}:{line_number}: {message}")


def check_review_due():
    failures = 0
    for path in ROOT.rglob("*.yml"):
        if ".git" in path.parts:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = re.match(r"^review_due:\s*(\d{4}-\d{2}-\d{2})\s*$", line)
            if match and date.fromisoformat(match.group(1)) < date.today():
                report(path, line_number, "review_due vencido")
                failures += 1
    return failures


def check_decision_ids():
    path = ROOT / "governance" / "decisiones.md"
    seen = set()
    failures = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^\| (D-\d+) \|", line)
        if match and match.group(1) in seen:
            report(path, line_number, f"ID duplicado {match.group(1)}")
            failures += 1
        elif match:
            seen.add(match.group(1))
    return failures


def main():
    return 1 if check_review_due() + check_decision_ids() else 0


if __name__ == "__main__":
    sys.exit(main())
