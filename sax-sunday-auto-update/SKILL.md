---
name: "sax-sunday-auto-update"
description: "Use when Jacob's client wants SAX service 7, Sunday Auto-Update ($40/mo add-on): 25 new leads added to their lead page every Sunday. Also use when Jacob says weekly leads, Sunday update, or lead refresh."
---

# Sunday Auto-Update — weekly lead refresh ($40/mo add-on)

**FIRST:** follow the sax-core skill (rules, ask-first list, privacy, prices).
**BEFORE "DONE":** run the sax-done-check skill.

NEEDS: the client must already have a Lead Generation Page (leads.html).

CLAUDE'S RECIPE:
- What runs it: a scheduled Claude task every Sunday morning (or a Make scenario, once tested).
- Each Sunday: find the next 25 new leads using the same research and checking rules as the Lead Generation Page. Skip anyone already on the page. Add the new leads to the top of the client's leads.html, marked New. Keep the old ones and their Sent status.
- Re-publish the page and confirm the new leads show.
- Send the owner a short note: "X new leads added this week."
JACOB'S GUIDE:
1. Confirm the client wants the weekly refresh ($40/mo add-on).
2. I set it to run every Sunday.
3. They just check the new leads each week.

## EXTRA SAFEGUARDS FOR THIS SERVICE
- Same privacy and lead-checking rules as the Lead Generation Page. Run the lead-list checks in sax-done-check every Sunday.
- If the scheduled run fails, tell Jacob that same day.

## DONE MEANS
- Every recipe step is complete.
- The sax-done-check passed 5 of 5 and was reported.
- Jacob saw a preview and approved it.
- Jacob was told which guide steps are his.
- New lessons were added to the SAX Lessons Log.
