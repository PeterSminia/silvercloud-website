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
from extra import latest, logo_strip, wp_card, certs, zorgkennis, tech_partners, POSTS, EVRESYS_URL, EVRESYS_LEEF, BLYOTT_URL, BLYOTT_AT
import extra

def icon(n):
    return f'<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{ICON[n]}</svg></span>'

WOLK = '<svg class="wolk" viewBox="0 0 400 160" aria-hidden="true"><path d="M10 120 C 30 80, 80 64, 140 70 C 175 20, 245 8, 290 24 C 330 38, 352 70, 364 98 H 400" fill="none" stroke="#9c9d9e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def page(path, title, desc, body, label='', nav='', sub=None):
    depth = path.count('/') + 1 if path else 0
    r = '../' * depth
    zorg = label == 'zorg'
    logo = f'<img src="{r}assets/img/silvercloud-zorg-logo-donker.svg" alt="SilverCloud Zorg">' if zorg else f'<img src="{r}assets/img/silvercloud-logo-kleur.svg" alt="SilverCloud">'
    items = [('', 'Home', 'home'), ('computing/', 'Computing', 'computing'), ('zorg/', 'Zorg', 'zorg'), ('kennis/', 'Kennis &amp; cases', 'kennis'), ('blog/', 'Blog', 'blog'), ('over-ons/', 'Over ons', 'over')]
    menu = ''.join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if k == nav else ""}>{t}</a></li>' for h, t, k in items)
    subnav = ''
    if sub:
        subs = [('zorg/', 'Overzicht', 'zorg', ''), ('zorg/netwerkregie/', 'Netwerkregie', 'netwerkregie', ''), ('zorg/caredesk/', 'CareDesk', 'caredesk', ''), ('zorg/zorgtechnologie/', 'Zorgtechnologie', 'zorgtech', ''),
                ('zorg/lokalisatie-leefcirkels/', 'Lokalisatie & Leefcirkels', 'lokalisatie', 'child child-first'), ('zorg/medewerkersveiligheid/', 'Medewerkersveiligheid', 'veiligheid', 'child'), ('zorg/assetguard/', 'Hulpmiddelenbeheer', 'assetguard', 'child')]
        kids = ('lokalisatie', 'veiligheid', 'assetguard')
        def _a(h, t, k):
            cur = ' aria-current="page"' if k == sub else (' class="parent-active"' if k == 'zorgtech' and sub in kids else '')
            return f'<a href="{r}{h}"{cur}>{t}</a>'
        subnav = '<nav class="sub-nav" aria-label="SilverCloud Zorg"><div class="container"><ul>' + ''.join(f'<li{(" class=" + chr(34) + c + chr(34)) if c else ""}>{_a(h, t, k)}</li>' for h, t, k, c in subs) + '</ul></div></nav>'
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
    <ul class="menu" id="menu">{menu}<li><a class="btn btn-primary" href="{r}afspraak/">Plan een afspraak</a></li></ul>
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
        <div class="footer-certs"><a href="{r}{extra.CERT_URLS[0][2]}">NEN 7510</a><a href="{r}{extra.CERT_URLS[1][2]}">ISO 27001</a><a href="{r}{extra.CERT_URLS[2][2]}">ISO 9001</a></div>
      </div>
      <div><h4>Computing</h4><ul><li><a href="{r}computing/#werkplek">Moderne werkplek</a></li><li><a href="{r}computing/#netwerken">Veilig netwerk</a></li><li><a href="{r}computing/#applicaties">Toegang tot applicaties</a></li><li><a href="{r}computing/#helpdesk">Servicedesk</a></li></ul></div>
      <div><h4>Zorg</h4><ul><li><a href="{r}zorg/netwerkregie/">Netwerkregie</a></li><li><a href="{r}zorg/caredesk/">CareDesk</a></li><li><a href="{r}zorg/zorgtechnologie/">Zorgtechnologie</a></li><li><a href="{r}zorg/lokalisatie-leefcirkels/">Lokalisatie &amp; Leefcirkels</a></li><li><a href="{r}zorg/medewerkersveiligheid/">Medewerkersveiligheid</a></li><li><a href="{r}zorg/assetguard/">Hulpmiddelenbeheer (AssetGuard)</a></li></ul></div>
      <div><h4>SilverCloud</h4><ul><li><a href="{r}over-ons/">Over ons &amp; werkwijze</a></li><li><a href="{r}kennis/">Kennis &amp; cases</a></li><li><a href="{r}blog/">Blog</a></li><li><a href="{r}partners/">Partners</a></li><li><a href="{r}afspraak/">Plan een afspraak</a></li><li><a href="{r}contact/">Contact</a></li><li><a href="{r}kwaliteit-informatiebeveiliging/">Kwaliteit &amp; certificering</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>© 2026 SilverCloud</span><span>Ohmstraat 18-A, 3861 NB Nijkerk · <a href="tel:+31882560050">088 256 00 50</a> · <a href="mailto:info@silvercloud.nl">info@silvercloud.nl</a> · KvK [invullen]</span><span><a href="{r}privacyverklaring/">Privacyverklaring</a> · <a href="{r}cookiebeleid/">Cookiebeleid</a> · <a href="{r}toegankelijkheidsverklaring/">Toegankelijkheid</a></span></div>
  </div>
</footer>
<span class="concept" title="Voorstel, nog niet definitief">Concept v0.4</span>
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
    elif kind == 'safe':
        b = '<circle cx="160" cy="112" r="58" fill="none" stroke="#ed6a3c" stroke-width="2" stroke-dasharray="4 6"/><circle cx="160" cy="112" r="38" fill="none" stroke="#ed6a3c" stroke-width="2"/><circle cx="160" cy="100" r="11" fill="#0f1b2d"/><path d="M140 136 a20 18 0 0 1 40 0" fill="#0f1b2d"/><rect x="172" y="114" width="16" height="22" rx="4" fill="#ed6a3c"/><circle cx="180" cy="121" r="3" fill="#fff"/><circle cx="70" cy="128" r="9" fill="#007a74"/><circle cx="250" cy="96" r="9" fill="#007a74"/><path d="M79 126 L124 116 M241 98 L196 106" stroke="#007a74" stroke-width="2" stroke-dasharray="3 5"/>'
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
    <p class="small muted" style="margin-top:16px">Gecertificeerd voor NEN 7510, ISO 27001 en ISO 9001</p>
  </div>
  <div class="hero-visual">{HERO_HOME}
  <div class="hero-logos"><a href="computing/index.html"><img src="assets/img/silvercloud-logo-kleur.svg" alt="SilverCloud Computing"></a><a href="zorg/index.html"><img src="assets/img/silvercloud-zorg-logo-kleur.svg" alt="SilverCloud Zorg"></a></div></div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Onze labels</span><h2>Waar kunnen wij u mee helpen?</h2>
  <div class="lijn"><p class="lead">Twee labels, één organisatie. Dezelfde mensen, dezelfde werkwijze, met kennis van uw sector.</p></div></div>
  <div class="grid-2">
    <a class="label-card label-computing" href="computing/">
      <span class="kicker">SilverCloud Computing</span>
      <h3 style="font-size:28px">IT zonder zorgen voor het mkb</h3>
      <p class="muted">Uw ICT-partner voor het mkb: wij regelen uw ICT, u onderneemt.</p>
      <ul><li>Moderne werkplek (BrainOnline 375)</li><li>Veilig netwerk</li><li>Toegang tot al uw bedrijfsapplicaties</li><li>Beveiliging, back-up en servicedesk</li></ul>
      <span class="go">Naar Computing →</span>
    </a>
    <a class="label-card label-zorg" href="zorg/">
      <span class="kicker">SilverCloud Zorg</span>
      <h3 style="font-size:28px">Technologie die werkt voor de zorg</h3>
      <p class="muted">Wij kennen de zorg: de cultuur, de uitdagingen, de applicaties en de manier van werken. En we verbinden netwerk, ondersteuning en zorgtechnologie.</p>
      <ul><li><strong>Netwerkregie</strong>: een netwerk waarop de zorg kan vertrouwen</li><li><strong>CareDesk</strong>: een servicedesk die de taal van de zorg spreekt</li><li><strong>Zorgtechnologie</strong>: lokalisatie, leefcirkels, medewerkersveiligheid en hulpmiddelen</li></ul>
      <span class="go">Naar Zorg →</span>
    </a>
  </div>
</div></section>


<section class="section deep"><div class="container grid-2" style="align-items:center">
  <div>
    <span class="kicker" style="color:var(--merk-oranje)">Uitgelicht · SilverCloud Zorg</span>
    <h2>Netwerkregie: een netwerk waarop de zorg kan vertrouwen</h2>
    <p class="lead" style="margin-top:16px">Niet méér netwerkbeheer, wel volledige regie over de digitale infrastructuur. Eén architectuur, security by design, open calculatie en gedeelde monitoring met uw eigen ICT-afdeling.</p>
    <div class="actions"><a class="btn btn-highlight" href="zorg/netwerkregie/">Meer over Netwerkregie</a><a class="btn btn-secondary" style="color:#fff;border-color:#fff" href="assets/downloads/whitepaper-netwerkregie-zorg.pdf" download>Download de whitepaper</a></div>
  </div>
  <div class="uniek" style="grid-template-columns:1fr 1fr">
    <div><h3>Architectuur</h3><p>Eén integraal netwerkdesign als fundament.</p></div>
    <div><h3>Regie</h3><p>Verantwoordelijk voor de volledige levenscyclus.</p></div>
    <div><h3>Transparantie</h3><p>Open calculatie en gedeelde dashboards.</p></div>
    <div><h3>Voor de zorg</h3><p>Segmentatie, redundantie en NEN 7510.</p></div>
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

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Uit de blog</span><h2>Laatste artikelen</h2><p><a class="btn-link" href="blog/">Alle {len(POSTS)} artikelen</a></p></div>
  {latest(r, 3)}
</div></section>

<section class="section"><div class="container">
  <p class="small muted" style="text-align:center;margin-bottom:24px">Wij werken samen met onder meer</p>
  {logo_strip(r)}
  <p style="text-align:center;margin-top:24px"><a class="btn-link" href="partners/">Onze partners</a></p>
</div></section>

{certs(r)}

