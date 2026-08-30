"""Real end-to-end check of the naming pipeline against the actual model API
— no mocks. Everything else in this test suite mocks litellm.completion, which
proves the code's logic but never proves the real model actually cooperates
with generate_slug's prompt/token-budget setup (e.g. that the reasoning-budget
bug documented in utils.py stays fixed). This file is what actually exercises
that.

Costs real tokens and a real network call, so it's excluded from the default
`pytest tests/` run (see pytest.ini's `addopts`) regardless of whether
credentials happen to be configured. Run it explicitly with:
    python3 -m pytest tests/ -m integration -v
Skips itself (rather than erroring) if PROXY_API_KEY isn't available (env or
swarm/.env), so it's still safe to run in an environment with no credentials.
"""
import os
import re

import pytest

import utils
from spawn_batch import SELF_DIR, load_dotenv

load_dotenv(SELF_DIR / ".env")

API_KEY = os.environ.get("PROXY_API_KEY")
BASE_URL = os.environ.get("PROXY_BASE_URL", "https://vertex-proxy-v26q.onrender.com/v1")
MODEL = os.environ.get("SWARM_MODEL", "vertex-proxy/gemini-flash")

pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not API_KEY, reason="requires a real PROXY_API_KEY (env or swarm/.env)"),
]


def test_real_model_call_produces_a_usable_folder_name():
    record_line = (
        '{"messages": [{"role": "user", "content": "What is 2 + 2?"}, '
        '{"role": "assistant", "content": "4"}]}'
    )

    full_hash = utils.content_hash(record_line)
    slug = utils.generate_slug(record_line, MODEL, API_KEY, BASE_URL)

    # "example" is generate_slug's silent-failure fallback — seeing it here
    # means the real call failed (bad credentials, reasoning-budget exhaustion,
    # timeout, ...), which is exactly the failure mode this test exists to
    # catch, so fail loudly instead of accepting a fallback as a pass.
    assert slug != "example", "generate_slug fell back — the real model call failed"
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug)

    name = utils.build_folder_name(full_hash, slug)
    assert name == f"{full_hash[:6]}-{slug}"
    assert len(name.split("-", 1)[0]) == 6
