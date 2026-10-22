---
name: sync-skill
description: Push a changed SAX skill to every place it lives — GitHub, Notion SAX Skills, the playbook (if a recipe changed) — and hand Jacob the fresh zip for Claude Settings. Run only when Jacob types /sync-skill or asks to sync a skill.
disable-model-invocation: true
argument-hint: "[skill-name, or blank for every changed skill]"
---

# Sync a skill everywhere

Jacob's rule: when a skill changes, all four copies must match — Claude Settings, GitHub, Notion SAX Skills, and the playbook if a recipe changed.

## 1. Find what changed
- If a skill name was given (`$ARGUMENTS`), use it. Otherwise run `git status --short` and list every skill folder with changes.
- Show Jacob the list in one short line.

## 2. Make the zip match
- Run `python3 scripts/rezip.py <skill-folder>` for each changed skill (the auto-zip hook usually already did this; run it anyway).

## 3. Check before anything leaves
- Run `python3 scripts/drift_check.py`. If it says DRIFT FOUND, stop, tell Jacob what drifted in plain words, and fix it first.
- Ask the `done-checker` agent to check each changed skill. Don't continue until it reports 5 of 5.

## 4. Ask Jacob first (this repo is PUBLIC)
- Show the changed lines (short) and ask: "OK to push to GitHub and update Notion?" Wait for a yes.

## 5. Push everywhere
1. **GitHub:** commit with a plain message ("Update sax-get-more-reviews: …") and push to `main`.
2. **Notion:** search Notion for "SAX Skills" (inside SAX — Business Home Base), open the page for that skill, and replace its text with the new SKILL.md, word for word.
3. **Playbook:** only if a build recipe or price changed — open "SAX — New Client Build Playbook + Jacob's Guide" in Google Drive (SAX Brand Files) and update that service's recipe to match.
4. **Claude Settings (the one-tap way):** call the `propose_skills` tool with `kind: "improvement"`, `target` = the skill name, the same name and description, and `skillMd` = the COMPLETE new SKILL.md, copied word for word from the repo file (never a partial edit). Tell Jacob: "Tap Save on the card." That replaces the skill in Settings — no zip, no Safari, no deleting.
   - Backup way, only if the card fails or the skill has extra files besides SKILL.md (like sax-photo-maker's sax_img.py): send the zip with SendUserFile and walk Jacob through Customize > Skills: turn the old one off, "..." > Delete, then "+" > "+ Create skill" > "Upload a skill".

## 6. Report
Use the done-checker's format: the real number of checks for each place (GitHub, Notion, playbook), and name anything not checked and why. Say "not done yet" until Jacob says he tapped Save (or uploaded the zip).
