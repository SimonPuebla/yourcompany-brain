#!/usr/bin/env python3
"""Verificación del canon sin dependencias externas."""

from datetime import date
from pathlib import Path
import argparse
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CLAIMS_PATH = ROOT / "canon" / "claim-registry.yml"
INBOX_PATH = ROOT / "_inbox"
APPROVED_STATUSES = {"approved", "approved_with_conditions"}
INBOX_FIELDS = ("id", "titulo", "clase", "angulo", "revisor", "destino", "fuente", "fecha_fuente", "detectado", "estado")
INBOX_CLASSES = {"A", "B"}
INBOX_STATES = {"propuesto", "aprobado", "rechazado", "aplicado", "bloqueado"}
LOCAL_PATH_MARKERS = ("/" + "Users/", "C:" + "\\Users")


def report(path, line_number, message):
    print(f"{path.relative_to(ROOT)}:{line_number}: {message}")


def unquote(value):
    return value.strip().strip('"').strip("'")


def text_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".yml", ".yaml", ".json", ".py"}:
            yield path


def check_review_due(warn_days=0):
    failures = 0
    today = date.today()
    for path in ROOT.rglob("*.yml"):
        if ".git" in path.parts:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = re.match(r"^review_due:\s*(\d{4}-\d{2}-\d{2})\s*$", line)
            if not match:
                continue
            review_due = date.fromisoformat(match.group(1))
            if review_due < today:
                report(path, line_number, f"review_due vencido: {review_due.isoformat()}")
                failures += 1
            elif (review_due - today).days <= warn_days:
                report(path, line_number, f"aviso: review_due vence en {(review_due - today).days} días")
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


def check_claims():
    """Un claim aprobado necesita owner, wording en ambos idiomas y source."""
    failures = 0
    current = None
    records = []
    for line_number, line in enumerate(CLAIMS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        claim_match = re.match(r"^  - id:\s*(.+)$", line)
        if claim_match:
            current = {"id": (unquote(claim_match.group(1)), line_number)}
            records.append(current)
            continue
        field_match = re.match(r"^    ([a-z_]+):\s*(.*)$", line)
        if current is not None and field_match:
            current[field_match.group(1)] = (unquote(field_match.group(2)), line_number)

    for claim in records:
        claim_id, start_line = claim["id"]
        if claim.get("status", ("", start_line))[0] not in APPROVED_STATUSES:
            continue
        for field in ("owner", "wording_es", "wording_en", "source"):
            value, line_number = claim.get(field, ("", start_line))
            if not value or "[COMPLETAR" in value:
                report(CLAIMS_PATH, line_number, f"claim {claim_id}: falta {field}")
                failures += 1
    return failures


def check_inbox():
    failures = 0
    seen = {}
    for path in sorted(INBOX_PATH.glob("*/C-*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            report(path, 1, "candidato sin frontmatter")
            failures += 1
            continue
        fields = {}
        for line_number, line in enumerate(lines[1 : lines.index("---", 1)], 2):
            match = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if match:
                fields[match.group(1)] = (unquote(match.group(2)), line_number)

        for field in INBOX_FIELDS:
            if not fields.get(field, ("", 1))[0]:
                report(path, 1, f"candidato: falta {field}")
                failures += 1

        candidate_id, id_line = fields.get("id", ("", 1))
        if candidate_id and candidate_id != path.stem:
            report(path, id_line, "id no coincide con el nombre del archivo")
            failures += 1
        if candidate_id in seen:
            report(path, id_line, f"id duplicado; primera aparición en {seen[candidate_id].relative_to(ROOT)}")
            failures += 1
        elif candidate_id:
            seen[candidate_id] = path

        for field, allowed in (("clase", INBOX_CLASSES), ("estado", INBOX_STATES)):
            value, line_number = fields.get(field, ("", 1))
            if value and value not in allowed:
                report(path, line_number, f"{field} inválido: {value}")
                failures += 1
        for field in ("fecha_fuente", "detectado"):
            value, line_number = fields.get(field, ("", 1))
            try:
                if value:
                    date.fromisoformat(value)
            except ValueError:
                report(path, line_number, f"{field} no tiene formato ISO válido")
                failures += 1
    return failures


def check_local_paths():
    failures = 0
    for path in text_files():
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(marker in line for marker in LOCAL_PATH_MARKERS):
                report(path, line_number, "ruta local no permitida")
                failures += 1
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
    ignored_dirs = {"skills", "scripts", ".github", ".claude", "templates", "automation"}
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
    parser.add_argument(
        "--proximos",
        type=int,
        default=0,
        metavar="DIAS",
        help="avisa que fechas de revision vencen dentro de esa cantidad de dias",
    )
    args = parser.parse_args()

    failures = check_review_due(args.proximos) + check_decision_ids() + check_claims() + check_inbox() + check_local_paths()
    if args.strict:
        failures += check_required_canon_fields() + check_placeholders()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
