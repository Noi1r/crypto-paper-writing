"""EVIDENCE.md ledger: read, append, validate, and audit a .tex file against it.

Ledger format (see SPEC.md), a single Markdown table::

    | ID | number/fact as printed in paper | command | log path | commit | machine | date | runs/median |
    |----|----|----|----|----|----|----|----|
    | E1 | 1.23 s | python3 measure.py | results/toy/run.json | 1a2b3c4 | toy-machine | 2026-01-01 | 5 / median |
    | E2 | 2.00× | derived: E1/E3 | - | - | - | 2026-01-01 | - |

Rules enforced here:

* every row has ID, printed value, command and (unless ``derived:``) a log path;
* IDs are unique; ``derived:`` references exist and have no cycles;
* with ``root`` given, log paths must exist;
* recognized numbers must link to evidence with ``\\ev{ID}`` (legacy ``\\evid``
  also works) or a same-line ``% EV:ID[,ID]`` comment;
* values and visible units must match the linked rows. This is a static source
  check, not a TeX interpreter or a check of measurement/proof correctness.
"""
from __future__ import annotations

import os
import re
import time
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

HEADER = ["ID", "number/fact as printed in paper", "command", "log path", "commit", "machine", "date", "runs/median"]
KEYS = ["id", "printed", "command", "log", "commit", "machine", "date", "runs"]
_HEADER_HINTS = [
    ("id", ("id",)),
    ("printed", ("number", "fact", "printed", "value")),
    ("command", ("command", "cmd")),
    ("log", ("log",)),
    ("commit", ("commit",)),
    ("machine", ("machine", "host")),
    ("date", ("date",)),
    ("runs", ("runs", "median", "repeat")),
]


@dataclass
class Issue:
    severity: str  # "error" | "warning"
    kind: str
    message: str
    line: int = 0
    number: str = ""
    path: str = ""

    def __str__(self) -> str:
        loc = f"{self.path}:{self.line}: " if self.path else (f"line {self.line}: " if self.line else "")
        return f"[{self.severity}] {self.kind}: {loc}{self.message}"


# ------------------------------------------------------------------ ledger I/O
def _split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells = re.split(r"(?<!\\)\|", s)
    return [c.strip().replace(r"\|", "|") for c in cells]


def _map_header(cells: list[str]) -> dict[int, str]:
    m: dict[int, str] = {}
    for i, c in enumerate(cells):
        lc = c.lower()
        for key, hints in _HEADER_HINTS:
            if key in m.values():
                continue
            if (key == "id" and lc.strip("`* ") == "id") or (key != "id" and any(h in lc for h in hints)):
                m[i] = key
                break
    return m


def read_ledger(path: str) -> list[dict]:
    """Parse the first Markdown table with an ``ID`` column.  Each row dict has KEYS + ``_line``."""
    rows: list[dict] = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    colmap: dict[int, str] | None = None
    column_count = 0
    has_separator = False
    for ln, line in enumerate(lines, 1):
        if not line.strip().startswith("|"):
            if colmap is not None:
                break  # end of the table
            continue
        cells = _split_row(line)
        if colmap is None:
            m = _map_header(cells)
            if "id" in m.values() and "printed" in m.values():
                colmap = m
                column_count = len(cells)
                missing = {"command", "log"} - set(m.values())
                if missing:
                    raise ValueError(f"{path}:{ln}: missing ledger columns: {', '.join(sorted(missing))}")
            continue
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            has_separator = True
            continue
        if not has_separator:
            raise ValueError(f"{path}:{ln}: missing table header separator")
        if len(cells) != column_count:
            raise ValueError(f"{path}:{ln}: expected {column_count} cells, found {len(cells)} (escape literal pipes as \\|)")
        row = {k: "" for k in KEYS}
        for i, c in enumerate(cells):
            if i in colmap:
                row[colmap[i]] = c
        row["_line"] = ln
        if row["id"]:
            rows.append(row)
        elif any(cells):
            raise ValueError(f"{path}:{ln}: evidence row has no ID")
    if colmap is None:
        raise ValueError(f"{path}: no evidence table with ID and printed-value columns")
    if not has_separator:
        raise ValueError(f"{path}: missing table header separator")
    return rows


