#!/usr/bin/env python3
"""Run the 50 BBEH-mini items in the agentic BrainCode setup against an
OpenAI-compatible endpoint (vLLM in Colab, serving the fine-tuned Llama).

Flow per item and run (the same two steps as the in-context experiment, now
with tools instead of a fixed context):

  1. Translate  - the model sees the task and has tools to read the language
                  spec, read the glossary entries the RAG retrieved for the item,
                  search the glossary, look up entries, and check a draft with
                  the swarm's own checker. It ends by calling submit_braincode.
  2. Solve      - a fresh conversation: the model sees only its BrainCode (never
                  the task text), has the same spec/glossary tools, and answers
                  with "The answer is: ...".

Scored with BBEH's own scorer (bbeh/evaluate.py). Results go to
runs/<condition>/<item>/r<k>/ (result.json, translation.md, response.md,
transcript.json), in the same format as evaluations/improvement, so they can be
analysed together.

    python run_braincode_agentic.py --base-url http://localhost:8000/v1 --model braincode-llama
    python run_braincode_agentic.py --model base-llama --condition braincode_agentic_base
    python run_braincode_agentic.py --model braincode-llama --condition baseline_ft --mode baseline
"""
import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "braincode_kit"
BENCH = HERE / "benchmark"
sys.path.insert(0, str(KIT))

TEMPERATURE, TOP_P = 0.6, 0.9          # Llama 3.1 Instruct's generation defaults (same as the in-context runs)
MAX_TOKENS = 4096
MAX_STEPS = 16                          # tool rounds per phase
MAX_TOOL_CHARS = 60_000                 # one tool result (~15k tokens)
ANSWER_SUFFIX = (
    "\n\nThink step by step, and when you provide the final answer, please use the prefix \"The answer is:\" "
    "without any modification, and provide the answer directly, with no formatting, no bolding, and no markup. "
    "For instance: \"The answer is: 42\" or \"The answer is: yes\". If the question is multiple choice with a "
    "single correct answer, the final answer must only be the letter corresponding to the correct answer. "
    "For example, \"The answer is: (a)\"")
BRAINCODE_RE = re.compile(r"```braincode\s*\n(.*?)```", re.S)

TRANSLATE_SYSTEM = """You translate tasks into BrainCode, a formal language with a fixed glossary of symbols. You do not solve the task.

You have tools:
- read_spec(section?): the BrainCode language specification (or the sections whose heading contains `section`).
- get_retrieved_context(): the glossary entries a retrieval system selected for this task, with the value-group catalog. Read it first.
- search_glossary(queries, kind?): search the glossary for symbols matching each query.
- glossary_entries(keys): full records for symbols or group values (e.g. `activity`, `country::JP`).
- check_braincode(braincode): the checker; it lists unknown symbols, invalid group values and quoted text that is too long.
- submit_braincode(braincode): submit your final translation. This ends the translation.

Rules:
- Write a `MODE REQUEST` document using only glossary symbols, group values (`group::key`), local handles and literals. Invent no symbols.
- Encode everything needed to solve the task: every fact, rule, entity, quantity, constraint and relation, the question, and the answer options or format. The solver will see only your BrainCode, never the task text.
- No quoted string may hold 8 or more words, except names and titles (`name=`, `title=`, `label=`, `caption=`).
- Check your draft with check_braincode, fix what it reports, then call submit_braincode."""

SOLVE_SYSTEM = """You solve tasks that are written in BrainCode, a formal language with a fixed glossary of symbols.

You have tools to read the language: read_spec(section?), get_retrieved_context(), search_glossary(queries, kind?), glossary_entries(keys). Use them when you need to know what a construct or symbol means. When you are done, reply with your reasoning and the final answer (no tool call)."""


