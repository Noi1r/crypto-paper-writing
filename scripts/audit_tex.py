#!/usr/bin/env python3
"""Audit LaTeX numbers against the paper project's EVIDENCE.md ledger."""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from papercheck import evidence


def selftest() -> int:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        ledger = root / "EVIDENCE.md"
        log = root / "result.log"
        log.write_text("1.23 s\n", encoding="utf-8")
        evidence.append_row(str(ledger), "1.23 s", "measure", "result.log", "toy-commit", "toy-machine", runs="5 / median")
        tex = root / "paper.tex"
        tex.write_text("\\begin{document}\nTime: 1.23 s\\ev{E1}.\n\\end{document}\n", encoding="utf-8")
        rows = evidence.read_ledger(str(ledger))
        if evidence.audit_tex(str(tex), rows):
            raise AssertionError("supported number rejected")
        if evidence.validate_ledger(rows, str(root)):
            raise AssertionError("complete ledger rejected")
        tex.write_text("\\begin{document}\nTime: 9.99 s\\ev{E1}.\n\\end{document}\n", encoding="utf-8")
        if not evidence.audit_tex(str(tex), rows):
            raise AssertionError("unsupported number accepted")
    print("audit_tex selftest passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", nargs="?", help="LaTeX file to audit")
    parser.add_argument("ledger", nargs="?", help="EVIDENCE.md ledger")
    parser.add_argument("--strict", action="store_true", help="audit bare integers too")
    parser.add_argument("--check-ledger", action="store_true", help="check the ledger (always enabled; retained for compatibility)")
    parser.add_argument("--root", help="resolve log paths here (default: ledger directory)")
    parser.add_argument("--single-file", action="store_true", help="audit just this file, without following input/include")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    if not args.tex or not args.ledger:
        parser.error("tex and ledger are required unless --selftest is used")
    try:
        rows = evidence.read_ledger(args.ledger)
        root = args.root or str(Path(args.ledger).resolve().parent)
        issues = evidence.validate_ledger(rows, root)
        for issue in issues:
            issue.path = str(Path(args.ledger).resolve())
        issues += evidence.audit_tex(args.tex, rows, strict=args.strict, recursive=not args.single_file)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"audit_tex: cannot complete audit: {error}", file=sys.stderr)
        return 2
    for issue in issues:
        print(issue)
    errors = sum(issue.severity == "error" for issue in issues)
    print(f"audit_tex: {errors} errors, {len(issues) - errors} warnings, {len(rows)} ledger rows")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
