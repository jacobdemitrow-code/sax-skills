---
name: "lead-text-writer"
description: "Use when Jacob gives a business name or type and wants a short outreach text in his voice. Writes 2 versions to pick from."
---

# Lead Text Writer

Write a short, friendly first-contact text from Jacob to a local business.

## Input
A business name, a business type, or both (e.g. "Rosa's Pool Care" or "pool cleaner in Perris"). If only a name is given, infer the type from the name. Don't ask follow-up questions unless the input is blank.

## Proof example (swap here later)
Current proof: "I helped my wife's cleaning business by automating her Facebook texts, setting up her Google Business Profile, and building her a live, hosted website."
When Jacob has a real client, he can replace this one line. If he names a different proof in the request, use that instead for this run.

## Voice
Jacob's own example, for tone only (don't copy it word for word):
"Hey, my name's Jacob. I just started an AI consulting agency. I helped my wife's business by automating her Facebook texts, setting up her Google business profile, and building her a live, hosted website. Would you like to learn more? Call or text back if you'd like to bring something like that to your business."

## Rules
- Short: 3 to 5 sentences, under 70 words. It's a text message.
- Warm and plain, like a neighbor talking. Contractions are fine.
- Open with "Hey" plus his name. Use the business name if given.
- Tie the proof to one thing that business would care about (missed calls, bookings, reviews, showing up on Google).
- No corporate or salesy words: no "leverage", "solutions", "streamline", "boost", "game-changer", "limited time", "unlock", "elevate", no exclamation stacks, no emojis, no em dashes.
- No prices, no links, no phone number (they reply to the same number).
- Always end by asking them to call or text back.

## Output
Give exactly 2 versions, labeled "Version 1" and "Version 2". Make them differ in angle (e.g. one leads with the proof, one leads with a problem the business likely has). Nothing else: no intro, no notes, no explanation.