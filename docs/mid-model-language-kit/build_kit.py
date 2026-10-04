"""Format-only conversion from frozen Markdown snapshots; standard library only."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sections(text):
    matches = list(re.finditer(r"^#{1,6} +.+$", text, re.M))
    boundaries = [0] + [m.start() for m in matches if m.start() != 0] + [len(text)]
    result = []
    for i, (start, end) in enumerate(zip(boundaries, boundaries[1:])):
        raw = text[start:end]
        heading = re.match(r"^(#{1,6}) +([^\r\n]+)", raw)
        result.append({"id": f"section-{i:03d}",
                       "title": heading.group(2) if heading else "Preamble",
                       "level": len(heading.group(1)) if heading else 0,
                       "start_line": text.count("\n", 0, start) + 1,
                       "raw_markdown": raw})
    assert "".join(s["raw_markdown"] for s in result) == text
    return result


def cells(line):
    return [x.strip() for x in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def make_index(parts):
    """Index original rows; do not infer signatures, types, status or meaning."""
    index = {}
    for part in parts:
        headers = None
        lines = part["raw_markdown"].splitlines()
        for n, line in enumerate(lines):
            if not line.startswith("|"):
                headers = None
                continue
            if n + 1 < len(lines) and re.match(r"\|\s*:?-", lines[n + 1]):
                headers = cells(line)
                continue
            if re.match(r"\|\s*:?-", line) or headers is None:
                continue
            row = cells(line)
            if not row:
                continue
            label = row[0].strip("`")
            key = label.split("(", 1)[0].strip() if re.match(r"^[A-Za-z_][A-Za-z_0-9]*\(", label) else label
            if not key:
                continue
            aliases = []
            for match in re.findall(r"natural-language synonyms: ([^)]*)", " ".join(row)):
                aliases.extend(x.strip() for x in match.split(","))
            index.setdefault(key, {"symbol": key, "occurrences": [], "source_alias_hints": []})
            index[key]["occurrences"].append({"section_id": part["id"], "section_title": part["title"],
                                             "source_line": part["start_line"] + n,
                                             "headers": headers, "cells": row, "raw_row": line})
            index[key]["source_alias_hints"] = sorted(set(index[key]["source_alias_hints"] + aliases))
    return sorted(index.values(), key=lambda e: e["symbol"])


def write_json(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    raw = (ROOT / "reference/glossary-source.md").read_bytes()
    parts = sections(raw.decode("utf-8"))
    index = make_index(parts)
    write_json("glossary.json", {
        "format_version": "1.0",
        "conversion": "lossless Markdown-to-JSON packaging; no semantic changes",
        "source_file": "reference/glossary-source.md", "source_sha256": digest(raw), "encoding": "utf-8",
        "authority": "Concatenate sections[].raw_markdown in order to recover the complete original. The index is a derived lookup aid only.",
        "sections": parts, "entries": index})
    (ROOT / "language-spec.md").write_bytes((ROOT / "reference/language-spec-source.md").read_bytes())
    (ROOT / "glossary.md").write_bytes(raw)
    spec_text = (ROOT / "language-spec.md").read_bytes().decode("utf-8")
    excerpts = []
    for number in (2, 3, 14):
        match = re.search(r"^## " + str(number) + r"\. .*?(?=^## |\Z)", spec_text, re.M | re.S)
        if not match:
            raise ValueError("Missing quick-reference source section " + str(number))
        excerpts.append(match.group())
    (ROOT / "quick-reference.md").write_text(
        "# Verbatim quick reference\n\nThis is an incomplete excerpt of language-spec.md, not a replacement or a revised specification. Read the full relevant sections for construct semantics, claims, evidence, constraints and examples. The following three sections are copied without edits.\n\n"
        + "\n".join(excerpts), encoding="utf-8")
    write_json("glossary-index.json", [{"symbol": e["symbol"], "source_alias_hints": e["source_alias_hints"],
                                       "section_ids": list(dict.fromkeys(o["section_id"] for o in e["occurrences"]))}
                                      for e in index])
    write_json("spec-index.json", [{k: s[k] for k in ("id", "title", "start_line")}
                                  for s in sections((ROOT / "language-spec.md").read_bytes().decode("utf-8"))])
    examples = []
    for s in parts:
        for i, m in enumerate(re.finditer(r"```braincode\r?\n(.*?)```", s["raw_markdown"], re.S)):
            examples.append({"id": f"{s['id']}-example-{i+1}", "source_section": s["id"],
                             "context_markdown": s["raw_markdown"][:m.start()], "braincode": m.group(1),
                             "status": "copied verbatim; source qualifications apply"})
    (ROOT / "examples.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in examples), encoding="utf-8")
    manifest = {"kit_format_version": "1.0", "content_policy": "format-only; all source content preserved",
                "source_snapshots": {"spec": digest((ROOT / "reference/language-spec-source.md").read_bytes()),
                                     "glossary": digest(raw)}, "files": {}}
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p.name != "manifest.json" and "__pycache__" not in p.parts:
            manifest["files"][p.relative_to(ROOT).as_posix()] = digest(p.read_bytes())
    write_json("manifest.json", manifest)
    print(f"Packaged {len(parts)} glossary sections, {len(index)} lookup keys, {len(examples)} unchanged examples.")


if __name__ == "__main__":
    main()
