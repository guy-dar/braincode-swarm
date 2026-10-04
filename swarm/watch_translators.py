#!/usr/bin/env python3
"""Live alerts on translator conversations, for watching a running loop.

Polls runs/translator_logs/ (live progress) and runs/translator_sessions/
(full transcripts, written when a translator finishes) and prints one line
per finding:

  SLOW      a model reply took longer than --slow seconds
  HEAVY     one call sent more than --heavy tokens (input + cached)
  REJECTED  --rejected or more model calls in a row came back empty (proxy pushback)
  LONG      a translator attempt has been running longer than --long minutes
  BIGTOOL   a tool result in a finished transcript is larger than --bigtool characters
  CONTEXT   a finished attempt's compactions and truncated tool results (context-limits.ts)

    python watch_translators.py --batches 5-8
"""
import argparse
import json
import re
import time
from pathlib import Path

SELF_DIR = Path(__file__).resolve().parent
LOGS = SELF_DIR / "runs" / "translator_logs"
SESSIONS = SELF_DIR / "runs" / "translator_sessions"
LINE = re.compile(r"^\s*([\d.]+)s (.*)$")
REPLY = re.compile(r"model reply: in (\d+) \+ cached (\d+), out (\d+)")
NAME = re.compile(r"^(\d+)-(\d+)(?:-attempt(\d+))?$")


def in_batches(stem: str, lo: int, hi: int) -> bool:
    m = NAME.match(stem)
    return bool(m) and lo <= int(m.group(1)) <= hi


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--batches", default="1-100")
    p.add_argument("--slow", type=float, default=90)
    p.add_argument("--heavy", type=int, default=70_000)
    p.add_argument("--rejected", type=int, default=3)
    p.add_argument("--long", type=float, default=12)
    p.add_argument("--bigtool", type=int, default=25_000)
    p.add_argument("--interval", type=float, default=15)
    args = p.parse_args()
    lo, hi = (int(x) for x in args.batches.split("-"))
    seen, started, session_mtime = set(), {}, {}

    def alert(key, text):
        if key not in seen:
            seen.add(key)
            print(text, flush=True)

    while True:
        now = time.time()
        for log in sorted(LOGS.glob("*-attempt*.log")):
            if not in_batches(log.stem, lo, hi):
                continue
            started.setdefault(log.stem, log.stat().st_ctime)
            rows = [(float(m.group(1)), m.group(2).strip()) for m in
                    map(LINE.match, log.read_text(encoding="utf-8", errors="replace").splitlines()) if m]
            turn_start, streak, turn = None, 0, 0
            finished = any("agent finished" in t for _, t in rows)
            for t, text in rows:
                if text.startswith("turn"):
                    turn_start, turn = t, turn + 1
                elif text.startswith("model reply"):
                    m = REPLY.search(text)
                    sent = int(m.group(1)) + int(m.group(2)) if m else 0
                    empty = m is not None and m.group(1) == m.group(2) == m.group(3) == "0"
                    wait = t - (turn_start or t)
                    if wait > args.slow:
                        alert(("slow", log.stem, turn), f"SLOW     {log.stem} turn {turn}: waited {wait:.0f}s for a reply"
                                                      + (" (rejected)" if empty else f" (sent {sent:,} tokens)"))
                    if sent > args.heavy:
                        # the context grows every turn: alert when crossing the threshold, then per +30k
                        bracket = (sent - args.heavy) // 30_000
                        alert(("heavy", log.stem, bracket), f"HEAVY    {log.stem} turn {turn}: one call sent {sent:,} "
                                                            f"tokens (the conversation so far)")
                    streak = streak + 1 if empty else 0
                    if streak >= args.rejected:
                        alert(("rej", log.stem, turn), f"REJECTED {log.stem}: {streak} rejected calls in a row (turn {turn})")
            minutes = (now - started[log.stem]) / 60
            if not finished and minutes > args.long and now - log.stat().st_mtime < 600:
                alert(("long", log.stem), f"LONG     {log.stem}: running {minutes:.0f} min, {turn} turns so far, "
                                          f"last activity: {rows[-1][1][:120] if rows else '-'}")
        for ctx_log in sorted(LOGS.glob("*-attempt*.context.jsonl")):
            stem = ctx_log.name[:-len(".context.jsonl")]
            if not in_batches(stem, lo, hi):
                continue
            events = []
            for line in ctx_log.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    events.append(json.loads(line))
                except ValueError:
                    pass
            comp = [e for e in events if e.get("event") == "compacted"]
            cut = sum(e.get("event") == "truncated" for e in events)
            failed = sum(e.get("event") == "summary_failed" for e in events)
            if comp or cut or failed:
                sizes = ", ".join(f"{e.get('tokens_before', 0) // 1000}k->{e.get('tokens_after', 0) // 1000}k"
                                  for e in comp)
                alert(("ctx", stem), f"CONTEXT  {stem}: {len(comp)} compaction(s)" + (f" ({sizes})" if comp else "")
                      + f", {cut} tool result(s) truncated" + (f", {failed} summary call(s) FAILED" if failed else ""))
        for sess in sorted(SESSIONS.glob("*.jsonl")):
            if not in_batches(sess.stem, lo, hi):
                continue
            mtime = sess.stat().st_mtime
            if session_mtime.get(sess.stem) == mtime:
                continue
            session_mtime[sess.stem] = mtime
            n = 0
            last_call = {}
            for line in sess.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("type") != "message":
                    continue
                n += 1
                msg = e.get("message") or {}
                for part in msg.get("content") or []:
                    if not isinstance(part, dict):
                        continue
                    if part.get("type") == "toolCall":
                        a = part.get("arguments") or part.get("args") or {}
                        last_call = a.get("command") or a.get("path") or json.dumps(a)[:100]
                    if msg.get("role") == "toolResult" and part.get("type") == "text":
                        size = len(part.get("text") or "")
                        if size > args.bigtool:
                            alert(("big", sess.stem, n), f"BIGTOOL  {sess.stem} message {n}: tool result of {size:,} "
                                                         f"characters from: {str(last_call)[:140]}")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