{cta('Waar staat uw organisatie nu?', 'Plan een vrijblijvend kennismakingsgesprek. We kijken samen naar uw huidige omgeving en de eerste stappen.', 'Plan een kennismaking', 'contact/', r)}
''', nav='home')

# ---------- COMPUTING ----------
r = '../'
page('computing', 'SilverCloud Computing – Uw ICT-partner voor het mkb',
 'SilverCloud Computing regelt de ICT voor het mkb: moderne werkplek, veilig netwerk, toegang tot al uw bedrijfsapplicaties, beveiliging, back-up en één servicedesk.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">SilverCloud Computing</span>
    <h1 class="display">U onderneemt. Wij regelen de ICT.</h1>
    <p class="lead">SilverCloud Computing neemt uw ICT uit handen. We regelen uw werkplek, een veilig netwerk, toegang tot uw bedrijfsapplicaties en alles wat daarbij hoort. Vaste afspraken, mensen die uw omgeving kennen, geen gedoe.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Plan een ICT-scan</a><a class="btn btn-link" href="#diensten">Wat we doen voor het mkb</a></div>
  </div>
  <div class="hero-visual">{HERO_COMP}
  <div class="hero-logos"><img src="{r}assets/img/silvercloud-logo-kleur.svg" alt="SilverCloud Computing"></div></div>
</div></section>

<section class="section mist" id="diensten"><div class="container">
  <div class="section-head"><span class="kicker">Wat we doen voor het mkb</span><h2>Alles wat uw ICT nodig heeft, onder één dak</h2>
  <div class="lijn"><p class="lead">U hoeft niet te weten hoe het werkt. U moet erop kunnen rekenen.</p></div></div>
  <div class="grid-3">
    <div class="card" id="werkplek">{icon('werkplek')}<h3>Moderne werkplek</h3><p>BrainOnline 375 is Microsoft 365, maar dan compleet. We vullen het aan met wat u als ondernemer echt nodig heeft, zoals een betere back-up en volledige support. Waar gewenst beheren we ook uw laptops en telefoons met Microsoft Intune. Daarom heet het 375: het gaat verder dan 365.</p></div>
    <div class="card" id="netwerken">{icon('netwerk')}<h3>Veilig netwerk</h3><p>Een netwerk dat is ontworpen voor uw organisatie, in plaats van gegroeid naar uw organisatie. Met proactieve monitoring en beheer, de juiste beveiligingsinstellingen en een internetverbinding die past bij uw locatie.</p></div>
    <div class="card" id="applicaties">{icon('cloud')}<h3>Toegang tot al uw applicaties</h3><p>Waar uw boekhouding, CRM, ERP en andere applicaties het ondersteunen, regelen we één veilige login (Single Sign-On) met meervoudige authenticatie. Voor applicaties die dat niet kunnen, zoeken we samen de veiligste werkbare oplossing.</p></div>
    <div class="card" id="beveiliging">{icon('schild')}<h3>Beveiliging &amp; back-up</h3><p>Updates, bescherming tegen virussen en phishing, en een back-up die verder gaat dan de standaardvoorziening van Microsoft. Gaat er iets mis, dan bent u snel weer aan het werk.</p></div>
    <div class="card" id="helpdesk">{icon('helpdesk')}<h3>Servicedesk</h3><p>Eén nummer, mensen die uw omgeving kennen. We lossen het op en voorkomen dat het opnieuw gebeurt.</p></div>
    <div class="card" id="telefonie">{icon('telefoon')}<h3>Telefonie &amp; samenwerken</h3><p>Vergaderen en samenwerken in Microsoft Teams, bellen met Xelion-telefonie. Goed bereikbaar, op kantoor en daarbuiten.</p></div>
  </div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Uw ICT-partner, maar dan anders</span><h2>Ontzorgen betekent vooruitkijken</h2>
  <p class="lead">Veel ICT-partijen wachten tot u belt. Wij zorgen dat u minder hoeft te bellen.</p></div>
  <div class="uniek">
    <div><h3>Proactief, niet reactief</h3><p>We monitoren uw omgeving en lossen problemen op voordat u ze merkt.</p></div>
    <div><h3>Voorspelbare kosten</h3><p>Vaste maandbedragen en vooraf heldere afspraken over wat er wel en niet in zit.</p></div>
    <div><h3>We denken mee</h3><p>Groeit u, verhuist u of wilt u slimmer werken? We maken samen een plan voor uw ICT.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Overstappen</span><h2>In vier stappen geregeld</h2><p class="lead">Overstappen klinkt als gedoe. Dat nemen wij voor onze rekening.</p></div>
  {steps([('Kennismaken', 'Wat doet u, wat werkt er en wat zit u dwars?'), ('ICT-scan', 'We brengen uw omgeving, risico’s en kosten in kaart.'), ('Overstap', 'Projectmatig gepland, op een moment dat u er zo min mogelijk last van heeft.'), ('Beheer &amp; verbeteren', 'Vaste afspraken, mensen die uw omgeving kennen en jaarlijks samen vooruitkijken.')])}
</div></section>

<section class="section mist"><div class="container narrow">
  <span class="kicker">Veelgestelde vragen</span><h2 style="margin-bottom:16px">Goed om te weten</h2>
  <details><summary>Voor welke organisaties werkt SilverCloud Computing?</summary><p>Voor mkb-organisaties die hun ICT goed geregeld willen hebben, zonder er zelf een afdeling voor op te bouwen. Heeft u al eigen ICT-mensen? Dan ondersteunen we hen en vullen we aan waar dat nodig is. Of u nu één locatie heeft of meerdere: we stemmen de dienstverlening af op uw omvang.</p></details>
  <details><summary>Hoeveel last hebben we van een overstap?</summary><p>Helemaal zonder hinder gaat een overstap zelden, en dat zeggen we liever eerlijk vooraf. We plannen de migratie projectmatig, bereiden zoveel mogelijk vooraf voor en spreken samen af wanneer we overschakelen, zodat u er zo min mogelijk last van heeft.</p></details>
  <details><summary>Hoe zit het met de kosten?</summary><p>Dat hangt af van wat we voor u regelen. Voor de werkplek met BrainOnline 375 betaalt u een vast bedrag per gebruiker per maand. Netwerk, beveiliging en andere diensten stemmen we af op uw situatie. Wat er wel en niet in zit, leggen we altijd vooraf vast.</p></details>
  <details><summary>Wat als we al een ICT-leverancier hebben voor een deel van onze omgeving?</summary><p>Dat kan prima: we stemmen met die partij af waar dat nodig is. Wilt u dat wij de regie over al uw ICT-leveranciers voeren, zodat u één aanspreekpunt heeft? Dan kunnen we dat als aanvullende dienst afspreken.</p></details>
</div></section>

{certs(r, 'Wij werken aantoonbaar zorgvuldig met uw gegevens: kwaliteit en informatiebeveiliging zijn onafhankelijk gecertificeerd. Dezelfde standaard die we in de zorg hanteren, krijgt u ook als mkb-klant.')}

{cta('Benieuwd hoe uw ICT ervoor staat?', 'Plan een vrijblijvende ICT-scan. U krijgt een helder beeld van werkplekken, netwerk, beveiliging en kosten, en wat er beter kan.', 'Plan een ICT-scan', r + 'contact/', r)}
''', label='computing', nav='computing')

