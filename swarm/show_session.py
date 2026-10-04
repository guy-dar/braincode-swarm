#!/usr/bin/env python3
"""Show an agent's full conversation with the model, with the size of every
message: what was attached, what each tool returned, what the model wrote.

    python show_session.py 5-12                      # translator 5-12
    python show_session.py migrations/batch-005/review/attempt1/session.jsonl
    python show_session.py 5-12 --full               # whole contents, not previews
    python show_session.py 5-12 --heaviest 15        # only the size summary

Sizes are characters, with a rough token estimate (chars / 4). Every model
call re-sends the whole conversation so far, so a heavy message is paid for
again on each later call; the progress log (runs/translator_logs/<tid>-attempt<N>.log)
has the exact tokens per call.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SELF_DIR = Path(__file__).resolve().parent
FILE_RE = re.compile(r'<file name="([^"]+)">\n?(.*?)</file>', re.S)


def resolve(arg: str) -> Path:
    p = Path(arg)
    if p.exists():
        return p
    p = SELF_DIR / "runs" / "translator_sessions" / f"{arg}.jsonl"
    if p.exists():
        return p
    sys.exit(f"no session {arg!r} (looked for a file, then runs/translator_sessions/{arg}.jsonl)")


def size(text: str) -> str:
    return f"{len(text):>7,} ch ~{len(text) // 4:>6,} tok"


def preview(text: str, n: int) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n] + " …"


def parts_of(message: dict) -> list:
    content = message.get("content")
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return content or []


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("session")
    p.add_argument("--full", action="store_true", help="print whole contents instead of previews")
    p.add_argument("--width", type=int, default=160, help="preview length")
    p.add_argument("--heaviest", type=int, default=10, help="how many heaviest items to list")
    args = p.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    path = resolve(args.session)
    show = (lambda t: str(t)) if args.full else (lambda t: preview(t, args.width))
    items = []          # (chars, label) for the heaviest list
    totals = {}
    n = 0
    print(f"# {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        e = json.loads(line)
        kind = e.get("type")
        if kind == "session":
            print(f"\n=== session {e.get('id')} started {e.get('timestamp')}")
            continue
        if kind == "model_change":
            print(f"    model: {e.get('provider')}/{e.get('modelId')}")
            continue
        if kind != "message":
            continue
        m = e.get("message") or {}
        role = m.get("role", "?")
        n += 1
        for part in parts_of(m):
            ptype = part.get("type")
            if ptype == "text":
                text = part.get("text") or ""
                files = FILE_RE.findall(text)
                if files:
                    rest = FILE_RE.sub("", text)
                    print(f"[{n:>3}] {role:<10} {size(text)}  ({len(files)} attached file(s) + {len(rest):,} ch of prompt)")
                    for name, body in files:
                        print(f"        attached {name:<40} {size(body)}")
                        items.append((len(body), f"[{n}] attached {name}"))
                    print(f"        prompt: {show(rest)}")
                    items.append((len(rest), f"[{n}] {role} prompt text"))
                else:
                    print(f"[{n:>3}] {role:<10} {size(text)}  {show(text)}")
                    items.append((len(text), f"[{n}] {role} text"))
                totals[role] = totals.get(role, 0) + len(text)
            elif ptype == "thinking":
                text = part.get("thinking") or ""
                print(f"[{n:>3}] {role:<10} {size(text)}  (reasoning) {show(text)}")
                totals["reasoning"] = totals.get("reasoning", 0) + len(text)
            elif ptype == "toolCall":
                args_text = json.dumps(part.get("arguments") or part.get("args") or part.get("input") or {},
                                       ensure_ascii=False)
                print(f"[{n:>3}] {role:<10} {size(args_text)}  CALL {part.get('name', '?')}: {show(args_text)}")
                items.append((len(args_text), f"[{n}] tool call {part.get('name', '?')}"))
                totals["tool calls"] = totals.get("tool calls", 0) + len(args_text)
            elif ptype == "image":
                print(f"[{n:>3}] {role:<10} (image)")
        if role == "assistant" and not parts_of(m):
            print(f"[{n:>3}] {role:<10}       (empty reply: a rejected or failed model call)")
    print("\n=== totals by kind (characters; each is re-sent on every later call)")
    for k, v in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"  {k:<12} {v:>9,} ch ~{v // 4:>7,} tok")
    print(f"\n=== {args.heaviest} heaviest items")
    for chars, label in sorted(items, reverse=True)[:args.heaviest]:
        print(f"  {chars:>9,} ch ~{chars // 4:>7,} tok  {label}")


if __name__ == "__main__":
    main()
