"""Decomposition-driven retrieval over glossary records.

Steps 1-4 run on the host before a translator starts (Retriever.retrieve):
  1. extract source-linked needs from the item           (needs.py)
  2. search each need: exact name/alias, BM25, dense     (search_need)
  3. fuse (RRF) and rerank against the need's context    (search_need)
  4. pull in full records + dependencies + shared rules  (expand)
Steps 5-7 are the translator's, through the kit: `check` a translation
against the needs, `widen` the search for anything unresolved, and fall
back to reading glossary.md directly.

The emphasis everywhere is recall: exact matches are never dropped by
reranking, per-need limits are generous, and expansion follows every
dependency and shared rule a retrieved record points at.
"""
import re
import threading
from pathlib import Path

from . import index as index_mod
from . import needs as needs_mod

# Query words appended per need kind: they steer BM25 toward the part of the
# glossary that kind of meaning lives in, without excluding anything else.
KIND_HINTS = {
    "action": "operation action perform",
    "object": "entity object resource value",
    "constraint": "requirement constraint include exclude limit",
    "negation": "exclude absence not reject decline",
    "correction": "revise correct amend replacement",
    "temporal": "duration time unit period day",
    "speech_act": "utter speech act ask inform respond propose",
    "claim": "claim relation outcome assert",
    "reasoning": "link supports rejects contradicts revises",
}
# Record kinds that answer a need kind most directly; a small rerank boost.
KIND_AFFINITY = {
    "action": {"operation", "constructor"},
    "object": {"value", "composite"},
    "constraint": {"constructor", "composite", "value"},
    "negation": {"constructor", "speech_act"},
    "correction": {"link", "speech_act"},
    "temporal": {"constructor", "value"},
    "speech_act": {"speech_act"},
    "claim": {"claim_relation"},
    "reasoning": {"link", "claim_relation"},
}
CODE_HEAD_RE = re.compile(r"^\s*(?:RECORD\s+(?:ACTION|GENERATE)|ACTION|UTTER|TERM|CLAIM|LINK)\s+([A-Za-z_][A-Za-z0-9_]*)",
                          re.M)
BIND_RE = re.compile(r"(?:->\s*|LET\s+|FOR\s+EACH\s+|TURN\s+)([A-Za-z_][A-Za-z0-9_]*)")
ATTR_VALUE_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*\s*=\s*([A-Za-z_][A-Za-z0-9_]*)(?:\.[A-Za-z_][A-Za-z0-9_]*)?")
# A quoted string where an operation expects an entity/resource/place: usually
# a missing vocabulary member papered over with a literal.
OP_STRING_ARG_RE = re.compile(r"(?:RECORD\s+ACTION|ACTION)\s+[A-Za-z_][A-Za-z0-9_]*\s*\(([^)]*)\)")
ENTITY_ARGS = {"target", "destination", "source", "location", "recipient", "resource", "object"}
BRAINCODE_BLOCK_RE = re.compile(r"```braincode\s*\n(.*?)```", re.S)
# An unclosed block (a real failure mode) runs to the next markdown heading.
UNCLOSED_BLOCK_RE = re.compile(r"```braincode\s*\n(.*?)(?=^#{1,3} |\Z)", re.S | re.M)
GRAMMAR_WORDS = {"TRUE", "FALSE", "USER", "AGENT", "REQUEST", "TRACE", "asserted", "observed", "inferred",
                 "assumed", "hypothesized", "reported", "attempted", "succeeded", "failed", "unknown"}


def braincode_code(text: str) -> str:
    """The BrainCode of a translation document: its ```braincode blocks, an
    unclosed block up to the next heading, or (no block at all) the text."""
    blocks = BRAINCODE_BLOCK_RE.findall(text)
    if blocks:
        return "\n".join(blocks)
    blocks = UNCLOSED_BLOCK_RE.findall(text)
    return "\n".join(blocks) if blocks else text


