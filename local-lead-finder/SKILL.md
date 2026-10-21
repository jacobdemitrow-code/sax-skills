---
name: "local-lead-finder"
description: "Use when Jacob gives a business type and an area and wants a lead list of local businesses with phone, email, Facebook and website status."
---

# Local Lead Finder

Build a lead list of local businesses for Jacob's outreach.

## Input
A business type and an area (e.g. "pool service, Perris" or "lawn care in Sun City and Menifee"). If either is missing, ask once in one line. Default to about 15 businesses unless he gives a number.

## How to search
1. Use Exa (semantic web search) to find businesses of that type in that area. Search a few ways: "[type] [town]", "[type] near [town] CA", and local directories such as Yelp, Google Maps listings, Nextdoor, Facebook pages and the chamber of commerce.
2. For each business, use Firecrawl to open its listing, website or Facebook page and pull the details. If those tools aren't available, use regular web search and fetch.
3. Skip national chains and franchises' corporate pages. Skip businesses clearly outside the area.
4. Remove duplicates (same name or same phone).

## What to pull
- Business name
- Town
- Local phone number
- Email, only if published somewhere you actually saw
- Facebook page link, if one exists
- Website status

## Rules
- Local numbers only. Never include toll-free numbers (800, 833, 844, 855, 866, 877, 888). If a business only lists a toll-free number, leave the phone blank.
- Never make up an email or guess one from a pattern (no info@ guesses). If none is published, leave it blank.
- Never make up any field. Blank is better than wrong.
- Website status:
  - "No website": no site of its own found. A Facebook page, Yelp page or directory listing does not count as a website.
  - "Has website": it has its own working domain.
  - "Unsure": you couldn't confirm either way.

## Output
One simple table with these columns: Business | Town | Phone | Email | Facebook | Website.
Sort "No website" first (best leads), then "Unsure", then "Has website". Within each group, list the ones with a phone number first.
Under the table, add one line: how many of each status.
No intro and no extra commentary.

## Saving
Only when Jacob asks, save the newest list to a new Google Doc named "Leads - [type] - [area] - [date]" using the Google Drive connector, and give him the link. Never overwrite or delete an existing Doc. If the connector can't create Docs, say so in one line and give the table for him to paste.