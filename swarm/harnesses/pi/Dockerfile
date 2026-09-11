# No official Pi image exists (unlike opencode's ghcr.io/anomalyco/opencode) —
# this builds one. Pi ships as a bundled JS CLI (needs Node >=22.19.0 present at
# runtime), not a compiled standalone binary, so the base image matters here in
# a way it didn't for opencode.
FROM node:24-bookworm-slim

# Pinned: unpinned once silently picked up a release that started sending
# `store` on every openai-completions request (compat.supportsStore), which
# vertex_ai hard-rejects with a 400 — broke every record with no code change
# on our side. Bump deliberately, not by a cache miss.
RUN npm install -g --ignore-scripts @earendil-works/pi-coding-agent@0.85.1

# Non-root is enforced at `docker run --user` time (see spawn_batch.py), matching
# the host UID so the writable /output mount just works.
RUN mkdir -p /workspace && chmod 777 /workspace
WORKDIR /workspace

COPY --chmod=644 models.template.json /opt/models.template.json
COPY --chmod=644 settings.json /opt/settings.json
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