def next_id(rows: list[dict], prefix: str = "E") -> str:
    nums = [int(m.group(1)) for r in rows if (m := re.fullmatch(rf"{re.escape(prefix)}(\d+)", r["id"]))]
    return f"{prefix}{max(nums, default=0) + 1}"


def _esc(s: str) -> str:
    return str(s).replace("|", r"\|").replace("\n", " ")


def append_row(path: str, printed: str, command: str, log: str, commit: str = "", machine: str = "",
               date: str | None = None, runs: str = "", id: str | None = None) -> str:
    rows = read_ledger(path) if os.path.exists(path) else []
    rid = id or next_id(rows)
    if any(r["id"] == rid for r in rows):
        raise ValueError(f"duplicate evidence ID {rid}")
    date = date or time.strftime("%Y-%m-%d")
    new = "| " + " | ".join(_esc(x) for x in [rid, printed, command, log, commit, machine, date, runs]) + " |\n"
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("# EVIDENCE\n\nReported measurements link to rows here.\n\n")
            f.write("| " + " | ".join(HEADER) + " |\n|" + "|".join(["---"] * len(HEADER)) + "|\n" + new)
        return rid
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    last = max(r["_line"] for r in rows) if rows else None
    if last is None:  # header exists but no rows: insert after separator
        for i, l in enumerate(lines):
            if re.match(r"^\|\s*:?-{2,}", l):
                last = i + 1
                break
    lines.insert(last, new)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return rid


def validate_ledger(rows: list[dict], root: str | None = None) -> list[Issue]:
    issues: list[Issue] = []
    ids = [r["id"] for r in rows]
    seen = set()
    dependencies: dict[str, list[str]] = {}
    for r in rows:
        ln = r.get("_line", 0)
        if r["id"] in seen:
            issues.append(Issue("error", "duplicate-id", f"ID {r['id']} appears twice", ln))
        seen.add(r["id"])
        if not re.fullmatch(r"[A-Z]+\d+", r["id"]):
            issues.append(Issue("error", "bad-id", f"invalid evidence ID {r['id']!r}; use E1, E2, ...", ln))
        for k in ("printed", "command"):
            if not r[k]:
                issues.append(Issue("error", "missing-field", f"{r['id']}: empty '{k}'", ln))
        derived = r["command"].lower().startswith("derived:")
        if derived:
            dependencies[r["id"]] = re.findall(r"\b([A-Z]+\d+)\b", r["command"])
            if not dependencies[r["id"]]:
                issues.append(Issue("error", "bad-derivation", f"{r['id']}: derived row has no evidence references", ln))
            for ref in dependencies[r["id"]]:
                if ref not in ids:
                    issues.append(Issue("error", "bad-derivation", f"{r['id']} derives from unknown {ref}", ln))
        else:
            if not r["log"] or r["log"] in ("-", "--"):
                issues.append(Issue("error", "missing-log", f"{r['id']}: measured value without a log path", ln))
            elif root is not None:
                for lp in re.split(r"[,;]\s*", r["log"].strip("`")):
                    lp = lp.strip("` ")
                    if lp and not os.path.isfile(os.path.join(root, lp)):
                        issues.append(Issue("error", "log-not-found", f"{r['id']}: {lp} is not a file under root", ln))
            for k in ("commit", "machine", "date", "runs"):
                if not r[k] or r[k] in ("-", "--"):
                    issues.append(Issue("warning", "missing-field", f"{r['id']}: empty '{k}'", ln))
    done: set[str] = set()
    active: list[str] = []

    def visit(rid: str) -> None:
        if rid in active:
            cycle = active[active.index(rid):] + [rid]
            issues.append(Issue("error", "derivation-cycle", " -> ".join(cycle)))
            return
        if rid in done:
            return
        active.append(rid)
        for ref in dependencies.get(rid, []):
            visit(ref)
        active.pop()
        done.add(rid)

    for rid in dependencies:
        visit(rid)
    return issues


