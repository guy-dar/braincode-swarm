#!/usr/bin/env python3
"""Improvement experiment: does encoding a task in BrainCode first help a model
solve it? A paired intervention study on BBEH mini with Llama 3.1 8B Instruct.

Conditions (the same item, the same model, 3 runs each):
  baseline   the BBEH item + BBEH's answer instruction -> answer
  braincode  call 1: language info (compact spec + the glossary entries the RAG
             retrieved for the item, with the value-group catalog) + the item
             -> the item written in BrainCode;
             call 2 (a fresh conversation): the same language info + that
             BrainCode only (never the original item) + the answer instruction
             -> answer

Commands
  sample     50 BBEH-mini items, stratified by task (2 per task + 4 extra), seeded -> sample.jsonl
  prepare    per item: needs + glossary retrieval from the evaluation's frozen
             reference (runs/main/reference, glossary g19) -> items/<key>/rag_context.md
  run        the model calls (resumable): runs/<condition>/<item>/r<k>/result.json
  status     progress and cost
  analyze    accuracy, McNemar, mixed-effects logistic model, figures -> results/

    python improve.py sample
    python improve.py prepare
    python improve.py run --runs 3 [--conditions baseline,braincode] [--limit N]
    python improve.py analyze

Scoring is BBEH's own (google-deepmind/bbeh, bbeh/evaluate.py), reproduced in
`evaluate_correctness`. Key: HF_TOKEN (needs the "Inference Providers"
permission); never printed.
"""
import argparse
import json
import os
import random
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL_DIR = HERE.parent
REF_RUN = EVAL_DIR / "runs" / "main"           # frozen reference + RAG index of the evaluation
DATA = HERE / "data" / "bbeh.parquet"
SAMPLE = HERE / "sample.jsonl"
ITEMS = HERE / "items"
RUNS = HERE / "runs"
RESULTS = HERE / "results"
PROMPTS = HERE / "prompts"

MODEL = "meta-llama/Llama-3.1-8B-Instruct"
PROVIDER = os.environ.get("IMPROVE_PROVIDER", "deepinfra")   # 128k context
ENDPOINT = "https://router.huggingface.co/v1/chat/completions"
TEMPERATURE, TOP_P = 0.6, 0.9                  # Llama 3.1 Instruct's own generation defaults
MAX_TOKENS = 4096
CONCURRENCY = 4
SEED = 2026
PER_TASK, TOTAL = 2, 50
# USD per 1M tokens [input, output]; for reporting only (provider list price, may change)
PRICE = (0.03, 0.05)

# BBEH's answer instruction (the format its scorer expects)
ANSWER_SUFFIX = (
    "\n\nThink step by step, and when you provide the final answer, please use the prefix \"The answer is:\" "
    "without any modification, and provide the answer directly, with no formatting, no bolding, and no markup. "
    "For instance: \"The answer is: 42\" or \"The answer is: yes\". If the question is multiple choice with a "
    "single correct answer, the final answer must only be the letter corresponding to the correct answer. "
    "For example, \"The answer is: (a)\"")
BRAINCODE_RE = re.compile(r"```braincode\s*\n(.*?)```", re.S)


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------- BBEH scoring (verbatim logic)

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


# ---------------------------------------------------------------------- sample

