---
name: "sax-google-profile-fix"
description: "Use when Jacob's client wants SAX service 10, Google Profile Fix ($250 one time): customers find the right business on Google, not another one with the same name. Also use when Jacob says Google profile, Google Business Profile, schema, \"customers can't find me on Google\", or See us on Google button."
---

# Google Profile Fix — $250 one time

**FIRST:** follow the sax-core skill (rules, ask-first list, privacy, prices).
**BEFORE "DONE":** run the sax-done-check skill.

PRICE: $250 one time, no monthly (set by Jacob, Oct 27). Included in the Everything Bundle.
Proven on Come Home to Clean, Oct 27. The problem: customers from Facebook searched Google and found OTHER businesses with the same name.
Market check (Oct 27): a one-time Google profile setup or fix usually runs 300 to 500 dollars. Ours is done-for-you for less.

COLLECT: business name, city, phone, website, Google review link (g.page/r/.../review), Facebook page link, price list, service area.
CLAUDE'S RECIPE:
- Get the Place ID with no login: open the client's Google review link. The sign-in page's web address shows placeid=ChIJ... Copy it.
- Make the Google link that works everywhere, even inside Facebook's app: https://www.google.com/maps/search/?api=1&query=BUSINESS+NAME+CITY+ST&query_place_id=PLACE_ID
- Google profile check (the client, or Jacob with the client, logged in): website, phone, hours, and category are all correct. Claude sees a screenshot to confirm. Claude never changes the profile itself.
- Website hidden code (schema): add or fix it on their site with the business name, phone, city, service area, Google + Facebook links, and every service with its starting price (from their price list). Use a REAL schema.org type, like HomeAndConstructionBusiness. "HouseCleaningService" is NOT real.
- Run validator.schema.org on the live page: 0 errors and 0 warnings. Google's Rich Results Test saying "No items detected" is normal for this kind of business, not an error.
- Add a "See us on Google" button to their links/QR page, using the link above.
- Add the same link to their Facebook page (Details > Links, label "See us on Google"). This needs a person logged in.
- Give the client one line to tell customers, like: Search "Business Name + City".
- Test: tap the Google link inside the Facebook app on a phone. It must open their profile, not a blank map.

LESSONS (Oct 27, Come Home to Clean):
- "HouseCleaningService" is not a real schema.org type (the validator gave 1 error). Use "HomeAndConstructionBusiness". Run validator.schema.org on every client site after adding schema.
- Inside Facebook's app, google.com/maps/place/?q=place_id:... opened a blank map and share.google/... said "URL isn't available". Only the maps/search/?api=1 link with query_place_id worked everywhere.

JACOB'S GUIDE:
1. Get the client's Google review link, Facebook page, and price list.
2. Sit with the client while they open their Google profile. Check website, phone, hours, and category, and send me a screenshot.
3. I fix the code on their website, test it, and add the "See us on Google" button.
4. Add the Google link to their Facebook page together (Details > Links).
5. Tap the link inside Facebook on your phone. It should open their Google profile.

## EXTRA SAFEGUARDS FOR THIS SERVICE
- ASK FIRST before changing anything in the client's Google profile or Facebook page, and before publishing their site live.
- No customer names, phones, or addresses go in the website code.

## DONE MEANS
- Every recipe step is complete.
- The sax-done-check passed 5 of 5 and was reported.
- Jacob saw a preview and approved it.
- Jacob was told which guide steps are his.
- New lessons were added to the SAX Lessons Log.
