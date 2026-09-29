#!/usr/bin/env bash
# Install the writing toolkit into an existing or new paper project.
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <paper-project-directory>" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="$1"
mkdir -p "$TARGET"
TARGET="$(cd "$TARGET" && pwd)"
if [ "$TARGET" = "$ROOT" ]; then
  echo "choose a separate paper-project directory" >&2
  exit 2
fi

mkdir -p "$TARGET/.paper-writing" "$TARGET/.claude/agents" \
  "$TARGET/.claude/skills" "$TARGET/.claude/commands" "$TARGET/paper"

for dir in agents skills commands templates figures references scripts papercheck; do
  if [ ! -e "$TARGET/.paper-writing/$dir" ]; then
    cp -R "$ROOT/$dir" "$TARGET/.paper-writing/$dir"
  fi
done

# Root-level links keep paths in the copied skills and LaTeX template usable.
for dir in skills templates figures references scripts papercheck; do
  if [ ! -e "$TARGET/$dir" ] && [ ! -L "$TARGET/$dir" ]; then
    ln -s ".paper-writing/$dir" "$TARGET/$dir"
  fi
done

for kind in agents skills commands; do
  for source in "$ROOT/$kind"/*; do
    [ -e "$source" ] || continue
    name="$(basename "$source")"
    if [ ! -e "$TARGET/.claude/$kind/$name" ] && [ ! -L "$TARGET/.claude/$kind/$name" ]; then
      ln -s "../../.paper-writing/$kind/$name" "$TARGET/.claude/$kind/$name"
    fi
  done
done

for source in "$ROOT/templates/blackboard"/*.md; do
  name="$(basename "$source")"
  if [ ! -e "$TARGET/$name" ]; then cp "$source" "$TARGET/$name"; fi
done
if [ -z "$(find "$TARGET/paper" -mindepth 1 -maxdepth 1 -print -quit)" ]; then
  cp -R "$ROOT/templates/paper/." "$TARGET/paper/"
fi
if [ ! -e "$TARGET/AGENTS.md" ]; then cp "$ROOT/templates/project/AGENTS.md" "$TARGET/AGENTS.md"; fi

echo "Writing toolkit installed in $TARGET"
echo "Open $TARGET/STATE.md and paper/README.md to begin."