# ------------------------------------------------------------------ static source audit
# Match a whole scalar, including common scientific notation. Mathematical
# expressions and macro expansions remain outside this lightweight checker.
_NUM_RX = re.compile(
    r"(?<![\w.])(?:(?<![-\d])[-+])?(?:\d{1,3}(?:(?:,|\{,\}|\\,)\d{3})+|\d+|(?=\.\d))"
    r"(?:\.\d+)?(?:[eE][-+]?\d+|\s*(?:\\times|\\cdot|×)\s*10\s*\^\s*\{?[-+]?\d+\}?)?(?!\d)"
)
_UNIT_RX = re.compile(
    r"(?:[\s~${}]|\\[,;! ])*-?(?:\\(?:mathrm|text|textrm|mathsf)\s*\{\s*)?"
    r"(?P<unit>\\mu\s*s|[µμ]s|\\times|×|\\%|%|[KMGT]i?B|kB|[kMGT]bits?|"
    r"seconds?|secs?|ms|us|ns|min|hours?|Hz|MHz|GHz|bytes?|bits?|cycles?|ops|rounds?|s|h|B|x)"
    r"(?![A-Za-z])"
)
_TAG_RX = re.compile(r"\\(?:ev|evid)\{([^}]*)\}")
_DROP_CMDS = (
    "label", "ref", "eqref", "cref", "Cref", "autoref", "pageref", "cite", "citep", "citet",
    "citeauthor", "citeyear", "url", "input", "include", "includegraphics", "usepackage",
    "documentclass", "bibliography", "bibliographystyle", "vspace", "hspace", "setlength",
    "addtolength", "begin", "end", "hypersetup", "definecolor", "setcounter", "addcontentsline",
    "newcommand", "renewcommand", "providecommand", "DeclareMathOperator", "multicolumn", "multirow",
    "cline", "cmidrule", "tabcolsep", "arraystretch", "resizebox", "scalebox", "rule", "linespread", "fontsize",
)
_DROP_RX = re.compile(
    rf"\\(?:{'|'.join(_DROP_CMDS)})\b\*?(?:\[[^\]]*\])*(?:\{{[^{{}}]*\}})?(?:\{{[^{{}}]*\}})?"
)
_SOURCE_RX = re.compile(
    r"\\(?P<include>input|include)(?![A-Za-z])\s*(?:\{(?P<braced>[^}]*)\}|(?P<bare>[^\s%{}]+))"
    r"|\\(?P<edge>begin|end)\{(?P<table>tabular\*?|tabularx|longtable)\}"
)


def _comment(line: str) -> tuple[str, str]:
    for i, char in enumerate(line):
        if char == '%':
            j = i - 1
            while j >= 0 and line[j] == '\\':
                j -= 1
            if (i - j - 1) % 2 == 0:
                return line[:i], line[i + 1:]
    return line, ''


def strip_tex(line: str) -> str:
    """Mask comments, evidence tags and non-prose arguments, preserving offsets."""
    code, _ = _comment(line)
    code += ' ' * (len(line) - len(code))
    code = _DROP_RX.sub(lambda m: ' ' * len(m[0]), code)
    code = _TAG_RX.sub(lambda m: ' ' * len(m[0]), code)
    # A link target is not prose, but its displayed text is.
    code = re.sub(r"\\href\{[^}]*\}", lambda m: ' ' * len(m[0]), code)
    return code


