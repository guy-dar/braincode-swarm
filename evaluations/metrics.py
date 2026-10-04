"""Measures for the BrainCode evaluations.

Determinism: which glossary symbols (and symbol types) a translation uses,
and Jensen-Shannon divergence between such distributions.
Expressivity: similarity between an original item and its round trip
(NL -> BrainCode -> NL): BLEU, ROUGE-L and word-level Levenshtein similarity,
all oriented so that higher = more similar = better.
"""
import json
import math
import re
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

SWARM = Path(__file__).resolve().parent.parent / "swarm"
sys.path.insert(0, str(SWARM))

from glossary import groups as groups_mod  # noqa: E402
from rag.retrieve import braincode_code  # noqa: E402

QUOTED_RE = re.compile(r'"(?:[^"\\]|\\.)*"')
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
WORD_RE = re.compile(r"[^\W_]+(?:'[^\W_]+)?", re.UNICODE)
TURN_MARK_RE = re.compile(r"<\|(user|assistant)\|>")


# ---------------------------------------------------------------------- symbols

def glossary_kinds(glossary_jsonl: Path) -> dict:
    """{symbol: kind} for every record of a (frozen) glossary."""
    kinds = {}
    for line in Path(glossary_jsonl).read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            kinds[r["symbol"]] = r.get("kind") or "unknown"
    return kinds


def code_of(document: str) -> str:
    """The BrainCode of a translation document, comments and quoted literals
    removed (exact-wording strings are content, not vocabulary)."""
    code = braincode_code(document)
    code = "\n".join(line.split("#", 1)[0] for line in code.splitlines())
    return QUOTED_RE.sub(" ", code)


def symbol_counts(document: str, kinds: dict) -> tuple:
    """(Counter of symbols, Counter of symbol types) used in a translation.
    Symbols are glossary symbols (each occurrence counts) and value-group
    atoms `group::key`; a symbol's type is its glossary kind, `group_value`
    for an atom."""
    code = code_of(document)
    symbols, types = Counter(), Counter()
    for m in groups_mod.ATOM_RE.finditer(code):
        symbols[f"{m.group(1)}::{m.group(2)}"] += 1
        types["group_value"] += 1
    rest = groups_mod.ATOM_RE.sub(" ", code)
    for tok in TOKEN_RE.findall(rest):
        kind = kinds.get(tok)
        if kind is None or kind in ("structural", "rule", "category_rule", "example"):
            continue
        symbols[tok] += 1
        types[kind] += 1
    return symbols, types


# ---------------------------------------------------------------------- divergence

def distribution(counts: Counter) -> dict:
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items() if v > 0} if total else {}


def js_divergence(p_counts: Counter, q_counts: Counter) -> float:
    """Jensen-Shannon divergence (base 2, in [0, 1]) between two count
    distributions over the union of their supports. Two empty inputs -> 0;
    one empty input -> 1."""
    p, q = distribution(p_counts), distribution(q_counts)
    if not p and not q:
        return 0.0
    if not p or not q:
        return 1.0
    js = 0.0
    for k in set(p) | set(q):
        pk, qk = p.get(k, 0.0), q.get(k, 0.0)
        mk = (pk + qk) / 2
        if pk:
            js += 0.5 * pk * math.log2(pk / mk)
        if qk:
            js += 0.5 * qk * math.log2(qk / mk)
    return max(0.0, min(1.0, js))


def mean_pairwise_js(runs: list) -> tuple:
    """(mean JS over all pairs of runs, share of identical pairs) for one
    item's runs (Counters). Fewer than two runs -> (None, None)."""
    pairs = list(combinations(runs, 2))
    if not pairs:
        return None, None
    values = [js_divergence(a, b) for a, b in pairs]
    return sum(values) / len(values), sum(v == 0.0 for v in values) / len(values)


# ---------------------------------------------------------------------- expressivity

def words(text: str) -> list:
    """Lower-cased word tokens; turn markers dropped."""
    return [w.lower() for w in WORD_RE.findall(TURN_MARK_RE.sub(" ", text or ""))]


def levenshtein(a: list, b: list) -> int:
    """Edit distance between two token sequences (insert / delete / substitute = 1)."""
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def word_levenshtein_similarity(reference: str, hypothesis: str) -> float:
    """1 - d_word(ref, hyp) / max(|ref|, |hyp|), in [0, 1]; 1 = identical words."""
    a, b = words(reference), words(hypothesis)
    if not a and not b:
        return 1.0
    return 1.0 - levenshtein(a, b) / max(len(a), len(b))


def bleu(reference: str, hypothesis: str) -> float:
    """Sentence BLEU (sacrebleu, exponential smoothing), scaled to [0, 1]."""
    import sacrebleu
    ref, hyp = " ".join(words(reference)), " ".join(words(hypothesis))
    return sacrebleu.sentence_bleu(hyp, [ref], smooth_method="exp").score / 100.0


def corpus_bleu(references: list, hypotheses: list) -> float:
    import sacrebleu
    refs = [" ".join(words(r)) for r in references]
    hyps = [" ".join(words(h)) for h in hypotheses]
    return sacrebleu.corpus_bleu(hyps, [refs]).score / 100.0


def rouge_l(reference: str, hypothesis: str) -> float:
    """ROUGE-L F1 on lower-cased words, in [0, 1]."""
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
    return scorer.score(" ".join(words(reference)), " ".join(words(hypothesis)))["rougeL"].fmeasure