# ---------- ZORG overzicht ----------
r = '../'
page('zorg', 'SilverCloud Zorg – Technologie die werkt voor de zorg',
 'SilverCloud Zorg verbindt netwerk, servicedesk en zorgtechnologie. Netwerkregie als fundament, met CareDesk, Lokalisatie & Leefcirkels en hulpmiddelenbeheer.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">SilverCloud Zorg</span>
    <h1 class="display">Technologie die werkt voor de zorg</h1>
    <p class="lead">Het begint bij een netwerk waarop de zorg kan vertrouwen. SilverCloud voert regie over uw digitale infrastructuur en bouwt daarop verder met een servicedesk en zorgtechnologie die werken op de werkvloer.</p>
    <div class="actions"><a class="btn btn-primary" href="netwerkregie/">Ontdek Netwerkregie</a><a class="btn btn-secondary" href="{r}assets/downloads/whitepaper-netwerkregie-zorg.pdf" download>Download de whitepaper</a></div>
  </div>
  <div class="hero-visual">{HERO_ZORG}</div>
</div></section>

<section class="section deep"><div class="container grid-2" style="align-items:center">
  <div>
    <span class="kicker" style="color:var(--merk-oranje)">Het fundament · Netwerkregie</span>
    <h2>Niet méér netwerkbeheer. Wel volledige regie over uw digitale infrastructuur.</h2>
    <p class="lead" style="margin-top:16px">Het netwerk is geen kostenpost, maar de digitale ruggengraat van uw zorgorganisatie. Wij nemen verantwoordelijkheid voor architectuur, beveiliging, beschikbaarheid, lifecycle en transparantie. Voor de hele levenscyclus.</p>
    <div class="actions"><a class="btn btn-highlight" href="netwerkregie/">Zo werkt Netwerkregie</a></div>
  </div>
  <div class="uniek" style="grid-template-columns:1fr 1fr">
    <div><h3>Architectuur</h3><p>Eén integraal netwerkdesign als fundament.</p></div>
    <div><h3>Regie</h3><p>Verantwoordelijk voor de volledige levenscyclus.</p></div>
    <div><h3>Transparantie</h3><p>Open calculatie en gedeelde monitoring.</p></div>
    <div><h3>Continu verbeteren</h3><p>Eén gezamenlijke roadmap.</p></div>
  </div>
</div></section>

{zorgkennis(r)}

<section class="section" id="oplossingen"><div class="container">
  <div class="section-head"><span class="kicker">Drie proposities, één regie</span><h2>Van digitale basis tot ondersteuning op de werkvloer</h2>
  <p class="lead">Netwerkregie is het fundament. Daarop bouwen CareDesk en Zorgtechnologie, met dezelfde regie, dezelfde aanpak en dezelfde kennis van de zorg.</p></div>
  <a class="prop-card" href="netwerkregie/" style="margin-bottom:32px;flex-direction:row;flex-wrap:wrap"><div class="art" style="flex:1 1 360px">{art('net')}</div><div class="body" style="flex:1 1 360px"><span class="num">01 · NETWERKREGIE · HET FUNDAMENT</span><h3 style="font-size:28px">Een netwerk waarop de zorg kan vertrouwen</h3><p class="muted" style="margin:0">Architectuur, security by design, 24/7 monitoring en lifecyclemanagement, met open calculatie en gedeelde dashboards voor uw eigen ICT-afdeling.</p><span class="tags">Architectuur · Security · Monitoring · Lifecycle</span><span class="btn-link">Meer over Netwerkregie</span></div></a>
  <div class="grid-2">
    <a class="prop-card" href="caredesk/"><div class="art">{art('care')}</div><div class="body"><span class="num">02 · CAREDESK</span><h3>Een servicedesk die de taal van de zorg spreekt</h3><p class="muted" style="margin:0">Meer dan een helpdesk: één aanspreekpunt, kennis van ECD’s, Zenya en AFAS, en regie richting al uw leveranciers.</p><span class="tags">Overnemen · Versterken · Optimaliseren</span><span class="btn-link">Meer over CareDesk</span></div></a>
    <div class="prop-card static"><div class="art">{art('lok')}</div><div class="body"><span class="num">03 · ZORGTECHNOLOGIE</span><h3>Zorgtechnologie die werkt op de werkvloer</h3><p class="muted" style="margin:0">Met de platforms van Evresys en Blyott, geleverd en geïntegreerd door SilverCloud. Van advies tot beheer.</p>
      <ul class="sublinks"><li><a href="lokalisatie-leefcirkels/">Lokalisatie &amp; Leefcirkels <span aria-hidden="true">→</span></a></li><li><a href="medewerkersveiligheid/">Medewerkersveiligheid <span aria-hidden="true">→</span></a></li><li><a href="assetguard/">Hulpmiddelenbeheer <span aria-hidden="true">→</span></a></li></ul>
      <a class="btn-link" href="zorgtechnologie/">Meer over Zorgtechnologie</a></div></div>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Waarom SilverCloud Zorg</span><h2>Wat ons anders maakt</h2>
  <div class="lijn accent"><p class="lead">We zijn niet alleen uitvoerder, maar partner. Niet alleen beheerder, maar regisseur. Dat ziet u terug in hoe we werken en afrekenen.</p></div></div>
  <div class="uniek">
    <div><h3>Architectuur boven producten</h3><p>We beginnen bij één integraal ontwerp en kiezen pas daarna de techniek. Elke wijziging en investering wordt daaraan getoetst.</p></div>
    <div><h3>Open calculatie</h3><p>Hardware en licenties tegen inzichtelijke inkoopprijzen met een vooraf afgesproken, vast opslagpercentage.</p></div>
    <div><h3>Gedeelde monitoring</h3><p>Uw eigen ICT-afdeling kijkt mee in dezelfde dashboards, meldingen en rapportages.</p></div>
    <div><h3>Kennis van de zorg</h3><p>We weten wat uitval betekent voor zorgalarmering, domotica en het ECD. We gaan pas weg als de zorg weer operationeel is.</p></div>
    <div><h3>Volledige integrator</h3><p>Van netwerk tot wearable en koppeling: wij leveren, integreren en beheren. Eén aanspreekpunt, ook richting andere leveranciers.</p></div>
    <div><h3>Eén team met uw ICT</h3><p>Heldere rollen, gedeelde kennis en een gezamenlijke meerjarenroadmap.</p></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Zorgspecifiek</span><h2>Ontworpen voor de eisen van de zorg</h2>
  <p class="lead" style="margin-top:16px">Een kantoornetwerk overleeft een uur storing. In de zorg raakt uitval direct de veiligheid van cliënten. Daarom ontwerpen we op beschikbaarheid, segmentatie en voorspelbare prestaties.</p></div>
  <ul class="checklist">
    <li>Zorgalarmering, domotica en medische apparatuur in eigen, afgeschermde netwerksegmenten</li>
    <li>Redundante internetverbindingen met 4G/5G-back-up op kritieke zorglocaties</li>
    <li>Gemonitorde noodstroom (UPS) en directe signalering bij spannings- of lijnuitval</li>
    <li>Bouwblokken per locatietype: wonen, behandelen, kantoor en ambulant</li>
    <li>Gecertificeerd voor NEN 7510, ISO 27001 en ISO 9001</li>
    <li>Kennis van ECD, Zenya, AFAS, TOPdesk en domotica-koppelingen</li>
  </ul>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Onze aanpak</span><h2>Eén doorlopende lijn</h2><p class="lead">Implementatie en adoptie zijn onderdeel van elke oplossing, geen los project.</p></div>
  {steps(WERKWIJZE)}
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Uit de blog</span><h2>Laatste artikelen</h2><p><a class="btn-link" href="{r}blog/">Alle artikelen</a></p></div>
  {latest(r, 3)}
</div></section>

{certs(r)}

{cta('Waar staat uw organisatie nu?', 'Plan een oriënterend gesprek over uw netwerk, servicedesk of zorgtechnologie.', 'Plan een kennismaking', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='zorg')

# ---------- NETWERKREGIE ----------
# Bronnen: Visiedocument Netwerkregie (uitgebreid + illustratievoorstellen), Dienstenpagina, Onepager,
# Homepagetekst Netwerkregie en de netwerkregie-presentaties.
r = '../../'
page('zorg/netwerkregie', 'Netwerkregie voor de zorg – SilverCloud Zorg',
 'Niet méér netwerkbeheer, wel volledige regie over uw digitale infrastructuur: architectuur, security by design, open calculatie en gedeelde monitoring.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Propositie 01 · Netwerkregie</span>
    <h1 class="display">Een netwerk waarop de zorg kan vertrouwen</h1>
    <p class="lead">Niet méér netwerkbeheer, wel volledige regie over uw digitale infrastructuur. Wij nemen verantwoordelijkheid voor architectuur, beveiliging, beschikbaarheid, doorontwikkeling én transparantie, voor de volledige levenscyclus van uw netwerk.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Plan een netwerkgesprek</a><a class="btn btn-secondary" href="{r}assets/downloads/whitepaper-netwerkregie-zorg.pdf" download>Download de whitepaper</a></div>
  </div>
  <div class="hero-visual"><div class="prop-card" style="pointer-events:none">{art('net').replace('viewBox="0 0 320 180"','viewBox="0 0 320 180" style="border-radius:14px"')}</div></div>
</div></section>

<section class="section mist"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Waarom</span><h2>Het netwerk is de digitale ruggengraat van de zorg</h2></div>
  <div class="lijn accent" style="margin-top:0"><p>Zorgapplicaties, domotica, zorgalarmering, medische apparatuur, telefonie, cloudplatformen en IoT zijn niet langer ondersteunend. Ze vormen het primaire proces. Als het netwerk niet beschikbaar is, raakt dat direct de kwaliteit, veiligheid en continuïteit van zorg.</p>
  <p>Toch worden veel netwerken nog beheerd vanuit techniek in plaats van vanuit visie. Apparatuur wordt vervangen als die is afgeschreven, locaties worden aangesloten als het moet en storingen worden opgelost als ze zich voordoen. Het gevolg: een omgeving die steeds complexer wordt en afhankelijk is van losse leveranciers.</p>
  <p><strong>SilverCloud gelooft dat dit anders moet.</strong></p></div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Van beheer naar regie</span><h2>De paradigmaverschuiving</h2></div>
  <div class="compare">
    <div class="before"><h3>Traditioneel netwerkbeheer</h3><ul><li>Apparatuurgedreven: start bij de techniek</li><li>Reactief: wachten tot het stuk gaat</li><li>Losse projecten en leveranciers</li><li>Vervangen wanneer het nodig is</li><li>Black box: verborgen marges, beperkt inzicht</li></ul></div>
    <div class="after"><h3>SilverCloud Netwerkregie</h3><ul><li>Architectuurgedreven: start bij het integrale design</li><li>Proactief: monitoring en lifecyclemanagement</li><li>Netwerk als onderdeel van de zorgketen</li><li>Vernieuwen volgens een gezamenlijke roadmap</li><li>Open calculatie en gedeelde dashboards</li></ul></div>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Het SilverCloud-regiemodel</span><h2>Vijf uitgangspunten</h2><p class="lead">Ze vormen de basis van iedere samenwerking.</p></div>
  <div class="pillars">
    <div class="pillar"><h3>Architectuur</h3><p>Eén integraal netwerkdesign als ‘single source of truth’. Elke wijziging wordt eraan getoetst. Zo voorkomen we technische schuld.</p></div>
    <div class="pillar"><h3>Regie</h3><p>Verantwoordelijk voor ontwerp, implementatie, beheer, beveiliging, monitoring, lifecycle en innovatie.</p></div>
    <div class="pillar"><h3>Transparantie</h3><p>Open calculatie en monitoring die ook uw eigen ICT-afdeling realtime inzicht geeft.</p></div>
    <div class="pillar"><h3>Voor de zorg</h3><p>Maximale beschikbaarheid, veilige segmentatie en een inrichting die past bij de functie van de locatie.</p></div>
    <div class="pillar"><h3>Continu verbeteren</h3><p>We vervangen niet omdat iets oud is, maar omdat het in de gezamenlijke roadmap past.</p></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Architectuur boven producten</span><h2>Eerst het ontwerp, dan de techniek</h2>
  <p class="lead" style="margin-top:16px">Veel leveranciers beginnen bij apparatuur. Wij beginnen bij de architectuur en kiezen daarna de technologie die het beste past. Zo ontstaat een netwerk dat niet afhankelijk is van één fabrikant.</p>
  <p class="small muted" style="margin-top:16px">Onze standaard doelarchitectuur bouwt op marktleidende technologie, zoals HPE Aruba voor switching en wifi en Fortinet voor next-generation firewalls, met centraal beheer vanuit één omgeving.</p></div>
  <div class="card"><h3>Het netwerkdesign omvat onder andere</h3><ul class="checklist"><li>Internetconnectiviteit en redundantie</li><li>Netwerksegmentatie (VLAN’s)</li><li>IP-, DNS- en DHCP-structuren</li><li>Wifi-architectuur, met slimme planning van accesspoints</li><li>Securitybeleid</li><li>Monitoring</li><li>Lifecycle van netwerkcomponenten</li></ul></div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Security by design</span><h2>Cybersecurity begint bij het ontwerp, niet bij de firewall</h2></div>
  <div class="grid-4">
    <div>{icon('schild')}<h3 style="margin:16px 0 8px">Zero Trust</h3><p class="muted">Geen automatische toegang op basis van een netwerkaansluiting. Elk apparaat en elke gebruiker wordt geverifieerd.</p></div>
    <div>{icon('netwerk')}<h3 style="margin:16px 0 8px">Segmentatie</h3><p class="muted">Zorgalarmering, domotica en medische apparatuur volledig gescheiden van kantoor- en gastenverkeer.</p></div>
    <div>{icon('oog')}<h3 style="margin:16px 0 8px">Next-generation firewalls</h3><p class="muted">Diepe inspectie, threat protection en centrale policies voor alle locaties.</p></div>
    <div>{icon('klok')}<h3 style="margin:16px 0 8px">24/7 monitoring</h3><p class="muted">Verdachte patronen worden direct gezien en op afstand opgelost.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Ontwikkeld voor de zorg</span><h2>Slim standaardiseren waar het kan</h2>
  <div class="lijn accent"><p class="lead">Geen zorglocatie is hetzelfde. Met gestandaardiseerde bouwblokken per locatietype blijft beheer eenvoudig, terwijl iedere locatie krijgt wat ze nodig heeft.</p></div></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Locatietype</th><th>Focus van het bouwblok</th></tr></thead>
    <tbody>
      <tr><td>Woonzorglocaties</td><td class="us">Veel domotica, zorgalarmering en veilige cliënten-wifi</td></tr>
      <tr><td>Behandelcentra</td><td class="us">Snelle, veilige toegang tot het ECD en stabiele medische IoT</td></tr>
      <tr><td>Hoofdkantoren</td><td class="us">Cloudapplicaties, telefonie en hybride werken</td></tr>
      <tr><td>Ambulante zorg</td><td class="us">Veilige toegang onderweg en thuis, via Zero Trust</td></tr>
    </tbody></table></div>
  <ul class="checklist" style="margin-top:32px">
    <li>Redundante internetverbindingen met 4G/5G-back-up op kritieke zorglocaties</li>
    <li>Gemonitorde noodstroom (UPS) en directe signalering bij spannings- of lijnuitval</li>
    <li>Netwerkinrichting direct afgestemd met domotica- en zorgalarmeringsleveranciers</li>
  </ul>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Transparantie</span><h2>Openheid als basis voor partnerschap</h2><p class="lead">Een strategisch partnerschap werkt alleen als beide partijen over dezelfde informatie beschikken.</p></div>
  <div class="grid-3">
    <div class="card">{icon('oog')}<h3>Open calculatie</h3><p>Hardware, licenties en componenten tegen inzichtelijke inkoopprijzen met een vooraf afgesproken, vast opslagpercentage. Soms is investeren de beste keuze, soms juist het verantwoord verlengen van de levensduur.</p></div>
    <div class="card">{icon('pad')}<h3>Gedeelde monitoring</h3><p>Uw ICT-afdeling krijgt realtime inzicht in beschikbaarheid, prestaties, storingen en trends. Rapportages vormen de basis voor gezamenlijke verbeteracties.</p></div>
    <div class="card">{icon('kaart')}<h3>Beheer per locatie</h3><p>De beheervergoeding volgt omvang en complexiteit van uw locaties, niet het aantal switches of accesspoints. Een extra switch betekent geen nieuwe offerte.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Vier disciplines, één regiemodel</span><h2>Wat we dagelijks voor u doen</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('oog')}<h3>Monitoring</h3><p>24/7 inzicht in beschikbaarheid en prestaties.</p></div>
    <div class="card flat">{icon('bel')}<h3>Reactief beheer</h3><p>Storingen snel en gecontroleerd oplossen.</p></div>
    <div class="card flat">{icon('schild')}<h3>Proactief beheer</h3><p>Preventief onderhoud, firmware-updates en capaciteitsanalyses.</p></div>
    <div class="card flat">{icon('pad')}<h3>Doorontwikkeling</h3><p>Lifecyclemanagement, innovatie en strategisch advies.</p></div>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">De overstap</span><h2>Een gecontroleerde transitie naar rust</h2><p class="lead">U hoeft niet eerst alles te vervangen. We nemen het beheer over zoals het is en moderniseren stap voor stap.</p></div>
  <div class="grid-2">
    <div class="route"><span class="badge">Fase 1</span><h3>Transitie &amp; implementatie</h3><ul class="checklist"><li>Beheeroverdracht ‘as-is’: direct operationele verantwoordelijkheid</li><li>Inventarisatie en integraal netwerkdesign</li><li>Elke storing is een stap richting de doelarchitectuur</li><li>Gefaseerde modernisering volgens de gezamenlijke roadmap</li></ul></div>
    <div class="route voorkeur"><span class="badge">Fase 2</span><h3>Reguliere dienstverlening</h3><ul class="checklist"><li>Netwerk volledig gestandaardiseerd</li><li>Centraal beheer, monitoring en updates op afstand</li><li>Van reactief blussen naar strategisch doorontwikkelen</li></ul></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:center">
  <div><span class="kicker">Whitepaper</span><h2>Lees onze visie op Netwerkregie</h2><p class="lead" style="margin-top:16px">De vijf uitgangspunten, slimme wifi-planning en onze aanpak, in één document.</p></div>
  {wp_card(r)}
</div></section>

<section class="section mist"><div class="container narrow">
  <span class="kicker">Veelgestelde vragen</span><h2 style="margin-bottom:16px">Goed om te weten</h2>
  <details><summary>Moeten we ons huidige netwerk eerst vervangen?</summary><p>Nee. We nemen het beheer ‘as-is’ over om de continuïteit te borgen. Daarna moderniseren we gefaseerd: defecte of verouderde apparatuur wordt vervangen door de nieuwe standaard, binnen de gezamenlijke roadmap.</p></details>
  <details><summary>Werkt SilverCloud met één vast merk?</summary><p>We beginnen bij de architectuur, niet bij een merk. Onze standaard doelarchitectuur gebruikt marktleidende technologie zoals HPE Aruba en Fortinet, omdat die centraal beheer en security goed ondersteunt. De keuze volgt altijd het ontwerp.</p></details>
  <details><summary>Wat ziet onze eigen ICT-afdeling?</summary><p>Hetzelfde als wij. Monitoringdashboards, meldingen en rapportages zijn volledig inzichtelijk voor uw interne ICT. We werken als één team met heldere rollen.</p></details>
  <details><summary>Hoe zijn de kosten opgebouwd?</summary><p>Hardware en licenties leveren we op basis van open calculatie: inzichtelijke inkoopprijs plus een vooraf afgesproken vast opslagpercentage. Het beheer is een vaste vergoeding op basis van omvang en complexiteit van uw locaties.</p></details>
  <details><summary>Werken jullie samen met onze andere leveranciers?</summary><p>Ja. Regie betekent dat leveranciers op elkaar aansluiten. Voor domotica, zorgalarmering en applicaties stemmen we de netwerkinrichting direct af met de betrokken partijen.</p></details>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Verdieping</span><h2>Meer over netwerken in de zorg</h2><p><a class="btn-link" href="{r}blog/#netwerk">Alle artikelen over netwerk &amp; ICT</a></p></div>
  {latest(r, 3, slugs=['het-belang-van-een-goed-netwerk-voor-jouw-zorginstelling', 'vier-it-trends-die-de-zorg-transformeren-van-administratielast-naar-ai', 'zo-zorg-je-voor-de-juiste-infrastructuur-om-ble-op-locatie-te-gebruiken'])}
</div></section>

{zorgkennis(r, True)}

{certs(r)}

{cta('Klaar voor een netwerk dat de zorg ondersteunt?', 'Bespreek uw huidige architectuur met onze specialisten. We laten zien wat Netwerkregie betekent voor beschikbaarheid, veiligheid en investeringen.', 'Plan een netwerkgesprek', r + 'contact/', r, 'Download de whitepaper', r + 'assets/downloads/whitepaper-netwerkregie-zorg.pdf')}
''', label='zorg', nav='zorg', sub='netwerkregie')

# ---------- CAREDESK ----------
# Bronnen: Voorzet Pagina CareDesk, Brochure CareDesk, CareDesk blueprint, Verkorte uitleg CareDesk, html-tekst voor website.
r = '../../'
page('zorg/caredesk', 'CareDesk – de servicedesk voor de zorg – SilverCloud Zorg',
 'CareDesk is meer dan een helpdesk: een complete serviceorganisatie voor zorg-ICT, met kennis van ECD’s, Zenya en AFAS, één aanspreekpunt en regie richting al uw leveranciers.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Propositie 02 · CareDesk</span>
    <h1 class="display">Een servicedesk die de taal van de zorg spreekt</h1>
    <p class="lead">CareDesk is meer dan een helpdesk. Het is een complete serviceorganisatie voor zorg-ICT: ondersteuning, beheer, regie, advies en procesverbetering in één dienst. Wij kennen de cultuur van de zorg en de applicaties waarmee uw medewerkers werken.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}afspraak/">Plan een kennismaking</a><a class="btn btn-secondary" href="{r}assets/downloads/brochure-caredesk.pdf" download>Download de brochure</a></div>
  </div>
  <div class="hero-visual">{CAREDESK_RING}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Meer dan een helpdesk</span><h2>Het traditionele helpdeskmodel past niet meer bij de zorg</h2>
  <div class="lijn accent"><p class="lead">Veel budget gaat naar generieke vragen over wachtwoorden, printers en hardware. De echte waarde zit in kennis van het ECD, koppelingen en werkprocessen. Als die niet goed werken, raakt dat direct de kwaliteit van zorg.</p></div></div>
  <div class="table-wrap"><table>
    <thead><tr><th></th><th>Traditionele helpdesk</th><th>CareDesk van SilverCloud</th></tr></thead>
    <tbody>
      <tr><td>Kennisniveau</td><td>Basis IT-kennis</td><td class="us">Diepgaande zorg- en ECD-expertise</td></tr>
      <tr><td>Aanpak</td><td>Reactief (break/fix)</td><td class="us">Proactief en adviserend</td></tr>
      <tr><td>Budgetfocus</td><td>Duur talent op generieke vragen</td><td class="us">Gerichte investering in zorgprocessen</td></tr>
      <tr><td>Aanspreekpunt</td><td>IT-afdeling als doorgeefluik</td><td class="us">Ketenregie, één aanspreekpunt</td></tr>
      <tr><td>Cultuur</td><td>Techniekgedreven</td><td class="us">Zorgbewust en dienstverlenend</td></tr>
    </tbody></table></div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Zorgcultuur</span><h2>Wij kennen de cultuur van de zorg</h2>
  <p class="lead" style="margin-top:16px">Hoge werkdruk, onregelmatige diensten en een sterk verantwoordelijkheidsgevoel. De manier waarop je communiceert, prioriteert en ondersteunt, moet daarbij passen.</p></div>
  <div class="lijn accent" style="margin-top:0"><p>Onze medewerkers zijn gewend om samen te werken met teams in de VVT, gehandicaptenzorg, GGZ en ziekenhuizen. We werken met begrijpelijke taal, korte lijnen, duidelijke afspraken en respect voor de dynamiek van zorgteams.</p>
  <p>We kennen veelgebruikte zorgapplicaties, zoals diverse ECD’s, Zenya en AFAS. Daardoor zien we sneller wat er speelt en helpen we zorgprofessionals niet alleen met “hoe los ik dit op?”, maar ook met “hoe kan ik hier slimmer mee werken?”.</p></div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Wat CareDesk onderscheidt</span><h2>Zorgkennis en regie in één dienst</h2></div>
  <div class="grid-2">
    <div class="card flat">{icon('helpdesk')}<h3>Eén aanspreekpunt (SPOC)</h3><p>Eén loket en één telefoonnummer voor al uw zorg-ICT-vragen. Wij bewaken opvolging en doorlooptijden en stemmen af met leveranciers van werkplekken, ECD’s, koppelingen en andere applicaties.</p></div>
    <div class="card flat">{icon('pad')}<h3>Van reactief naar proactief</h3><p>We sturen op het voorkomen van problemen en op procesverbetering, met continue monitoring en heldere servicelevels, KPI’s en rapportages.</p></div>
    <div class="card flat">{icon('werkplek')}<h3>Applicatie-expertise</h3><p>Diepgaande kennis van ECD’s, Zenya, AFAS en andere zorgapplicaties, zodat vragen in één keer goed worden opgepakt.</p></div>
    <div class="card flat">{icon('bel')}<h3>Urgentie begrijpen</h3><p>Een storing is geen ticket: hij kan het primaire proces raken. We prioriteren op impact voor cliënt en zorgmedewerker. Ook ’s avonds en in het weekend, als u dat wilt.</p></div>
  </div>
</div></section>

<section class="section" id="modellen"><div class="container">
  <div class="section-head"><span class="kicker">Inzetmodellen</span><h2>Overnemen, versterken of optimaliseren</h2><p class="lead">Iedere zorgorganisatie heeft een andere uitgangssituatie. CareDesk sluit op alle drie aan.</p></div>
  <div class="grid-3">
    <div class="route voorkeur"><span class="badge">Onze voorkeur</span><h3>Complete overname</h3><p class="muted">Een volwaardige serviceorganisatie die 1e- en 2e-lijns support, applicatie-expertise, monitoring, incident- en probleemmanagement, procesoptimalisatie en heldere servicelevels combineert. De meeste rust en de sterkste positie als SPOC.</p>
      <ul class="checklist"><li>U stopt met het zelf managen van een servicedesk</li><li>Eén aanspreekpunt voor de hele ICT-keten</li><li>Waar gewenst fysiek aanwezig op locatie</li><li>Uw ICT-afdeling verschuift van uitvoering naar regie</li></ul></div>
    <div class="route"><span class="badge">Versterking</span><h3>Uw servicedesk versterken</h3><p class="muted">CareDesk als uitbreiding of verdieping van uw eigen team, met naadloze aansluiting op uw processen.</p>
      <ul class="checklist"><li>Extra capaciteit bij piekbelasting</li><li>Specialistische kennis van zorgapplicaties</li><li>Avond-, weekend- en verlengde bereikbaarheid</li><li>Tijdelijke ondersteuning bij projecten</li></ul></div>
    <div class="route"><span class="badge">Optimalisatie</span><h3>Processen verbeteren</h3><p class="muted">Veel helpdesks zijn historisch gegroeid. Wij maken ze robuuster, transparanter en beter stuurbaar.</p>
      <ul class="checklist"><li>Incident- en changeprocessen</li><li>Werkafspraken, routering en escalaties</li><li>Rapportages, KPI’s en stuurinformatie</li><li>Servicelevels en doorlooptijden</li></ul></div>
  </div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">De overgang</span><h2>Projectmatig, zonder verstoring van de zorg</h2><p class="lead">Overname of uitbreiding van een servicedesk doen we altijd gestructureerd, voor een soepele transitie.</p></div>
  {steps([('Audit &amp; inventarisatie', 'Processen, applicaties en meldingen gedetailleerd in kaart.'), ('Kennisoverdracht', 'Diepgaande afstemming op uw zorgcontext en teams.'), ('SLA &amp; kaders', 'Afspraken over servicetijden, escalaties en fysieke aanwezigheid.'), ('Go-live', 'Een stabiele, voorspelbare en naadloze dienstverlening.')])}
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Wat het oplevert</span><h2>Meer focus op zorg, minder op techniek</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('klok')}<h3>Tijdwinst</h3><p>Minder tijdverlies door ICT-problemen voor zorgprofessionals.</p></div>
    <div class="card flat">{icon('mens')}<h3>Kwaliteit</h3><p>Hogere gebruikerstevredenheid en betere prestaties van applicaties.</p></div>
    <div class="card flat">{icon('pad')}<h3>Efficiëntie</h3><p>Lagere totale kosten door een efficiëntere werkwijze.</p></div>
    <div class="card flat">{icon('oog')}<h3>Ruimte</h3><p>Meer rust en focus op zorginhoud en innovatie.</p></div>
  </div>
  <p class="small muted" style="margin-top:32px">CareDesk werkt naadloos samen met <a href="{r}zorg/netwerkregie/">Netwerkregie</a>: één partij voor netwerk én service, met dezelfde monitoring en dezelfde regie.</p>
</div></section>

<section class="section mist"><div class="container grid-2" style="align-items:center">
  <div><span class="kicker">Brochure</span><h2>Alles over CareDesk op een rij</h2><p class="lead" style="margin-top:16px">De inzetmodellen, de overgang en wat CareDesk oplevert, in één document.</p></div>
  <a class="card download wp" href="{r}assets/downloads/brochure-caredesk.pdf" download><span class="kicker">Brochure · pdf</span><h3>CareDesk: dé servicedesk voor zorgorganisaties</h3><p>Meer dan een helpdesk: ondersteuning, beheer, regie, advies en procesoptimalisatie in één dienst.</p><span class="btn btn-primary" style="align-self:flex-start">Download de brochure</span></a>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Verdieping</span><h2>Lees verder</h2></div>
  {latest(r, 3, slugs=['helpdesk-uitbesteden-de-eerste-stap-naar-strategische-it', 'vier-it-trends-die-de-zorg-transformeren-van-administratielast-naar-ai', 'wildgroei-aan-applicaties-zo-hou-je-overzicht-in-je-applicatielandschap'])}
</div></section>

{zorgkennis(r, True)}

{certs(r)}

{cta('Ontdek wat CareDesk voor uw servicedesk kan betekenen', 'Laten we in gesprek gaan over ICT-ondersteuning die écht werkt voor uw zorgverleners.', 'Plan een kennismaking', r + 'afspraak/', r, 'Download de brochure', r + 'assets/downloads/brochure-caredesk.pdf')}
''', label='zorg', nav='zorg', sub='caredesk')

# ---------- ZORGTECHNOLOGIE (overzicht) ----------
r = '../../'
page('zorg/zorgtechnologie', 'Zorgtechnologie – SilverCloud Zorg',
 'Zorgtechnologie die werkt op de werkvloer: lokalisatie & leefcirkels, medewerkersveiligheid en hulpmiddelenbeheer. Evresys en Blyott, geleverd en geïntegreerd door SilverCloud Zorg.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Propositie 03 · Zorgtechnologie</span>
    <h1 class="display">Zorgtechnologie die werkt op de werkvloer</h1>
    <p class="lead">Meer vrijheid voor cliënten, veiligheid voor medewerkers en minder zoeken naar hulpmiddelen. SilverCloud levert de oplossingen van Evresys en Blyott als volledige integrator: van advies en netwerk tot wearables, koppelingen, adoptie en beheer.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}afspraak/">Plan een adviesgesprek</a><a class="btn btn-link" href="#toepassingen">Bekijk de toepassingen</a></div>
  </div>
  <div class="hero-visual">{LEEF}</div>
</div></section>

<section class="section mist" id="toepassingen"><div class="container">
  <div class="section-head"><span class="kicker">Drie toepassingen</span><h2>Eén aanpak, drie toepassingen</h2>
  <div class="lijn accent"><p class="lead">Ze draaien op hetzelfde netwerk, worden door dezelfde mensen ingericht en beheerd, en versterken elkaar. Veel organisaties beginnen met één toepassing en groeien door.</p></div></div>
  <div class="grid-3">
    <a class="prop-card" href="{r}zorg/lokalisatie-leefcirkels/"><div class="art">{art('lok')}</div><div class="body"><span class="num">LOKALISATIE &amp; LEEFCIRKELS</span><h3>Weet altijd waar uw cliënt is, en wanneer het nodig is</h3><span class="tags">Zorgalarmering · Leefcirkels · Dwaaldetectie · Deurintegratie</span><span class="btn-link">Meer over Lokalisatie</span></div></a>
    <a class="prop-card" href="{r}zorg/medewerkersveiligheid/"><div class="art">{art('safe')}</div><div class="body"><span class="num">MEDEWERKERSVEILIGHEID</span><h3>Nooit alleen bij een escalatie</h3><span class="tags">Persoonsalarm · Stille alarmering · Locatie · Push-to-Talk</span><span class="btn-link">Meer over Medewerkersveiligheid</span></div></a>
    <a class="prop-card" href="{r}zorg/assetguard/"><div class="art">{art('asset')}</div><div class="body"><span class="num">HULPMIDDELENBEHEER</span><h3>Elk hulpmiddel binnen seconden gevonden</h3><span class="tags">AssetGuard · Snelvinden · TOPdesk · Inzicht</span><span class="btn-link">Meer over Hulpmiddelenbeheer</span></div></a>
  </div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Volledige integrator</span><h2>Technologie alleen is niet genoeg</h2>
  <p class="lead">Het resultaat wordt bepaald door de juiste implementatie en zorgvuldig beheer, niet door het platform alleen. Wij gooien geen product over de schutting, maar zijn pas tevreden als het resultaat op de werkvloer er is.</p></div>
  <div class="grid-2">
    <div class="route" style="background:transparent;border-color:#3a4a5e"><span class="badge">Evresys</span><h3>Cliënten en medewerkers</h3><p style="color:#c6d1dd">Zorgalarmering, realtime lokalisatie, leefcirkels en dwaaldetectie, deurintegratie, medewerkersveiligheid en Push-to-Talk. Als totaaloplossing of als aanvulling op uw zorgoproepsysteem. <a href="{EVRESYS_URL}" rel="noopener" target="_blank" style="color:#fff">Meer op evresys.com</a></p></div>
    <div class="route" style="background:transparent;border-color:#3a4a5e"><span class="badge">Blyott</span><h3>Hulpmiddelen</h3><p style="color:#c6d1dd">Realtime lokalisatie van tilliften, rolstoelen, infuuspompen en andere hulpmiddelen via Bluetooth, met onze AssetGuard-dienstverlening en koppelingen met TOPdesk en assetmanagement. <a href="{BLYOTT_AT}" rel="noopener" target="_blank" style="color:#fff">Meer op blyott.com</a></p></div>
  </div>
  <div class="uniek" style="margin-top:48px;grid-template-columns:repeat(4,1fr)">
    <div><h3>Consultancy &amp; advies</h3><p>Situatie, doelen en infrastructuur in kaart. Welke route en welk platform past?</p></div>
    <div><h3>Implementatie &amp; integratie</h3><p>Netwerk, gateways, wearables, tags en koppelingen met zorgoproep, deuren en TOPdesk.</p></div>
    <div><h3>Adoptie &amp; begeleiding</h3><p>Training en begeleiding, zodat medewerkers er echt mee werken.</p></div>
    <div><h3>Beheer &amp; support</h3><p>Doorlopend beheer, monitoring en servicedesk. Eén aanspreekpunt.</p></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Samenhang</span><h2>Zorgtechnologie werkt pas als het geheel klopt</h2>
  <p class="lead" style="margin-top:16px">Alarmering, lokalisatie en sensoren leveren alleen waarde als ze stabiel draaien en goed worden ondersteund. Daarom combineren we Zorgtechnologie met onze andere twee proposities.</p></div>
  <ul class="checklist">
    <li><strong>Op een netwerk dat erop is ontworpen</strong>: dekking, segmentatie en beschikbaarheid via <a href="{r}zorg/netwerkregie/">Netwerkregie</a></li>
    <li><strong>Met ondersteuning die de zorg begrijpt</strong>: vragen en storingen via <a href="{r}zorg/caredesk/">CareDesk</a>, één aanspreekpunt</li>
    <li><strong>Behoud wat goed werkt</strong>: Evresys als aanvulling op uw bestaande zorgoproepsysteem, of als complete basis. <a href="{r}zorg/lokalisatie-leefcirkels/#aanvulling">Zo werkt de aanvulling</a></li>
    <li><strong>Geborgd</strong>: ingericht volgens NEN 7510, ISO 27001 en ISO 9001</li>
  </ul>
</div></section>

{tech_partners(r)}

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Uit de praktijk</span><h2>Wat zorgorganisaties zeggen</h2><p><a class="btn-link" href="{r}kennis/">Alle cases</a></p></div>
  <div class="grid-2">
    <figure class="quote lijn accent"><blockquote>“Je ziet dat medewerkers die het systeem een paar keer hebben gebruikt, niet meer zonder willen.”</blockquote><figcaption>Janneke Boevink, projectleider, Argos Zorggroep</figcaption></figure>
    <figure class="quote lijn accent"><blockquote>“In SilverCloud vonden we een partner die actief meedacht en kennis had van de zorgsector.”</blockquote><figcaption>Wiebe de Vries, Zorggroep Elde Maasduinen</figcaption></figure>
  </div>
  <div class="actions" style="margin-top:32px"><a class="btn btn-secondary" href="{r}assets/downloads/whitepaper-evresys-twee-routes.pdf" download>Whitepaper: twee routes</a><a class="btn btn-secondary" href="{r}assets/downloads/10-voordelen-realtime-lokalisatie.pdf" download>10 voordelen van realtime lokalisatie</a></div>
</div></section>

{zorgkennis(r, True)}

{certs(r)}

{cta('Welke zorgtechnologie past bij uw organisatie?', 'In een adviesgesprek brengen we samen in kaart wat er al is, wat ontbreekt en waar de meeste winst zit.', 'Plan een adviesgesprek', r + 'afspraak/', r)}
''', label='zorg', nav='zorg', sub='zorgtech')

# ---------- LOKALISATIE ----------
# Bronnen: Voorzet Pagina Realtime Lokalisatie (Evresys), Evresys x SilverCloud basispresentatie,
# aanvullingen Route 1 en Route 2, en de drie Evresys-whitepapers.
r = '../../'
page('zorg/lokalisatie-leefcirkels', 'Lokalisatie & Leefcirkels – Blyott en Evresys, geïntegreerd door SilverCloud Zorg',
 'Zorgalarmering, realtime lokalisatie, leefcirkels en hulpmiddelen vinden. SilverCloud Zorg levert de oplossingen van Evresys en Blyott als volledige integrator: van advies tot beheer.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Zorgtechnologie · Lokalisatie &amp; Leefcirkels</span>
    <h1 class="display">Weet altijd waar uw cliënt is, en wanneer het nodig is</h1>
    <p class="lead">Zorgalarmering, realtime lokalisatie, persoonlijke leefcirkels en het terugvinden van hulpmiddelen. SilverCloud Zorg levert de oplossingen van Evresys en Blyott als volledige integrator: van advies en netwerk tot wearables, koppelingen, adoptie en beheer.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}contact/">Vraag een adviesgesprek aan</a><a class="btn btn-link" href="#routes">Welke route past bij u?</a></div>
  </div>
  <div class="hero-visual">{LEEF}</div>
</div></section>

<section class="section deep"><div class="container">
  <div class="section-head"><span class="kicker" style="color:var(--merk-oranje)">Volledige integrator</span><h2>Technologie alleen is niet genoeg</h2>
  <p class="lead">Het resultaat wordt bepaald door de juiste implementatie én zorgvuldig beheer, niet door het platform alleen. Wij gooien geen product over de schutting, maar zijn pas tevreden als het resultaat op de werkvloer er is.</p></div>
  <div class="grid-2">
    <div class="route" style="background:transparent;border-color:#3a4a5e"><span class="badge">Evresys</span><h3>Cliënten en medewerkers</h3><p style="color:#c6d1dd">Eén platform voor zorgalarmering, realtime lokalisatie, leefcirkels en dwaaldetectie, deurintegratie, medewerkersveiligheid en Push-to-Talk. Als complete totaaloplossing of als aanvulling op uw zorgoproepsysteem.</p></div>
    <div class="route" style="background:transparent;border-color:#3a4a5e"><span class="badge">Blyott</span><h3>Hulpmiddelen</h3><p style="color:#c6d1dd">Realtime lokalisatie van tilliften, rolstoelen, infuuspompen en andere mobiele hulpmiddelen via Bluetooth (BLE), met onze AssetGuard-dienstverlening en koppelingen met TOPdesk en assetmanagement. <a href="{r}zorg/assetguard/">Meer over AssetGuard</a></p></div>
  </div>
  <div class="uniek" style="margin-top:48px;grid-template-columns:repeat(4,1fr)">
    <div><h3>Consultancy &amp; advies</h3><p>Situatie, doelen en infrastructuur in kaart. Welke route en welk platform past?</p></div>
    <div><h3>Implementatie &amp; integratie</h3><p>Netwerk, gateways, wearables, tags en koppelingen met zorgoproep, deuren en TOPdesk.</p></div>
    <div><h3>Adoptie &amp; begeleiding</h3><p>Training en begeleiding, zodat medewerkers er echt mee werken.</p></div>
    <div><h3>Beheer &amp; support</h3><p>Doorlopend beheer, monitoring en servicedesk. Eén aanspreekpunt.</p></div>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Toepassingen</span><h2>Wat het oplevert op de werkvloer</h2></div>
  <div class="grid-4">
    <div class="card flat">{icon('cirkel')}<h3>Meer vrijheid voor cliënten</h3><p>Persoonlijke leefcirkels en dwaaldetectie per cliënt.</p></div>
    <div class="card flat">{icon('bel')}<h3>Sneller hulp op de juiste plek</h3><p>Bij elk alarm direct de locatie van cliënt of wearable.</p></div>
    <div class="card flat">{icon('radio')}<h3>Medewerkersveiligheid</h3><p>Persoonsalarm en Push-to-Talk voor collegiale hulp bij escalaties. <a href="{r}zorg/medewerkersveiligheid/">Meer hierover</a></p></div>
    <div class="card flat">{icon('tillift')}<h3>Minder zoeken</h3><p>Tilliften, infuuspompen en andere hulpmiddelen binnen seconden gevonden.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Functionaliteiten</span><h2>Wat we voor u inrichten</h2></div>
  <div class="grid-3">
    <div class="card flat">{icon('bel')}<h3>Zorgalarmering</h3><p>Cliënten activeren een alarm via een wearable. Medewerkers ontvangen de melding op hun werkplek of in de app, inclusief locatie.</p></div>
    <div class="card flat">{icon('pin')}<h3>Realtime lokalisatie</h3><p>Bij iedere melding is de locatie van cliënt of wearable direct zichtbaar, binnen en buiten.</p></div>
    <div class="card flat">{icon('cirkel')}<h3>Leefcirkels &amp; dwaaldetectie</h3><p>Per cliënt de gewenste bewegingsvrijheid instellen. Verlaat iemand de zone, dan volgt automatisch een melding.</p></div>
    <div class="card flat">{icon('deur')}<h3>Deurintegratie</h3><p>Leefcirkels gekoppeld aan deuren en toegang, zodat vrijheid en veiligheid per cliënt samenkomen.</p></div>
    <div class="card flat">{icon('radio')}<h3>Medewerkersveiligheid &amp; Push-to-Talk</h3><p>Persoonsalarm voor medewerkers en smartphones die werken als portofoon, per team, afdeling of verdieping. <a href="{r}zorg/medewerkersveiligheid/">Lees meer</a></p></div>
    <div class="card flat">{icon('kaart')}<h3>Hulpmiddelen &amp; assettracking</h3><p>Hulpmiddelen vinden en het gebruik inzichtelijk maken, voortbouwend op onze jarenlange ervaring met <a href="{r}zorg/assetguard/">AssetGuard</a> en Blyott.</p></div>
  </div>
</div></section>

{tech_partners(r)}

<section class="section" id="aanvulling"><div class="container">
  <div class="section-head"><span class="kicker">Evresys als aanvulling</span><h2>Behoud wat goed werkt. Voeg toe wat nog ontbreekt.</h2>
  <div class="lijn accent"><p class="lead">Veel zorginstellingen hebben al jaren een goed werkend zorgoproepsysteem. Evresys hoeft dat niet te vervangen: het werkt ernaast en voegt precies de functies toe die nog ontbreken.</p></div></div>
  <div class="grid-2" style="align-items:start">
    <div class="card flat">{icon('bel')}<h3>Wat is een zorgoproepsysteem?</h3><p>Een zorgoproepsysteem (ook wel verpleegoproepsysteem) is de vaste alarmketen van een zorglocatie. Cliënten roepen hulp in met een oproepknop, trekkoord of halszender. Het systeem stuurt de oproep naar de juiste medewerker, op een zorgtelefoon, pieper of werkplek. Vaak zijn ook domotica en sensoren erop aangesloten, zoals deur- en bedsensoren.</p><p>De infrastructuur ligt er, medewerkers kennen de werkwijze en de alarmopvolging is ingericht. Als die basis goed functioneert, is vervangen zelden het logische vertrekpunt.</p></div>
    <div class="card flat">{icon('cirkel')}<h3>Wat Evresys daaraan toevoegt</h3><p>Een klassiek zorgoproepsysteem is niet primair ontworpen voor nauwkeurige lokalisatie of individuele bewegingsvrijheid. Daar voegt Evresys context aan toe:</p>
      <ul class="checklist"><li><strong>Leefcirkels per cliënt</strong>, in plaats van een hele afdeling op dezelfde manier af te sluiten</li><li><strong>Dwaalalarmering</strong>, met de melding via de Evresys App óf via uw bestaande zorgoproepsysteem</li><li><strong>Binnen- en buitenlokalisatie</strong> als onderdeel van de zorgrespons</li><li><strong>Deurintegratie</strong>: toegang dynamisch per cliënt</li><li><strong>Medewerkersveiligheid en Push-to-Talk</strong> als extra laag</li></ul></div>
  </div>
  <h3 style="margin:48px 0 16px">Twee systemen, één zorgproces</h3>
  <div class="table-wrap"><table>
    <thead><tr><th>Bestaand zorgoproepsysteem</th><th>Evresys voegt toe</th><th>Gezamenlijk resultaat</th></tr></thead>
    <tbody>
      <tr><td>Oproep- en alarmdistributie</td><td>Locatie en context</td><td class="us">Gerichtere opvolging</td></tr>
      <tr><td>Bestaande apparatuur en werkwijze</td><td>Leefcirkels</td><td class="us">Meer individuele vrijheid</td></tr>
      <tr><td>Bekende werkplek van de medewerker</td><td>Dwaalalarm</td><td class="us">Alarm in de bestaande keten</td></tr>
      <tr><td>Bestaande investering</td><td>Aanvullende infrastructuur</td><td class="us">Geen volledige vervanging</td></tr>
    </tbody></table></div>
  <div class="grid-2" style="margin-top:48px;align-items:start">
    <div><h3>Waarom dit verstandig is</h3><p class="muted">Een volledige vervanging raakt techniek, gebouwen, werkprocessen, scholing en continuïteit. Met een aanvullende aanpak koppelt u innovatie los van vervanging. U behoudt de vertrouwde alarmketen en voegt Evresys alleen toe waar nieuwe zorgdoelen daarom vragen. Evresys werkt daarbij samen met uw bestaande leverancier, niet ertegen.</p></div>
    <div><h3>Wanneer is dit logisch?</h3><ul class="checklist"><li>Uw zorgoproepsysteem functioneert goed en heeft nog voldoende levensduur</li><li>U wilt leefcirkels, dwaaldetectie, locatie of wandelzones die het huidige systeem niet goed biedt</li><li>U wilt innoveren per locatie, afdeling of doelgroep</li><li>Bestaande werkprocessen en investeringen wegen zwaar</li></ul></div>
  </div>
  <div class="actions" style="margin-top:32px"><a class="btn btn-primary" href="{r}assets/downloads/whitepaper-evresys-aanvulling-zorgoproepsysteem.pdf" download>Download de whitepaper: Evresys als aanvulling</a><a class="btn btn-link" href="{EVRESYS_LEEF}" rel="noopener" target="_blank">Leefcirkels bij Evresys</a></div>
</div></section>

<section class="section mist" id="routes"><div class="container">
  <div class="section-head"><span class="kicker">Twee routes, één platform</span><h2>Niet iedere organisatie begint op hetzelfde punt</h2>
  <div class="lijn accent"><p class="lead">De vraag is niet welk systeem weg moet, maar welke functies goed geregeld zijn, wat ontbreekt en welke architectuur de meeste waarde geeft met zo min mogelijk onnodige verandering.</p></div></div>
  <div class="grid-2">
    <div class="route"><span class="badge">Route 1 · Totaaloplossing</span><h3>Beginnen met één geïntegreerde basis</h3><p class="muted">Voor kleinere organisaties, nieuwe locaties of situaties zonder zorgoproepsysteem. Evresys vormt de basis: van draadloze infrastructuur en wearables tot alarmering, lokalisatie, leefcirkels en bediening via app of webportaal.</p>
      <ul class="checklist"><li>Eén platform en één beheeromgeving in plaats van meerdere leveranciers</li><li>Gebruik van BLE in geschikte wifi-accesspoints, of een nieuw netwerk met BLE-gateways</li><li>Klein starten, later uitbreiden naar extra ruimtes, functies of locaties</li></ul>
      <a class="btn-link" href="{r}assets/downloads/whitepaper-evresys-totaaloplossing.pdf" download>Whitepaper: totaaloplossing (pdf)</a></div>
    <div class="route voorkeur"><span class="badge">Route 2 · Aanvulling</span><h3>Behouden wat goed werkt, gericht toevoegen</h3><p class="muted">Voor grotere instellingen met een goed werkend zorgoproepsysteem. Dat blijft de vertrouwde alarmketen. Evresys voegt lokalisatie, leefcirkels, dwaaldetectie en deurfunctionaliteit toe, met meldingen waar gewenst via de bestaande keten.</p>
      <ul class="checklist"><li>Geen ingrijpend vervangingstraject</li><li>Innoveren per locatie, afdeling of doelgroep</li><li>Bestaande investeringen en werkprocessen blijven behouden</li></ul>
      <a class="btn-link" href="{r}assets/downloads/whitepaper-evresys-aanvulling-zorgoproepsysteem.pdf" download>Whitepaper: aanvulling (pdf)</a></div>
  </div>
  <p style="margin-top:24px"><a class="btn btn-secondary" href="{r}assets/downloads/whitepaper-evresys-twee-routes.pdf" download>Download: Twee routes naar slimme zorgtechnologie</a></p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Onze werkwijze</span><h2>Van kennismaking tot support</h2></div>
  {steps([('Kennismaken', 'Uw situatie, doelen en bestaande systemen in kaart.'), ('Advies', 'De route en de oplossing die passen bij uw organisatie.'), ('Implementatie', 'Netwerk, wearables, tags en koppelingen, op maat ingericht.'), ('Training &amp; evaluatie', 'Medewerkers leren ermee werken, we evalueren samen.'), ('Support &amp; onderhoud', 'Doorlopend beheer en één aanspreekpunt.')])}
  <p class="small muted" style="margin-top:32px">Lokalisatie draait op uw netwerk. Daarom combineren we deze oplossingen graag met <a href="{r}zorg/netwerkregie/">Netwerkregie</a>, zodat dekking, segmentatie en beschikbaarheid vanaf het begin kloppen. Kwaliteit en informatiebeveiliging zijn geborgd met ISO 9001, ISO 27001 en NEN 7510.</p>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Verdieping</span><h2>Uit de praktijk</h2><p><a class="btn-link" href="{r}blog/#veiligheid">Meer over veiligheid</a></p></div>
  {latest(r, 3, slugs=['bescherming-op-de-werkvloer-medewerkersveiligheid-in-zorginstellingen', 'van-gevangenis-naar-de-zorg-praktische-lessen-over-medewerkersveiligheid', 'samenwerken-aan-zorginnovatie-silvercloud-en-evresys-bundelen-krachten'])}
</div></section>

{cta('Welke route past bij uw organisatie?', 'In een adviesgesprek brengen we samen in kaart wat er al is en wat nog ontbreekt.', 'Vraag een adviesgesprek aan', r + 'contact/', r)}
''', label='zorg', nav='zorg', sub='lokalisatie')