def normalize_number(tok: str) -> str | None:
    t = tok.replace('{,}', '').replace('\\,', '').replace(',', '').lstrip('+')
    t = re.sub(r"\s*(?:\\times|\\cdot|×)\s*10\s*\^\s*\{?([-+]?\d+)\}?", r"e\1", t)
    try:
        d = Decimal(t)
    except InvalidOperation:
        return None
    # Decimal equality preserves all digits, without rounding through normalize().
    return str(d) if d else '0'


def numbers_in(text: str) -> list[str]:
    return [n for m in _NUM_RX.finditer(text) if (n := normalize_number(m[0])) is not None]


def _unit(raw: str) -> str:
    aliases = {
        r'\times': '×', 'x': '×', r'\%': '%', 'µs': 'us', 'μs': 'us',
        'sec': 's', 'secs': 's', 'second': 's', 'seconds': 's', 'hour': 'h', 'hours': 'h',
        'byte': 'B', 'bytes': 'B', 'bits': 'bit', 'cycles': 'cycle', 'rounds': 'round',
    }
    if re.fullmatch(r"\\mu\s*s", raw):
        return 'us'
    return aliases.get(raw, raw)


@dataclass(frozen=True)
class Quantity:
    value: str
    unit: str | None
    raw: str
    start: int
    end: int
    measurement: bool


def _quantities(text: str) -> list[Quantity]:
    found = []
    for m in _NUM_RX.finditer(text):
        value = normalize_number(m[0])
        if value is None:
            continue
        unit_match = _UNIT_RX.match(text, m.end())
        unit = _unit(unit_match['unit']) if unit_match else None
        before = text[max(0, m.start() - 2):m.start()]
        measurement = bool(unit or re.search(r'[.,eE]|\\times|\\cdot|×', m[0]) or before.endswith(('^', '^{')))
        end = unit_match.end() if unit_match else m.end()
        found.append(Quantity(value, unit, text[m.start():end], m.start(), end, measurement))
    return found


def _matches(q: Quantity, other: Quantity) -> bool:
    # No automatic conversion or inference of units declared only in headings.
    return Decimal(q.value) == Decimal(other.value) and (q.unit is None or q.unit == other.unit)


def _audit_line(raw: str, rows: dict[str, dict], strict: bool) -> list[Issue]:
    code, comment = _comment(raw)
    cleaned = strip_tex(code)
    quantities = _quantities(cleaned)
    bindings: dict[int, list[str]] = {}
    issues = []
    for tag in _TAG_RX.finditer(code):
        eid = tag[1].strip()
        if eid not in rows:
            issues.append(Issue('error', 'unknown-id', f'{tag[0]} not in EVIDENCE.md'))
        # Inline tags belong to the immediately preceding quantity on this line.
        preceding = [i for i, q in enumerate(quantities) if q.end <= tag.start()]
        if not preceding or not re.fullmatch(r"[\s${},.;:~\)\]]*", cleaned[quantities[preceding[-1]].end:tag.start()]):
            issues.append(Issue('error', 'orphan-tag', f'{tag[0]} needs a literal quantity immediately before it on the same line'))
            continue
        bindings.setdefault(preceding[-1], []).append(eid)
    line_ids = []
    if re.match(r'\s*EV:', comment):
        match = re.match(r'\s*EV:\s*([A-Za-z0-9_-]+(?:\s*,\s*[A-Za-z0-9_-]+)*)', comment)
        if not match:
            issues.append(Issue('error', 'bad-tag', 'use % EV:E1 or % EV:E1,E2'))
        else:
            line_ids = [eid.strip() for eid in match[1].split(',')]
            for eid in line_ids:
                if eid not in rows:
                    issues.append(Issue('error', 'unknown-id', f'EV:{eid} not in EVIDENCE.md'))
            if not quantities:
                issues.append(Issue('error', 'orphan-tag', 'EV comment has no literal quantities on this line'))
    for i, q in enumerate(quantities):
        ids = bindings.get(i, line_ids)
        if not (strict or q.measurement or ids):
            continue
        if not ids:
            issues.append(Issue('error', 'unlinked', f'{q.raw.strip()} needs \\ev{{ID}} or a same-line % EV:ID', number=q.value))
        elif all(eid in rows for eid in ids) and not any(
            _matches(q, candidate) for eid in ids for candidate in _quantities(rows[eid]['printed'])
        ):
            printed = '; '.join(f"{eid}: {rows[eid]['printed']}" for eid in ids)
            issues.append(Issue('error', 'mismatch', f'{q.raw.strip()} does not match linked value/unit ({printed})', number=q.value))
    return issues


