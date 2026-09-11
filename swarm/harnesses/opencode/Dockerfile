# Thin wrapper over the official image — adds our provider config and an
# entrypoint that knows this harness's exact CLI invocation, so the host side
# (spawn_batch.py) never needs to know it. Everything opencode-specific lives
# here; spawn_batch.py's `docker run` is identical across every harness.
FROM ghcr.io/anomalyco/opencode

# The config must NOT live under /reference: spawn_batch.py mounts the host's
# reference/ directory there, and a directory mount replaces the directory and
# everything in it. It used to work only because the mount was a single file
# (reference/DESIGN_DOC.md), so the sibling config survived; when that became a
# whole-directory mount the config vanished and every model failed to resolve.
# /opt is not mounted by anything, and the entrypoint points opencode at it
# explicitly rather than relying on config discovery.
#
# `RUN mkdir` first, deliberately: COPY --chmod applies its mode to an
# auto-created parent directory too, and 644 on a directory strips the
# execute/traverse bit, silently making everything inside unreadable to a
# non-root user (found the hard way — root doesn't hit this, non-root does).
RUN mkdir -p /opt
COPY --chmod=644 config.jsonc /opt/opencode.jsonc
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
