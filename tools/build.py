# Bouwt de statische SilverCloud-site in public/ (eerste voorstel).
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'public')

ICON = {
 'werkplek': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'netwerk': '<rect x="9" y="3" width="6" height="5" rx="1"/><rect x="3" y="16" width="6" height="5" rx="1"/><rect x="15" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M6 16v-2h12v2"/>',
 'telefoon': '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 'helpdesk': '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
 'cloud': '<path d="M7 18a4 4 0 0 1-.5-8 6 6 0 0 1 11.5 1.5A3.5 3.5 0 0 1 17.5 18Z"/>',
 'schild': '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'oog': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'klok': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'pad': '<path d="M3 12h4l3-8 4 16 3-8h4"/>',
 'mens': '<circle cx="12" cy="7" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'pin': '<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 'bel': '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
 'cirkel': '<circle cx="12" cy="12" r="9" stroke-dasharray="3 3"/><circle cx="12" cy="12" r="2"/>',
 'deur': '<path d="M5 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17"/><path d="M3 21h18M14 12h.01"/>',
 'radio': '<rect x="7" y="7" width="10" height="14" rx="2"/><path d="M10 3l2 4M10 11h4"/>',
 'tillift': '<path d="M5 21h14M7 21V9l10-5v4"/><circle cx="17" cy="13" r="2"/>',
 'kaart': '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/>',
 'pijl': '<path d="M4 12h16M14 6l6 6-6 6"/>',
}
def icon(n):
    return f'<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{ICON[n]}</svg></span>'

WOLK = '<svg class="wolk" viewBox="0 0 400 160" aria-hidden="true"><path d="M10 120 C 30 80, 80 64, 140 70 C 175 20, 245 8, 290 24 C 330 38, 352 70, 364 98 H 400" fill="none" stroke="#9c9d9e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def page(path, title, desc, body, label='', nav='', sub=None):
    depth = path.count('/') + 1 if path else 0
    r = '../' * depth
    zorg = label == 'zorg'
    logo = f'<img src="{r}assets/img/silvercloud-zorg-logo-donker.svg" alt="SilverCloud Zorg">' if zorg else f'<img src="{r}assets/img/silvercloud-logo-kleur.svg" alt="SilverCloud">'
    items = [('', 'Home', 'home'), ('computing/', 'Computing', 'computing'), ('zorg/', 'Zorg', 'zorg'), ('kennis/', 'Kennis &amp; cases', 'kennis'), ('over-ons/', 'Over ons', 'over')]
    menu = ''.join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if k == nav else ""}>{t}</a></li>' for h, t, k in items)
    subnav = ''
    if sub:
        subs = [('zorg/', 'Overzicht', 'zorg'), ('zorg/netwerkregie/', 'Netwerkregie', 'netwerkregie'), ('zorg/caredesk/', 'CareDesk', 'caredesk'), ('zorg/lokalisatie-leefcirkels/', 'Lokalisatie & Leefcirkels', 'lokalisatie'), ('zorg/assetguard/', 'Hulpmiddelenbeheer', 'assetguard')]
        subnav = '<nav class="sub-nav" aria-label="SilverCloud Zorg"><div class="container"><ul>' + ''.join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if k == sub else ""}>{t}</a></li>' for h, t, k in subs) + '</ul></div></nav>'
    html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{r}assets/css/site.css">
</head>
<body class="{'label-' + label if label else ''}">
<a class="skip" href="#inhoud">Direct naar de inhoud</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand{' zorg' if zorg else ''}" href="{r}">{logo}</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul class="menu" id="menu">{menu}<li><a class="btn btn-primary" href="{r}contact/">Contact</a></li></ul>
  </div>
</header>
{subnav}
<main id="inhoud">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="{r}assets/img/silvercloud-logo-kleur-op-donker.svg" alt="SilverCloud">
        <p>Eén partner, twee expertises: betrouwbare IT voor het mkb en technologie die werkt voor de zorg.</p>
      </div>
      <div><h4>Computing</h4><ul><li><a href="{r}computing/#werkplek">Digitale werkplek</a></li><li><a href="{r}computing/#netwerken">Slimme netwerken</a></li><li><a href="{r}computing/#telefonie">Zakelijke telefonie</a></li><li><a href="{r}computing/#helpdesk">Helpdesk &amp; beheer</a></li></ul></div>
      <div><h4>Zorg</h4><ul><li><a href="{r}zorg/netwerkregie/">Netwerkregie</a></li><li><a href="{r}zorg/caredesk/">CareDesk</a></li><li><a href="{r}zorg/lokalisatie-leefcirkels/">Lokalisatie &amp; Leefcirkels</a></li><li><a href="{r}zorg/assetguard/">Hulpmiddelenbeheer (AssetGuard)</a></li></ul></div>
      <div><h4>SilverCloud</h4><ul><li><a href="{r}over-ons/">Over ons &amp; werkwijze</a></li><li><a href="{r}kennis/">Kennis &amp; cases</a></li><li><a href="{r}contact/">Contact</a></li><li><a href="#">Privacyverklaring</a></li><li><a href="#">Algemene voorwaarden</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>© 2026 SilverCloud</span><span>Ohmstraat 18-A, 3861 NB Nijkerk · <a href="tel:+31882560050">088 256 00 50</a> · <a href="mailto:info@silvercloud.nl">info@silvercloud.nl</a> · KvK [invullen]</span></div>
  </div>
</footer>
<span class="concept" title="Eerste voorstel, nog niet definitief">Concept v0.2</span>
<script>
  (function () {{
    var b = document.querySelector('.menu-toggle'), m = document.getElementById('menu');
    if (!b) return;
    b.addEventListener('click', function () {{ var o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); }});
  }})();
</script>
</body>
</html>
'''
    import re
    html = re.sub(r'href="((?:\.\./)*[a-z0-9/-]*/)(#[a-z-]+)?"', lambda m: f'href="{m.group(1)}index.html{m.group(2) or ""}"', html)
    html = re.sub(r'href="(#[a-z-]+)?"', lambda m: f'href="index.html{m.group(1) or ""}"' if m.group(1) is None else m.group(0), html)
    html = re.sub(r'href="((?:\.\./)+)"', r'href="\1index.html"', html)
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(html)

def cta(title, text, primary, href, r, secondary=None, href2=None):
    sec = f'<a class="btn btn-secondary" href="{href2}">{secondary}</a>' if secondary else ''
    return f'''<section class="section"><div class="container"><div class="cta-band">{WOLK}
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="actions"><a class="btn btn-highlight" href="{href}">{primary}</a>{sec}</div>
</div></div></section>'''

def steps(items):
    return '<div class="steps">' + ''.join(f'<div class="step"><h3>{t}</h3><p>{p}</p></div>' for t, p in items) + '</div>'

WERKWIJZE = [('Luisteren', 'Zorgproces of bedrijfsvoering, techniek, risico’s en bestaande investeringen begrijpen.'),
             ('Ontwerpen', 'Bepalen wat blijft en wat verandert, vastgelegd in één architectuur.'),
             ('Implementeren', 'Projectmatig, met duidelijke verantwoordelijkheden en minimale verstoring.'),
             ('Adoptie', 'Gebruikers, beheerders en processen meenemen in de verandering.'),
             ('Beheren', 'Prestaties bewaken en leveranciers op elkaar laten aansluiten.'),
             ('Verbeteren', 'Roadmap, rapportages en nieuwe mogelijkheden periodiek evalueren.')]

# ---------- Illustraties ----------
HERO_HOME = '''<svg viewBox="0 0 560 460" role="img" aria-label="Illustratie: SilverCloud verbindt mkb en zorg onder één wolk">
  <rect x="0" y="40" width="560" height="420" rx="18" fill="#f3f6f9"/>
  <path d="M60 210 C 90 150, 160 126, 240 136 C 290 56, 400 36, 460 72 C 500 96, 520 140, 530 180" fill="none" stroke="#9c9d9e" stroke-width="10" stroke-linecap="round"/>
  <rect x="60" y="240" width="200" height="180" rx="14" fill="#4697d2"/>
  <rect x="300" y="240" width="200" height="180" rx="14" fill="#00aba3"/>
  <rect x="88" y="270" width="144" height="88" rx="8" fill="#fff"/>
  <rect x="100" y="282" width="120" height="8" rx="4" fill="#e8f2fa"/><rect x="100" y="298" width="80" height="8" rx="4" fill="#e8f2fa"/>
  <rect x="100" y="318" width="52" height="28" rx="4" fill="#2b74b5"/><rect x="160" y="318" width="60" height="28" rx="4" fill="#e8f2fa"/>
  <rect x="140" y="358" width="40" height="10" fill="#fff"/><rect x="120" y="368" width="80" height="6" rx="3" fill="#fff"/>
  <text x="160" y="404" text-anchor="middle" font-family="Exo 2, sans-serif" font-weight="700" font-size="18" fill="#0f1b2d">Computing</text>
  <path d="M340 360 V300 l60 -36 l60 36 V360 Z" fill="#fff"/><rect x="388" y="320" width="24" height="40" fill="#e3f4f2"/>
  <path d="M394 296 h12 M400 290 v12" stroke="#007a74" stroke-width="4" stroke-linecap="round"/>
  <text x="400" y="404" text-anchor="middle" font-family="Exo 2, sans-serif" font-weight="700" font-size="18" fill="#0f1b2d">Zorg</text>
  <circle cx="280" cy="200" r="34" fill="#ed6a3c"/><path d="M266 200 h28 M280 186 v28" stroke="#0f1b2d" stroke-width="4" stroke-linecap="round"/>
  <path d="M160 240 V214 Q160 200 174 200 H246 M400 240 V214 Q400 200 386 200 H314" fill="none" stroke="#0f1b2d" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
