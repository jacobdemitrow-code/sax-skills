#!/usr/bin/env python3
"""Rebuild a skill's .zip from its folder so the two always match.

Usage:
  python3 scripts/rezip.py <path inside a skill folder>   # rezip that one skill
  python3 scripts/rezip.py --all                         # rezip every skill

The zip holds "<skill>/" plus every file in the folder, the same layout
Claude Settings expects. Secret files (keys.env, *.env) are never zipped.
"""
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_NAMES = {".DS_Store", "keys.env"}
SKIP_SUFFIXES = {".env", ".pyc"}
SKIP_DIRS = {"__pycache__", ".git"}


def skill_dir_for(path: Path):
    """Nearest folder (inside the repo) that holds a SKILL.md."""
    path = path.resolve()
    for d in [path] + list(path.parents):
        if d == ROOT or ROOT not in d.parents:
            return None
        if d.is_dir() and (d / "SKILL.md").exists():
            return d
    return None


def files_in(skill: Path):
    out = []
    for f in sorted(skill.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(skill)
        if any(p in SKIP_DIRS for p in rel.parts):
            continue
        if f.name in SKIP_NAMES or f.suffix in SKIP_SUFFIXES:
            continue
        out.append(f)
    return out


def rezip(skill: Path) -> Path:
    zip_path = skill.parent / (skill.name + ".zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(skill.name + "/", "")
        for f in files_in(skill):
            z.write(f, f"{skill.name}/{f.relative_to(skill).as_posix()}")
    return zip_path


def all_skills():
    return sorted(p.parent for p in ROOT.rglob("SKILL.md")
                  if ".claude" not in p.relative_to(ROOT).parts
                  and ".git" not in p.relative_to(ROOT).parts)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--all":
        for s in all_skills():
            print("rezipped", rezip(s).relative_to(ROOT))
    else:
        s = skill_dir_for(Path(sys.argv[1]))
        if s is None:
            sys.exit(0)  # not inside a skill folder: nothing to do
        print("rezipped", rezip(s).relative_to(ROOT))
