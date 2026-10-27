#!/usr/bin/env python3
"""Weekly drift check for the SAX skills repo. Read-only: changes nothing.

Checks:
  1. Every skill's .zip matches its folder (same files, same contents).
  2. Every price in a service skill matches the price table in sax-core.
  3. Every price in README.md matches sax-core.
  4. No secret files (keys.env, *.env) are tracked by git.
Exit code 0 = all good, 1 = something drifted (details printed).
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rezip import ROOT, all_skills, files_in  # noqa: E402

problems = []
MONEY = re.compile(r"\$[\d,]+")


def check_zips():
    for skill in all_skills():
        zp = skill.parent / (skill.name + ".zip")
        rel = zp.relative_to(ROOT)
        if not zp.exists():
            problems.append(f"{rel}: zip is missing")
            continue
        want = {f"{skill.name}/{f.relative_to(skill).as_posix()}": f.read_bytes()
                for f in files_in(skill)}
        with zipfile.ZipFile(zp) as z:
            have = {n: z.read(n) for n in z.namelist() if not n.endswith("/")}
        for name in sorted(set(want) | set(have)):
            if name not in have:
                problems.append(f"{rel}: missing {name}")
            elif name not in want:
                problems.append(f"{rel}: has extra file {name}")
            elif want[name] != have[name]:
                problems.append(f"{rel}: {name} is different from the folder")


def core_prices():
    """{skill-name: {'$400', '$50'}} from the sax-core table, plus bundle prices."""
    text = (ROOT / "sax-core" / "SKILL.md").read_text()
    table = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[4].startswith("sax-"):
            table[cells[4]] = set(MONEY.findall(cells[2] + " " + cells[3]))
    bundle = set()
    for line in text.splitlines():
        if "Everything Bundle" in line:
            bundle |= set(MONEY.findall(line))
    return table, bundle


def check_prices():
    table, bundle = core_prices()
    if len(table) != 10:
        problems.append(f"sax-core: expected 10 services in the price table, found {len(table)}")
    allowed_any = set().union(*table.values()) | bundle
    for skill, ok in table.items():
        f = ROOT / skill / "SKILL.md"
        if not f.exists():
            problems.append(f"{skill}: listed in sax-core but folder is missing")
            continue
        for n, line in enumerate(f.read_text().splitlines(), 1):
            for amt in MONEY.findall(line):
                if amt not in ok | bundle:
                    problems.append(f"{skill}/SKILL.md line {n}: {amt} doesn't match sax-core ({' + '.join(sorted(ok))})")
    readme = ROOT / "README.md"
    for n, line in enumerate(readme.read_text().splitlines(), 1):
        for amt in MONEY.findall(line):
            if amt not in allowed_any:
                problems.append(f"README.md line {n}: {amt} isn't a sax-core price")


def check_secrets():
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    for t in tracked:
        name = Path(t).name
        if name == "keys.env" or name.endswith(".env"):
            problems.append(f"{t}: secret file is tracked by git (public repo!)")


def check_plugin_list():
    """Every top-level skill folder must be listed in the plugin, and nothing extra."""
    import json
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp.exists():
        problems.append(".claude-plugin/marketplace.json is missing (the SAX Skills plugin)")
        return
    listed = {p.strip("./") for p in json.loads(mp.read_text())["plugins"][0].get("skills", [])}
    folders = {p.parent.name for p in ROOT.glob("*/SKILL.md")}
    for s in sorted(folders - listed):
        problems.append(f"{s}: skill folder is not in the SAX Skills plugin list (marketplace.json)")
    for s in sorted(listed - folders):
        problems.append(f"{s}: listed in the SAX Skills plugin but the folder is missing")


if __name__ == "__main__":
    check_plugin_list()
    check_zips()
    check_prices()
    check_secrets()
    if problems:
        print(f"DRIFT FOUND ({len(problems)}):")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    n = len(all_skills())
    print(f"ALL GOOD: {n} zips match their folders, prices match sax-core, no secret files tracked.")
