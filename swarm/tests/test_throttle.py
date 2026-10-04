"""The throttle gateway: forwarding, the in-flight limit, and adaptation to rejections."""
import json
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import throttle


class FakeUpstream:
    """Answers POST /v1/chat/completions; the first `reject` calls get 429."""

    def __init__(self, reject=0, delay=0.0):
        self.reject, self.delay = reject, delay
        self.lock = threading.Lock()
        self.calls = self.inflight = self.peak = 0
        outer = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                self.rfile.read(int(self.headers.get("Content-Length") or 0))
                with outer.lock:
                    outer.calls += 1
                    n = outer.calls
                    outer.inflight += 1
                    outer.peak = max(outer.peak, outer.inflight)
                time.sleep(outer.delay)
                with outer.lock:
                    outer.inflight -= 1
                status = 429 if n <= outer.reject else 200
                body = json.dumps({"path": self.path, "n": n}).encode()
                self.send_response(status)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}/v1"


def _call(port):
    req = urllib.request.Request(f"http://127.0.0.1:{port}/v1/chat/completions", data=b"{}", method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, None


def _server(upstream, gate):
    s = throttle.ThrottleServer(upstream.url, "127.0.0.1", 0, gate).start()
    return s, s.httpd.server_address[1]


def test_forwards_path_and_body():
    up = FakeUpstream()
    s, port = _server(up, throttle.Gate(max_inflight=2))
    status, body = _call(port)
    assert status == 200 and body["path"] == "/v1/chat/completions"
    s.stop()


def test_inflight_limit_is_enforced():
    up = FakeUpstream(delay=0.3)
    s, port = _server(up, throttle.Gate(max_inflight=2))
    threads = [threading.Thread(target=_call, args=(port,)) for _ in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert up.calls == 6 and up.peak <= 2
    s.stop()


def test_rejection_passes_through_and_cools_down():
    up = FakeUpstream(reject=1)
    gate = throttle.Gate(max_inflight=4, min_inflight=2, cooldown_s=0.5)
    s, port = _server(up, gate)
    assert _call(port)[0] == 429           # passed back unchanged, not retried
    # The response reaches the client just before the gateway records the
    # rejection (release() runs after the body is sent): wait for it to settle.
    deadline = time.monotonic() + 2
    while gate.snapshot()["inflight"] and time.monotonic() < deadline:
        time.sleep(0.01)
    assert up.calls == 1 and gate.limit == 3
    started = time.monotonic()
    assert _call(port)[0] == 200           # waits out the cooldown first
    assert time.monotonic() - started >= 0.4
    assert gate.snapshot()["rejected"] == 1
    s.stop()


def test_limit_recovers_after_successes():
    gate = throttle.Gate(max_inflight=3, min_inflight=1, raise_after=2, cooldown_s=0.01)
    gate.acquire(); gate.release(rejected=True)
    assert gate.limit == 2
    time.sleep(0.02)
    for _ in range(2):
        gate.acquire(); gate.release(rejected=False)
    assert gate.limit == 3