def tool_schemas(phase: str) -> list:
    def fn(name, desc, props, required):
        return {"type": "function", "function": {"name": name, "description": desc, "parameters": {
            "type": "object", "properties": props, "required": required}}}
    tools = [
        fn("read_spec", "Read the BrainCode language specification, or only the sections whose heading contains "
           "`section`.", {"section": {"type": "string"}}, []),
        fn("get_retrieved_context", "The glossary entries retrieved for this task, with the value-group catalog.",
           {}, []),
        fn("search_glossary", "Search the glossary; one result list per query.",
           {"queries": {"type": "array", "items": {"type": "string"}}, "kind": {"type": "string"}}, ["queries"]),
        fn("glossary_entries", "Full glossary records for symbols or group values.",
           {"keys": {"type": "array", "items": {"type": "string"}}}, ["keys"]),
    ]
    if phase == "translate":
        tools += [
            fn("check_braincode", "Check a BrainCode draft with the glossary checker.",
               {"braincode": {"type": "string"}}, ["braincode"]),
            fn("submit_braincode", "Submit the final BrainCode translation (ends the translation).",
               {"braincode": {"type": "string"}}, ["braincode"]),
        ]
    return tools


# ---------------------------------------------------------------------- tools (the swarm's own RAG + checker)

class Tools:
    def __init__(self):
        from rag.retrieve import Retriever
        self.retriever = Retriever(dense=True, glossary_path=KIT / "reference" / "glossary.jsonl",
                                   index_dir=KIT / "rag" / "index", use_llm=False)
        self.spec = (KIT / "reference" / "language-spec.compact.md").read_text(encoding="utf-8")
        self.lock = threading.Lock()

    def read_spec(self, section=None, **_):
        if not section:
            return self.spec
        parts = re.split(r"(?m)^(?=#{1,4} )", self.spec)
        hits = [p for p in parts if p.splitlines() and section.lower() in p.splitlines()[0].lower()]
        return "\n".join(hits) if hits else f"No section heading contains {section!r}. Call read_spec() for all."

    def get_retrieved_context(self, item_key, **_):
        return (BENCH / "items" / item_key / "rag_context.md").read_text(encoding="utf-8")

    def search_glossary(self, queries=None, kind="", **_):
        from rag.retrieve import render_candidates
        queries = queries if isinstance(queries, list) else [str(queries or "")]
        with self.lock:
            return "\n\n".join(render_candidates({"text": q, "candidates": self.retriever.search_need(q, "", kind or "")})
                               for q in queries[:8])

    def glossary_entries(self, keys=None, **_):
        from rag.server import render_entries
        keys = keys if isinstance(keys, list) else [str(keys or "")]
        with self.lock:
            return render_entries({k: self.retriever.entry(k) for k in keys[:20]})

    def check_braincode(self, braincode="", item_key=None, **_):
        from rag.retrieve import render_check
        doc = "```braincode\n" + strip_fence(braincode) + "\n```"
        with self.lock:
            report = self.retriever.check(doc, [])
        return render_check(report)

    def call(self, name, args, item_key):
        fn = getattr(self, name, None)
        if fn is None or name.startswith("_") or name == "call":
            return f"Unknown tool {name!r}."
        try:
            out = fn(item_key=item_key, **(args or {}))
        except TypeError as e:
            return f"Bad arguments for {name}: {e}"
        return out if len(out) <= MAX_TOOL_CHARS else out[:MAX_TOOL_CHARS] + "\n…[truncated]"


def strip_fence(code: str) -> str:
    m = BRAINCODE_RE.search(code or "")
    return (m.group(1) if m else (code or "")).strip()


# ---------------------------------------------------------------------- model client

API_KEY = "local"   # vLLM ignores it; --api-key-env names a variable for hosted endpoints


def chat(base_url, model, messages, tools):
    body = {"model": model, "messages": messages, "max_tokens": MAX_TOKENS, "temperature": TEMPERATURE,
            "top_p": TOP_P}
    if tools:
        body.update({"tools": tools, "tool_choice": "auto"})
    for attempt in range(3):
        req = urllib.request.Request(base_url.rstrip("/") + "/chat/completions", method="POST",
                                     data=json.dumps(body).encode("utf-8"),
                                     headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"})
        try:
            with urllib.request.urlopen(req, timeout=900) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            if e.code == 400 and "context" in detail.lower() and trim_oldest_tool_result(messages):
                continue                              # too long: drop the oldest tool output and retry
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail[:300]}")
    raise RuntimeError("context still too long after trimming")


