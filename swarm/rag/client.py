"""Python client for the RAG server, for host-side models and scripts.

    from rag.client import RagClient
    rag = RagClient()                       # http://127.0.0.1:$RAG_PORT
    ctx = rag.retrieve(item_content, format="text")
    rag.search("cheapest first", kind="constraint")
    rag.entry("pick_up")

`RagClient.local()` gives the same interface in-process, with no server.
"""
import json
import os
import urllib.error
import urllib.request
from urllib.parse import quote


class RagClient:
    def __init__(self, base_url: str = None, timeout: int = 300):
        port = os.environ.get("RAG_PORT", "8765")
        self.base_url = (base_url or os.environ.get("RAG_URL") or f"http://127.0.0.1:{port}").rstrip("/")
        self.timeout = timeout

    def _call(self, method, path, payload=None):
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(self.base_url + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = resp.read().decode("utf-8")
                ctype = resp.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"RAG {path}: HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}") from None
        return json.loads(body) if ctype.startswith("application/json") else body

    def health(self):
        return self._call("GET", "/health")

    def needs(self, content, use_llm=True, format=None):
        return self._call("POST", "/needs", {"content": content, "use_llm": use_llm, "format": format})

    def retrieve(self, content, needs=None, use_llm=None, format=None):
        return self._call("POST", "/retrieve", {"content": content, "needs": needs, "use_llm": use_llm, "format": format})

    def search(self, text, context="", kind="", k=15, keep=12, format=None):
        return self._call("POST", "/search", {"text": text, "context": context, "kind": kind, "k": k, "keep": keep,
                                              "format": format})

    def widen(self, text, context="", kind="", format=None):
        return self._call("POST", "/widen", {"text": text, "context": context, "kind": kind, "format": format})

    def entry(self, key):
        return self._call("GET", "/entry/" + quote(key, safe=""))

    def check(self, translation, needs, format=None):
        return self._call("POST", "/check", {"translation": translation, "needs": needs, "format": format})

    def reload(self):
        return self._call("POST", "/reload", {})

    @staticmethod
    def local(dense=True, use_llm=True):
        return LocalRag(dense=dense, use_llm=use_llm)


class LocalRag:
    """Same methods as RagClient, backed by an in-process Retriever."""

    def __init__(self, dense=True, use_llm=True):
        from .retrieve import Retriever
        self.retriever = Retriever(dense=dense, use_llm=use_llm)

    def retrieve(self, content, needs=None, use_llm=None, format=None):
        from .retrieve import render_context
        result = self.retriever.retrieve(content, needs=needs, use_llm=use_llm)
        return render_context(result, self.retriever) if format == "text" else result

    def search(self, text, context="", kind="", k=15, keep=12, format=None):
        from .retrieve import render_candidates
        result = {"text": text, "candidates": self.retriever.search_need(text, context, kind, k=k, keep=keep)}
        return render_candidates(result) if format == "text" else result

    def widen(self, text, context="", kind="", format=None):
        from .retrieve import render_candidates
        result = self.retriever.widen(text, context, kind)
        return render_candidates(result) if format == "text" else result

    def entry(self, key):
        return self.retriever.entry(key)

    def check(self, translation, needs, format=None):
        from .retrieve import render_check
        report = self.retriever.check(translation, needs)
        return render_check(report) if format == "text" else report

    def reload(self):
        return self.retriever.reload()