class Retriever:
    def __init__(self, dense: bool = True, glossary_path: Path = None, index_dir: Path = index_mod.INDEX_DIR,
                 use_llm: bool = True):
        self.dense = dense
        self.glossary_path = glossary_path
        self.index_dir = index_dir
        self.use_llm = use_llm
        self._lock = threading.Lock()
        self.index = index_mod.build(dense=dense, glossary_path=glossary_path, index_dir=index_dir)

    def reload(self):
        """Rebuild from the current glossary.jsonl; queries in flight finish
        on the old index (the swap is a single reference assignment)."""
        fresh = index_mod.build(dense=self.dense, glossary_path=self.glossary_path, index_dir=self.index_dir)
        with self._lock:
            self.index = fresh
        return {"records": len(fresh.records), "glossary_sha": fresh.glossary_sha}

    # ------------------------------------------------------------------ step 2+3
    def search_need(self, text: str, context: str = "", kind: str = "", k: int = 15, keep: int = 12,
                    _vecs=None) -> list:
        """Candidates for one need, best first:
        [{"id", "symbol", "kind", "score", "reasons": [...]}]. Exact matches
        always survive; `keep` bounds the rest."""
        idx = self.index
        hinted = f"{text} {KIND_HINTS.get(kind, '')}"
        fused, reasons = {}, {}

        def add(rid, rank, why):
            fused[rid] = fused.get(rid, 0.0) + index_mod.rrf(rank)
            reasons.setdefault(rid, []).append(why)

        exact = idx.exact(text)
        for rank, rid in enumerate(exact, 1):
            add(rid, rank, "exact")
        for rank, (rid, _) in enumerate(idx.keyword(hinted, k), 1):
            add(rid, rank, "keyword")
        need_vec = ctx_vec = None
        if idx.dense:
            if _vecs is not None:
                need_vec, ctx_vec = _vecs
            else:
                vecs = idx.embed_queries([text, f"{text}\n{context}" if context else text])
                need_vec, ctx_vec = vecs[0], vecs[1]
            for rank, (rid, _) in enumerate(idx.semantic(need_vec, k), 1):
                add(rid, rank, "semantic")

        if not fused:
            return []
        # Rerank: fused rank evidence + similarity to the need *in its
        # conversational context* + a small boost for the record kinds this
        # need kind is usually expressed with.
        max_fused = max(fused.values())
        sims = idx.similarity(ctx_vec, list(fused)) if idx.dense else {}
        affinity = KIND_AFFINITY.get(kind, set())
        scored = []
        for rid, value in fused.items():
            rec = idx.by_id[rid]
            score = 0.55 * (value / max_fused) + 0.45 * max(sims.get(rid, 0.0), 0.0)
            if rec["kind"] in affinity:
                score += 0.05
            scored.append((score, rid))
        scored.sort(reverse=True)
        exact_set = set(exact)
        out, kept = [], 0
        for score, rid in scored:
            is_exact = rid in exact_set
            if not is_exact and kept >= keep:
                continue
            if not is_exact:
                kept += 1
            rec = idx.by_id[rid]
            out.append({"id": rid, "symbol": rec["symbol"], "kind": rec["kind"], "score": round(score, 4),
                        "reasons": sorted(set(reasons[rid]))})
        return out

    # ------------------------------------------------------------------ step 4
    def expand(self, seed_ids: list, max_depth: int = 3) -> dict:
        """{record_id: why} for the seeds, every dependency (transitively, up
        to max_depth), every shared rule of anything included, every record a
        deprecated seed was superseded by, and the core rules."""
        idx = self.index
        why = {}

        def include(rid, reason):
            if rid in idx.by_id and rid not in why:
                why[rid] = reason
                return True
            return False

        frontier = []
        for rid in seed_ids:
            rec = idx.by_id.get(rid)
            if rec is None:
                continue
            if rec["status"] == "Deprecated":
                for sup in rec.get("superseded_by") or []:
                    if include(sup, f"replaces deprecated {rec['symbol']}"):
                        frontier.append(sup)
                continue
            if include(rid, "candidate"):
                frontier.append(rid)
        for depth in range(max_depth):
            nxt = []
            for rid in frontier:
                for dep in idx.by_id[rid].get("dependencies") or []:
                    if include(dep, f"dependency of {idx.by_id[rid]['symbol']}"):
                        nxt.append(dep)
            frontier = nxt
        # `related` is a migrator-curated "look at this too" edge: one hop,
        # never transitive, so it can't snowball the context.
        for rid in list(why):
            for rel in idx.by_id[rid].get("related") or []:
                include(rel, f"related to {idx.by_id[rid]['symbol']}")
        for rid in list(why):
            for rule in idx.by_id[rid].get("shared_rules") or []:
                include(rule, f"rule governing {idx.by_id[rid]['symbol']}")
        for rec in idx.all_records:
            if rec.get("core") and rec["status"] != "Deprecated":
                include(rec["id"], "core")
        return why

    # ------------------------------------------------------------------ pipeline
    def retrieve(self, content: str, needs: list = None, use_llm: bool = None, k: int = 15, keep: int = 12,
                 needs_method: str = "supplied") -> dict:
        use_llm = self.use_llm if use_llm is None else use_llm
        if needs is None:
            segments, needs, method = needs_mod.extract_needs(content, use_llm=use_llm)
        else:
            segments, method = needs_mod.segment(content), needs_method
            for i, need in enumerate(needs, 1):
                need.setdefault("id", f"n{i}")
                need.setdefault("context", needs_mod.turn_context(segments, need.get("source") or []))
        idx = self.index
        vecs = None
        if idx.dense and needs:
            queries = []
            for need in needs:
                queries += [need["text"], f"{need['text']}\n{need.get('context', '')}"]
            vecs = idx.embed_queries(queries)
        seeds = []
        for i, need in enumerate(needs):
            pair = (vecs[2 * i], vecs[2 * i + 1]) if vecs is not None else None
            need["candidates"] = self.search_need(need["text"], need.get("context", ""), need.get("kind", ""),
                                                  k=k, keep=keep, _vecs=pair)
            for c in need["candidates"]:
                if c["id"] not in seeds:
                    seeds.append(c["id"])
        included = self.expand(seeds)
        return {
            "glossary_sha": idx.glossary_sha,
            "needs_method": method,
            "segments": segments,
            "needs": needs,
            "records": [{"id": rid, "why": why} for rid, why in included.items()],
        }

    def widen(self, text: str, context: str = "", kind: str = "") -> dict:
        """Step 6: a deliberately broad search for an unresolved need — larger
        k, every content word on its own, and the records rules mention."""
        idx = self.index
        main = self.search_need(text, context, kind, k=40, keep=30)
        seen = {c["id"] for c in main}
        sub = []
        words = [w for w in re.findall(r"[^\W\d_]{4,}", text, re.UNICODE)][:12]
        for word in words:
            for c in self.search_need(word, "", kind, k=8, keep=5):
                if c["id"] not in seen:
                    seen.add(c["id"])
                    c["reasons"] = sorted(set(c["reasons"]) | {f"subterm:{word}"})
                    sub.append(c)
        mentioned = []
        for c in main[:10]:
            rec = idx.by_id[c["id"]]
            for rule in rec.get("shared_rules") or []:
                for m in idx.by_id.get(rule, {}).get("mentions") or []:
                    if m not in seen and m in idx.by_id:
                        seen.add(m)
                        mentioned.append({"id": m, "symbol": idx.by_id[m]["symbol"], "kind": idx.by_id[m]["kind"],
                                          "score": 0.0, "reasons": [f"mentioned by {rule}"]})
        return {"text": text, "candidates": main + sub + mentioned}

    def entry(self, key: str) -> dict:
        idx = self.index
        rec = idx.by_id.get(key) or idx.by_symbol.get(key)
        if rec is None:
            lowered = {s.lower(): r for s, r in idx.by_symbol.items()}
            rec = lowered.get(key.lower())
        if rec is None:
            return {}
        out = {"record": rec, "shared_rules": [idx.by_id[r] for r in rec.get("shared_rules") or [] if r in idx.by_id],
               "dependencies": [idx.by_id[d] for d in rec.get("dependencies") or [] if d in idx.by_id]}
        if rec.get("superseded_by"):
            out["superseded_by"] = [idx.by_id[s] for s in rec["superseded_by"] if s in idx.by_id]
        return out

    # ------------------------------------------------------------------ step 5
    def check(self, translation: str, needs: list) -> dict:
        """Compare a translation against the needs. A need counts as covered
        when one of its candidate symbols appears in the BrainCode, or the
        translator's coverage table names it as covered. Also reports
        identifiers in symbol positions that are not glossary symbols — an
        invented symbol is the commonest silent failure."""
        idx = self.index
        code = braincode_code(translation)
        code_nocomments = "\n".join(line.split("#", 1)[0] for line in code.splitlines())
        used_words = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", code_nocomments))
        used_symbols = sorted(w for w in used_words if w in idx.by_symbol)

        bound = set(BIND_RE.findall(code_nocomments))
        unknown_heads = sorted({h for h in CODE_HEAD_RE.findall(code_nocomments) if h not in idx.by_symbol})
        unbound_values = sorted({v for v in ATTR_VALUE_RE.findall(code_nocomments)
                                 if v not in idx.by_symbol and v not in bound and v not in GRAMMAR_WORDS
                                 and not re.match(r"^t\d+$", v)})
        deprecated = sorted(w for w in used_symbols if idx.by_symbol[w]["status"] == "Deprecated")

        coverage_rows = {}
        claimed_absent = {}
        for line in translation.splitlines():
            m = re.match(r"^\|\s*(n\d+)\s*\|(.*)\|\s*$", line.strip())
            if m:
                coverage_rows[m.group(1)] = m.group(2)
                cells = [c.strip() for c in m.group(2).split("|")]
                expressed = cells[1] if len(cells) >= 2 else ""
                for word in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expressed):
                    if word in idx.by_symbol and word not in used_words:
                        claimed_absent.setdefault(word, []).append(m.group(1))
        string_args = []
        for args in OP_STRING_ARG_RE.findall(code_nocomments):
            for name, literal in re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\"([^\"]*)\"", args):
                if name in ENTITY_ARGS and f'{name}="{literal}"' not in string_args:
                    string_args.append(f'{name}="{literal}"')
        results = []
        for need in needs:
            syms = [c["symbol"] for c in need.get("candidates") or []]
            hit = [s for s in syms if s in used_words]
            row = coverage_rows.get(need.get("id", ""), "")
            declared = bool(row) and not re.search(r"\bunresolved\b", row, re.I)
            status = "covered" if hit else ("declared" if declared else "unresolved")
            results.append({"id": need.get("id"), "kind": need.get("kind"), "text": need.get("text"),
                            "status": status, "matched_symbols": hit})
        return {
            "needs": results,
            "unresolved": [r["id"] for r in results if r["status"] == "unresolved"],
            "used_symbols": used_symbols,
            "unknown_symbols_in_head_position": unknown_heads,
            "unbound_attribute_values": unbound_values,
            "deprecated_symbols_used": deprecated,
            "claimed_but_absent": claimed_absent,
            "string_literals_as_operation_arguments": string_args,
        }