def trim_oldest_tool_result(messages) -> bool:
    for m in messages:
        if m["role"] == "tool" and not m["content"].startswith("[trimmed"):
            m["content"] = "[trimmed to fit the context window; call the tool again if you need it]"
            return True
    return False


TEXT_CALL_RE = re.compile(r"\{\s*\"name\"\s*:\s*\"(\w+)\"\s*,\s*\"(?:parameters|arguments)\"\s*:\s*(\{.*\})\s*\}", re.S)
# Llama 3.1's own custom-tool format: <function=name>{"arg": ...}</function>, which the
# model also writes as <function=name(arg="...")>{}</function>
FUNC_TAG_RE = re.compile(r"<function=(\w+)(\((.*?)\))?>(.*?)</function>", re.S)


def kwargs_of(inner: str) -> dict:
    import ast
    try:
        call = ast.parse(f"f({inner})", mode="eval").body
        return {kw.arg: ast.literal_eval(kw.value) for kw in call.keywords if kw.arg}
    except (SyntaxError, ValueError):
        return {}


def tool_calls_of(msg) -> list:
    """(id, name, args, native?) for native tool calls, or calls the model wrote as
    text: Llama's <function=...> tags, or {"name": ..., "parameters": ...} JSON."""
    calls = []
    for tc in msg.get("tool_calls") or []:
        try:
            args = json.loads(tc["function"].get("arguments") or "{}")
        except json.JSONDecodeError:
            args = {}
        calls.append((tc.get("id") or f"call_{len(calls)}", tc["function"]["name"], args, True))
    text = (msg.get("content") or "").replace("<|python_tag|>", "")
    if not calls and text:
        for m in FUNC_TAG_RE.finditer(text):
            args = {}
            body = m.group(4).strip()
            if body and body != "{}":
                try:
                    args = json.loads(body)
                except json.JSONDecodeError:
                    args = {}
            if not args and m.group(3):
                args = kwargs_of(m.group(3))
            calls.append((f"text_{len(calls)}", m.group(1), args, False))
        if not calls:
            m = TEXT_CALL_RE.search(text)
            if m:
                try:
                    calls.append(("text_0", m.group(1), json.loads(m.group(2)), False))
                except json.JSONDecodeError:
                    pass
    return calls


def agent(base_url, model, tools_impl, item_key, system, user, phase, transcript):
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    schemas = tool_schemas(phase)
    usage = Counter()
    for _ in range(MAX_STEPS):
        d = chat(base_url, model, messages, schemas)
        u = d.get("usage") or {}
        usage["prompt_tokens"] += u.get("prompt_tokens", 0)
        usage["completion_tokens"] += u.get("completion_tokens", 0)
        msg = d["choices"][0]["message"]
        calls = tool_calls_of(msg)
        assistant = {"role": "assistant", "content": msg.get("content") or ""}
        if msg.get("tool_calls"):
            assistant["tool_calls"] = msg["tool_calls"]
        messages.append(assistant)
        transcript.append({"phase": phase, "assistant": assistant.get("content", "")[:4000],
                           "calls": [(n, json.dumps(a)[:400]) for _, n, a, _ in calls]})
        if not calls:
            if phase == "translate" and BRAINCODE_RE.search(assistant["content"]):
                return strip_fence(assistant["content"]), usage, "text"
            if phase == "solve":
                return assistant["content"], usage, "text"
            messages.append({"role": "user", "content": "Call submit_braincode with your final BrainCode."})
            continue
        text_results = []
        for call_id, name, args, native in calls:
            if phase == "translate" and name == "submit_braincode":
                code = strip_fence(args.get("braincode", ""))
                if code:
                    return code, usage, "submitted"
                result = "submit_braincode needs the argument `braincode` with your BrainCode document."
            else:
                result = tools_impl.call(name, args, item_key)
            transcript.append({"phase": phase, "tool": name, "result_chars": len(result)})
            if native:
                messages.append({"role": "tool", "tool_call_id": call_id, "name": name, "content": result})
            else:
                text_results.append(f"### {name} result\n\n{result}")
        if text_results:   # calls written as text: results come back as a message
            messages.append({"role": "user", "content": "\n\n".join(text_results)})
    return (None, usage, "step limit") if phase == "translate" else (messages[-1].get("content", ""), usage,
                                                                      "step limit")


