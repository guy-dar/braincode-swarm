"""Step 1 of retrieval: decompose a data item into separate, source-linked needs.

The host numbers the item first (`t<turn>:s<sentence>`, the same locators a
translation uses in SOURCE), so every need points back into the item. A mid
model does the decomposition (prompt: kit/needs_prompt.md); if that call fails
or returns nothing usable, a heuristic clause splitter takes over, so
retrieval never blocks on the LLM.
"""
import json
import random
import os
import re
import sys
import time
from pathlib import Path

SWARM_DIR = Path(__file__).resolve().parent.parent
PROMPT_PATH = SWARM_DIR / "kit" / "needs_prompt.md"

TURN_RE = re.compile(r"<\|(user|assistant)\|>")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?。！？])\s+|\n+")
NEED_KINDS = ("action", "object", "constraint", "negation", "correction", "temporal",
              "speech_act", "claim", "reasoning")
MAX_SEGMENT_CHARS = 400
MAX_PROMPT_CHARS = 48_000
MAX_NEEDS = 120
# Waits between need-extraction retries (seconds, jittered); then heuristic.
LLM_RETRY_WAITS_S = (30, 90)

NEGATION_RE = re.compile(r"\b(not|no|never|without|don't|dont|doesn't|isn't|aren't|won't|can't|cannot|avoid|exclude|except|nor)\b", re.I)
CORRECTION_RE = re.compile(r"\b(actually|instead|i meant|rather|correction|scratch that|change it|make it)\b", re.I)
TEMPORAL_RE = re.compile(r"\b(\d+\s*(min|minute|hour|day|week|month|year)s?|today|tomorrow|yesterday|before|after|until|by \w+day|deadline|daily|weekly|monthly|first|then|finally)\b", re.I)
REASONING_RE = re.compile(r"\b(because|therefore|so that|since|thus|hence|which means|due to|as a result)\b", re.I)


def segment(content: str) -> list:
    """Split an item into numbered segments:
    [{"loc": "t1:s1", "turn": 1, "speaker": "USER", "text": ...}, ...].
    Text without turn tags is one USER turn (a bare prompt)."""
    content = content or ""
    parts = TURN_RE.split(content)
    turns = []
    if len(parts) == 1:
        turns.append(("USER", content))
    else:
        if parts[0].strip():
            turns.append(("USER", parts[0]))
        for role, text in zip(parts[1::2], parts[2::2]):
            turns.append(("USER" if role == "user" else "AGENT", text))
    segments = []
    for t, (speaker, text) in enumerate(turns, 1):
        s = 0
        for sentence in SENT_SPLIT_RE.split(text):
            sentence = sentence.strip()
            while sentence:
                piece, sentence = sentence[:MAX_SEGMENT_CHARS], sentence[MAX_SEGMENT_CHARS:]
                s += 1
                segments.append({"loc": f"t{t}:s{s}", "turn": t, "speaker": speaker, "text": piece.strip()})
    return segments


def numbered_text(segments: list) -> str:
    """The item as the translator and the need extractor see it:
    one segment per line, `t1:s2 [USER] ...`, with a blank line between turns."""
    lines, last_turn = [], None
    for seg in segments:
        if last_turn is not None and seg["turn"] != last_turn:
            lines.append("")
        lines.append(f"{seg['loc']} [{seg['speaker']}] {seg['text']}")
        last_turn = seg["turn"]
    return "\n".join(lines)


def turn_context(segments: list, locs: list, window: int = 600) -> str:
    """The text around a need's source: its own segments plus neighbours in
    the same turn, up to `window` characters — what reranking compares against."""
    turns = {int(l.split(":")[0][1:]) for l in locs if re.match(r"^t\d+:s\d+$", l)}
    text = " ".join(seg["text"] for seg in segments if seg["turn"] in turns)
    return text[:window]


def heuristic_needs(segments: list) -> list:
    """Fallback decomposition: one need per sentence, typed by surface cues.
    Coarser than the LLM's, but every sentence still gets searched."""
    needs = []
    for seg in segments:
        text = seg["text"]
        if len(text) < 3:
            continue
        if seg["speaker"] == "USER" and text.rstrip().endswith("?"):
            kind = "speech_act"
        elif CORRECTION_RE.search(text):
            kind = "correction"
        elif NEGATION_RE.search(text):
            kind = "negation"
        elif REASONING_RE.search(text):
            kind = "reasoning"
        elif TEMPORAL_RE.search(text):
            kind = "temporal"
        elif seg["speaker"] == "AGENT":
            kind = "claim"
        else:
            kind = "action"
        needs.append({"kind": kind, "text": text[:200], "source": [seg["loc"]]})
    return needs[:MAX_NEEDS * 2]


