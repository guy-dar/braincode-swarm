"""The derived search index over glossary records — and only glossary records.

Built from reference/glossary.jsonl; never edited by hand. Three channels:

- exact:   symbol / alias / id phrases -> records (a phrase found in the
           need text forces the record in, whatever the other channels say)
- keyword: BM25 over symbol words, aliases, definition, category, signature,
           expansion and contrast (`not`)
- dense:   fastembed multilingual sentence embeddings, one vector per record,
           cached by record text so a migration only re-embeds what changed

    python -m rag.cli build
"""
import hashlib
import json
import os
import re
import threading
import unicodedata
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi

SWARM_DIR = Path(__file__).resolve().parent.parent
INDEX_DIR = SWARM_DIR / "rag" / "index"
MODEL_DIR = SWARM_DIR / "rag" / "models"
DEFAULT_MODEL = os.environ.get("RAG_EMBED_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)
STOPWORDS = {
    "a", "an", "the", "of", "to", "in", "on", "for", "and", "or", "is", "are", "be", "it", "its",
    "this", "that", "with", "as", "by", "at", "from", "not", "no", "can", "may", "must", "any", "all",
    "i", "me", "my", "you", "your", "we", "our", "do", "does", "did", "have", "has", "was", "were",
    "will", "would", "should", "could", "if", "then", "than", "so", "but", "about", "into", "only",
}
# Aliases too short or too common to force a record in by exact match alone
# ("I", "me", "S", "14", "in"). They still count through BM25 and dense.
MIN_EXACT_ALIAS_CHARS = 3


def _stem(word: str) -> str:
    """Deliberately light suffix stripping — enough that "temples"/"temple"
    and "walking"/"walk" meet, without a dependency or aggressive conflation."""
    for suffix, min_len in (("ies", 5), ("ing", 6), ("ed", 5), ("es", 5), ("s", 4)):
        if word.endswith(suffix) and len(word) >= min_len:
            if suffix == "ies":
                return word[:-3] + "y"
            if suffix == "es" and not word.endswith(("ses", "xes", "ches", "shes")):
                return word[:-1]
            return word[: -len(suffix)]
    return word


def tokenize(text: str, keep_stopwords: bool = False) -> list:
    text = unicodedata.normalize("NFKC", str(text or "")).lower()
    words = WORD_RE.findall(text.replace("_", " "))
    return [_stem(w) for w in words if keep_stopwords or w not in STOPWORDS]


def phrase_key(text: str) -> tuple:
    return tuple(tokenize(text, keep_stopwords=True))


def record_search_text(record: dict) -> str:
    parts = [record["symbol"].replace("_", " "), " ".join(record.get("aliases") or []),
             record.get("category", "").replace("-", " "), record.get("kind", "").replace("_", " "),
             record.get("definition", ""), record.get("signature", ""), record.get("expansion", ""),
             record.get("not", "")]
    return "\n".join(p for p in parts if p)


def record_embed_text(record: dict) -> str:
    """Shorter than the BM25 text: what the record *means*, not its typing."""
    aliases = ", ".join(record.get("aliases") or [])
    head = record["symbol"].replace("_", " ")
    if aliases:
        head += f" ({aliases})"
    body = record.get("definition", "")
    if record.get("expansion"):
        body += " = " + record["expansion"]
    category = record.get("category") or record.get("kind", "")
    return f"{head}: {body} [{category}]"[:1200]


class Embedder:
    """Lazy, shared fastembed model. Loading costs a second or two (and a
    one-time ~200 MB download into rag/models/), so it happens once per process."""
    _lock = threading.Lock()
    _models = {}

    def __init__(self, model_name: str = DEFAULT_MODEL):
        self.model_name = model_name

    def _model(self):
        with Embedder._lock:
            if self.model_name not in Embedder._models:
                from fastembed import TextEmbedding
                MODEL_DIR.mkdir(parents=True, exist_ok=True)
                Embedder._models[self.model_name] = TextEmbedding(self.model_name, cache_dir=str(MODEL_DIR))
            return Embedder._models[self.model_name]

    def embed(self, texts: list) -> np.ndarray:
        if not texts:
            return np.zeros((0, 1), dtype=np.float32)
        model = self._model()
        with Embedder._lock:  # onnxruntime sessions are not reliably re-entrant across threads
            vectors = np.array(list(model.embed(list(texts))), dtype=np.float32)
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return vectors / norms


class GlossaryIndex:
    """In-memory index. `dense=False` gives a keyword+exact-only index (tests,
    or hosts that can't run the embedding model)."""

    def __init__(self, records: list, dense: bool = True, model_name: str = DEFAULT_MODEL,
                 index_dir: Path = INDEX_DIR, glossary_sha: str = ""):
        self.all_records = records
        self.by_id = {r["id"]: r for r in records}
        self.by_symbol = {r["symbol"]: r for r in records}
        # Deprecated records stay resolvable by `entry` but are never offered
        # as candidates; structural grammar tokens are documented by the spec.
        self.records = [r for r in records if r["status"] != "Deprecated" and r["kind"] != "structural"]
        self.ids = [r["id"] for r in self.records]
        self.position = {rid: i for i, rid in enumerate(self.ids)}
        self.glossary_sha = glossary_sha

        self.doc_tokens = [tokenize(record_search_text(r)) for r in self.records]
        self.bm25 = BM25Okapi(self.doc_tokens) if self.records else None

        self.phrases = {}
        for r in self.records:
            for phrase in [r["symbol"], r["symbol"].replace("_", " "), *(r.get("aliases") or [])]:
                if len(phrase.strip()) < MIN_EXACT_ALIAS_CHARS:
                    continue
                key = phrase_key(phrase)
                if not key or (len(key) == 1 and key[0] in STOPWORDS):
                    continue
                self.phrases.setdefault(key, set()).add(r["id"])
        self.max_phrase_len = max((len(k) for k in self.phrases), default=1)

        self.dense = dense
        self.embedder = Embedder(model_name) if dense else None
        self.vectors = self._load_or_embed(index_dir) if dense else None

    # ------------------------------------------------------------------ build/persist
    def _load_or_embed(self, index_dir: Path) -> np.ndarray:
        texts = [record_embed_text(r) for r in self.records]
        hashes = [hashlib.sha1((self.embedder.model_name + "\0" + t).encode("utf-8")).hexdigest() for t in texts]
        cache_path = index_dir / "embeddings.npz"
        cached = {}
        if cache_path.exists():
            try:
                data = np.load(cache_path, allow_pickle=False)
                cached = dict(zip(data["hashes"].tolist(), data["vectors"]))
            except Exception:
                cached = {}
        missing = [i for i, h in enumerate(hashes) if h not in cached]
        if missing:
            fresh = self.embedder.embed([texts[i] for i in missing])
            for i, vec in zip(missing, fresh):
                cached[hashes[i]] = vec
        vectors = np.stack([cached[h] for h in hashes]) if hashes else np.zeros((0, 1), dtype=np.float32)
        index_dir.mkdir(parents=True, exist_ok=True)
        np.savez(cache_path, hashes=np.array(hashes), vectors=vectors)
        (index_dir / "manifest.json").write_text(json.dumps({
            "glossary_sha": self.glossary_sha, "records_indexed": len(self.records),
            "records_total": len(self.all_records), "model": self.embedder.model_name,
            "re_embedded": len(missing),
        }, indent=2), encoding="utf-8")
        return vectors

    # ------------------------------------------------------------------ channels
    def exact(self, text: str) -> list:
        """Record ids whose symbol/alias phrase occurs in the text, plus any
        `backticked` or literal symbol named outright."""
        tokens = tokenize(text, keep_stopwords=True)
        hits = []
        for n in range(min(self.max_phrase_len, len(tokens)), 0, -1):
            for i in range(len(tokens) - n + 1):
                for rid in self.phrases.get(tuple(tokens[i:i + n]), ()):
                    if rid not in hits:
                        hits.append(rid)
        for word in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", text):
            rec = self.by_symbol.get(word)
            if rec and rec["id"] in self.position and rec["id"] not in hits and len(word) >= MIN_EXACT_ALIAS_CHARS:
                hits.append(rec["id"])
        return hits

    def keyword(self, text: str, k: int) -> list:
        tokens = tokenize(text)
        if not tokens or self.bm25 is None:
            return []
        scores = self.bm25.get_scores(tokens)
        order = np.argsort(-scores)[:k]
        return [(self.ids[i], float(scores[i])) for i in order if scores[i] > 0]

    def embed_queries(self, texts: list) -> np.ndarray:
        return self.embedder.embed(texts) if self.dense else None

    def semantic(self, query_vec, k: int) -> list:
        if not self.dense or query_vec is None or self.vectors is None or not len(self.vectors):
            return []
        sims = self.vectors @ query_vec
        order = np.argsort(-sims)[:k]
        return [(self.ids[i], float(sims[i])) for i in order]

    def similarity(self, query_vec, rids: list) -> dict:
        if not self.dense or query_vec is None:
            return {}
        return {rid: float(self.vectors[self.position[rid]] @ query_vec) for rid in rids if rid in self.position}


def load_records(path: Path = None):
    import sys
    if str(SWARM_DIR) not in sys.path:
        sys.path.insert(0, str(SWARM_DIR))
    from glossary import records as rec_mod
    path = Path(path) if path else rec_mod.GLOSSARY_JSONL
    return rec_mod.load(path), hashlib.sha256(path.read_bytes()).hexdigest()


def build(dense: bool = True, glossary_path: Path = None, index_dir: Path = INDEX_DIR) -> GlossaryIndex:
    records, sha = load_records(glossary_path)
    return GlossaryIndex(records, dense=dense, index_dir=index_dir, glossary_sha=sha)


def is_stale(glossary_path: Path = None, index_dir: Path = INDEX_DIR) -> bool:
    _, sha = load_records(glossary_path)
    manifest = index_dir / "manifest.json"
    if not manifest.exists():
        return True
    try:
        return json.loads(manifest.read_text(encoding="utf-8")).get("glossary_sha") != sha
    except ValueError:
        return True


def rrf(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank)


__all__ = ["GlossaryIndex", "Embedder", "build", "is_stale", "tokenize", "rrf", "load_records"]
