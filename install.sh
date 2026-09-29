#!/usr/bin/env bash
# Register local Codex skills, or install writing assets into a paper project.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd -P)"

register_skills() {
  local source_dir="$1" registration_dir="$2" link_prefix="$3"
  local source name link expected
  mkdir -p "$registration_dir"
  for source in "$source_dir"/*; do
    [ -f "$source/SKILL.md" ] || continue
    name="$(basename "$source")"
    link="$registration_dir/$name"
    expected="$link_prefix/$name"
    if [ ! -e "$link" ] && [ ! -L "$link" ]; then
      ln -s "$expected" "$link"
    elif [ ! -L "$link" ] || [ "$(readlink "$link")" != "$expected" ]; then
      echo "Kept existing Codex skill: $registration_dir/$name"
    fi
  done
}

if [ "${1:-}" = "--user" ] && [ "$#" -le 2 ]; then
  SKILL_DEST="${2:-$HOME/.agents/skills}"
  register_skills "$ROOT/skills" "$SKILL_DEST" "$ROOT/skills"
  echo "Codex user skills registered in $SKILL_DEST"
  echo "Skill links use this checkout: $ROOT"
  echo 'Start a new Codex turn and use $cpw-init to prepare a paper project.'
  exit 0
fi

if [ "$#" -ne 1 ] || [ "${1:-}" = "--user" ]; then
  echo "usage: $0 <paper-project-directory> | --user [skills-directory]" >&2
  exit 2
fi

TARGET="$1"
mkdir -p "$TARGET"
TARGET="$(cd "$TARGET" && pwd -P)"
case "$TARGET/" in
  "$ROOT/"*)
    echo "choose a paper-project directory outside the toolkit" >&2
    exit 2
    ;;
esac

# Registration is project-local. Individual skill links can be customized, but
# symlinked registration/asset roots could write into unrelated configuration.
for registration_dir in "$TARGET/.agents" "$TARGET/.agents/skills" "$TARGET/.paper-writing"; do
  if [ -L "$registration_dir" ]; then
    echo "use a project-local directory instead of a symlink: $registration_dir" >&2
    exit 2
  fi
done

mkdir -p "$TARGET/.paper-writing" "$TARGET/.agents/skills" "$TARGET/paper"

# Add missing resources without replacing customized files or following target
# symlinks. This also supplies new skill folders to an older installation.
copy_missing() {
  local source_path="$1" target_path="$2" child_path
  if [ -e "$target_path" ] || [ -L "$target_path" ]; then
    if [ -d "$source_path" ] && [ ! -L "$source_path" ] && \
       [ -d "$target_path" ] && [ ! -L "$target_path" ]; then
      for child_path in "$source_path"/* "$source_path"/.[!.]* "$source_path"/..?*; do
        [ -e "$child_path" ] || [ -L "$child_path" ] || continue
        copy_missing "$child_path" "$target_path/$(basename "$child_path")"
      done
    fi
  else
    cp -R "$source_path" "$target_path"
  fi
}

for dir in skills templates figures references scripts papercheck docs; do
  copy_missing "$ROOT/$dir" "$TARGET/.paper-writing/$dir"
done

# Keep reusable assets and their documentation in one namespace. Project folders
# named scripts/, skills/, etc. are unrelated to the installed toolkit.
for name in README.md SPEC.md SOURCE.md LICENSE .gitignore; do
  if [ ! -e "$TARGET/.paper-writing/$name" ] && [ ! -L "$TARGET/.paper-writing/$name" ]; then
    cp "$ROOT/$name" "$TARGET/.paper-writing/$name"
  fi
done

register_skills "$TARGET/.paper-writing/skills" "$TARGET/.agents/skills" "../../.paper-writing/skills"

# Retire only links created by the previous installer. Preserve custom entries
# and do not traverse a user-supplied symlink to another configuration directory.
if [ -d "$TARGET/.claude" ] && [ ! -L "$TARGET/.claude" ]; then
  for kind in agents skills commands; do
    legacy_dir="$TARGET/.claude/$kind"
    [ -d "$legacy_dir" ] && [ ! -L "$legacy_dir" ] || continue
    for link in "$legacy_dir"/*; do
      [ -L "$link" ] || continue
      name="$(basename "$link")"
      if [ "$(readlink "$link")" = "../../.paper-writing/$kind/$name" ]; then
        rm "$link"
      fi
    done
    rmdir "$legacy_dir" 2>/dev/null || true
  done
  rmdir "$TARGET/.claude" 2>/dev/null || true
fi

for source in "$ROOT/templates/blackboard"/*.md; do
  name="$(basename "$source")"
  if [ ! -e "$TARGET/$name" ] && [ ! -L "$TARGET/$name" ]; then cp "$source" "$TARGET/$name"; fi
done
if [ -z "$(find "$TARGET/paper" -mindepth 1 -maxdepth 1 -print -quit)" ]; then
  cp -R "$ROOT/templates/paper/." "$TARGET/paper/"
fi
if [ ! -e "$TARGET/AGENTS.md" ] && [ ! -L "$TARGET/AGENTS.md" ]; then
  cp "$ROOT/templates/project/AGENTS.md" "$TARGET/AGENTS.md"
fi

echo "Codex writing toolkit installed in $TARGET"
echo "Open $TARGET/STATE.md and .paper-writing/templates/project/AGENTS.md to begin."
echo 'Use $cpw-init, $cpw-write, or another installed skill in Codex.'
echo "Existing files are kept; missing resources are added, but existing file contents are not upgraded."