def _llm_settings():
    if str(SWARM_DIR) not in sys.path:
        sys.path.insert(0, str(SWARM_DIR))
    import utils
    utils.load_dotenv(SWARM_DIR / ".env")
    model = os.environ.get("NEEDS_MODEL") or os.environ.get("SWARM_MODEL", "vertex-proxy/gemini-3.5-flash")
    return (model.rsplit("/", 1)[-1], os.environ.get("PROXY_API_KEY"),
            os.environ.get("NEEDS_BASE_URL") or os.environ.get("PROXY_BASE_URL", "https://vertex-proxy-v26q.onrender.com/v1"))


def _parse_json(raw: str):
    raw = (raw or "").strip()
    raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)
    for opener, closer in (("{", "}"), ("[", "]")):
        start, end = raw.find(opener), raw.rfind(closer)
        if start != -1 and end > start:
            try:
                return json.loads(raw[start:end + 1])
            except ValueError:
                continue
    return None


def llm_needs(segments: list, timeout: int = 180) -> list:
    """Ask the mid model for needs. Returns [] on any failure."""
    model_id, api_key, base_url = _llm_settings()
    if not api_key:
        return []
    text = numbered_text(segments)
    if len(text) > MAX_PROMPT_CHARS:
        text = text[:MAX_PROMPT_CHARS] + "\n[... item truncated for decomposition; later segments use heuristic needs ...]"
    prompt = PROMPT_PATH.read_text(encoding="utf-8").replace("{numbered_item}", text)
    import litellm
    data = None
    for attempt, wait in enumerate(LLM_RETRY_WAITS_S + (None,), 1):
        try:
            response = litellm.completion(
                model=f"openai/{model_id}", api_key=api_key, api_base=base_url,
                messages=[{"role": "user", "content": prompt}],
                temperature=0, max_tokens=16_000, timeout=timeout,
            )
            data = _parse_json(response.choices[0].message.content or "")
            if data is not None:
                break
            problem = "unparseable response"
        except Exception as e:
            problem = f"{type(e).__name__}: {str(e)[:120]}"
        # The proxy rate-limits bursts (Cloudflare 429s); a heuristic fallback
        # is much coarser, so it is worth waiting out a transient error.
        if wait is None:
            print(f"needs: LLM decomposition failed after {attempt} tries ({problem}); using heuristic", file=sys.stderr)
            return []
        time.sleep(wait * random.uniform(0.75, 1.25))
    items = data.get("needs") if isinstance(data, dict) else data
    if not isinstance(items, list):
        return []
    needs = []
    for item in items:
        if not isinstance(item, dict) or not str(item.get("text", "")).strip():
            continue
        kind = item.get("kind") if item.get("kind") in NEED_KINDS else "object"
        source = item.get("source") or []
        needs.append({"kind": kind, "text": str(item["text"]).strip()[:300],
                      "source": [source] if isinstance(source, str) else [str(s) for s in source]})
    return needs[:MAX_NEEDS]


def extract_needs(content: str, use_llm: bool = True) -> tuple:
    """(segments, needs, method). Needs get stable ids n1..nN and a context
    window; segments past the LLM's truncation point get heuristic needs."""
    segments = segment(content)
    needs, method = [], "heuristic"
    if use_llm:
        needs = llm_needs(segments)
        if needs:
            method = "llm"
            covered_len = len(numbered_text(segments))
            if covered_len > MAX_PROMPT_CHARS:
                cut, total = [], 0
                for seg in segments:
                    total += len(seg["text"]) + 20
                    if total > MAX_PROMPT_CHARS:
                        cut.append(seg)
                needs += heuristic_needs(cut)
                method = "llm+heuristic-tail"
    if not needs:
        needs = heuristic_needs(segments)
    for i, need in enumerate(needs, 1):
        need["id"] = f"n{i}"
        need["context"] = turn_context(segments, need.get("source") or [])
    return segments, needs, method
