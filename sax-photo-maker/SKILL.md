---
name: sax-photo-maker
description: Use when Jacob or a SAX build needs a photo (website, flyer, social post, menu card) and no real client photo exists. Makes realistic AI photos for free with Hugging Face (best quality, ~5 a day) and Cloudflare (3 seconds, ~100+ a day). Also use when Jacob says "make a photo of", "AI photo", or "picture for the site".
---

# SAX Photo Maker

Free AI photos in seconds. Set up Oct 21, 2026. sax-core rules always win.

## The order (every time)
1. **Client's real photos first.** AI photos only when there are none.
2. **Hugging Face** (Z-Image Turbo): best quality, wide 1536×1024, about 17 s, about 5 a day. Use for the hero and main photos.
3. **Cloudflare** (FLUX schnell): 3 s, square 1024×1024, about 100+ a day. Use for everything else and when Hugging Face runs out. The script switches over by itself.
4. Do NOT use Canva or Moda for photos (Jacob's rule). Imagine only when it has credits.

## Setup in a new Claude Code chat (Claude does all of it)
1. Find the Google Drive doc **"SAX — Photo Maker Keys (PRIVATE, do not share)"** and read its three lines (HF_TOKEN, CF_API_TOKEN, CF_ACCOUNT_ID). The Drive reader adds backslashes before underscores: remove every `\` before using them.
2. Write them to `keys.env` in the session scratchpad, next to a copy of `sax_img.py` (umask 077). **Never** put keys in this repo, a page, a chat summary, or any public place.
3. `pip install gradio_client pillow` (a venv is fine).
4. Run: `python sax_img.py "subject and scene" out.jpg` (add `hf` or `cf` to force one).
5. Look at the photo before showing Jacob: hands, faces, odd objects, text. Redo it once if something looks off.

## Writing the prompt
The script adds the camera/light/texture recipe. You write only the subject and scene:
- Who (age, everyday look, clothes), doing what, where, plus 1–2 props.
- Plain words. No "8k", "masterpiece", "realistic".
- Say what IS there, not what isn't.

## Rules
- Show Jacob the photo in chat. Ask before saving it to Drive or putting it on a live site.
- Never make photos of real, named people, and never fake "customer" or "review" photos.
- Never present an AI photo as a real job, team, or customer photo of the client.
- If a key stops working, tell Jacob right away and give him the key page link:
  Hugging Face https://huggingface.co/settings/tokens · Cloudflare https://dash.cloudflare.com/profile/api-tokens
