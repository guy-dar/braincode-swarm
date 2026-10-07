#!/usr/bin/env python3
"""Phases 3 and 4a of the ProofWriter experiment, against an OpenAI-compatible
endpoint (vLLM in Colab serving Qwen 2.5 as `base-qwen` and the fine-tuned
adapter as `braincode-qwen`).

    # phase 3: plain Qwen 2.5 on the English items
    python run_proofwriter.py --model base-qwen --condition baseline --input english
    # phase 4a: the fine-tuned Qwen on the successful BrainCode translations
    python run_proofwriter.py --model braincode-qwen --condition braincode_ft --input braincode
    # optional controls
    python run_proofwriter.py --model base-qwen --condition braincode_base --input braincode
    python run_proofwriter.py --model braincode-qwen --condition baseline_ft --input english

English runs are scored here (`The answer is: True|False|Unknown`). BrainCode
runs take two calls in one conversation: the model reasons in English from the
BrainCode problem and ends with `The answer is: ...` (reasoning.md; scored here
as the secondary `direct_correct`), then writes only its verdict as a BrainCode
block from fixed templates (response.md), constrained by a prefilled block start,
greedy decoding, a short cap and a stop at the closing fence. They are scored back in the
repository, after Gemini back-translators read that verdict block
(evaluations/proofwriter/pw.py backtranslate). Each run is saved in
runs/<condition>/<item>/r<k>/: result.json, response.md, prompt.json (the exact
messages) and, for BrainCode runs, reasoning.md. Finished runs are kept;
errored runs are redone.
"""
import argparse
import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark"
RUNS = HERE / "runs"
# Qwen 2.5 Instruct's own generation defaults (generation_config.json)
SAMPLING = {"temperature": 0.7, "top_p": 0.8, "top_k": 20, "repetition_penalty": 1.05}
MAX_TOKENS = 4096

OWA = ("Open-world assumption: the theory is all you know. A statement is True if the theory implies it, False "
       "if the theory implies its negation, and Unknown if the theory implies neither. Do not assume that "
       "anything the theory does not say is false.")
ENGLISH_SUFFIX = ("\n\n" + OWA + "\n\nThink step by step. End with one final line, exactly one of:\n"
                  "The answer is: True\nThe answer is: False\nThe answer is: Unknown")
# Deliberately unlike both training system prompts: the read-direction one ("You read and write BrainCode...")
# cues restating the task in English, not solving it.
BRAINCODE_SYSTEM = ("You solve logic problems written in BrainCode, a formal language with a fixed glossary of "
                    "symbols. You reason to an answer; you do not restate or re-translate the problem.")
# Two calls in one conversation: (1) reason in English from the BrainCode problem; (2) write only the verdict,
# in BrainCode, from fixed templates. The verdict block is the "relevant part" that Gemini back-translates;
# it never contains the theory.
BRAINCODE_PROMPT = """Below is a logic problem written in BrainCode: a theory of facts and rules, and a statement in question.

{owa}

Solve it. Reason step by step in plain English:
1. Say which statement is in question.
2. List the facts that matter.
3. Apply the rules one at a time, writing down each new fact you derive and which rule and facts gave it, until nothing new follows.
4. Decide: the statement holds, its negation holds, or neither can be established.

Do not translate, restate or re-encode the problem: reason about it. End with one final line, exactly one of:
The answer is: True
The answer is: False
The answer is: Unknown

```braincode
{code}
```"""
VERDICT_PROMPT = """Now write your decision as a short ```braincode verdict block: 2 to 5 lines, nothing else. Do not copy the theory.

1. The statement in question is the target of the problem's `UTTER ask` line. Rebuild it with TERM lines (copy the ones it needs from the problem). Call its final handle `q`.
2. Then add the verdict that matches your answer, unchanged apart from `q`:

True (the statement holds):
CLAIM statement(fact=q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM

False (its negation holds):
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM

Unknown (neither can be established):
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate : CLAIM
CLAIM statement(fact=not_q) BY role_agent STATUS hypothesized SOURCE "theory" -> candidate_negation : CLAIM

Example. For a different problem whose statement in question is "The bear does not chase the dog" and whose answer is False:
```braincode
TERM activity(verb="chase", actor="bear", object=animal_label::dog) -> chase_dog : TERM
TERM negation(target=chase_dog) -> q : TERM
TERM negation(target=q) -> not_q : TERM
CLAIM statement(fact=not_q) BY role_agent STATUS inferred SOURCE "theory" -> verdict : CLAIM
```"""
# Call 2 is constrained to stay a verdict: the block is started for the model (prefill), decoding is greedy,
# it stops at the closing fence, and it is short. The fine-tuned model otherwise re-encodes the whole problem.
VERDICT_PREFILL = "```braincode\nTERM "
VERDICT_OPTIONS = {"temperature": 0.0, "max_tokens": 400, "stop": ["```"], "continue_final_message": True,
                   "add_generation_prompt": False}
ANSWER_RE = re.compile(r"The (?:final )?answer is:?\s*\**\s*(True|False|Unknown)\b", re.I)
BLOCK_RE = re.compile(r"```braincode\s*\n(.*?)```", re.S)


def log(msg):
    print(msg, flush=True)


def chat(base_url: str, model: str, messages: list, **options) -> dict:
    """options override the request body: max_tokens, sampling, stop, or vLLM's prefill flags
    (continue_final_message / add_generation_prompt) to continue a started assistant message."""
    body = json.dumps({"model": model, "messages": messages, "max_tokens": MAX_TOKENS, **SAMPLING,
                       **options}).encode()
    for attempt in range(4):
        req = urllib.request.Request(f"{base_url}/chat/completions", data=body, method="POST",
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=900) as resp:
                r = json.loads(resp.read())
            ch = r["choices"][0]
            u = r.get("usage") or {}
            return {"text": ch["message"].get("content") or "", "finish_reason": ch.get("finish_reason"),
                    "prompt_tokens": u.get("prompt_tokens", 0), "completion_tokens": u.get("completion_tokens", 0)}
        except urllib.error.HTTPError as e:
            detail = e.read()[:400].decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail}")