</svg>'''

HERO_ZORG = '''<svg viewBox="0 0 560 460" role="img" aria-label="Illustratie: drie lagen - netwerk, ondersteuning en zorgtechnologie - onder één zorglocatie">
  <rect x="0" y="20" width="560" height="440" rx="18" fill="#e3f4f2"/>
  <path d="M40 150 C 70 96, 140 76, 210 84 C 256 18, 360 6, 412 40 C 448 64, 466 100, 476 132 H 540" fill="none" stroke="#9c9d9e" stroke-width="9" stroke-linecap="round"/>
  <path d="M150 230 l130 -64 l130 64 v54 H150 Z" fill="#fff" stroke="#0f1b2d" stroke-width="3" stroke-linejoin="round"/>
  <rect x="190" y="242" width="40" height="42" fill="#e3f4f2"/><rect x="330" y="242" width="40" height="42" fill="#e3f4f2"/><rect x="262" y="236" width="36" height="48" fill="#00aba3"/>
  <path d="M272 210 h16 M280 202 v16" stroke="#007a74" stroke-width="4" stroke-linecap="round"/>
  <rect x="60" y="300" width="440" height="40" rx="10" fill="#00aba3"/>
  <text x="280" y="326" text-anchor="middle" font-family="Exo 2, sans-serif" font-weight="700" font-size="16" fill="#0f1b2d">Lokalisatie &amp; Leefcirkels</text>
  <rect x="60" y="348" width="440" height="40" rx="10" fill="#007a74"/>
  <text x="280" y="374" text-anchor="middle" font-family="Exo 2, sans-serif" font-weight="700" font-size="16" fill="#fff">CareDesk</text>
  <rect x="60" y="396" width="440" height="40" rx="10" fill="#0f1b2d"/>
  <text x="280" y="422" text-anchor="middle" font-family="Exo 2, sans-serif" font-weight="700" font-size="16" fill="#fff">Netwerkregie</text>
  <circle cx="470" cy="210" r="22" fill="#ed6a3c"/><circle cx="470" cy="210" r="44" fill="none" stroke="#ed6a3c" stroke-width="2" stroke-dasharray="4 6"/>
</svg>'''

HERO_COMP = '''<svg viewBox="0 0 560 460" role="img" aria-label="Illustratie: werkplek, netwerk en telefonie in één beheerde omgeving">
  <rect x="0" y="20" width="560" height="440" rx="18" fill="#e8f2fa"/>
  <path d="M40 150 C 70 96, 140 76, 210 84 C 256 18, 360 6, 412 40 C 448 64, 466 100, 476 132 H 540" fill="none" stroke="#9c9d9e" stroke-width="9" stroke-linecap="round"/>
  <rect x="80" y="190" width="260" height="170" rx="12" fill="#fff" stroke="#0f1b2d" stroke-width="3"/>
  <rect x="100" y="210" width="220" height="16" rx="4" fill="#e8f2fa"/>
  <rect x="100" y="238" width="100" height="100" rx="8" fill="#4697d2"/><rect x="212" y="238" width="108" height="44" rx="8" fill="#e8f2fa"/><rect x="212" y="294" width="108" height="44" rx="8" fill="#ed6a3c"/>
  <path d="M170 360 v24 M130 392 h80" stroke="#0f1b2d" stroke-width="5" stroke-linecap="round"/>
  <rect x="380" y="200" width="110" height="64" rx="10" fill="#2b74b5"/>
  <circle cx="404" cy="232" r="6" fill="#fff"/><circle cx="426" cy="232" r="6" fill="#fff"/><circle cx="448" cy="232" r="6" fill="#e8f2fa"/>
  <rect x="390" y="290" width="90" height="130" rx="14" fill="#0f1b2d"/><rect x="402" y="306" width="66" height="84" rx="6" fill="#4697d2"/>
  <path d="M340 232 H380 M340 330 H390" stroke="#0f1b2d" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>
</svg>'''

CAREDESK_RING = '''<svg viewBox="0 0 520 520" role="img" aria-label="Diagram: de zorgprofessional in het midden, CareDesk als regiering, leveranciers daaromheen">
  <circle cx="260" cy="260" r="236" fill="#f3f6f9"/>
  <circle cx="260" cy="260" r="150" fill="none" stroke="#007a74" stroke-width="34"/>
  <text font-family="Exo 2, sans-serif" font-weight="700" font-size="15" fill="#fff" letter-spacing="3"><textPath href="#ring" startOffset="25%" text-anchor="middle">CAREDESK · ÉÉN LOKET · REGIE</textPath></text>
  <path id="ring" d="M260 110 a150 150 0 1 1 -0.1 0" fill="none"/>
  <circle cx="260" cy="260" r="84" fill="#fff" stroke="#9c9d9e" stroke-width="2"/>
  <circle cx="260" cy="240" r="20" fill="#00aba3"/><path d="M226 292 a34 30 0 0 1 68 0" fill="#00aba3"/>
  <text x="260" y="320" text-anchor="middle" font-family="IBM Plex Sans, sans-serif" font-weight="600" font-size="13" fill="#0f1b2d">Zorgprofessional</text>
  <g font-family="IBM Plex Sans, sans-serif" font-weight="600" font-size="14" fill="#0f1b2d" text-anchor="middle">
    <rect x="210" y="16" width="100" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="260" y="39">ECD</text>
    <rect x="404" y="140" width="104" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="456" y="163">Werkplek</text>
    <rect x="404" y="344" width="104" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="456" y="367">Netwerk</text>
    <rect x="200" y="468" width="120" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="260" y="491">Koppelingen</text>
    <rect x="8" y="344" width="112" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="64" y="367">Leveranciers</text>
    <rect x="8" y="140" width="112" height="36" rx="18" fill="#fff" stroke="#dce3ea"/><text x="64" y="163">Applicaties</text>
  </g>
