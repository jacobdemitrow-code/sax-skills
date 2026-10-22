#!/usr/bin/env python3
"""PreToolUse hook: stop keys and tokens from landing in this PUBLIC repo.

- Edit/Write: blocks writing a key-looking value into any file git would track.
  (Writing keys.env is allowed only because .gitignore keeps it out of git.)
- Bash: before `git add`, `git commit` or `git push`, scans what's staged and
  blocks if a secret file or key-looking value would go to GitHub.
Exit code 2 = blocked; the message tells Claude why.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

PATTERNS = [
    (r"hf_[A-Za-z0-9]{20,}", "Hugging Face token"),
    (r"sk-(?:ant-)?[A-Za-z0-9_\-]{20,}", "API key (sk-)"),
    (r"gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}", "GitHub token"),
    (r"AKIA[0-9A-Z]{16}", "AWS key"),
    (r"xox[abprs]-[A-Za-z0-9\-]{10,}", "Slack token"),
    (r"AIza[0-9A-Za-z_\-]{35}", "Google API key"),
    (r"(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-\.]{20,}", "key=value secret"),
]


def find_secret(text):
    for pat, label in PATTERNS:
        m = re.search(pat, text or "")
        if m:
            # Allow obvious placeholders such as os.environ["CF_API_TOKEN"]
            if "environ" in text[max(0, m.start() - 40):m.end()]:
                continue
            return label
    return None


def ignored(path):
    r = subprocess.run(["git", "check-ignore", "-q", path], cwd=ROOT)
    return r.returncode == 0


def block(msg):
    print("SECRET GUARD: " + msg + " This repo is PUBLIC. Keep keys in keys.env "
          "(git ignores it) or Jacob's private Drive doc.", file=sys.stderr)
    sys.exit(2)


data = json.load(sys.stdin)
tool = data.get("tool_name", "")
ti = data.get("tool_input") or {}

if tool in ("Edit", "Write", "MultiEdit"):
    path = ti.get("file_path", "")
    text = ti.get("content", "") + ti.get("new_string", "")
    for e in ti.get("edits") or []:
        text += e.get("new_string", "")
    label = find_secret(text)
    if label and not ignored(path):
        block(f"{label} found in {os.path.basename(path)}, which git would publish.")

elif tool == "Bash":
    cmd = ti.get("command", "")
    if re.search(r"\bgit\b.*\b(add|commit|push)\b", cmd):
        if re.search(r"\bgit\b.*\badd\b.*(keys\.env|\.env\b)", cmd):
            block("that command would stage a .env key file.")
        staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT,
                                capture_output=True, text=True).stdout.split()
        for f in staged:
            if os.path.basename(f) == "keys.env" or f.endswith(".env"):
                block(f"{f} is staged.")
        diff = subprocess.run(["git", "diff", "--cached", "-U0"], cwd=ROOT,
                              capture_output=True, text=True).stdout
        added = "\n".join(l for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
        label = find_secret(added)
        if label:
            block(f"{label} is in the staged changes.")

sys.exit(0)
