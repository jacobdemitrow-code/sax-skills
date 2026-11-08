---
name: sync-skill
description: Push a changed SAX skill to every place it lives — GitHub (the master copy), Notion SAX Skills, and the playbook if a recipe changed. Run only when Jacob types /sync-skill or asks to sync a skill.
disable-model-invocation: true
argument-hint: "[skill-name, or blank for every changed skill]"
---

# Sync a skill everywhere

Jacob's rule (Oct 21, corrected Nov 8): GitHub is the MASTER copy, but Claude chats load the copy installed in Settings > Skills, and that copy does NOT update itself from GitHub (found Nov 8: Settings still had the Oct 21 sax-core while GitHub had Oct 27). So every sync ends with Jacob uploading the new zip in Settings > Skills. Notion SAX Skills and the playbook must match too.

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
4. **Confirm it's live:** fetch the raw GitHub URL above for each changed skill and confirm the new text is there. That is what every chat will now read. A NEW skill folder must also be added to the `skills` list in `.claude-plugin/marketplace.json` (drift_check.py catches it if not).
   - Claude Settings: give Jacob the zip link for each changed skill (`https://github.com/jacobdemitrow-code/sax-skills/raw/main/<skill>.zip`) and ask him to upload it in Settings > Skills. Do NOT use the propose_skills Save card (it shows no Save button for Jacob — tested Oct 21, iPad Safari).

## 6. Report
Use the done-checker's format: the real number of checks for each place (GitHub raw link, Notion, playbook), and name anything not checked and why.
