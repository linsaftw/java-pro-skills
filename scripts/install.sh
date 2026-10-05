#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "${1:-}" == "--user" ]]; then
  DEST="${HOME}/.claude/skills"
elif [[ "${1:-}" == "--project" && -n "${2:-}" ]]; then
  DEST="${2%/}/.claude/skills"
else
  echo "usage: $0 --user | --project /path/to/project" >&2
  exit 2
fi
mkdir -p "$DEST"
for d in "$ROOT"/plugins/java-pro-skills/skills/*; do
  [[ -d "$d" ]] || continue
  name="$(basename "$d")"
  rm -rf "$DEST/$name"
  cp -R "$d" "$DEST/$name"
done
echo "Installed skills to $DEST"