# ---------------------------------------------------------------------- BBEH scoring (google-deepmind/bbeh evaluate.py)

def strip_latex(response: str) -> str:
    if response.startswith("$") and response.endswith("$"):
        response = response[1:-1]
    if "boxed{" in response and response.endswith("}"):
        response = response[0:-1].split("boxed{")[1]
    if "text{" in response and response.endswith("}"):
        response = response[0:-1].split("text{")[1]
    if "texttt{" in response and response.endswith("}"):
        response = response[0:-1].split("texttt{")[1]
    return response


def extract_answer(sample: str) -> str:
    answer = sample
    for prefix in ["The answer is:", "The final answer is ", "The final answer is: ", "The answer is "]:
        if prefix in answer:
            answer = answer.split(prefix)[-1].strip()
    if answer.endswith("."):
        answer = answer[:-1]
    return strip_latex(answer)


def fuzzy_match(prediction: str, reference: str) -> bool:
    if prediction == reference:
        return True
    if len(prediction) == 3 and prediction[0] == "(" and prediction[-1] == ")":
        return prediction[1] == reference
    if len(reference) == 3 and reference[0] == "(" and reference[-1] == ")":
        return reference[1] == prediction
    try:
        if float(prediction) == float(reference):
            return True
    except ValueError:
        pass
    if prediction.replace("'", "") == reference.replace("'", ""):
        return True
    if f"[{reference}]" == prediction or f"[{prediction}]" == reference:
        return True
    if prediction.endswith("?") and prediction[:-1] == reference:
        return True
    return False


def preprocess_sample(sample: str) -> str:
    prediction = extract_answer(sample.strip()).lower()
    prediction = prediction.replace(", ", ",").replace("**", "")
    prediction = prediction.split("\n")[0]
    return prediction[0:-1] if prediction.endswith(".") else prediction


def evaluate_correctness(sample: str, reference: str) -> bool:
    return fuzzy_match(preprocess_sample(sample), reference.strip().lower().replace(", ", ","))


# ---------------------------------------------------------------------- runner