# ---------------------------------------------------------------------- text rendering

def _compact(rec: dict) -> str:
    import sys
    if str(index_mod.SWARM_DIR) not in sys.path:
        sys.path.insert(0, str(index_mod.SWARM_DIR))
    from glossary.render import compact_line
    return compact_line(rec)


def render_context(result: dict, retriever: Retriever, glossary_version: str = "") -> str:
    idx = retriever.index
    lines = [
        "# Glossary retrieval for this item",
        "",
        f"Glossary {glossary_version or ''} (sha {result['glossary_sha'][:12]}). "
        f"{len(result['needs'])} needs (decomposition: {result['needs_method']}), "
        f"{len(result['records'])} glossary records retrieved.",
        "",
        "Every need below must end up expressed in the translation, or listed as unresolved in the coverage table "
        "*after* widening the search (`node /kit/rag.mjs widen \"<need text>\"`). Candidates are ranked best first; "
        "`exact` means a symbol or alias phrase literally occurs in the need.",
        "",
        "## Needs and candidates",
        "",
        "| need | kind | source | meaning | candidates |",
        "|---|---|---|---|---|",
    ]
    for need in result["needs"]:
        cands = ", ".join(f"`{c['symbol']}`" + ("*" if "exact" in c["reasons"] else "")
                          for c in (need.get("candidates") or [])[:12]) or "—"
        src = ", ".join(need.get("source") or [])
        text = need["text"].replace("|", "/")
        lines.append(f"| {need['id']} | {need['kind']} | {src} | {text} | {cands} |")
    lines += ["", "(* = exact name/alias match)", "", "## Retrieved records", ""]

    included = {r["id"]: r["why"] for r in result["records"]}
    rules = [rid for rid in included if idx.by_id[rid]["kind"] in ("rule", "category_rule")]
    others = [rid for rid in included if rid not in rules]
    if rules:
        lines += ["### Shared rules that govern the records below (full text)", ""]
        for rid in sorted(rules, key=lambda r: (not idx.by_id[r].get("core"), idx.by_id[r]["symbol"])):
            rec = idx.by_id[rid]
            lines += [f"**{rec['symbol']}** ({rid}; {included[rid]})", "", rec["definition"].strip(), ""]
    order = ["operation", "speech_act", "constructor", "composite", "claim_relation", "link", "value",
             "attribute", "example"]
    for kind in order:
        group = [rid for rid in others if idx.by_id[rid]["kind"] == kind]
        if not group:
            continue
        lines += [f"### {kind.replace('_', ' ')}s", ""]
        for rid in sorted(group, key=lambda r: (idx.by_id[r].get("category", ""), idx.by_id[r]["symbol"])):
            rec = idx.by_id[rid]
            if kind == "example":
                lines += [f"- {rec['symbol']} ({included[rid]}): {rec['definition'].splitlines()[0]}", "",
                          "```braincode", rec.get("code") or "", "```", ""]
            else:
                lines.append(f"- {_compact(rec)}  ⟵ {included[rid]}")
        lines.append("")
    return "\n".join(lines)


