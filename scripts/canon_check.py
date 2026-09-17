#!/usr/bin/env python3
"""Verificación mínima del canon sin dependencias externas."""

from datetime import date
from pathlib import Path
import argparse
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


def check_required_canon_fields():
    failures = 0
    for path in (ROOT / "canon").glob("*.yml"):
        text = path.read_text(encoding="utf-8")
        for field in ("owner:", "source:", "review_due:"):
            if field not in text:
                report(path, 1, f"falta {field}")
                failures += 1
    return failures


def check_placeholders():
    failures = 0
    ignored_dirs = {"skills", "scripts", ".github"}
    ignored_files = {"README.md", "PUBLISHING.md", "CONTRIBUTING.md"}
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if any(part in ignored_dirs for part in path.relative_to(ROOT).parts):
            continue
        if path.name in ignored_files:
            continue
        if path.suffix not in {".md", ".yml", ".yaml", ".json"}:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "[COMPLETAR" in line:
                report(path, line_number, "placeholder pendiente")
                failures += 1
    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="falla si quedan placeholders o campos canonicos minimos sin declarar",
    )
    args = parser.parse_args()

    failures = check_review_due() + check_decision_ids()
    if args.strict:
        failures += check_required_canon_fields() + check_placeholders()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
