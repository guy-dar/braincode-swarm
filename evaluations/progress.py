"""One-line evaluation status with cost per company and per model (forward + back-translation)."""
import glob
import json
import os
from collections import Counter, defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))
models = {m["name"]: m for m in json.load(open("models.json", encoding="utf-8"))["models"]}
company_of = {name: m["company"] for name, m in models.items()}
company_of.update({"gpt-6.1-sol": "OpenAI", "gpt-6-luna": "OpenAI", "claude-opus-5.5": "Claude", "gpt-6-astra": "OpenAI",
                   "o4-mini": "OpenAI"})
done, status, cost = Counter(), defaultdict(Counter), Counter()
backs, back_cost = Counter(), Counter()
for p in glob.glob("runs/main/*/*/r*/result.json"):
    r = json.load(open(p, encoding="utf-8"))
    done[r["model"]] += 1
    status[r["model"]][r["status"]] += 1
    cost[r["model"]] += r.get("cost_usd") or 0
for p in glob.glob("runs/main/*/*/r*/back/result.json"):
    r = json.load(open(p, encoding="utf-8"))
    backs[r["model"]] += 1
    back_cost[r["model"]] += r.get("cost_usd") or 0
planned = {"gemini-flash-3.7": 144, "gemini-flash-high-3.7": 144, "claude-sonnet-5.5": 54, "claude-haiku-4.5": 54,
           "gpt-6.1-sol": 54, "gpt-6-luna": 54,   # OpenAI stopped by the user part-way
           "o4-mini": 18}                          # probe: 1 run per shared item
by_company = defaultdict(float)
parts = []
for m in planned:
    c = cost[m] + back_cost[m]
    by_company[company_of.get(m, "?")] += c
    s = status[m]
    extra = f", back {backs[m]}/48" if m.startswith("gemini") else (", STOPPED" if m.startswith("gpt") else (", probe" if m == "o4-mini" else ""))
    parts.append(f"{m} {done[m]}/{planned[m]} (ok {s['success']}, fail {s['failed']}, err {s['error']}{extra}) ${c:.2f}")
total = sum(by_company.values())
print("COMPANIES: " + ", ".join(f"{k} ${v:.2f}" for k, v in sorted(by_company.items())) + f" | TOTAL ${total:.2f}")
print("MODELS: " + "; ".join(parts))