def render_candidates(result: dict) -> str:
    lines = [f"# Candidates for: {result.get('text', '')}", ""]
    for c in result["candidates"]:
        lines.append(f"- `{c['symbol']}` ({c['kind']}, {c['score']}) — {', '.join(c['reasons'])}  [{c['id']}]")
    return "\n".join(lines)


def render_check(report: dict) -> str:
    lines = ["# Coverage check", ""]
    for r in report["needs"]:
        mark = {"covered": "OK ", "declared": "DECL", "unresolved": "MISS"}[r["status"]]
        lines.append(f"- [{mark}] {r['id']} ({r['kind']}): {r['text']}"
                     + (f" — via {', '.join(r['matched_symbols'])}" if r["matched_symbols"] else ""))
    lines.append("")
    if report["unresolved"]:
        lines.append(f"Unresolved: {', '.join(report['unresolved'])} — widen the search for each before declaring a gap.")
    for key, label in (("unknown_symbols_in_head_position", "Not glossary symbols (after ACTION/UTTER/TERM/CLAIM/LINK)"),
                       ("unbound_attribute_values", "Attribute values that are neither glossary symbols nor bound handles"),
                       ("deprecated_symbols_used", "Deprecated symbols used"),
                       ("string_literals_as_operation_arguments",
                        "Quoted strings where an operation expects a glossary entity (missing vocabulary?)")):
        if report.get(key):
            lines.append(f"{label}: {', '.join(report[key])}")
    if report.get("claimed_but_absent"):
        lines.append("Coverage table names symbols the BrainCode never uses: "
                     + ", ".join(f"{s} ({', '.join(n)})" for s, n in report["claimed_but_absent"].items()))
    return "\n".join(lines)


__all__ = ["Retriever", "render_context", "render_candidates", "render_check"]