</svg>'''

LEEF = '''<svg viewBox="0 0 560 420" role="img" aria-label="Plattegrond met een cliënt binnen een persoonlijke leefcirkel, een medewerker en een gelokaliseerde tillift">
  <rect x="0" y="0" width="560" height="420" rx="18" fill="#e3f4f2"/>
  <g fill="#fff" stroke="#0f1b2d" stroke-width="3"><rect x="40" y="40" width="200" height="150" rx="6"/><rect x="40" y="210" width="200" height="170" rx="6"/><rect x="260" y="40" width="260" height="340" rx="6"/></g>
  <path d="M240 110 v40 M240 270 v40 M260 300 v40" stroke="#e3f4f2" stroke-width="8"/>
  <text x="56" y="70" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#4a5a6e">Huiskamer</text>
  <text x="56" y="240" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#4a5a6e">Kamer 12</text>
  <text x="276" y="70" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#4a5a6e">Gang &amp; tuin</text>
  <ellipse cx="300" cy="190" rx="200" ry="120" fill="#00aba3" fill-opacity=".14" stroke="#007a74" stroke-width="2.5" stroke-dasharray="8 7"/>
  <circle cx="330" cy="200" r="14" fill="#00aba3"/><text x="352" y="205" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#0f1b2d">Cliënt</text>
  <circle cx="78" cy="300" r="14" fill="#4697d2"/><text x="98" y="305" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#0f1b2d">Medewerker</text>
  <rect x="430" y="300" width="28" height="28" rx="6" fill="#ed6a3c"/><text x="420" y="350" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600" fill="#0f1b2d">Tillift</text>
  <path d="M470 50 l18 0 l0 40" fill="none" stroke="#ed6a3c" stroke-width="3"/><text x="400" y="110" font-family="IBM Plex Sans, sans-serif" font-size="12" fill="#4a5a6e">Deur volgt leefcirkel</text>
</svg>'''

def art(kind):
    # kleine kaartillustraties voor de drie proposities
    base = '<svg viewBox="0 0 320 180" aria-hidden="true"><rect width="320" height="180" fill="var(--accent-soft)"/>'
    wl = '<path d="M20 70 C 40 40, 80 30, 120 34 C 146 4, 200 -2, 230 14 C 252 26, 262 44, 268 62 H 320" fill="none" stroke="#9c9d9e" stroke-width="5" stroke-linecap="round"/>'
    if kind == 'net':
        b = '<g stroke="#0f1b2d" stroke-width="2.5" fill="#fff"><circle cx="160" cy="110" r="18" fill="#007a74"/><circle cx="80" cy="140" r="12"/><circle cx="240" cy="140" r="12"/><circle cx="100" cy="80" r="12"/><circle cx="220" cy="80" r="12"/></g><path d="M160 110 L80 140 M160 110 L240 140 M160 110 L100 80 M160 110 L220 80" stroke="#0f1b2d" stroke-width="2"/>'
    elif kind == 'care':
        b = '<circle cx="160" cy="110" r="46" fill="none" stroke="#007a74" stroke-width="14"/><circle cx="160" cy="102" r="10" fill="#00aba3"/><path d="M142 128 a18 16 0 0 1 36 0" fill="#00aba3"/><g fill="#fff" stroke="#dce3ea"><rect x="40" y="96" width="56" height="24" rx="12"/><rect x="224" y="96" width="56" height="24" rx="12"/></g>'
    elif kind == 'asset':
        b = '<g stroke="#0f1b2d" stroke-width="2.5" fill="#fff"><rect x="96" y="70" width="128" height="80" rx="10"/></g><rect x="110" y="84" width="60" height="10" rx="5" fill="#e3f4f2"/><rect x="110" y="102" width="40" height="10" rx="5" fill="#e3f4f2"/><path d="M196 92 a14 14 0 1 1 -0.1 0" fill="none" stroke="#007a74" stroke-width="4"/><path d="M206 116 l12 12" stroke="#007a74" stroke-width="5" stroke-linecap="round"/><rect x="110" y="122" width="22" height="16" rx="4" fill="#ed6a3c"/><circle cx="60" cy="128" r="9" fill="#00aba3"/><circle cx="262" cy="104" r="9" fill="#00aba3"/>'
    else:
        b = '<ellipse cx="160" cy="116" rx="96" ry="48" fill="#00aba3" fill-opacity=".18" stroke="#007a74" stroke-width="2" stroke-dasharray="6 6"/><circle cx="170" cy="116" r="10" fill="#00aba3"/><rect x="226" y="126" width="18" height="18" rx="4" fill="#ed6a3c"/><circle cx="96" cy="100" r="9" fill="#4697d2"/>'
    return base + wl + b + '</svg>'

# ---------- HOME ----------
r = ''
page('', 'SilverCloud – Betrouwbare IT voor het mkb en de zorg',
 'SilverCloud is één partner met twee expertises: SilverCloud Computing voor het mkb en SilverCloud Zorg voor zorgorganisaties.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Eén partner, twee expertises</span>
    <h1 class="display">Technologie die gewoon werkt.</h1>
    <p class="lead">SilverCloud helpt mkb- en zorgorganisaties met stabiele, veilige en toekomstgerichte IT. Wij nemen de regie, zodat u zich kunt richten op uw klanten, cliënten en medewerkers.</p>
    <div class="actions"><a class="btn btn-primary" href="computing/">Voor het mkb</a><a class="btn btn-primary label-zorg" style="--accent:var(--zorg)" href="zorg/">Voor de zorg</a></div>
  </div>
  <div class="hero-visual">{HERO_HOME}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Onze labels</span><h2>Waar kunnen wij u mee helpen?</h2>
  <div class="lijn"><p class="lead">Twee labels, één organisatie. Dezelfde mensen, dezelfde werkwijze, met kennis van uw sector.</p></div></div>
  <div class="grid-2">
    <a class="label-card label-computing" href="computing/">
      <span class="kicker">SilverCloud Computing</span>
      <h3 style="font-size:28px">IT zonder zorgen voor het mkb</h3>
      <p class="muted">Wij beheren uw werkplekken, netwerk, telefonie en helpdesk, tegen transparante kosten.</p>
      <ul><li>Digitale werkplek (BrainOnline 375)</li><li>Slimme, veilige netwerken</li><li>Zakelijke telefonie</li><li>Helpdesk en beheer</li></ul>
      <span class="go">Naar Computing →</span>
    </a>
    <a class="label-card label-zorg" href="zorg/">
      <span class="kicker">SilverCloud Zorg</span>
      <h3 style="font-size:28px">Technologie die werkt voor de zorg</h3>
      <p class="muted">Wij verbinden infrastructuur, ondersteuning en zorgtechnologie, zodat er meer ruimte is voor zorg.</p>
      <ul><li>Netwerkregie</li><li>CareDesk: de servicedesk voor de zorg</li><li>Lokalisatie &amp; Leefcirkels</li><li>Hulpmiddelenbeheer met AssetGuard</li></ul>
      <span class="go">Naar Zorg →</span>
    </a>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Waarom SilverCloud</span><h2>Regie over techniek, ruimte voor uw werk</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('oog')}<h3>Wij kennen uw praktijk</h3><p>We begrijpen wat een storing betekent op de werkvloer, in de winkel of op de afdeling.</p></div>
    <div class="card flat">{icon('netwerk')}<h3>Samenhang</h3><p>Architectuur, implementatie, leveranciersregie en beheer in één hand.</p></div>
    <div class="card flat">{icon('klok')}<h3>Continuïteit</h3><p>We denken in levenscyclus en roadmap, niet in losse projecten.</p></div>
    <div class="card flat">{icon('mens')}<h3>Korte lijnen</h3><p>Persoonlijk contact met specialisten die uw omgeving kennen.</p></div>
  </div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Onze werkwijze</span><h2>Van advies tot continu verbeteren</h2>
  <p class="lead">Projectondersteuning is geen los product. Het is hoe wij werken, bij elke oplossing.</p></div>
  {steps(WERKWIJZE)}
</div></section>

<section class="section"><div class="container narrow">
  <figure class="quote lijn accent"><blockquote>“In SilverCloud vonden we een partner die actief meedacht, kennis had van de zorgsector en ervaring met integraties.”</blockquote><figcaption>Wiebe de Vries, Zorggroep Elde Maasduinen · <a href="kennis/#zgem">Lees de case</a></figcaption></figure>
</div></section>

{cta('Waar staat uw organisatie nu?', 'Plan een vrijblijvend kennismakingsgesprek. We kijken samen naar uw huidige omgeving en de eerste stappen.', 'Plan een kennismaking', 'contact/', r)}
''', nav='home')

