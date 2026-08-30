# Thin wrapper over the official image — adds our provider config and an
# entrypoint that knows this harness's exact CLI invocation, so the host side
# (spawn_batch.py) never needs to know it. Everything opencode-specific lives
# here; spawn_batch.py's `docker run` is identical across every harness.
FROM ghcr.io/anomalyco/opencode

# `RUN mkdir` first, deliberately: COPY --chmod applies its mode to an
# auto-created parent directory too, and 644 on a directory strips the
# execute/traverse bit, silently making everything inside unreadable to a
# non-root user (found the hard way — root doesn't hit this, non-root does).
RUN mkdir -p /reference
COPY --chmod=644 config.jsonc /reference/opencode.jsonc
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
