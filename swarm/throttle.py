#!/usr/bin/env python3
"""A local gateway in front of the model proxy that spaces calls out.

Every model call of the loop (translators, migration agents, need
extraction) goes through it. It bounds how many calls are in flight at once
(independently of how many containers run: an agent over the limit just
waits for a slot), and adapts that bound to what the proxy tolerates:

- a 429/503 from upstream starts a cooldown (no new call starts until it
  ends; 15 s, doubling per consecutive rejection, up to 120 s) and lowers the
  in-flight limit by one (not below THROTTLE_MIN);
- every THROTTLE_RAISE_AFTER successes in a row raise it by one again, up to
  THROTTLE_CONCURRENCY.

It never retries: a rejected call is passed back to the caller unchanged
(pi's own retry policy applies as before). Responses are streamed through as
they arrive, so streamed completions keep streaming.

    python throttle.py --upstream https://…/v1 --port 8766     # standalone
"""
import argparse
import http.client
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

HOP_BY_HOP = {"connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te", "trailer",
              "transfer-encoding", "upgrade", "content-length", "host"}
REJECT_STATUSES = {429, 502, 503, 504}


class Gate:
    """Adaptive in-flight limit + shared cooldown."""

    def __init__(self, max_inflight: int = 6, min_inflight: int = 2, raise_after: int = 20,
                 cooldown_s: float = 15.0, max_cooldown_s: float = 120.0):
        self.max_inflight = max(1, max_inflight)
        self.min_inflight = max(1, min(min_inflight, self.max_inflight))
        self.limit = self.max_inflight
        self.raise_after = raise_after
        self.base_cooldown = cooldown_s
        self.max_cooldown = max_cooldown_s
        self.cond = threading.Condition()
        self.inflight = 0
        self.cooldown_until = 0.0
        self.next_cooldown = cooldown_s
        self.streak = 0
        self.stats = {"calls": 0, "rejected": 0, "waited_s": 0.0, "cooldowns": 0, "min_limit_seen": self.limit}

    def acquire(self):
        started = time.monotonic()
        with self.cond:
            while True:
                now = time.monotonic()
                if now < self.cooldown_until:
                    self.cond.wait(self.cooldown_until - now)
                    continue
                if self.inflight < self.limit:
                    self.inflight += 1
                    self.stats["calls"] += 1
                    self.stats["waited_s"] += time.monotonic() - started
                    return
                self.cond.wait(1.0)

    def release(self, rejected: bool):
        with self.cond:
            self.inflight -= 1
            if rejected:
                self.stats["rejected"] += 1
                self.streak = 0
                now = time.monotonic()
                if now >= self.cooldown_until:   # one cooldown per burst, not per rejected call
                    self.cooldown_until = now + self.next_cooldown
                    self.next_cooldown = min(self.next_cooldown * 2, self.max_cooldown)
                    self.stats["cooldowns"] += 1
                    self.limit = max(self.min_inflight, self.limit - 1)
                    self.stats["min_limit_seen"] = min(self.stats["min_limit_seen"], self.limit)
            else:
                self.streak += 1
                self.next_cooldown = self.base_cooldown
                if self.streak >= self.raise_after and self.limit < self.max_inflight:
                    self.limit += 1
                    self.streak = 0
            self.cond.notify_all()

    def snapshot(self) -> dict:
        with self.cond:
            return {**self.stats, "waited_s": round(self.stats["waited_s"], 1), "limit": self.limit,
                    "inflight": self.inflight, "cooling_s": round(max(0.0, self.cooldown_until - time.monotonic()), 1)}


def make_handler(upstream: str, gate: Gate):
    up = urlsplit(upstream.rstrip("/"))
    base_path = up.path  # e.g. /v1
    conn_cls = http.client.HTTPSConnection if up.scheme == "https" else http.client.HTTPConnection

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"   # close after each response: no chunked re-encoding needed

        def log_message(self, fmt, *args):
            pass

        def _forward(self):
            if self.path == "/throttle/stats":
                body = __import__("json").dumps(gate.snapshot()).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(body)
                return
            length = int(self.headers.get("Content-Length") or 0)
            body = self.rfile.read(length) if length else None
            # Callers use http://<throttle>/v1/...; map /v1 onto the upstream's base path.
            path = base_path + (self.path[len("/v1"):] if self.path.startswith("/v1") else self.path)
            headers = {k: v for k, v in self.headers.items() if k.lower() not in HOP_BY_HOP}
            headers["Host"] = up.netloc
            gate.acquire()
            rejected = False
            try:
                conn = conn_cls(up.netloc, timeout=900)
                conn.request(self.command, path, body=body, headers=headers)
                resp = conn.getresponse()
                rejected = resp.status in REJECT_STATUSES
                self.send_response(resp.status, resp.reason)
                for k, v in resp.getheaders():
                    if k.lower() not in HOP_BY_HOP:
                        self.send_header(k, v)
                self.send_header("Connection", "close")
                self.end_headers()
                while True:
                    chunk = resp.read1(65536) if hasattr(resp, "read1") else resp.read(65536)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    self.wfile.flush()
                conn.close()
            except (ConnectionError, OSError, http.client.HTTPException) as e:
                rejected = True
                try:
                    self.send_response(502, "Bad Gateway")
                    self.end_headers()
                    self.wfile.write(f"throttle: upstream error: {e}".encode())
                except OSError:
                    pass
            finally:
                gate.release(rejected)

        do_GET = do_POST = do_PUT = do_DELETE = _forward

    return Handler


class ThrottleServer:
    def __init__(self, upstream: str, host: str = "0.0.0.0", port: int = 8766, gate: Gate = None):
        self.gate = gate or Gate()
        self.httpd = ThreadingHTTPServer((host, port), make_handler(upstream, self.gate))
        self.httpd.daemon_threads = True
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True, name="throttle")

    def start(self):
        self.thread.start()
        return self

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()


def gate_from_env() -> Gate:
    return Gate(max_inflight=int(os.environ.get("THROTTLE_CONCURRENCY", "6")),
                min_inflight=int(os.environ.get("THROTTLE_MIN", "2")),
                raise_after=int(os.environ.get("THROTTLE_RAISE_AFTER", "20")))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--upstream", required=True)
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=8766)
    args = p.parse_args(argv)
    server = ThrottleServer(args.upstream, args.host, args.port, gate_from_env())
    print(f"throttle on {args.host}:{args.port} -> {args.upstream}", file=sys.stderr)
    server.httpd.serve_forever()


if __name__ == "__main__":
    main()