def messages_for(item: dict, kind: str, with_spec: bool) -> list:
    if kind == "english":
        return [{"role": "user", "content": item["input"] + ENGLISH_SUFFIX}]
    system = BRAINCODE_SYSTEM
    if with_spec:
        system += "\n\n# BrainCode language specification\n\n" + (BENCH / "language-spec.compact.md").read_text(
            encoding="utf-8")
    system += "\n\n# Glossary entries used by the problem\n\n" + item["glossary_entries"]
    return [{"role": "system", "content": system},
            {"role": "user", "content": BRAINCODE_PROMPT.format(owa=OWA, code=item["braincode"])}]


def run_one(args, item: dict, k: int) -> dict:
    out = RUNS / args.condition / item["item_key"] / f"r{k}"
    res_path = out / "result.json"
    if res_path.exists() and json.loads(res_path.read_text(encoding="utf-8"))["status"] == "ok":
        return {"skipped": True}
    out.mkdir(parents=True, exist_ok=True)
    msgs = messages_for(item, args.input, args.spec)
    (out / "prompt.json").write_text(json.dumps(msgs, ensure_ascii=False, indent=1), encoding="utf-8")
    record = {"item": item["item_key"], "depth": item["depth"], "label": item["label"], "condition": args.condition,
              "input": args.input, "run": k, "model": args.model, "sampling": SAMPLING, "with_spec": args.spec}
    t0 = time.time()
    try:
        r = chat(args.base_url, args.model, msgs)
        record.update({"status": "ok", "finish_reason": r["finish_reason"], "prompt_tokens": r["prompt_tokens"],
                       "completion_tokens": r["completion_tokens"]})
        if args.input == "english":
            (out / "response.md").write_text(r["text"], encoding="utf-8")
            m = ANSWER_RE.findall(r["text"])
            pred = m[-1].lower() if m else "none"
            record.update({"prediction": pred, "correct": pred == item["label"].lower()})
        else:   # reasoning, then the verdict block; scored after back-translation, in the repository
            (out / "reasoning.md").write_text(r["text"], encoding="utf-8")
            m = ANSWER_RE.findall(r["text"])          # secondary score: the decision in English (call 1)
            direct = m[-1].lower() if m else "none"
            msgs2 = msgs + [{"role": "assistant", "content": r["text"]}, {"role": "user", "content": VERDICT_PROMPT},
                            {"role": "assistant", "content": VERDICT_PREFILL}]
            (out / "prompt.json").write_text(json.dumps(msgs2, ensure_ascii=False, indent=1), encoding="utf-8")
            r2 = chat(args.base_url, args.model, msgs2, **VERDICT_OPTIONS)
            verdict = VERDICT_PREFILL + r2["text"].split("```")[0].rstrip() + "\n```\n"
            (out / "response.md").write_text(verdict, encoding="utf-8")
            blocks = BLOCK_RE.findall(verdict)
            record.update({"prediction": None, "correct": None, "has_answer_block": bool(blocks),
                           "direct_prediction": direct, "direct_correct": direct == item["label"].lower(),
                           "finish_reason": [r["finish_reason"], r2["finish_reason"]],
                           "prompt_tokens": r["prompt_tokens"] + r2["prompt_tokens"],
                           "completion_tokens": r["completion_tokens"] + r2["completion_tokens"]})
    except Exception as e:  # noqa: BLE001 - recorded; redone on the next run
        record.update({"status": "error", "problem": str(e)[:400], "correct": None})
    record["duration_s"] = round(time.time() - t0, 1)
    res_path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return record


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:8000/v1")
    p.add_argument("--model", required=True, help="served model name: base-qwen or braincode-qwen")
    p.add_argument("--condition", required=True)
    p.add_argument("--input", choices=["english", "braincode"], required=True)
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--workers", type=int, default=16)
    p.add_argument("--no-spec", dest="spec", action="store_false",
                   help="BrainCode input: leave the compact spec (~10k tokens) out of the system prompt")
    args = p.parse_args(argv)
    items = [json.loads(line) for line in (BENCH / "sample.jsonl").read_text(encoding="utf-8").splitlines()
             if line.strip()]
    if args.input == "braincode":
        missing = sum(i["braincode"] is None for i in items)
        items = [i for i in items if i["braincode"]]
        log(f"{len(items)} items with a successful translation ({missing} without one are left out)")
    if args.limit:
        items = items[:args.limit]
    jobs = [(it, k) for k in range(1, args.runs + 1) for it in items]
    log(f"{args.condition}: {len(jobs)} runs ({len(items)} items x {args.runs}) on {args.model}, {args.input} input")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(run_one, args, it, k): (it, k) for it, k in jobs}
        for f in as_completed(futs):
            it, k = futs[f]
            r = f.result()
            if r.get("skipped"):
                continue
            if r["status"] != "ok":
                state = "ERROR " + r["problem"][:120]
            elif r["correct"] is None:
                state = (("verdict block" if r["has_answer_block"] else "NO verdict block")
                         + f"; English answer {r['direct_prediction']} (gold {it['label']})")
            else:
                state = ("correct" if r["correct"] else "wrong") + f" (pred {r['prediction']}, gold {it['label']})"
            log(f"{args.condition} {it['item_key']} r{k} -> {state}")


if __name__ == "__main__":
    main()