# ---------- MEDEWERKERSVEILIGHEID ----------
# Bronnen: Interakt-partnerdagpresentatie (toepassingen), Evresys-documenten (persoonsalarm, Push-to-Talk),
# blogs 'Bescherming op de werkvloer', 'Van gevangenis naar de zorg' en 'RTLS voor medewerkersveiligheid'.
r = '../../'
page('zorg/medewerkersveiligheid', 'Medewerkersveiligheid – SilverCloud Zorg',
 'Persoonsalarm, stille alarmering, locatie bij een alarm en Push-to-Talk: technologie die zorgmedewerkers beschermt. Geleverd en geïntegreerd door SilverCloud Zorg.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Zorgtechnologie · Medewerkersveiligheid</span>
    <h1 class="display">Nooit alleen bij een escalatie</h1>
    <p class="lead">Agressie tegen zorgmedewerkers neemt toe. Met persoonsalarm, stille alarmering, locatie bij een alarm en directe teamcommunicatie roepen medewerkers binnen seconden hulp in, overal in het gebouw. SilverCloud levert, integreert en beheert de oplossing van Evresys.</p>
    <div class="actions"><a class="btn btn-primary" href="{r}afspraak/">Plan een adviesgesprek</a><a class="btn btn-link" href="#oplossingen">Bekijk de mogelijkheden</a></div>
  </div>
  <div class="hero-visual" style="border-radius:18px;overflow:hidden">{art('safe')}</div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Waarom</span><h2>Veilig werken is de basis voor goede zorg</h2>
  <div class="lijn accent"><p class="lead">In de gehandicaptenzorg, GGZ en ziekenhuizen is snelle hulp bij een escalatie geen luxe maar noodzaak. En ook in de ouderenzorg wil een medewerker in de nachtdienst weten dat er direct backup komt.</p></div></div>
  <div class="grid-3">
    <div class="card flat">{icon('mens')}<h3>Mensen</h3><p>Medewerkers die zich veilig voelen, blijven. Wie bij een escalatie snel hulp krijgt, gaat met een gerust hart naar huis.</p></div>
    <div class="card flat">{icon('klok')}<h3>Tijd</h3><p>Bij een alarm telt elke seconde. Met locatie-informatie gaan collega’s direct naar de juiste plek, zonder zoeken.</p></div>
    <div class="card flat">{icon('schild')}<h3>Aantoonbaar</h3><p>Aantoonbare maatregelen voor een veilige werkplek, met registratie van meldingen en opvolging.</p></div>
  </div>
</div></section>

<section class="section" id="oplossingen"><div class="container">
  <div class="section-head"><span class="kicker">Mogelijkheden</span><h2>Wat we voor uw medewerkers inrichten</h2></div>
  <div class="grid-3">
    <div class="card flat">{icon('bel')}<h3>Persoonsalarm</h3><p>Via een wearable, badge of zorgtelefoon met fysieke alarmknop. Geen ontgrendelen of app zoeken: één druk en de melding gaat uit.</p></div>
    <div class="card flat">{icon('oog')}<h3>Stille alarmering</h3><p>Onopvallend hulp inroepen, bijvoorbeeld met een knop onder de tafel in een spreekkamer. Een zichtbaar alarm kan juist escaleren.</p></div>
    <div class="card flat">{icon('pin')}<h3>Locatie bij elk alarm</h3><p>Collega’s zien direct waar hulp nodig is, overal in het gebouw en waar gewenst ook buiten.</p></div>
    <div class="card flat">{icon('radio')}<h3>Push-to-Talk</h3><p>De smartphone als portofoon, per team, afdeling of verdieping. Direct collegiale hulp inroepen en afstemmen.</p></div>
    <div class="card flat">{icon('netwerk')}<h3>Gebouwbrede dekking</h3><p>Dekking die niet ophoudt bij de kamer of de afdeling, op een netwerk dat er volgens <a href="{r}zorg/netwerkregie/">Netwerkregie</a> op is ontworpen.</p></div>
    <div class="card flat">{icon('deur')}<h3>Koppeling met uw systemen</h3><p>Als aanvulling op uw bestaande zorgoproep- of domoticasysteem, of als onderdeel van één platform voor cliënten én medewerkers.</p></div>
  </div>
</div></section>

<section class="section deep"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker" style="color:var(--merk-oranje)">Uit de praktijk</span><h2>Bewezen in de meest veeleisende omgevingen</h2>
  <p class="lead" style="margin-top:16px">De technologie van onze partner Evresys is doorontwikkeld in het gevangeniswezen, waar medewerkers met noodknoppen en Push-to-Talk binnen seconden collega’s alarmeren. Die kennis is teruggebracht naar de zorg, met de menselijke maat die daar hoort.</p>
  <div class="actions"><a class="btn btn-highlight" href="{r}blog/van-gevangenis-naar-de-zorg-praktische-lessen-over-medewerkersveiligheid/">Lees: van gevangenis naar de zorg</a><a class="btn btn-secondary" style="color:#fff;border-color:#fff" href="{EVRESYS_URL}" rel="noopener" target="_blank">Meer over Evresys</a></div></div>
  <div class="uniek" style="grid-template-columns:1fr 1fr">
    <div><h3>Gehandicaptenzorg</h3><p>Snel hulp bij fysiek sterke cliënten die hun impulsen niet altijd kunnen beheersen.</p></div>
    <div><h3>GGZ</h3><p>Stille alarmknoppen in spreekkamers, zodat een gesprek niet onnodig escaleert.</p></div>
    <div><h3>Ziekenhuizen</h3><p>Bescherming bij agressie van gefrustreerde patiënten of bezoekers.</p></div>
    <div><h3>Ouderenzorg</h3><p>Zekerheid in de avond- en nachtdienst, als er weinig collega’s zijn.</p></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Privacy &amp; draagvlak</span><h2>Over veiligheid, niet over controle</h2>
  <p class="lead" style="margin-top:16px">Locatie van medewerkers is gevoelig. Met de juiste aanpak worden sceptici ambassadeurs.</p></div>
  <ul class="checklist">
    <li>Start met een pilot op de afdeling met de meeste incidenten</li>
    <li>Betrek de ondernemingsraad vanaf dag één</li>
    <li>Locatie wordt gebruikt bij een alarm, niet voor prestatiemeting</li>
    <li>Duidelijke afspraken over wie welke gegevens mag zien</li>
    <li>Ingericht volgens NEN 7510 en ISO 27001</li>
  </ul>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Volledige integrator</span><h2>Van advies tot beheer, één aanspreekpunt</h2>
  <p class="lead">SilverCloud levert de oplossing van <a href="{EVRESYS_URL}" rel="noopener" target="_blank">Evresys</a> als volledige integrator: advies, netwerk en dekking, wearables en koppelingen, training van medewerkers en doorlopend beheer.</p></div>
  {steps([('Kennismaken', 'Waar ontstaan incidenten, en wat is er al?'), ('Advies', 'De juiste combinatie van alarmering, locatie en communicatie.'), ('Implementatie', 'Dekking, apparatuur en koppelingen ingericht.'), ('Training', 'Medewerkers oefenen en weten wat te doen.'), ('Beheer', 'Monitoring, support en periodieke evaluatie.')])}
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Verdieping</span><h2>Meer over medewerkersveiligheid</h2><p><a class="btn-link" href="{r}blog/#veiligheid">Alle artikelen over veiligheid</a></p></div>
  {latest(r, 3, slugs=['rtls-voor-medewerkersveiligheid-de-verborgen-game-changer', 'bescherming-op-de-werkvloer-medewerkersveiligheid-in-zorginstellingen', 'de-echte-kosten-van-onveiligheid-wat-kost-een-incident-jouw-zorginstelling'])}
</div></section>

{certs(r)}

{cta('Hoe veilig werken uw medewerkers nu?', 'Plan een adviesgesprek. We kijken samen waar de risico’s zitten en welke oplossing past bij uw locaties.', 'Plan een adviesgesprek', r + 'afspraak/', r)}
''', label='zorg', nav='zorg', sub='veiligheid')

# ---------- HULPMIDDELENBEHEER (AssetGuard) ----------
# Bron: Realtime localisatie - IoT/Website info (productbeschrijvingen Snelvinden, Insight,
# TOPdesk-integratie, Advies), Overzicht AssetGuard.docx, 10 voordelen van Realtime lokalisatie.pdf,
# Customer Testimonial ZGEM.pdf en blog Argos-case (maart 2025).
r = '../../'
page('zorg/assetguard', 'Hulpmiddelenbeheer met AssetGuard – SilverCloud Zorg',
 'Met AssetGuard vinden zorgmedewerkers tilliften, rolstoelen en andere hulpmiddelen binnen seconden terug. Realtime lokalisatie, TOPdesk-integratie en rapportages als ontzorgende dienst.', f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="badge">Zorgtechnologie · Hulpmiddelenbeheer</span>
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
  <p class="lead">AssetGuard bestaat uit modules die u stap voor stap inzet. Alles wordt geleverd als ontzorgende dienst op het platform van <a href="{BLYOTT_AT}" rel="noopener" target="_blank">Blyott</a>, met SilverCloud als integrator.</p></div>
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

{tech_partners(r)}

{cta('Ook meer tijd voor goede zorg?', 'We helpen u graag met het opzetten van een pilot op één locatie.', 'Bespreek een pilot', r + 'contact/', r, 'Lees de klantcases', r + 'kennis/')}
''', label='zorg', nav='zorg', sub='assetguard')

