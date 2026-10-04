"""HTTP access to the glossary RAG, so any model — a translator inside a
container (through kit/rag.mjs), the migrator, or a future role — queries
the same index the same way.

Endpoints (JSON in, JSON out; add `"format": "text"` to get the rendered text
a model would read instead):

  GET  /health
  POST /needs     {content}                          -> segments + needs (step 1)
  POST /retrieve  {content, needs?, use_llm?}         -> needs + candidates + expanded records (steps 1-4)
  POST /search    {text | queries[], context?, kind?, k?, keep?}  -> candidates per need (steps 2-3)
  POST /widen     {text, context?, kind?}             -> broad candidates for an unresolved need (step 6)
  GET  /entry/<symbol-or-id>                         -> full record + its rules and dependencies
  POST /entries   {keys[]}                           -> several records, compact (format=text)
  POST /check     {translation, needs}                -> coverage of needs by a translation (step 5)
  POST /reload                                       -> rebuild from the current glossary.jsonl

    python -m rag.cli serve [--port 8765] [--host 0.0.0.0]
"""
import json
import sys
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

from . import needs as needs_mod
from .retrieve import Retriever, render_candidates, render_check, render_context


def _glossary_version():
    try:
        from glossary import manifest
        return manifest.current_version()
    except Exception:
        return ""


def render_entries(found: dict) -> str:
    """Compact text for entry lookups: each record on one line, plus the
    names (not texts) of its rules and its dependencies on one line each.
    Rule texts are already in the translator's attached context."""
    from glossary.render import compact_line
    lines = []
    for key, data in found.items():
        if not data:
            lines.append(f"- {key}: no such glossary record")
            continue
        rec = data["record"]
        lines.append(f"- {compact_line(rec)}  [{rec['id']}]")
        if data.get("shared_rules"):
            lines.append("    rules: " + ", ".join(r["symbol"] for r in data["shared_rules"]))
        for dep in data.get("dependencies") or []:
            lines.append(f"    depends on: {compact_line(dep)}")
        for sup in data.get("superseded_by") or []:
            lines.append(f"    replaced by: {compact_line(sup)}")
    return "\n".join(lines)


def make_handler(retriever: Retriever):
    class Handler(BaseHTTPRequestHandler):
        server_version = "BrainCodeRAG/1"

        def log_message(self, fmt, *args):  # quiet: the loop has its own logging
            pass

        def _send(self, status, payload, text=None):
            body = (text if text is not None else json.dumps(payload, ensure_ascii=False)).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "text/plain; charset=utf-8" if text is not None else "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _body(self):
            length = int(self.headers.get("Content-Length") or 0)
            if not length:
                return {}
            return json.loads(self.rfile.read(length).decode("utf-8"))

        def do_GET(self):
            try:
                if self.path == "/health":
                    idx = retriever.index
                    return self._send(200, {"ok": True, "records": len(idx.records), "dense": idx.dense,
                                            "glossary_sha": idx.glossary_sha, "glossary_version": _glossary_version()})
                if self.path.startswith("/entry/"):
                    key = unquote(self.path[len("/entry/"):].split("?", 1)[0])
                    found = retriever.entry(key)
                    if not found:
                        return self._send(404, {"error": f"no glossary record {key!r}"})
                    return self._send(200, found)
                self._send(404, {"error": "unknown path"})
            except Exception as e:
                self._send(500, {"error": f"{type(e).__name__}: {e}"})

        def do_POST(self):
            try:
                req = self._body()
                as_text = req.get("format") == "text"
                if self.path == "/needs":
                    segments, needs, method = needs_mod.extract_needs(req.get("content", ""),
                                                                      use_llm=req.get("use_llm", True))
                    payload = {"method": method, "needs": needs, "numbered": needs_mod.numbered_text(segments)}
                    return self._send(200, payload, json.dumps(needs, indent=1, ensure_ascii=False) if as_text else None)
                if self.path == "/retrieve":
                    result = retriever.retrieve(req.get("content", ""), needs=req.get("needs"),
                                                use_llm=req.get("use_llm"))
                    text = render_context(result, retriever, _glossary_version()) if as_text else None
                    return self._send(200, result, text)
                if self.path == "/search":
                    # Several needs in one call ("queries"): one round trip
                    # for the model instead of one per lookup.
                    queries = req.get("queries") or [req.get("text", "")]
                    results = [{"text": q, "candidates": retriever.search_need(
                        q, req.get("context", ""), req.get("kind", ""), k=int(req.get("k", 15)),
                        keep=int(req.get("keep", 12)))} for q in queries]
                    payload = results[0] if len(results) == 1 else {"results": results}
                    text = "\n\n".join(render_candidates(r) for r in results) if as_text else None
                    return self._send(200, payload, text)
                if self.path == "/entries":
                    found = {key: retriever.entry(key) for key in req.get("keys") or []}
                    if as_text:
                        return self._send(200, None, render_entries(found))
                    return self._send(200, found)
                if self.path == "/widen":
                    result = retriever.widen(req.get("text", ""), req.get("context", ""), req.get("kind", ""))
                    return self._send(200, result, render_candidates(result) if as_text else None)
                if self.path == "/check":
                    report = retriever.check(req.get("translation", ""), req.get("needs") or [])
                    return self._send(200, report, render_check(report) if as_text else None)
                if self.path == "/reload":
                    return self._send(200, retriever.reload())
                self._send(404, {"error": "unknown path"})
            except Exception as e:
                traceback.print_exc(file=sys.stderr)
                self._send(500, {"error": f"{type(e).__name__}: {e}"})

    return Handler


class RagServer:
    """A server running in a daemon thread — how the loop hosts it, sharing
    its own Retriever so a reindex after migration is visible immediately."""

    def __init__(self, retriever: Retriever, host: str = "0.0.0.0", port: int = 8765):
        self.retriever = retriever
        self.httpd = ThreadingHTTPServer((host, port), make_handler(retriever))
        self.httpd.daemon_threads = True
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True, name="rag-server")

    def start(self):
        self.thread.start()
        return self

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()

    def serve_forever(self):
        self.httpd.serve_forever()