def audit_tex(tex_path: str, ledger_rows: list[dict], strict: bool = False,
              body_only: bool = True, recursive: bool = True) -> list[Issue]:
    """Audit literal quantities in the source and reachable literal input/include files.

    Includes resolve from the entry file's directory, as with a build run there.
    Conditional branches are scanned conservatively; preamble definitions, macro
    expansion and rendered graphics are not interpreted.
    """
    entry = Path(tex_path).resolve()
    by_id = {r['id']: r for r in ledger_rows}
    issues: list[Issue] = []
    active: list[Path] = []
    table_depth = 0

    def visit(path: Path) -> None:
        nonlocal table_depth
        active.append(path)
        lines = path.read_text(encoding='utf-8').splitlines()
        has_document = any(r'\begin{document}' in _comment(line)[0] for line in lines)
        in_body = not (body_only and has_document)
        ignored_from = 0
        for ln, raw in enumerate(lines, 1):
            code, comment = _comment(raw)
            if re.match(r'\s*(?:papercheck|crbench):ignore-begin\b', comment):
                if ignored_from:
                    issues.append(Issue('error', 'ignore-block', 'nested ignore block', ln, path=str(path)))
                ignored_from = ln
                continue
            if re.match(r'\s*(?:papercheck|crbench):ignore-end\b', comment):
                if not ignored_from:
                    issues.append(Issue('error', 'ignore-block', 'ignore-end without ignore-begin', ln, path=str(path)))
                ignored_from = 0
                continue
            if ignored_from or re.match(r'\s*(?:papercheck|crbench):ignore\b', comment):
                continue
            if body_only and r'\begin{document}' in code:
                in_body = True
                offset = code.index(r'\begin{document}') + len(r'\begin{document}')
                code = ' ' * offset + code[offset:]
            if not in_body:
                continue
            end_document = r'\end{document}' in code
            if end_document:
                code = code.split(r'\end{document}', 1)[0]
            events = list(_SOURCE_RX.finditer(code))
            in_table = table_depth > 0 or any(e['edge'] == 'begin' for e in events)
            for issue in _audit_line(code + ('%' + comment if comment else ''), by_id, strict or in_table):
                issue.line, issue.path = ln, str(path)
                issues.append(issue)
            for event in events:
                if event['table']:
                    table_depth = max(0, table_depth + (1 if event['edge'] == 'begin' else -1))
                    continue
                if not recursive:
                    continue
                name = event['braced'] if event['braced'] is not None else event['bare']
                if not name or re.search(r'[\\#$]', name):
                    issues.append(Issue('error', 'unresolved-input', f'cannot statically resolve {event[0]}', ln, path=str(path)))
                    continue
                child = entry.parent / name.strip()
                if not child.suffix:
                    child = child.with_suffix('.tex')
                child = child.resolve()
                if child in active:
                    issues.append(Issue('error', 'include-cycle', f'recursive include of {child}', ln, path=str(path)))
                elif not child.is_file():
                    issues.append(Issue('error', 'missing-input', f'included source not found: {child}', ln, path=str(path)))
                else:
                    visit(child)
            if end_document:
                break
        if ignored_from:
            issues.append(Issue('error', 'ignore-block', 'unclosed ignore block', ignored_from, path=str(path)))
        active.pop()

    visit(entry)
    return issues