# ---------- KENNIS & CASES ----------
r = '../'
page('kennis', 'Kennis & cases – SilverCloud',
 'Praktijkverhalen van zorgorganisaties, whitepapers over netwerkregie en lokalisatie, video’s en de blog van SilverCloud.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Kennis &amp; cases</span>
  <h1 class="display" style="margin:16px 0">Uit de praktijk</h1>
  <p class="lead">Hoe organisaties met SilverCloud werken, en wat ze daarvan leerden. Plus whitepapers, video’s en {len(POSTS)} blogartikelen om verder te lezen. Alle downloads zijn direct beschikbaar, zonder formulier.</p>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Klantcases</span><h2>Zorgorganisaties aan het woord</h2></div>
  <div class="grid-2">
    <article class="card case" id="argos">
      <span class="kicker">Argos Zorggroep · AssetGuard Snelvinden</span>
      <h3>“Een kwart van de werktijd ging verloren aan zoeken”</h3>
      <p>Argos Zorggroep heeft 11 locaties in de regio Rotterdam. Een nulmeting liet zien dat medewerkers ongeveer een kwart van hun werktijd kwijt waren aan zoeken. In februari 2024 startte een pilot in verpleeghuis Breede Vliet (180 bewoners). De resultaten waren zo goed dat de oplossing naar drie nieuwe locaties gaat.</p>
      <p><strong>Lessen:</strong> betrek teamleiders vanaf het begin, stel per locatie een projectgroep samen met verschillende functies en bepaal per huis welke hulpmiddelen een tag krijgen.</p>
      <blockquote class="mini">“We hebben niet alleen een product gekocht, maar een partner gevonden die meedenkt over toekomstbestendige zorg.” <span>Janneke Boevink, projectleider, Argos Zorggroep</span></blockquote>
      <a class="btn-link" href="{r}blog/een-kwart-van-de-werktijd-ging-verloren-aan-zoeken-argos-zorggroep-over-realtime-lokalisatie-van-hulpmiddelen/">Lees het hele verhaal</a>
    </article>
    <article class="card case" id="zgem">
      <span class="kicker">Zorggroep Elde Maasduinen · RTLS + TOPdesk</span>
      <h3>1.700 tags en één bronsysteem</h3>
      <p>Na eerdere proeven met wifi-oplossingen koos ZGEM voor de Bluetooth Low Energy-oplossing van Blyott, met SilverCloud als systeemintegrator. TOPdesk is het bronsysteem; SilverCloud bouwde de koppeling met het lokalisatiesysteem. Elke medewerker bespaart zo’n 25 minuten zoektijd per week.</p>
      <blockquote class="mini">“In SilverCloud vonden we een partner die actief meedacht en kennis had van de zorgsector.” <span>Wiebe de Vries, ZGEM</span></blockquote>
      <a class="btn-link" href="{r}assets/downloads/klantcase-zgem-realtime-lokalisatie.pdf">Download de case (pdf)</a>
      <a class="btn-link" href="{r}blog/grootschalige-implementatie-van-real-time-lokalisatie-bij-zorggroep-elde-maasduinen/">Lees over de implementatie</a>
    </article>
    <article class="card case" id="spits">
      <span class="kicker">SPITS Oosterwolde · Blyott en Wiliot</span>
      <h3>Samen innoveren met lokalisatie</h3>
      <p>Een samenwerking tussen SPITS Oosterwolde, Blyott, Wiliot en SilverCloud rond het lokaliseren van hulpmiddelen met nieuwe sensortechnologie.</p>
      <a class="btn-link" href="{r}blog/unieke-samenwerking-silvercloud-zorg-iot-spits-oosterwolde-blyott-en-wiliot/">Lees over de samenwerking</a>
      <a class="btn-link" href="{r}blog/spits-testimonial/">Bekijk de testimonial</a>
    </article>
    <article class="card case" id="znwv">
      <span class="kicker">ZNWV · Slimme vergaderkamers</span>
      <h3>Moderne vergaderruimtes voor hybride werken</h3>
      <p>SilverCloud richtte de vergaderkamers in voor ZNWV, zodat collega’s op locatie en op afstand eenvoudig samen kunnen werken.</p>
      <a class="btn-link" href="{r}blog/silvercloud-zorgiot-richt-vergaderkamers-in-voor-znwv/">Lees meer</a>
    </article>
  </div>
  <p class="small muted" style="margin-top:24px">Praktijkverhalen over Netwerkregie en CareDesk volgen.</p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Downloads</span><h2>Whitepapers en factsheets</h2></div>
  <div class="grid-3">
    {wp_card(r)}
    <a class="card download" href="{r}assets/downloads/brochure-caredesk.pdf" download>{icon('helpdesk')}<h3>Brochure CareDesk</h3><p>Dé servicedesk voor zorgorganisaties: overnemen, versterken of optimaliseren.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/whitepaper-evresys-twee-routes.pdf" download>{icon('cirkel')}<h3>Twee routes naar slimme zorgtechnologie</h3><p>Evresys als totaaloplossing of als aanvulling op een bestaand zorgoproepsysteem.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/whitepaper-evresys-totaaloplossing.pdf" download>{icon('bel')}<h3>Evresys als totaaloplossing</h3><p>Voor kleinere zorgorganisaties en nieuwe locaties zonder zorgoproepsysteem.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/whitepaper-evresys-aanvulling-zorgoproepsysteem.pdf" download>{icon('deur')}<h3>Evresys als aanvulling</h3><p>Lokalisatie en leefcirkels naast een bestaand zorgoproepsysteem.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/10-voordelen-realtime-lokalisatie.pdf" download>{icon('pin')}<h3>10 voordelen van realtime lokalisatie</h3><p>Wat lokalisatie oplevert voor de zorgmedewerker, de zorgmanager en de cliënt.</p><span class="btn-link">Download (pdf)</span></a>
    <a class="card download" href="{r}assets/downloads/klantcase-zgem-realtime-lokalisatie.pdf" download>{icon('mens')}<h3>Klantcase Zorggroep Elde Maasduinen</h3><p>Realtime lokalisatie met TOPdesk-integratie in de praktijk.</p><span class="btn-link">Download (pdf)</span></a>
  </div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Video &amp; webinars</span><h2>Bekijk en luister</h2></div>
  <div class="grid-2">
    <div class="video"><iframe src="https://player.vimeo.com/video/885122327?dnt=1" title="Webinar realtime lokalisatie" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>
    <div class="video"><iframe src="https://player.vimeo.com/video/555633421?dnt=1" title="Zorgmedewerker in de praktijk" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>
    <div class="video"><iframe src="https://player.vimeo.com/video/908604204?dnt=1" title="Zorgmanager met de juiste tools" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>
    <div class="video"><iframe src="https://player.vimeo.com/video/555632960?dnt=1" title="Realtime lokalisatie in het kort" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><span class="kicker">Blog</span><h2>{len(POSTS)} artikelen uit de zorgpraktijk</h2><p><a class="btn btn-secondary" href="{r}blog/">Naar de blog</a></p></div>
  {latest(r, 3)}
</div></section>

{cta('Wilt u zo’n resultaat ook?', 'We delen graag onze ervaringen en kijken samen wat bij uw organisatie past.', 'Neem contact op', r + 'contact/', r)}
''', nav='kennis')

# ---------- OVER ONS ----------
r = '../'
page('over-ons', 'Over SilverCloud – werkwijze en visie',
 'SilverCloud: ICT-specialisten die de zorg kennen. Cultuur, uitdagingen, applicaties en zorgtechnologie, met dezelfde zorgvuldigheid voor het mkb.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Over SilverCloud</span>
  <h1 class="display" style="margin:16px 0">ICT-specialisten die de zorg kennen</h1>
  <p class="lead">SilverCloud helpt organisaties om technologie betrouwbaar onderdeel te maken van hun dagelijkse werk. In de zorg betekent dat: weten hoe zorgteams werken, welke uitdagingen er spelen, welke applicaties en zorgtechnologie er draaien en hoe je daarover communiceert. Die kennis is ons vertrekpunt, de techniek volgt.</p>
  <div class="lijn"><p>We werken naast uw interne organisatie en andere leveranciers. Niet vanuit losse producten, maar vanuit architectuur, duidelijke regie en een gezamenlijke roadmap. Zo ontstaat een omgeving die vandaag betrouwbaar werkt en morgen kan meegroeien.</p></div>
</div></section>

{zorgkennis(r)}

<section class="section mist"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Zorgervaring in het team</span><h2>Geen techneuten op afstand</h2>
  <p class="lead" style="margin-top:16px">Onze kennis van de zorg komt uit de praktijk, niet uit een brochure.</p></div>
  <ul class="checklist">
    <li>Ervaring als interim hoofd ICT en programmamanager bij complexe zorgprojecten</li>
    <li>Collega’s die zelf jaren in de ouderenzorg hebben gewerkt</li>
    <li>Dagelijks in contact met zorgteams in VVT, gehandicaptenzorg, GGZ en ziekenhuizen</li>
    <li>Kennis van ECD’s, Zenya, AFAS, TOPdesk, domotica en zorgalarmering</li>
    <li>Gecertificeerd voor NEN 7510: de norm voor informatiebeveiliging in de zorg</li>
    <li>Partner van zorgorganisaties als Argos Zorggroep en Zorggroep Elde Maasduinen</li>
  </ul>
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

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Het team</span><h2>De mensen achter SilverCloud</h2><p class="lead">Small enough to know you, large enough to serve you. Een team van meer dan tien professionals, van systeemtechniek en netwerkarchitectuur tot projectmanagement, adoptie en begeleiding.</p></div>
  <div class="team">
    <div><span class="avatar">PS</span><h3>Peter Sminia</h3><p><strong>Managing Partner</strong></p><p>Strategie, beleid en innovatie in de zorg. Vaak gevraagd als interim hoofd ICT of programmamanager bij complexe zorgprojecten.</p></div>
    <div><span class="avatar">WK</span><h3>Wim Koopman</h3><p><strong>Managing Partner</strong></p><p>De techniek achter de schermen: architectuur, implementatie en beheer.</p></div>
    <div><span class="avatar">KD</span><h3>Karla Dokter</h3><p><strong>Commercieel Manager</strong></p><p>Passie voor de zorg, interesse in techniek. Eerste aanspreekpunt voor zorgorganisaties.</p></div>
    <div><span class="avatar">NK</span><h3>Nana van Kleef</h3><p><strong>Frontoffice</strong></p><p>Zes jaar ervaring in de ouderenzorg, nu de spil op kantoor en van onze webshop.</p></div>
  </div>
</div></section>

<section class="section"><div class="container grid-2" style="align-items:start">
  <div><span class="kicker">Kwaliteit &amp; informatiebeveiliging</span><h2>Gecertificeerd, en dat merkt u in het werk</h2>
  <p class="lead" style="margin-top:16px">Certificering is voor ons geen stempel, maar een manier van werken: continu verbeteren en zorgvuldig omgaan met informatie.</p></div>
  <div><ul class="checklist"><li><strong>NEN 7510</strong>: informatiebeveiliging in de zorg</li><li><strong>ISO 27001</strong>: informatiebeveiliging</li><li><strong>ISO 9001</strong>: kwaliteitsmanagement</li></ul><p style="margin-top:16px"><a class="btn-link" href="{r}kwaliteit-informatiebeveiliging/">Ons beleid en de certificaten</a></p></div>
</div></section>

<section class="section mist"><div class="container">
  <div class="section-head"><span class="kicker">Partners</span><h2>Sterke techniek, één regisseur</h2><p><a class="btn-link" href="{r}partners/">Over onze partners</a></p></div>
  {logo_strip(r)}
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
    <p><a class="btn btn-primary" href="{r}afspraak/">Direct een afspraak plannen</a></p>
    <div class="lijn" style="margin-top:32px">
      <p><strong>SilverCloud</strong><br>Ohmstraat 18-A<br>3861 NB Nijkerk</p>
      <p><a href="tel:+31882560050">088 256 00 50</a><br><a href="mailto:info@silvercloud.nl">info@silvercloud.nl</a></p>
    </div>
  </div>
  <form class="form card" action="https://formsubmit.co/sales@silvercloud.nl" method="POST">
    <input type="hidden" name="_subject" value="Contactaanvraag via de website"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="row"><label>Naam<input name="naam" autocomplete="name" required></label><label>Organisatie<input name="organisatie" autocomplete="organization"></label></div>
    <div class="row"><label>E-mailadres<input type="email" name="email" autocomplete="email" required></label><label>Telefoon<input type="tel" name="telefoon" autocomplete="tel"></label></div>
    <label>Waar gaat uw vraag over?<select name="onderwerp"><option>SilverCloud Computing (mkb)</option><option>Netwerkregie (zorg)</option><option>CareDesk (zorg)</option><option>Lokalisatie &amp; Leefcirkels (zorg)</option><option>Hulpmiddelenbeheer / AssetGuard (zorg)</option><option>Iets anders</option></select></label>
    <label>Uw vraag<textarea name="bericht"></textarea></label>
    <button class="btn btn-primary" type="submit">Verstuur</button>
  </form>
</div></section>
''', nav='')
extra.build(page, cta, OUT)
extra.afspraak_page(page)
import juridisch
juridisch.build(page, OUT)
print('ok')
