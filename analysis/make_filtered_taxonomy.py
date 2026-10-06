#!/usr/bin/env python3
"""
Generate taxonomy/filtered/*.md — only rows where BOTH host_a and host_b
are non-empty (i.e. both parsers returned a host).
"""
from pathlib import Path

TAXONOMY_DIR = Path("taxonomy")
FILTERED_DIR = TAXONOMY_DIR / "filtered"
FILTERED_DIR.mkdir(exist_ok=True)

SKIP = {"NOTES.md", "_index.json"}


def parse_table(text: str):
    lines = text.splitlines()
    header_idx = next(
        (i for i, l in enumerate(lines) if l.startswith("| Pair") or l.startswith("|Pair")),
        None,
    )
    if header_idx is None:
        return lines, [], []
    preamble = lines[: header_idx + 2]  # title + description + table header + separator
    rows = []
    raw_lines = []
    for line in lines[header_idx + 2 :]:
        if not line.strip() or not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 4:
            continue
        host_a = cols[2].strip("`").strip()
        host_b = cols[3].strip("`").strip()
        rows.append((host_a, host_b, line))
        raw_lines.append(line)
    return preamble, rows, raw_lines


total_in = total_out = 0

for md_file in sorted(TAXONOMY_DIR.glob("*.md")):
    if md_file.name in SKIP:
        continue

    text = md_file.read_text()
    preamble, rows, _ = parse_table(text)

    both_succeed = [line for (ha, hb, line) in rows if ha and hb]
    total_in += len(rows)
    total_out += len(both_succeed)

    out_file = FILTERED_DIR / md_file.name
    content = "\n".join(preamble + both_succeed) + "\n"
    out_file.write_text(content)
    print(f"{md_file.name:35s}  {len(rows):3d} total → {len(both_succeed):3d} both-succeed")

print(f"\nTotal: {total_out}/{total_in} rows kept ({100*total_out//total_in if total_in else 0}%)")