# ---------- COMPUTING ----------
r = '../'
page('computing', 'SilverCloud Computing – De managed service provider voor het mkb',
 'SilverCloud Computing beheert werkplekken, netwerken, telefonie en helpdesk voor het mkb, tegen transparante kosten.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">SilverCloud Computing</span>
    <h1 class="display">De managed service provider voor het mkb</h1>
    <p class="lead">Wij nemen alle zorgen rond uw IT uit handen. Van werkplek en netwerk tot telefonie en helpdesk: wij zorgen dat alles werkt, tegen transparante kosten.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Neem contact op</a><a class="btn btn-link" href="#diensten">Bekijk de diensten</a></div>
  </div>
  <div class="hero-visual">{HERO_COMP}</div>
</div></section>

<section class="section mist" id="diensten"><div class="container">
  <div class="section-head"><span class="kicker">Onze diensten</span><h2>Alles wat uw IT nodig heeft, in één beheerde omgeving</h2>
  <div class="lijn"><p class="lead">U krijgt één aanspreekpunt en vaste afspraken. Wij houden de techniek up-to-date en veilig.</p></div></div>
  <div class="grid-2">
    <div class="card" id="werkplek">{icon('werkplek')}<h3>Digitale werkplek: BrainOnline 375</h3><p>Een veilige, beheerde werkplek met Microsoft 365, uw bedrijfsapplicaties en back-up. Op kantoor en thuis werkt u in dezelfde vertrouwde omgeving.</p><a class="btn-link" href="{r}contact/">Vraag een voorstel aan</a></div>
    <div class="card" id="netwerken">{icon('netwerk')}<h3>Slimme netwerken</h3><p>Stabiele en veilige netwerken met next-generation firewalls, wifi en proactieve monitoring. Inclusief de internetverbinding die bij uw locatie past.</p><a class="btn-link" href="{r}contact/">Bespreek uw netwerk</a></div>
    <div class="card" id="telefonie">{icon('telefoon')}<h3>Zakelijke telefonie</h3><p>Hosted telefonie met mobiele apps, wachtrijen en rapportages. Bereikbaar waar u ook werkt.</p><a class="btn-link" href="{r}contact/">Meer over telefonie</a></div>
    <div class="card" id="helpdesk">{icon('helpdesk')}<h3>Helpdesk &amp; beheer</h3><p>Menselijke, deskundige support van mensen die uw omgeving kennen. Met duidelijke servicelevels en rapportages.</p><a class="btn-link" href="{r}contact/">Neem contact op</a></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="grid-3">
    <div>{icon('mens')}<h3 style="margin:16px 0 8px">Menselijk</h3><p class="muted">Persoonlijke service en korte lijnen met specialisten.</p></div>
    <div>{icon('oog')}<h3 style="margin:16px 0 8px">Transparant</h3><p class="muted">Een vaste prijs per gebruiker en heldere afspraken. Geen verrassingen.</p></div>
    <div>{icon('schild')}<h3 style="margin:16px 0 8px">Proactief en veilig</h3><p class="muted">Monitoring, updates en beveiliging vóórdat er iets misgaat.</p></div>
  </div>
</div></section>

<section class="section mist"><div class="container narrow">
  <span class="kicker">Veelgestelde vragen</span><h2 style="margin-bottom:16px">Goed om te weten</h2>
  <details><summary>Voor welke organisaties werkt SilverCloud Computing?</summary><p>[Invullen vanuit het doelgroep-/marktsegmentdocument, bijvoorbeeld omvang en sectoren.]</p></details>
  <details><summary>Kunnen we overstappen zonder stilstand?</summary><p>Ja. We plannen de migratie projectmatig, testen vooraf en schakelen over op een moment dat u het minst merkt.</p></details>
  <details><summary>Hoe zit het met de kosten?</summary><p>U betaalt een vast bedrag per gebruiker per maand voor werkplek en beheer. Wat er wel en niet in zit, leggen we vooraf vast.</p></details>
</div></section>

{cta('Klaar voor IT zonder zorgen?', 'Vertel ons hoe uw organisatie werkt. We komen met een concreet voorstel.', 'Neem contact op', r + 'contact/', r)}
''', label='computing', nav='computing')

# ---------- ZORG overzicht ----------
r = '../'
page('zorg', 'SilverCloud Zorg – Technologie die werkt voor de zorg',
 'SilverCloud Zorg verbindt netwerk, servicedesk en zorgtechnologie: Netwerkregie, CareDesk, Lokalisatie & Leefcirkels en hulpmiddelenbeheer met AssetGuard.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">SilverCloud Zorg</span>
    <h1 class="display">Technologie die werkt voor de zorg</h1>
    <p class="lead">SilverCloud verbindt infrastructuur, ondersteuning en zorgtechnologie. Zo zijn zorgorganisaties minder tijd kwijt aan techniek en houden ze meer ruimte voor goede, veilige zorg.</p>
    <div class="actions"><a class="btn btn-primary" href="#oplossingen">Ontdek onze oplossingen</a><a class="btn btn-secondary" href="{r}contact/">Plan een kennismaking</a></div>
  </div>
  <div class="hero-visual">{HERO_ZORG}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">De uitdaging</span><h2>De zorg wordt digitaler. De samenhang wordt belangrijker.</h2>
  <div class="lijn accent"><p class="lead">Netwerken, ECD’s, cloud, mobiele devices, alarmering en domotica zijn onderdeel van het primaire proces. Elk onderdeel moet werken, maar vooral het geheel.</p></div></div>
  <div class="grid-3">
    <div class="card flat">{icon('netwerk')}<h3>Infrastructuur</h3><p>Losse uitbreidingen maken het netwerk kwetsbaar. Een storing raakt direct de zorgapplicaties, alarmering en communicatie.</p></div>
    <div class="card flat">{icon('helpdesk')}<h3>Ondersteuning</h3><p>Medewerkers weten niet waar ze met hun vraag terechtkunnen. Leveranciers wijzen naar elkaar.</p></div>
    <div class="card flat">{icon('pin')}<h3>Zorgtechnologie</h3><p>Systemen voor alarmering, lokalisatie en toegang werken naast elkaar in plaats van samen.</p></div>
  </div>
</div></section>

<section class="section" id="oplossingen"><div class="container">
  <div class="section-head"><span class="kicker">Vier oplossingen</span><h2>Van digitale basis tot ondersteuning op de werkvloer</h2></div>
  <div class="grid-2">
    <a class="prop-card" href="netwerkregie/"><div class="art">{art('net')}</div><div class="body"><span class="num">01 · NETWERKREGIE</span><h3>Een netwerk waarop de zorg kan vertrouwen</h3><span class="tags">Architectuur · Security · Monitoring · Lifecycle</span><span class="btn-link">Meer over Netwerkregie</span></div></a>
    <a class="prop-card" href="caredesk/"><div class="art">{art('care')}</div><div class="body"><span class="num">02 · CAREDESK</span><h3>Een servicedesk die de taal van de zorg spreekt</h3><span class="tags">Support · Applicatiekennis · Eén loket · Ketenregie</span><span class="btn-link">Meer over CareDesk</span></div></a>
    <a class="prop-card" href="lokalisatie-leefcirkels/"><div class="art">{art('lok')}</div><div class="body"><span class="num">03 · LOKALISATIE &amp; LEEFCIRKELS</span><h3>Weten waar het ertoe doet</h3><span class="tags">Lokalisatie · Leefcirkels · Alarmering · Assettracking</span><span class="btn-link">Meer over Lokalisatie</span></div></a>
    <a class="prop-card" href="assetguard/"><div class="art">{art('asset')}</div><div class="body"><span class="num">04 · HULPMIDDELENBEHEER</span><h3>Elk hulpmiddel binnen seconden gevonden</h3><span class="tags">AssetGuard · Snelvinden · TOPdesk · Inzicht</span><span class="btn-link">Meer over AssetGuard</span></div></a>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Waarom SilverCloud Zorg</span><h2>De verbindende laag tussen zorg en technologie</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('oog')}<h3>Wij kennen de zorg</h3><p>We begrijpen de impact van storingen en veranderingen op de werkvloer.</p></div>
    <div class="card flat">{icon('netwerk')}<h3>Wij verbinden</h3><p>Architectuur, implementatie, leveranciersregie en beheer in samenhang.</p></div>
    <div class="card flat">{icon('klok')}<h3>Continuïteit</h3><p>We werken vanuit levenscyclus en roadmap, niet vanuit losse projecten.</p></div>
    <div class="card flat">{icon('mens')}<h3>Bruikbaar</h3><p>Technologie wordt pas waardevol als mensen en processen ermee werken.</p></div>
  </div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Onze aanpak</span><h2>Eén doorlopende lijn</h2><p class="lead">Implementatie en adoptie zijn onderdeel van elke oplossing, geen los project.</p></div>
  {steps(WERKWIJZE)}
</div></section>

{cta('Waar staat uw organisatie nu?', 'Plan een oriënterend gesprek over uw netwerk, servicedesk of zorgtechnologie.', 'Plan een kennismaking', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='zorg')

# ---------- NETWERKREGIE ----------
r = '../../'
page('zorg/netwerkregie', 'Netwerkregie voor de zorg – SilverCloud Zorg',
 'Niet méér netwerkbeheer, wel volledige regie over uw digitale infrastructuur. Netwerkregie van SilverCloud Zorg.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Netwerkregie</span>
    <h1 class="display">Een netwerk waarop de zorg kan vertrouwen</h1>
    <p class="lead">Niet méér netwerkbeheer, wel volledige regie over uw digitale infrastructuur. Wij nemen verantwoordelijkheid voor architectuur, beveiliging, beschikbaarheid en vernieuwing van uw complete netwerk.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Vraag een netwerkassessment aan</a></div>
  </div>
  <div class="hero-visual"><div class="prop-card" style="pointer-events:none">{art('net').replace('viewBox="0 0 320 180"','viewBox="0 0 320 180" style="border-radius:14px"')}</div></div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Van beheer naar regie</span><h2>Waarom reactief netwerkbeheer niet meer volstaat</h2>
  <div class="lijn accent"><p class="lead">Zorgapplicaties, domotica, zorgalarmering, medische apparatuur en IoT maken het netwerk bedrijfskritisch. Het netwerk is de digitale ruggengraat van uw organisatie.</p></div></div>
  <div class="compare">
    <div class="before"><h3>Traditioneel netwerkbeheer</h3><ul><li>Reactief: storingen oplossen als ze er zijn</li><li>Losse projecten en uitbreidingen</li><li>Vervangen als het stuk is</li><li>Beperkt inzicht in prestaties en kosten</li></ul></div>
    <div class="after"><h3>SilverCloud Netwerkregie</h3><ul><li>Eén integraal netwerkdesign als fundament</li><li>Eén roadmap voor de hele levenscyclus</li><li>Proactief vernieuwen en standaardiseren</li><li>Gedeelde monitoring en open calculatie</li></ul></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Vijf pijlers</span><h2>Zo houden we uw netwerk beheersbaar, veilig en toekomstbestendig</h2></div>
  <div class="pillars">
    <div class="pillar"><h3>Architectuur</h3><p>Eén integraal netwerkdesign als ‘single source of truth’.</p></div>
    <div class="pillar"><h3>Regie</h3><p>Verantwoordelijkheid voor de volledige levenscyclus.</p></div>
    <div class="pillar"><h3>Transparantie</h3><p>Open calculatie en gedeeld inzicht in prestaties en investeringen.</p></div>
    <div class="pillar"><h3>Voor de zorg</h3><p>Afgestemd op woonlocaties, behandelcentra en hoofdkantoren.</p></div>
    <div class="pillar"><h3>Continu verbeteren</h3><p>Roadmap, monitoring en proactieve vernieuwing.</p></div>
  </div>
</div></section>

<section class="section mist"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Architectuur boven producten</span><h2>Eerst het ontwerp, dan de apparatuur</h2>
  <p class="lead" style="margin-top:16px">Veel leveranciers beginnen bij de apparatuur. Wij beginnen bij de architectuur. Iedere wijziging wordt getoetst aan het netwerkdesign.</p></div>
  <div class="card"><h3>Het netwerkdesign omvat onder andere</h3><ul class="muted" style="margin:0;padding-left:20px;display:grid;gap:6px"><li>Internetconnectiviteit en redundantie</li><li>Netwerksegmentatie (VLAN’s)</li><li>IP-, DNS- en DHCP-structuren</li><li>Wifi-architectuur</li><li>Securitybeleid: next-generation firewalls, ZTNA, segmentatie</li><li>Monitoring en lifecycle van componenten</li></ul></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Vier disciplines, één regiemodel</span><h2>Wat we dagelijks voor u doen</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('oog')}<h3>Monitoring</h3><p>24/7 inzicht in beschikbaarheid en prestaties.</p></div>
    <div class="card flat">{icon('bel')}<h3>Reactief beheer</h3><p>Storingen snel en gecontroleerd oplossen.</p></div>
    <div class="card flat">{icon('schild')}<h3>Proactief beheer</h3><p>Preventief onderhoud, firmware-updates en capaciteitsanalyses.</p></div>
    <div class="card flat">{icon('pad')}<h3>Doorontwikkeling</h3><p>Lifecyclemanagement, innovatie en strategische vernieuwing.</p></div>
  </div>
</div></section>

{cta('Klaar voor een netwerk dat de zorg ondersteunt?', 'Bespreek uw huidige architectuur met onze specialisten, of start met een netwerkassessment.', 'Vraag een assessment aan', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='netwerkregie')

# ---------- CAREDESK ----------
page('zorg/caredesk', 'CareDesk – de servicedesk voor de zorg – SilverCloud Zorg',
 'CareDesk is meer dan een helpdesk: één loket, kennis van zorgapplicaties en regie richting leveranciers.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">CareDesk</span>
    <h1 class="display">Een servicedesk die begrijpt waarom uw vraag nú belangrijk is</h1>
    <p class="lead">CareDesk is de servicedesk die de taal van de zorg spreekt. Met kennis van zorgapplicaties, één loket voor uw medewerkers en regie richting al uw ICT-leveranciers.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Plan een kennismaking</a><a class="btn btn-link" href="#modellen">Bekijk de inzetmodellen</a></div>
  </div>
  <div class="hero-visual">{CAREDESK_RING}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Meer dan een helpdesk</span><h2>Het traditionele helpdeskmodel past niet meer bij de zorg</h2>
  <div class="lijn accent"><p class="lead">Veel budget gaat naar generieke vragen over wachtwoorden en printers. De echte waarde zit in kennis van het ECD, koppelingen en werkprocessen.</p></div></div>
  <div class="table-wrap"><table>
    <thead><tr><th></th><th>Traditionele helpdesk</th><th>CareDesk van SilverCloud</th></tr></thead>
    <tbody>
      <tr><td>Kennisniveau</td><td>Basis IT-kennis</td><td class="us">Zorg- en ECD-expertise</td></tr>
      <tr><td>Aanpak</td><td>Reactief (break/fix)</td><td class="us">Proactief en adviserend</td></tr>
      <tr><td>Aanspreekpunt</td><td>IT-afdeling als doorgeefluik</td><td class="us">Eén loket met ketenregie</td></tr>
      <tr><td>Cultuur</td><td>Techniekgedreven</td><td class="us">Zorgbewust en dienstverlenend</td></tr>
    </tbody></table></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Wat CareDesk onderscheidt</span><h2>Zorgkennis en regie in één dienst</h2></div>
  <div class="grid-2">
    <div class="card flat">{icon('bel')}<h3>Urgentie begrijpen</h3><p>Een storing is niet alleen een ticket. Het kan het primaire proces raken, en zo handelen we ook.</p></div>
    <div class="card flat">{icon('werkplek')}<h3>Kennis van zorgapplicaties</h3><p>Thuis in veelgebruikte toepassingen zoals diverse ECD’s, Zenya en AFAS.</p></div>
    <div class="card flat">{icon('schild')}<h3>Proactief</h3><p>We voorkomen dat problemen terugkeren en verbeteren het gebruik van systemen.</p></div>
    <div class="card flat">{icon('netwerk')}<h3>Ketenregie</h3><p>Eén loket voor medewerkers en actieve coördinatie met andere ICT-leveranciers.</p></div>
  </div>
</div></section>

<section class="section mist" id="modellen"><div class="container">
  <div class="section-head"><span class="kicker">Drie inzetmodellen</span><h2>CareDesk zoals het bij uw organisatie past</h2></div>
  <div class="grid-3">
    <div class="route voorkeur"><span class="badge">Onze voorkeur</span><h3>Complete overname</h3><p class="muted">Eén volwaardige serviceorganisatie en één aanspreekpunt voor alle zorg-ICT-vragen.</p></div>
    <div class="route"><span class="badge">Versterking</span><h3>Uw team versterken</h3><p class="muted">Extra capaciteit, specialistische applicatiekennis en ruimere beschikbaarheid naast uw eigen team.</p></div>
    <div class="route"><span class="badge">Optimalisatie</span><h3>Processen verbeteren</h3><p class="muted">Incident-, change-, escalatie- en rapportageprocessen professionaliseren.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Zorgvuldige overgang</span><h2>In vier stappen naar CareDesk</h2><p class="lead">Overname of uitbreiding gebeurt altijd projectmatig, zodat het zorgproces niet wordt verstoord.</p></div>
  <div class="steps" style="grid-template-columns:repeat(4,1fr)">
    <div class="step"><h3>Audit &amp; inventarisatie</h3><p>Huidige situatie, applicaties en afspraken in kaart.</p></div>
    <div class="step"><h3>Kennisoverdracht</h3><p>Kennis vastleggen en overdragen aan het CareDesk-team.</p></div>
    <div class="step"><h3>SLA &amp; kaders</h3><p>Servicelevels, routering en escalatie afspreken.</p></div>
    <div class="step"><h3>Go-live</h3><p>Gecontroleerd live, met nazorg en rapportage.</p></div>
  </div>
</div></section>

{cta('Een servicedesk die meedenkt met de zorg?', 'We vertellen u graag hoe CareDesk in uw organisatie kan werken.', 'Plan een kennismaking', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='caredesk')

# ---------- LOKALISATIE ----------
page('zorg/lokalisatie-leefcirkels', 'Lokalisatie & Leefcirkels – powered by Evresys – SilverCloud Zorg',
 'Meer vrijheid voor cliënten, sneller hulp op de juiste plek en minder zoeken naar hulpmiddelen. Lokalisatie & Leefcirkels, powered by Evresys.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Lokalisatie &amp; Leefcirkels</span>
    <h1 class="display">Weten waar het ertoe doet</h1>
    <p class="lead">Zorgalarmering, realtime lokalisatie, persoonlijke leefcirkels en het terugvinden van hulpmiddelen in één platform. SilverCloud Zorg verzorgt advies, implementatie, integratie, adoptie en beheer.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Vraag een adviesgesprek aan</a><a class="btn btn-link" href="#routes">Twee routes</a></div>
    <p class="small muted" style="margin-top:16px">Powered by Evresys</p>
  </div>
  <div class="hero-visual">{LEEF}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Toepassingen</span><h2>Wat het oplevert op de werkvloer</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('cirkel')}<h3>Meer vrijheid voor cliënten</h3><p>Persoonlijke leefcirkels en dwaaldetectie per cliënt.</p></div>
    <div class="card flat">{icon('bel')}<h3>Sneller hulp op de juiste plek</h3><p>Bij elk alarm direct de locatie van cliënt of wearable.</p></div>
    <div class="card flat">{icon('radio')}<h3>Veiliger werken</h3><p>Persoonsalarm en Push-to-Talk voor collegiale hulp.</p></div>
    <div class="card flat">{icon('tillift')}<h3>Minder zoeken</h3><p>Tilliften, infuuspompen en andere hulpmiddelen snel gevonden.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Functionaliteiten</span><h2>Eén platform, zes functies</h2></div>
  <div class="grid-3">
    <div class="card flat">{icon('bel')}<h3>Zorgalarmering</h3><p>Melding via een wearable, direct naar de juiste medewerker.</p></div>
    <div class="card flat">{icon('pin')}<h3>Realtime lokalisatie</h3><p>Locatie van cliënt of wearable bij iedere melding, binnen en buiten.</p></div>
    <div class="card flat">{icon('cirkel')}<h3>Leefcirkels &amp; dwaaldetectie</h3><p>Bewegingsvrijheid per cliënt, met automatische signalering.</p></div>
    <div class="card flat">{icon('deur')}<h3>Deurintegratie</h3><p>Toegang die zich aanpast aan de leefcirkel van de cliënt.</p></div>
    <div class="card flat">{icon('radio')}<h3>Medewerkersveiligheid</h3><p>Persoonsalarm en Push-to-Talk maken van de smartphone een portofoon.</p></div>
    <div class="card flat">{icon('kaart')}<h3>Hulpmiddelen &amp; assettracking</h3><p>Voortbouwend op jarenlange <a href="{r}zorg/assetguard/">AssetGuard</a>-ervaring van SilverCloud.</p></div>
  </div>
</div></section>

<section class="section mist" id="routes"><div class="container">
  <div class="section-head"><span class="kicker">Twee routes, één platform</span><h2>Geen vervanging om de vervanging</h2>
  <div class="lijn accent"><p class="lead">De vraag is niet welk systeem weg moet, maar welke functies goed geregeld zijn, wat ontbreekt en wat cliënten en medewerkers de meeste waarde geeft.</p></div></div>
  <div class="grid-2">
    <div class="route"><span class="badge">Route 1</span><h3>Geïntegreerde basis</h3><p class="muted">Voor kleinere organisaties, nieuwe locaties of situaties zonder zorgoproepsysteem. Evresys vormt de basis voor alarmering, lokalisatie en leefcirkels.</p></div>
    <div class="route"><span class="badge">Route 2</span><h3>Slimme aanvulling</h3><p class="muted">Voor organisaties met een goed werkend zorgoproepsysteem. U behoudt uw investering en voegt locatie, leefcirkels en context toe.</p></div>
  </div>
</div></section>

{cta('Welke route past bij uw organisatie?', 'In een adviesgesprek brengen we samen in kaart wat er al is en wat nog ontbreekt.', 'Vraag een adviesgesprek aan', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='lokalisatie')

# ---------- HULPMIDDELENBEHEER (AssetGuard) ----------
# Bron: Realtime localisatie - IoT/Website info (productbeschrijvingen Snelvinden, Insight,
# TOPdesk-integratie, Advies), Overzicht AssetGuard.docx, 10 voordelen van Realtime lokalisatie.pdf,
# Customer Testimonial ZGEM.pdf en blog Argos-case (maart 2025).
r = '../../'
page('zorg/assetguard', 'Hulpmiddelenbeheer met AssetGuard – SilverCloud Zorg',
 'Met AssetGuard vinden zorgmedewerkers tilliften, rolstoelen en andere hulpmiddelen binnen seconden terug. Realtime lokalisatie, TOPdesk-integratie en rapportages als ontzorgende dienst.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Hulpmiddelenbeheer · AssetGuard</span>
    <h1 class="display">Nooit meer zoeken naar de tillift</h1>
    <p class="lead">Met AssetGuard ziet een zorgmedewerker in één zoekopdracht waar een hulpmiddel staat. Minder loopwerk, minder frustratie en meer tijd voor de cliënt. Voor de organisatie levert het inzicht op in gebruik, onderhoud en investeringen.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Start een pilot</a><a class="btn btn-secondary" href="#modules">Bekijk de modules</a></div>
  </div>
  <div class="hero-visual" style="border-radius:18px;overflow:hidden">{art('asset')}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Het probleem</span><h2>Zoeken kost de zorg meer dan u denkt</h2>
  <div class="lijn accent"><p class="lead">Hulpmiddelen worden gedeeld door teams en afdelingen en staan zelden op een vaste plek. Bij Argos Zorggroep bleek uit een nulmeting dat ongeveer een kwart van de werktijd opging aan het zoeken naar spullen.</p></div></div>
  <div class="grid-3">
    <div class="card flat">{icon('klok')}<h3>Tijd</h3><p>Een rondje door een groot verpleeghuis kost al snel een half uur. Tijd die van de cliënt afgaat.</p></div>
    <div class="card flat">{icon('schild')}<h3>Kwaliteit en veiligheid</h3><p>Hulpmiddelen die niet te vinden zijn, missen hun onderhoud. Bij een recall weet u niet waar ze staan.</p></div>
    <div class="card flat">{icon('kaart')}<h3>Kosten</h3><p>Zonder inzicht in gebruik wordt er bijgekocht of gehuurd, terwijl er elders hulpmiddelen ongebruikt in de kast staan.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Zo werkt het</span><h2>Een tag op het hulpmiddel, een app in de hand</h2></div>
  <div class="steps steps-4">
    <div class="step"><h3>Taggen</h3><p>Samen bepalen we welke hulpmiddelen een Bluetooth-tag (BLE) krijgen en welk type tag het beste past.</p></div>
    <div class="step"><h3>Uw netwerk benutten</h3><p>We inventariseren uw wifi-accesspoints. Waar nodig maken we het netwerk geschikt, in overleg met uw netwerkbeheerder.</p></div>
    <div class="step"><h3>Zoeken en vinden</h3><p>Typ bijvoorbeeld “tillift” in de app op telefoon of tablet en zie direct de actuele locaties.</p></div>
    <div class="step"><h3>Scannen</h3><p>Scan de QR-code op de tag voor de laatste onderhoudsdatum en gebruiksinstructies.</p></div>
  </div>
</div></section>

<section class="section mist" id="modules"><div class="container">
  <div class="section-head"><span class="kicker">Modulair platform</span><h2>Begin met vinden, groei naar regie</h2>
  <p class="lead">AssetGuard bestaat uit modules die u stap voor stap inzet. Alles wordt geleverd als ontzorgende dienst, in samenwerking met Blyott.</p></div>
  <div class="grid-2">
    <div class="card">{icon('pin')}<h3>AssetGuard Snelvinden</h3><p>De kernmodule: realtime locatie, status en beschikbaarheid van bedden, tilliften, rolstoelen, infuuspompen, maar ook laptops of VR-brillen. Afhankelijk van uw accesspoints filtert de AssetGuard Proxyserver de Bluetooth-signalen, zodat er geen onnodig dataverkeer ontstaat.</p></div>
    <div class="card">{icon('netwerk')}<h3>AssetGuard Integratie (TOPdesk)</h3><p>Een tweerichtingskoppeling met TOPdesk Asset Management. Locatie, temperatuur en batterijstatus komen in TOPdesk, en onderhoudsgegevens uit TOPdesk zijn zichtbaar in de app. Een tag koppelt u in twee seconden via een QR-scan. Is TOPdesk nog niet ingericht? Dan helpt <em>TOPdesk Get Ready</em> u op weg.</p></div>
    <div class="card">{icon('oog')}<h3>AssetGuard Insight</h3><p>Power BI-dashboards in uw eigen huisstijl: gebruiksgraad, beschikbaarheid, onderhoudsstatus, zoekgedrag en batterijstatus. Ook zichtbaar: hoe vaak een tilband is gewassen of dat een medicijnkar een temperatuurgrens heeft overschreden.</p></div>
    <div class="card">{icon('mens')}<h3>Advies, training en consultancy</h3><p>Hulp bij een hulpmiddelenstrategie, projectmanagement van initiatie tot oplevering, inrichting van TOPdesk Asset Management en adoptiebegeleiding op de werkvloer.</p></div>
  </div>
  <p class="muted" style="margin-top:24px">In ontwikkeling: <strong>AssetGuard Workflow</strong>, voor geautomatiseerde werkprocessen en taakbeheer rond hulpmiddelen.</p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">AssetGuard Insight</span><h2>Van onderbuikgevoel naar onderbouwde keuzes</h2>
  <p class="lead">Zijn er echt te weinig tilliften, of staan ze op de verkeerde plek? Insight laat het zien.</p></div>
  <figure class="shot"><img src="{r}assets/img/assetguard-insight-dashboard.jpg" alt="Dashboard van AssetGuard Insight met bewegingen per locatie en per hulpmiddel" width="1400" height="608" loading="lazy"><figcaption>Voorbeeld uit AssetGuard Insight: bewegingen per locatie en per hulpmiddel.</figcaption></figure>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Wat het oplevert</span><h2>Resultaat voor de hele organisatie</h2></div>
  <div class="stats">
    <div class="stat"><strong>99%</strong><span>van de hulpmiddelen correct onderhouden, doordat alles vindbaar is</span></div>
    <div class="stat"><strong>10–15%</strong><span>mogelijke besparing op nieuwe aanschaf of huur, door beter gebruik van wat er al is</span></div>
    <div class="stat"><strong>1.700</strong><span>tags in gebruik bij Zorggroep Elde Maasduinen, inclusief TOPdesk-koppeling</span></div>
  </div>
  <div class="grid-3" style="margin-top:48px">
    <div><h3>Zorgmedewerker</h3><p>Weet in seconden waar het hulpmiddel staat en loopt er in één keer naartoe.</p></div>
    <div><h3>Manager en facilitair</h3><p>Ziet wat niet of nauwelijks wordt gebruikt en onderbouwt investeringen met data.</p></div>
    <div><h3>Cliënt</h3><p>Wordt sneller geholpen, omdat de medewerker minder lang weg is om iets te zoeken.</p></div>
  </div>
</div></section>

<section class="section"><div class="container narrow">
  <figure class="quote lijn accent"><blockquote>“Je ziet dat medewerkers die het systeem een paar keer hebben gebruikt, niet meer zonder willen.”</blockquote><figcaption>Janneke Boevink, projectleider, Argos Zorggroep · <a href="{r}kennis/#argos">Lees de case</a></figcaption></figure>
</div></section>

<section class="section mist"><div class="container narrow">
  <span class="kicker">Service</span><h2 style="margin-bottom:16px">Goed om te weten</h2>
  <details><summary>Hoe wordt AssetGuard geleverd?</summary><p>Als dienst (SaaS) met 24/7 monitoring en een Nederlandstalige helpdesk tijdens kantooruren. Bij een storing herstelt het systeem zichzelf automatisch.</p></details>
  <details><summary>Wat als er hulpmiddelen of kamers bijkomen?</summary><p>Nieuwe hulpmiddeltypes, accesspoints, tagtypes en kamernummerwijzigingen zijn inbegrepen in de dienstverlening, zonder extra kosten.</p></details>
  <details><summary>Wat kost het?</summary><p>De implementatie heeft een vast tarief: inventarisatie van het netwerk, installatie, configuratie en een dag ondersteuning voor gebruikers en beheerders. Daarnaast betaalt u een maandbedrag. Voor Insight is per gebruiker een Power BI Pro-licentie nodig. Actuele prijzen ontvangt u op aanvraag.</p></details>
  <details><summary>Wat is het verschil met Lokalisatie &amp; Leefcirkels?</summary><p>AssetGuard richt zich op hulpmiddelen. <a href="{r}zorg/lokalisatie-leefcirkels/">Lokalisatie &amp; Leefcirkels</a> (powered by Evresys) richt zich op cliënten en medewerkers: alarmering, lokalisatie en persoonlijke leefcirkels. Beide sluiten op elkaar aan.</p></details>
</div></section>

{cta('Ook meer tijd voor goede zorg?', 'We helpen u graag met het opzetten van een pilot op één locatie.', 'Bespreek een pilot', r + 'contact/', r, 'Lees de klantcases', r + 'kennis/')}
''', label='zorg', nav='zorg', sub='assetguard')

