#!/usr/bin/env python3
"""Haalt alle afbeeldingen en PDF's die nog naar silvercloudzorgiot.nl verwijzen binnen
en zet ze in assets/wp/. Daarna worden de verwijzingen in alle HTML-bestanden omgezet
naar lokale paden. Zo blijft de nieuwe site werken als de oude WordPress-site uit gaat.

Gebruik (in de root van de repo):  python3 tools/download-assets.py
Alleen standaard Python 3 nodig."""
import re, os, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
PREFIX = "https://www.silvercloudzorgiot.nl/nijkerk/wp-content/uploads/"
pat = re.compile(re.escape(PREFIX) + r'[^"\'\s)<>]+')

htmls = [p for p in ROOT.rglob("*.html") if "scripts" not in p.parts]
urls = sorted({u for p in htmls for u in pat.findall(p.read_text(encoding="utf-8"))})
print(f"{len(urls)} bestanden te downloaden")
ok = set()
for u in urls:
    dest = ROOT / "assets" / "wp" / u[len(PREFIX):]
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        except Exception as e:
            print("  mislukt:", u, e); continue
    ok.add(u)
for p in htmls:
    s = p.read_text(encoding="utf-8")
    depth = len(p.relative_to(ROOT).parts) - 1
    pre = "../" * depth
    new = pat.sub(lambda m: (pre + "assets/wp/" + m.group(0)[len(PREFIX):]) if m.group(0) in ok else m.group(0), s)
    if new != s:
        p.write_text(new, encoding="utf-8")
print(f"klaar: {len(ok)} bestanden lokaal, HTML bijgewerkt")
