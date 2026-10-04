#!/bin/sh
# Installed as grep and find (see Dockerfile), ahead of the real binaries on
# PATH. Agents may only search the paths mounted for them: the allowlist and
# the argument parsing live in guard-search.mjs. A recursive search of the
# whole filesystem (`grep -rn X /`) never finishes in a container and once
# burned a translator's entire time budget twice in one batch.
name="$(basename "$0")"
real="/usr/bin/$name"
[ -x "$real" ] || real="/bin/$name"
exec node /usr/local/lib/guard-search.mjs "$name" "$real" "$@"