# ---------- KENNIS & CASES ----------
r = '../'
page('kennis', 'Kennis & cases – SilverCloud',
 'Praktijkverhalen van zorgorganisaties en whitepapers van SilverCloud over netwerkregie en realtime lokalisatie.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Kennis &amp; cases</span>
  <h1 class="display" style="margin:16px 0">Uit de praktijk</h1>
  <p class="lead">Hoe organisaties met SilverCloud werken, en wat ze daarvan leerden. Plus onze whitepapers om verder te lezen.</p>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Klantcases</span><h2>Zorgorganisaties aan het woord</h2></div>
  <div class="grid-2">
    <article class="card case" id="argos">
      <span class="kicker">Argos Zorggroep · AssetGuard Snelvinden</span>
      <h3>“Een kwart van de werktijd ging verloren aan zoeken”</h3>
      <p>Argos Zorggroep heeft 11 locaties in de regio Rotterdam. Een nulmeting liet zien dat medewerkers ongeveer een kwart van hun werktijd kwijt waren aan zoeken. In februari 2024 startte een pilot in verpleeghuis Breede Vliet (180 bewoners). De resultaten waren zo goed dat de oplossing naar drie nieuwe locaties gaat.</p>
      <p><strong>Lessen:</strong> betrek teamleiders vanaf het begin, stel per locatie een projectgroep samen met verschillende functies en bepaal per huis welke hulpmiddelen een tag krijgen.</p>
      <blockquote class="mini">“Mensen kijken even in de app en gaan dan gelijk de goede richting op.” <span>Arco Olofsen, Manager Wonen &amp; Zorg, Breede Vliet</span></blockquote>
    </article>
    <article class="card case" id="zgem">
      <span class="kicker">Zorggroep Elde Maasduinen · RTLS + TOPdesk</span>
      <h3>1.700 tags en één bronsysteem</h3>
      <p>Na eerdere proeven met wifi-oplossingen koos ZGEM voor de Bluetooth Low Energy-oplossing van Blyott, met SilverCloud als systeemintegrator. TOPdesk is het bronsysteem; SilverCloud bouwde de koppeling met het lokalisatiesysteem. Een zorgtechnoloog met verpleegkundige achtergrond begeleidde de adoptie vanaf de pilotlocatie.</p>
      <blockquote class="mini">“In SilverCloud vonden we een partner die actief meedacht en kennis had van de zorgsector.” <span>Wiebe de Vries, ZGEM</span></blockquote>
      <a class="btn-link" href="{r}assets/downloads/klantcase-zgem-realtime-lokalisatie.pdf">Download de case (pdf)</a>
    </article>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Downloads</span><h2>Whitepapers en factsheets</h2></div>
  <div class="grid-3">
    <a class="card download" href="{r}assets/downloads/whitepaper-netwerkregie-zorg.pdf">{icon('netwerk')}<h3>Whitepaper: Netwerkregie voor de zorg</h3><p>Van technisch netwerkbeheer naar een veilige, voorspelbare en toekomstbestendige infrastructuur. Vijf uitgangspunten.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/10-voordelen-realtime-lokalisatie.pdf">{icon('pin')}<h3>10 voordelen van realtime lokalisatie</h3><p>Wat lokalisatie oplevert voor de zorgmedewerker, de zorgmanager en de cliënt.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/klantcase-zgem-realtime-lokalisatie.pdf">{icon('mens')}<h3>Klantcase Zorggroep Elde Maasduinen</h3><p>Realtime lokalisatie met TOPdesk-integratie in de praktijk.</p><span class="btn-link">Download (pdf)</span></a>
  </div>
</div></section>

{cta('Wilt u zo’n resultaat ook?', 'We delen graag onze ervaringen en kijken samen wat bij uw organisatie past.', 'Neem contact op', r + 'contact/', r)}
''', nav='kennis')

# ---------- OVER ONS ----------
r = '../'
page('over-ons', 'Over SilverCloud – werkwijze en visie',
 'SilverCloud combineert technische expertise met kennis van het mkb en de zorg. Lees over onze visie en werkwijze.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Over SilverCloud</span>
  <h1 class="display" style="margin:16px 0">De verbindende laag tussen mensen en technologie</h1>
  <p class="lead">SilverCloud helpt organisaties om technologie betrouwbaar onderdeel te maken van hun dagelijkse werk. We combineren technische expertise met kennis van de praktijk, en nemen verantwoordelijkheid voor de samenhang.</p>
  <div class="lijn"><p>We werken naast uw interne organisatie en andere leveranciers. Niet vanuit losse producten, maar vanuit architectuur, duidelijke regie en een gezamenlijke roadmap. Zo ontstaat een omgeving die vandaag betrouwbaar werkt en morgen kan meegroeien.</p></div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Onze werkwijze</span><h2>Zes stappen, één lijn</h2></div>
  {steps(WERKWIJZE)}
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Waar we voor staan</span><h2>Onze principes</h2></div>
  <div class="grid-2">
    <div class="card flat"><h3>Praktijk vóór techniek</h3><p>We beginnen bij continuïteit, veiligheid en werkprocessen. De techniek volgt.</p></div>
    <div class="card flat"><h3>Regie vóór losse producten</h3><p>Architectuur, leveranciers en beheer als samenhangend geheel.</p></div>
    <div class="card flat"><h3>Pragmatisch vernieuwen</h3><p>Behouden wat goed werkt, gericht toevoegen waar waarde ontbreekt.</p></div>
    <div class="card flat"><h3>Transparant samenwerken</h3><p>Inzicht, duidelijke verantwoordelijkheden en voorspelbare afspraken.</p></div>
  </div>
</div></section>

<section class="section mist"><div class="container narrow">
  <span class="kicker">Het team</span><h2>De mensen achter SilverCloud</h2>
  <p class="lead" style="margin-top:16px">[Teamfoto en korte introductie invullen.]</p>
</div></section>

{cta('Kennismaken?', 'We horen graag waar uw organisatie staat en waar u naartoe wilt.', 'Neem contact op', '../contact/' , r)}
''', nav='over')

