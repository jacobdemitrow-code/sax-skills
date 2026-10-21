# SAX photo maker: Hugging Face (Z-Image, ~5/day) first, Cloudflare (FLUX schnell, ~100+/day) as backup.
# Keys come from env HF_TOKEN / CF_API_TOKEN, or from keys.env next to this file (never commit it).
# Usage: python sax_img.py "subject and scene" out.jpg [hf|cf|auto]
import base64, json, os, shutil, sys, urllib.request
from pathlib import Path

STYLE = (" Shot on a Canon EOS R6 with a 35mm lens, Kodak Portra 400 color, soft natural window light, "
         "ordinary everyday people with slightly asymmetrical features, visible skin pores, realistic fabric "
         "texture, unposed documentary snapshot, sharp focus, natural hands, no text, no logos, no watermark.")

keys = Path(__file__).with_name("keys.env")
if keys.exists():
    for line in keys.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

def hf(prompt, out):
    from gradio_client import Client
    c = Client("Tongyi-MAI/Z-Image-Turbo", token=os.environ["HF_TOKEN"], verbose=False)
    r = c.predict(prompt=prompt, resolution="1536x1024 ( 3:2 )", seed=0, steps=8, shift=3,
                  random_seed=True, api_name="/generate")
    f = r[0][0]["image"] if isinstance(r[0], list) else r[0]
    from PIL import Image
    Image.open(f).convert("RGB").save(out, quality=93)

def cf_call(path, body=None):
    req = urllib.request.Request("https://api.cloudflare.com/client/v4" + path,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": "Bearer " + os.environ["CF_API_TOKEN"],
                                          "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=120))

def cf(prompt, out):
    acct = os.environ.get("CF_ACCOUNT_ID") or cf_call("/accounts")["result"][0]["id"]
    r = cf_call(f"/accounts/{acct}/ai/run/@cf/black-forest-labs/flux-1-schnell", {"prompt": prompt, "steps": 8})
    Path(out).write_bytes(base64.b64decode(r["result"]["image"]))

if __name__ == "__main__":
    prompt = sys.argv[1].rstrip(". ") + "." + STYLE
    out, mode = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "auto")
    order = {"hf": [hf], "cf": [cf], "auto": [hf, cf]}[mode]
    for fn in order:
        need = "HF_TOKEN" if fn is hf else "CF_API_TOKEN"
        if not os.environ.get(need):
            print(f"skip {fn.__name__}: no {need}"); continue
        try:
            fn(prompt, out); print(f"ok {fn.__name__} -> {out}"); break
        except Exception as e:
            print(f"{fn.__name__} failed: {str(e)[:200]}")
