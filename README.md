# sax-skills

Backup copies of Jacob's SAX skills, matching what is installed in Claude (Settings > Skills).
Last updated: Oct 21, 2026.

Each skill has a folder with its SKILL.md, plus a .zip of that folder ready to upload in Claude.

| Skill | What it is |
|---|---|
| sax-core | The one rulebook: Jacob's 6 rules, ask-first list, privacy, the 9 services and prices, brand |
| sax-done-check | The 5-check gate to run before saying done, saved, fixed or working |
| sax-helpers | Tool Picker, Helper Ladder and Expert Finder for when a SAX skill isn't enough |
| sax-never-miss-a-lead | Service 1 — $400 + $50/mo |
| sax-win-back-old-customers | Service 2 — $150 + $30/mo |
| sax-get-more-reviews | Service 3 — $150 + $30/mo |
| sax-know-your-price | Service 4 — $200 + $20/mo |
| sax-get-found-online | Service 5 — $800 + $50/mo |
| sax-lead-generation-page | Service 6 — $300 + $40/mo |
| sax-sunday-auto-update | Service 7 — $40/mo add-on, 25 new leads every Sunday |
| sax-one-scan-qr | Service 8 — $125 + $25/mo |
| sax-price-menu-graphic | Service 9 — $60 one time add-on, not in the bundle |
| come-home-to-clean-quotes | Per-job price quotes for Come Home to Clean |
| lead-text-writer | Short outreach texts in Jacob's voice |
| local-lead-finder | Local business lead lists with phone and email |
| sax-photo-maker | Free AI photos: Hugging Face (best) + Cloudflare (fast). Keys live in a private Drive doc, never here |

`old/` holds sax-always-on-protocol and sax-house-rules, replaced by sax-core on Oct 21.

Everything Bundle: services 1-8 (QR included free) — $2,000 + $260/mo.

## Automations (Claude Code, added Oct 21)

| What | Where | What it does |
|---|---|---|
| Auto-zip hook | `.claude/hooks/auto-zip.sh` | When Claude edits a skill, its .zip is rebuilt so folder and zip always match |
| Secret guard hook | `.claude/hooks/secret-guard.py` | Blocks keys and tokens from being saved or pushed here (this repo is public) |
| Done-checker helper | `.claude/agents/done-checker.md` | A separate helper runs the 5 checks with fresh eyes |
| /sync-skill | `.claude/skills/sync-skill/SKILL.md` | Pushes a changed skill to GitHub, Notion and the playbook — asks first |
| SAX Skills plugin | `.claude-plugin/marketplace.json` | Optional: lets this repo be installed as a plugin in Claude Code |

**This repo is the master copy.** Before using a SAX skill, Claude reads its newest version from `https://raw.githubusercontent.com/jacobdemitrow-code/sax-skills/main/<skill>/SKILL.md`, so a change pushed here works in every chat. No zip uploads to Claude Settings.
| Weekly drift check | `scripts/drift_check.py` | Sunday morning check: zips match folders, prices match sax-core, no key files |

`keys.env` stays out of git (see `.gitignore`). Run `python3 scripts/drift_check.py` any time.