# ---------- CONTACT ----------
page('contact', 'Contact – SilverCloud', 'Neem contact op met SilverCloud voor een kennismaking of adviesgesprek.', f'''
<section class="hero"><div class="container grid-2" style="align-items:start">
  <div>
    <span class="badge">Contact</span>
    <h1 class="display" style="margin:16px 0">Laten we kennismaken</h1>
    <p class="lead">Vertel ons kort waar u mee bezig bent. We nemen binnen één werkdag contact met u op.</p>
    <div class="lijn" style="margin-top:32px">
      <p><strong>SilverCloud</strong><br>Ohmstraat 18-A<br>3861 NB Nijkerk</p>
      <p><a href="tel:+31882560050">088 256 00 50</a><br><a href="mailto:info@silvercloud.nl">info@silvercloud.nl</a></p>
    </div>
  </div>
  <form class="form card" action="#" method="post" onsubmit="alert('Dit is een concept: het formulier is nog niet gekoppeld.'); return false;">
    <p class="note">Concept: dit formulier is nog niet gekoppeld aan een mailbox of CRM.</p>
    <div class="row"><label>Naam<input name="naam" autocomplete="name" required></label><label>Organisatie<input name="organisatie" autocomplete="organization"></label></div>
    <div class="row"><label>E-mailadres<input type="email" name="email" autocomplete="email" required></label><label>Telefoon<input type="tel" name="telefoon" autocomplete="tel"></label></div>
    <label>Waar gaat uw vraag over?<select name="onderwerp"><option>SilverCloud Computing (mkb)</option><option>Netwerkregie (zorg)</option><option>CareDesk (zorg)</option><option>Lokalisatie &amp; Leefcirkels (zorg)</option><option>Hulpmiddelenbeheer / AssetGuard (zorg)</option><option>Iets anders</option></select></label>
    <label>Uw vraag<textarea name="bericht"></textarea></label>
    <button class="btn btn-primary" type="submit">Verstuur</button>
  </form>
</div></section>
''', nav='')
print('ok')
