# No official Pi image exists (unlike opencode's ghcr.io/anomalyco/opencode) —
# this builds one. Pi ships as a bundled JS CLI (needs Node >=22.19.0 present at
# runtime), not a compiled standalone binary, so the base image matters here in
# a way it didn't for opencode.
FROM node:24-bookworm-slim

RUN npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# Non-root is enforced at `docker run --user` time (see spawn_batch.py), matching
# the host UID so the writable /output mount just works.
RUN mkdir -p /workspace && chmod 777 /workspace
WORKDIR /workspace

COPY --chmod=644 models.template.json /opt/models.template.json
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