def slug(task: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", task.lower()).strip("_")


def cmd_sample(args):
    import pandas as pd
    d = pd.read_parquet(DATA)
    mini = d[d["mini"].astype(str) == "1"].reset_index().rename(columns={"index": "row"})
    rng = random.Random(SEED)
    tasks = sorted(mini["task"].unique())
    picked = []
    for t in tasks:
        rows = mini[mini["task"] == t].to_dict("records")
        rng.shuffle(rows)
        picked.append(rows)
    items = [rows[i] for rows in picked for i in range(PER_TASK)]
    extra_tasks = rng.sample(range(len(tasks)), TOTAL - len(items))
    items += [picked[i][PER_TASK] for i in extra_tasks]
    with SAMPLE.open("w", encoding="utf-8") as fh:
        for r in items:
            fh.write(json.dumps({"item_key": f"{slug(r['task'])}-{r['row']}", "task": r["task"], "row": int(r["row"]),
                                 "input": r["input"], "target": r["target"], "chars": len(r["input"])},
                                ensure_ascii=False) + "\n")
    log(f"improve: sampled {len(items)} items from {len(tasks)} tasks ({PER_TASK} per task + "
        f"{TOTAL - PER_TASK * len(tasks)} extra) -> {SAMPLE.name}")


def load_sample():
    return [json.loads(line) for line in SAMPLE.read_text(encoding="utf-8").splitlines() if line.strip()]


# ---------------------------------------------------------------------- prepare (retrieval)

def cmd_prepare(args):
    sys.path.insert(0, str(EVAL_DIR))
    import run_eval
    from rag import needs as needs_mod
    from rag.retrieve import render_context
    meta = json.loads((REF_RUN / "meta.json").read_text(encoding="utf-8"))
    items = load_sample()
    with run_eval.Services(REF_RUN.name, need_rag=False) as svc:
        def one(item):
            idir = ITEMS / item["item_key"]
            if (idir / "rag_context.md").exists():
                return "cached"
            idir.mkdir(parents=True, exist_ok=True)
            content = item["input"]
            _, needs, method = needs_mod.extract_needs(content, use_llm=True)
            stripped = [{k: v for k, v in n.items() if k not in ("id", "context")} for n in needs]
            result = svc.retriever.retrieve(content, needs=stripped, needs_method=method)
            (idir / "needs.json").write_text(json.dumps({"translator_id": item["item_key"], "needs": result["needs"]},
                                                        ensure_ascii=False, indent=1), encoding="utf-8")
            (idir / "rag_context.md").write_text(render_context(result, svc.retriever, meta["glossary_version"]),
                                                 encoding="utf-8")
            return method
        with ThreadPoolExecutor(max_workers=4) as pool:
            done = list(pool.map(one, items))
    log(f"improve: prepared {len(items)} items; needs by method {dict(Counter(done))}")


def language_info(item_key: str) -> str:
    spec = (REF_RUN / "reference" / "language-spec.compact.md").read_text(encoding="utf-8")
    rag = (ITEMS / item_key / "rag_context.md").read_text(encoding="utf-8")
    return ("# BrainCode language specification\n\n" + spec + "\n\n# Glossary entries retrieved for this task "
            "(with the value-group catalog)\n\n" + rag)


# ---------------------------------------------------------------------- model calls

_key_lock = threading.Lock()
_key = None


def hf_key() -> str:
    global _key
    with _key_lock:
        if _key is None:
            _key = os.environ.get("HF_TOKEN") or subprocess.run(
                ["powershell.exe", "-NoProfile", "-Command",
                 "[Environment]::GetEnvironmentVariable('HF_TOKEN','User')"],
                capture_output=True, text=True).stdout.strip()
        if not _key:
            sys.exit("improve: no HF_TOKEN")
        return _key


def chat(messages: list) -> dict:
    """One chat completion, streamed: tokens keep the connection busy, so the
    gateway does not time out (HTTP 504) on long prompts with long answers.
    Retries only on rate limits / unavailable (no tokens spent)."""
    body = json.dumps({"model": f"{MODEL}:{PROVIDER}", "messages": messages, "max_tokens": MAX_TOKENS,
                       "temperature": TEMPERATURE, "top_p": TOP_P, "stream": True,
                       "stream_options": {"include_usage": True}}).encode("utf-8")
    for attempt in range(4):
        req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
            "Authorization": f"Bearer {hf_key()}", "Content-Type": "application/json"})
        try:
            parts, finish, usage = [], None, {}
            with urllib.request.urlopen(req, timeout=600) as resp:
                for raw in resp:
                    line = raw.decode("utf-8", "replace").strip()
                    if not line.startswith("data:"):
                        continue
                    data = line[5:].strip()
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    usage = chunk.get("usage") or usage
                    for ch in chunk.get("choices") or []:
                        parts.append((ch.get("delta") or {}).get("content") or "")
                        finish = ch.get("finish_reason") or finish
            return {"text": "".join(parts), "finish_reason": finish,
                    "prompt_tokens": usage.get("prompt_tokens", 0),
                    "completion_tokens": usage.get("completion_tokens", 0)}
        except urllib.error.HTTPError as e:
            detail = e.read()[:300].decode("utf-8", "replace")
            if e.code in (429, 502, 503, 504) and attempt < 3:
                time.sleep(10 * (attempt + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail}")


def prompt(name: str) -> str:
    return (PROMPTS / name).read_text(encoding="utf-8")


def run_one(item: dict, condition: str, k: int) -> dict:
    out = RUNS / condition / item["item_key"] / f"r{k}"
    res_path = out / "result.json"
    if res_path.exists():
        done = json.loads(res_path.read_text(encoding="utf-8"))
        if done["status"] == "ok":
            return done          # an errored call (e.g. out of credit) is redone, overwriting its result
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    calls, record = [], {"item": item["item_key"], "task": item["task"], "condition": condition, "run": k,
                         "model": MODEL, "provider": PROVIDER, "temperature": TEMPERATURE}
    try:
        if condition == "baseline":
            msgs = [{"role": "user", "content": item["input"] + ANSWER_SUFFIX}]
            r = chat(msgs)
            calls.append(r)
            answer_text = r["text"]
        else:
            info = language_info(item["item_key"])
            msgs1 = [{"role": "system", "content": info},
                     {"role": "user", "content": prompt("translate.md").replace("{{TASK}}", item["input"])}]
            r1 = chat(msgs1)
            calls.append(r1)
            (out / "translation.md").write_text(r1["text"], encoding="utf-8")
            blocks = BRAINCODE_RE.findall(r1["text"])
            code = "\n".join(blocks) if blocks else r1["text"]
            record["translation_has_block"] = bool(blocks)
            msgs2 = [{"role": "system", "content": info},
                     {"role": "user", "content": prompt("solve.md").replace("{{BRAINCODE}}", code) + ANSWER_SUFFIX}]
            r2 = chat(msgs2)
            calls.append(r2)
            answer_text = r2["text"]
        (out / "response.md").write_text(answer_text, encoding="utf-8")
        correct = evaluate_correctness(answer_text, item["target"])
        record.update({"status": "ok", "prediction": preprocess_sample(answer_text)[:200], "target": item["target"],
                       "correct": correct, "has_answer_prefix": any(p in answer_text for p in (
                           "The answer is", "The final answer is")),
                       "finish_reasons": [c["finish_reason"] for c in calls]})
    except Exception as e:  # noqa: BLE001 - recorded, not retried
        record.update({"status": "error", "problem": str(e)[:400], "correct": None})
    pt = sum(c["prompt_tokens"] for c in calls)
    ct = sum(c["completion_tokens"] for c in calls)
    record.update({"prompt_tokens": pt, "completion_tokens": ct,
                   "cost_usd": round((pt * PRICE[0] + ct * PRICE[1]) / 1e6, 5),
                   "duration_s": round(time.time() - t0, 1)})
    res_path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
    return record


def cmd_run(args):
    items = load_sample()
    if args.items:
        items = [i for i in items if i["item_key"] in set(args.items.split(","))]
    if args.limit:
        items = items[:args.limit]
    conditions = args.conditions.split(",")
    jobs = [(it, c, k) for k in range(1, args.runs + 1) for it in items for c in conditions]
    log(f"improve: {len(jobs)} runs ({len(items)} items x {conditions} x {args.runs}); {MODEL} via {PROVIDER}")
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        futs = {pool.submit(run_one, *j): j for j in jobs}
        for f in as_completed(futs):
            it, c, k = futs[f]
            r = f.result()
            log(f"improve: {c:9} {it['item_key']:32} r{k} -> "
                + ("ERROR " + r.get("problem", "")[:120] if r["status"] == "error"
                   else ("correct" if r["correct"] else "wrong") + f"  (pred {r['prediction'][:40]!r}, "
                        f"target {r['target'][:40]!r}) ${r['cost_usd']:.4f}"))


def all_results():
    return [json.loads(p.read_text(encoding="utf-8")) for p in RUNS.glob("*/*/r*/result.json")]


def cmd_status(args):
    rs = all_results()
    by = defaultdict(Counter)
    cost = Counter()
    for r in rs:
        by[r["condition"]]["error" if r["status"] == "error" else ("correct" if r["correct"] else "wrong")] += 1
        cost[r["condition"]] += r.get("cost_usd") or 0
    for c, n in sorted(by.items()):
        tot = sum(n.values())
        ok = n["correct"] + n["wrong"]
        log(f"{c:9} runs {tot:3}  correct {n['correct']:3}  wrong {n['wrong']:3}  error {n['error']:3}  "
            f"accuracy {n['correct'] / ok if ok else float('nan'):.1%}  ${cost[c]:.3f}")


# ---------------------------------------------------------------------- analysis

def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / den
    return p, centre - half, centre + half


LABELS = {"baseline": "Baseline", "braincode": "BrainCode first (in-context)",
          "braincode_agentic_ft": "BrainCode, agentic, fine-tuned", "braincode_agentic_base": "BrainCode, agentic, base",
          "baseline_ft": "Baseline, fine-tuned"}
COLORS = {"baseline": "#52514e", "braincode": "#2a78d6", "braincode_agentic_ft": "#eb6834",
          "braincode_agentic_base": "#1baf7a", "baseline_ft": "#8a8880"}


def ordered_conditions(df) -> list:
    known = [c for c in LABELS if c in set(df["condition"])]
    return known + sorted(set(df["condition"]) - set(known) - {"smoke_ft"})


def cmd_analyze(args):
    """Every condition found under runs/ (the in-context runs here, and agentic /
    fine-tuned runs copied back from Colab), each compared with the baseline."""
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM
    from statsmodels.stats.contingency_tables import mcnemar
    RESULTS.mkdir(exist_ok=True)
    every = [r for r in all_results() if not r["condition"].startswith("smoke")]
    errors = Counter(r["condition"] for r in every if r["status"] == "error")
    df = pd.DataFrame([r for r in every if r["status"] == "ok"])
    df["correct"] = df["correct"].astype(int)
    conds = ordered_conditions(df)
    lines = ["# Improvement: BBEH mini, Llama 3.1 8B Instruct, baseline vs BrainCode", "",
             f"{df['item'].nunique()} items ({df['task'].nunique()} tasks). Scoring: BBEH's evaluate.py. "
             f"Errored runs left out: {dict(errors) or 'none'}.", "",
             "## Accuracy (all runs)", "", "| condition | runs | correct | accuracy | 95% CI (Wilson) |",
             "|---|---:|---:|---:|---|"]
    acc = {}
    for c in conds:
        sub = df[df["condition"] == c]
        p_, lo, hi = wilson(int(sub["correct"].sum()), len(sub))
        acc[c] = (p_, lo, hi)
        lines.append(f"| {LABELS.get(c, c)} | {len(sub)} | {int(sub['correct'].sum())} | {p_:.1%} | "
                     f"{lo:.1%}–{hi:.1%} |")
    maj_all = (df.groupby(["item", "condition"])["correct"].mean().unstack() >= 0.5)
    for c in conds:
        if c == "baseline":
            continue
        pair = df[df["condition"].isin(["baseline", c])].copy()
        shared = set(pair[pair.condition == "baseline"].item) & set(pair[pair.condition == c].item)
        pair = pair[pair["item"].isin(shared)]
        pair["treated"] = (pair["condition"] == c).astype(int)
        maj = maj_all.loc[sorted(shared), ["baseline", c]].astype(int)
        a = int(((maj["baseline"] == 1) & (maj[c] == 1)).sum())
        b = int(((maj["baseline"] == 1) & (maj[c] == 0)).sum())
        c_ = int(((maj["baseline"] == 0) & (maj[c] == 1)).sum())
        d = int(((maj["baseline"] == 0) & (maj[c] == 0)).sum())
        mc = mcnemar([[a, b], [c_, d]], exact=True)
        lines += ["", f"## {LABELS.get(c, c)} vs baseline ({len(shared)} paired items)", "",
                  "McNemar, exact, on the per-item majority vote over runs:", "",
                  f"| | {LABELS.get(c, c)} correct | wrong |", "|---|---:|---:|",
                  f"| baseline correct | {a} | {b} |", f"| baseline wrong | {c_} | {d} |", "",
                  f"Discordant pairs: {b} baseline-only vs {c_} {c}-only; exact p = {mc.pvalue:.4f}.", ""]
        try:
            fit = BinomialBayesMixedGLM.from_formula("correct ~ treated", {"item": "0 + C(item)"}, pair).fit_vb()
            coef, sd = float(fit.fe_mean[1]), float(fit.fe_sd[1])
            lines.append(f"- Mixed-effects logistic model `correct ~ condition + (1 | item)`: effect (log-odds) "
                         f"{coef:+.3f} (posterior SD {sd:.3f}); odds ratio {np.exp(coef):.2f} "
                         f"(≈95% interval {np.exp(coef - 1.96 * sd):.2f}–{np.exp(coef + 1.96 * sd):.2f}); "
                         f"item random-effect SD {float(np.exp(fit.vcp_mean[0])):.2f}")
        except Exception as e:  # noqa: BLE001 - e.g. no variation
            lines.append(f"- Mixed-effects model not estimable: {e}")
        try:
            gee = sm.GEE.from_formula("correct ~ treated", groups="item", data=pair, family=sm.families.Binomial(),
                                      cov_struct=sm.cov_struct.Exchangeable()).fit()
            lines.append(f"- GEE check (item-clustered): log-odds {gee.params['treated']:+.3f}, "
                         f"p = {gee.pvalues['treated']:.4f}")
        except Exception as e:  # noqa: BLE001
            lines.append(f"- GEE not estimable: {e}")
    lines += ["", "One model and one benchmark, so the model and benchmark terms of the design formula "
                  "(`Correct ~ condition + model + benchmark + condition × model + (1|item)`) drop out."]
    per_task = df.groupby(["task", "condition"])["correct"].mean().unstack()[conds]
    lines += ["", "## Accuracy per task", "", "| task | " + " | ".join(LABELS.get(c, c) for c in conds) + " |",
              "|---|" + "---:|" * len(conds)]
    for t, row in per_task.sort_index().iterrows():
        lines.append(f"| {t} | " + " | ".join(f"{row[c]:.0%}" if row[c] == row[c] else "—" for c in conds) + " |")
    lines += ["", "## Diagnostics", ""]
    for c in conds:
        sub = df[df["condition"] == c]
        extra = ""
        if "translation_has_block" in sub and sub["translation_has_block"].notna().any():
            extra = f"; translations with a braincode block {sub['translation_has_block'].mean():.0%}"
        lines.append(f"- {LABELS.get(c, c)}: answers with the required prefix {sub.has_answer_prefix.mean():.0%}"
                     f"{extra}; cost ${sub['cost_usd'].sum():.3f}")
    (RESULTS / "improvement.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    df.drop(columns=[c for c in ("finish_reasons",) if c in df]).to_csv(RESULTS / "improvement_runs.csv", index=False)
    figures(df, acc, per_task, conds)
    log(f"improve: wrote {RESULTS / 'improvement.md'}")


def figures(df, acc, per_task, conds):
    sys.path.insert(0, str(EVAL_DIR))
    import analyze
    import matplotlib.pyplot as plt
    analyze.style()
    fig, ax = plt.subplots(figsize=(2.2 + 1.5 * len(conds), 4.2))
    for i, c in enumerate(conds):
        p_, lo, hi = acc[c]
        ax.bar(i, p_, width=0.55, color=COLORS.get(c, "#9e9c95"))
        ax.errorbar(i, p_, yerr=[[p_ - lo], [hi - p_]], color="#0b0b0b", capsize=5, linewidth=1.2)
        ax.text(i, hi + 0.01, f"{p_:.1%}", ha="center", va="bottom", fontsize=9)
    ax.set_xticks(range(len(conds)), [LABELS.get(c, c).replace(" (", "\n(").replace(", ", ",\n", 1)
                                       for c in conds], fontsize=8.5)
    ax.set_ylabel("Accuracy (higher = better)")
    ax.set_title("BBEH mini (50 items), Llama 3.1 8B", loc="left")
    ax.set_ylim(0, max([0.5] + [acc[c][2] + 0.08 for c in conds]))
    analyze.save(fig, RESULTS / "improvement_accuracy.png")
    pt = per_task.sort_values("baseline")
    fig, ax = plt.subplots(figsize=(7.5, 0.32 * len(pt) + 1.4))
    y = list(range(len(pt)))
    for t_i, (_, row) in enumerate(pt.iterrows()):
        vals = [row[c] for c in conds if row[c] == row[c]]
        ax.plot([min(vals), max(vals)], [t_i, t_i], color="#e4e2dc", linewidth=2, zorder=1)
    for z, c in enumerate(conds):
        ax.scatter(pt[c], y, color=COLORS.get(c, "#9e9c95"), s=40, label=LABELS.get(c, c), zorder=2 + z,
                   edgecolors="#fcfcfb", linewidths=1)
    ax.set_yticks(y, list(pt.index))
    ax.set_xlabel("Accuracy (higher = better)")
    ax.set_xlim(-0.03, 1.03)
    ax.set_title("Accuracy per task", loc="left")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=min(3, len(conds)))
    analyze.save(fig, RESULTS / "improvement_per_task.png")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", choices=["sample", "prepare", "run", "status", "analyze"])
    p.add_argument("--runs", type=int, default=3)
    p.add_argument("--conditions", default="baseline,braincode")
    p.add_argument("--items", default="")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args(argv)
    sys.path.insert(0, str(EVAL_DIR.parent / "swarm"))
    {"sample": cmd_sample, "prepare": cmd_prepare, "run": cmd_run, "status": cmd_status,
     "analyze": cmd_analyze}[args.command](args)


if __name__ == "__main__":
    main()
