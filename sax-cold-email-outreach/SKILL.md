---
name: "sax-cold-email-outreach"
description: "Use when Jacob wants SAX's own cold email outreach to local service businesses: the agent team (Chief of Staff, Lead Finder, Lead Checker, Email Writer) that finds leads, checks them, writes one unique email each, saves them as Pending, and emails Jacob a Send all button. Also use when he says cold email, outreach, Finder, Send all, outreach tracker, follow-up email, reply check, write a cold email, or wants to build the same system for a client."
---

# SAX Cold Email Outreach (Claude agent team + Make sender)

**FIRST:** follow the sax-core skill (rules, ask-first list, privacy).
**BEFORE "DONE":** run the sax-done-check skill. Use the checks in section 8 below.
Built Oct 24, moved to the Claude agent team Oct 26, 2026. Next steps: Drive doc "SAX — Next Session".

## 1. The goal
Weekdays, the agent team finds 5 real local leads, checks them, writes one unique email each, and saves them to the tracker as Pending. Jacob gets ONE summary email with a "Send all" button. Nothing goes to a business until Jacob taps. Claude costs come from Jacob's $100/mo Claude API credit. No cold texts (cold calls and texts got hang-ups).

## 2. How it runs
- **Scheduled task "SAX daily lead team"** (Claude Code, weekdays 8:40 AM PT). It does, in order: sent / reply / bounce check on the tracker → starts one Chief of Staff session → re-checks every lead itself with Exa (Firecrawl only if Exa fails) → adds kept leads to the tracker as Pending → emails Jacob the summary with Send all, plus one line: "Today's team cost: $X.XX. Month so far: $Y.YY of $100."
- **Claude Managed Agents** (Jacob's Console account, platform.claude.com):
  - Chief of Staff: runs the 3 helpers, reads every email before it finishes, returns JSON rows.
  - Lead Finder: finds businesses with a real, published email and 2–3 website observations.
  - Lead Checker: a separate agent. Re-opens every page and drops anything it can't confirm.
  - Email Writer: writes one email per kept lead from checked facts only.
- **Make only sends.** "SAX Outreach - Send Approved Batch" (6759157) is the Send all button: each tap sends 10 Pending leads and handles follow-ups. "SAX Outreach - Finder + Writer" (6759114) is OFF and replaced by the agent team.
- Tracker: Google Sheet "SAX Outreach Tracker" 1iLqA2Mdz29jmbBg0lEbozusEWAiBAnrf4uBsGEmjR9g. Columns A–N: Date found, Niche, Business, Town, Email, Phone, Website, Why them, Subject, Email body, Status, Date emailed, Notes, Follow-up date. Status: Pending, Skip, Emailed, Followed up, Replied, Stop, Bounced.
- The Send all key and the API key never go in a skill, doc, or GitHub.

## 3. Niche and area
- Mon electricians, Tue pool service, Wed pest control, Thu pet groomers, Fri med spas.
- The Chief of Staff uses today's niche from this list. If a batch is the wrong niche, say so at the top of the summary email.
- Perris and Moreno Valley first, then Menifee, Riverside, Hemet, San Jacinto, Lake Elsinore, Murrieta, Temecula.
- Small local owner-run businesses only. Skip chains, franchises, and anyone already in the tracker (same name or website).

## 4. Finding leads that are real
- Most trade sites hide their email. Search for the email FIRST: `pest control Perris "@gmail.com"`, `"@yahoo.com"`, the business name plus "email". A different town or wording each search.
- Good places: the business's own site (home, contact, about, footer), Nextdoor, Yelp, BBB, Facebook About.
- Open the contact page first. Max 3 pages per business. No email after contact + home = skip.
- Record the exact page URL where each email was seen. Never guess an email.
- Before describing a button, open where it goes. Only say something is "missing" after checking home AND contact/booking.
- A site that won't load: retry once, then skip. Never write that a site is down.

## 5. Writing the email
- One email per business, unique: its own opening, angle, and closing question. No two emails share any of those.
- Plain, friendly, short: about 70–110 words before the signature. Sounds like a real local person. No hype, no exclamation marks, no emojis.
- Open with one specific, confirmed detail from THEIR site (name the button, page, hours, or form).
- Name the problem in plain words: calls or quote requests that sit, go to voicemail, or wait for a call back.
- Proof: Jacob first built this (instant replies, missed-call text back, simple booking page) for his wife's cleaning business here in the Inland Empire. Do not name her business.
- End with ONE easy yes/no question, tailored to that business. Take turns between the free 15-minute Money Leak Audit and "Want me to send a quick example of what your customers would see?" The example goes in Jacob's reply, never as a link in the cold email.
- NO links. NO prices. Never claim anything that isn't a checked fact.
- No season or "you're swamped" claims unless their own page says it.
- Greet the owner by first name only if it was confirmed; otherwise "Hi <Business> team,". Never "Hi there". No two emails in one batch may start with the same 3 words.
- Subject: 3–7 words, specific to that business (for example "Your Book Now button"). No clickbait.
- End with exactly this signature:

Jacob Demitrow
SAX (StratAI Apex)
951-418-0216
jacobdemitrow@gmail.com

40906 Mayberry Ave., Hemet, CA 92544 | Not interested? Reply 'stop' and I won't email again.

## 6. Replies
- Booking link (Google Calendar, "Free 15-Min Money Leak Audit", Mon–Fri 9:00–4:30 PT): https://calendar.app.google/4hXHkR6RhwiX7wPWA. It goes in Jacob's REPLY only. Never in a cold email.
- The daily task saves reply drafts in Jacob's Gmail Drafts. It never sends them.
- Reply template (copy it exactly, fill in the first name):
  Hi [first name], / Great, thanks for getting back to me! Grab any 15-minute time that works for you here: / https://calendar.app.google/4hXHkR6RhwiX7wPWA / I'll call you at the number you enter. If none of those times work, just reply with a good time and I'll make it work. / Talk soon, / Jacob Demitrow / SAX (StratAI Apex) / 951-418-0216 / jacobdemitrow@gmail.com
- Stop, unsubscribe, or not interested = Status Stop. Never email them again.

## 7. DOs and DON'Ts
- Don't trust the Finder. 6 of the first 12 leads had false claims ("no website," "site couldn't load," "no text option"). The Checker re-opens everything, then Claude re-checks with Exa (Firecrawl only as a backup: its free credits run low).
- Keep costs low: medium effort on helpers, max 3 pages per business, no whole pages printed in bash, workflows off.
- Gmail strips CSS "background" in the summary email. Build the Send all button as a table cell with bgcolor, plus a plain link under it.
- Send Tue–Thu mornings when possible. Don't send on weekends.
- The summary email says: "Best time to tap Send all: a Tue–Thu morning. If it's after 2 PM, wait until the next weekday morning."
- After any Make change, confirm every scenario's ON/OFF with scenarios_list.
- Never send, post, or tap the Send all link. Jacob taps it.

## 8. Done-check for this build (5 different checks)
1. **Run:** the scheduled task ran, and the session finished (idle, not failed). Note its cost.
2. **Tracker:** the rows and statuses match what should have happened (Pending / Emailed + date), with an Exa (or Firecrawl) re-check note in col M.
3. **Gmail sent:** only the expected emails went out, to the right people, with no duplicates.
4. **Summary email:** it arrived, and the Send all button and plain link are both visible.
5. **Claims:** every Pending email's facts were confirmed on the live site.

## 9. The math (added Nov 8): how many clients the machine makes
One equation decides everything. Track these 4 numbers in the tracker every week; change ONE at a time.

**Clients a month = N x R x A x C**
- N = businesses contacted a month. R = share that reply (any human reply). A = share of replies that book the free audit. C = share of audits that pay.
- Measured so far (Oct 21 to Nov 6, about 140 strangers): calls/texts 0 of 70, plain DMs 0 of 25, DMs WITH a sample page 1 of 20 (5%), cold emails 0 of 25 (1 auto-reply, so emails ARE landing). Follow-ups sent: 0 of 4. Audits: 0. Clients: 0.
- Rule of three: 0 of 25 does NOT mean email is dead. With 25 sends the true reply rate could still be anything up to about 12%. Under 50 contacts per change, say "too early", never "it failed".
- Outside benchmarks (vendor data, treat as rough): average cold email reply about 3 to 3.5%; small lists under 50 about 5.8%; 3 to 5 follow-ups about doubles replies (8.3% vs 4.1%), and about 42% of all replies come from follow-ups; "want to see it in action / can I show you a quick example" CTAs get the most positive replies.

**What the equation says to do, in order (biggest lift first):**
1. **Send the follow-ups.** Replies roughly double with follow-ups and ours were never sent. Sequence: day 0 email, day 3 follow-up (one line, same thread), day 7 last touch that offers the sample page. Make route 2 already sends follow-up 1; touch 3 needs a Make change (ask Jacob).
2. **Lead with the sample.** The only thing that got a yes was showing something (1 of 20). Every email's question becomes "Want me to send a quick example of what your customers would see?" The example itself goes in the REPLY or the day-7 follow-up, never in email 1 (no links in a cold email).
3. **Double N.** At R 3%, A 50%, C 33%: 1 client needs about 200 contacts (200 x .03 x .5 x .33 = 1). 5 leads a day = 100 a month = about half a client a month. 10 a day = 1 a month. Cost measured Oct 27: $0.94 per 5 leads, so 10 a day is about $40 a month of the $100 budget.
4. **Fewer steps, fewer breaks.** A run with 7 steps at 95% each finishes clean about 70% of the time (0.95^7). The daily lead team should do ONE job: leads + sent check + summary. Monday and Friday idea emails move to the Saturday improver or get dropped (they make reports, not clients).

**Scoreboard (the improver reads these from the tracker each Saturday):** N this month, R, A, C, expected clients = N x R x A x C, and the one change being tested right now. If R is under 2% after 100 sends with follow-ups, change the subject/opening. If R is over 3% but A is 0, the problem is the reply and the booking link, not the email.
