#!/usr/bin/env bash
# PostToolUse hook: after Claude edits a file inside a skill folder,
# rebuild that skill's .zip so the folder and zip always match.
input=$(cat)
file=$(printf '%s' "$input" | python3 -c 'import json,sys; d=json.load(sys.stdin); print((d.get("tool_input") or {}).get("file_path",""))' 2>/dev/null)
[ -z "$file" ] && exit 0
case "$file" in *.zip) exit 0 ;; esac
python3 "$CLAUDE_PROJECT_DIR/scripts/rezip.py" "$file"
exit 0