def run_one(args, tools_impl, item, k):
    out = HERE / "runs" / args.condition / item["item_key"] / f"r{k}"
    res_path = out / "result.json"
    if res_path.exists() and json.loads(res_path.read_text(encoding="utf-8"))["status"] == "ok":
        return json.loads(res_path.read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    t0, transcript, usage = time.time(), [], Counter()
    record = {"item": item["item_key"], "task": item["task"], "condition": args.condition, "run": k,
              "model": args.model, "provider": "vllm (colab)", "temperature": TEMPERATURE, "mode": args.mode}
    try:
        if args.mode == "baseline":
            d = chat(args.base_url, args.model, [{"role": "user", "content": item["input"] + ANSWER_SUFFIX}], None)
            answer = d["choices"][0]["message"].get("content") or ""
            usage["prompt_tokens"] += (d.get("usage") or {}).get("prompt_tokens", 0)
            usage["completion_tokens"] += (d.get("usage") or {}).get("completion_tokens", 0)
        else:
            code, u1, how = agent(args.base_url, args.model, tools_impl, item["item_key"], TRANSLATE_SYSTEM,
                                  "Translate this task into BrainCode:\n\n" + item["input"], "translate", transcript)
            usage.update(u1)
            record["translation_end"] = how
            if not code:
                raise RuntimeError(f"no BrainCode submitted ({how})")
            (out / "translation.md").write_text("```braincode\n" + code + "\n```\n", encoding="utf-8")
            record["check"] = tools_impl.check_braincode(code)[:2000]
            answer, u2, how2 = agent(args.base_url, args.model, tools_impl, item["item_key"], SOLVE_SYSTEM,
                                     "Below is a task written in BrainCode. Work out what it asks and solve it."
                                     "\n\n```braincode\n" + code + "\n```" + ANSWER_SUFFIX, "solve", transcript)
            usage.update(u2)
            record["solve_end"] = how2
        (out / "response.md").write_text(answer, encoding="utf-8")
        record.update({"status": "ok", "prediction": preprocess_sample(answer)[:200], "target": item["target"],
                       "correct": evaluate_correctness(answer, item["target"]),
                       "has_answer_prefix": "The answer is" in answer or "The final answer is" in answer,
                       "tool_calls": sum(1 for t in transcript if "tool" in t)})
    except Exception as e:  # noqa: BLE001 - recorded, redone on the next run
        record.update({"status": "error", "problem": str(e)[:400], "correct": None})
    record.update({"prompt_tokens": usage["prompt_tokens"], "completion_tokens": usage["completion_tokens"],
                   "cost_usd": 0.0, "duration_s": round(time.time() - t0, 1)})
    (out / "transcript.json").write_text(json.dumps(transcript, ensure_ascii=False, indent=1), encoding="utf-8")
    res_path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return record


def main(argv=None):
    global API_KEY, MAX_TOOL_CHARS
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url", default="http://localhost:8000/v1")
    p.add_argument("--model", default="braincode-llama", help="served model name (vLLM --served-model-name / LoRA name)")
    p.add_argument("--condition", default="braincode_agentic_ft", help="results folder name under runs/")
    p.add_argument("--mode", choices=["braincode", "baseline"], default="braincode")
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--limit", type=int, default=0, help="first N items only (smoke test)")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--api-key-env", default="", help="environment variable holding an API key (hosted endpoints)")
    p.add_argument("--max-tool-chars", type=int, default=MAX_TOOL_CHARS,
                   help="cap on one tool result (lower it on small GPUs with a short context)")
    args = p.parse_args(argv)
    MAX_TOOL_CHARS = args.max_tool_chars
    if args.api_key_env:
        API_KEY = os.environ.get(args.api_key_env) or sys.exit(f"{args.api_key_env} is not set")
    items = [json.loads(line) for line in (BENCH / "sample.jsonl").read_text(encoding="utf-8").splitlines() if line]
    if args.limit:
        items = items[:args.limit]
    tools_impl = Tools() if args.mode == "braincode" else None
    jobs = [(it, k) for k in range(1, args.runs + 1) for it in items]
    print(f"{len(jobs)} runs: {len(items)} items x {args.runs}, condition {args.condition}, model {args.model}",
          flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(run_one, args, tools_impl, it, k): (it, k) for it, k in jobs}
        for f in as_completed(futs):
            it, k = futs[f]
            r = f.result()
            results.append(r)
            print(f"{it['item_key']:32} r{k} -> " + (f"ERROR {r.get('problem', '')[:100]}" if r["status"] == "error"
                  else ("correct" if r["correct"] else "wrong") + f" (pred {r['prediction'][:30]!r}, target "
                  f"{r['target'][:30]!r})"), flush=True)
    ok = [r for r in results if r["status"] == "ok"]
    acc = sum(r["correct"] for r in ok) / len(ok) if ok else float("nan")
    summary = {"condition": args.condition, "model": args.model, "runs": len(results), "ok": len(ok),
               "errors": len(results) - len(ok), "correct": sum(r["correct"] for r in ok), "accuracy": acc}
    (HERE / "runs" / args.condition / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
