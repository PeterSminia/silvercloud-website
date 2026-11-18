# Aanvullingen v0.3: blog (alle artikelen van silvercloudzorgiot.nl), partners, doorverwijzingen.
# Wordt aangeroepen vanuit build.py en gebruikt dezelfde page()-functie en stijl.
import json, os, re, html as _html

HERE = os.path.dirname(__file__)
OLD = 'https://www.silvercloudzorgiot.nl/nijkerk/wp-content/uploads/'
esc = _html.escape
MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december']

POSTS = json.load(open(os.path.join(HERE, 'posts.json'), encoding='utf-8'))
POSTS.sort(key=lambda p: p['date'], reverse=True)

CATS = [('netwerk', 'Netwerk &amp; ICT'), ('lokalisatie', 'Lokalisatie &amp; hulpmiddelen'), ('veiligheid', 'Veiligheid'),
        ('praktijk', 'Praktijk &amp; mensen'), ('nieuws', 'Nieuws &amp; partners')]
CAT = dict(CATS)


def _cats(p):
    t = (p['title'] + ' ' + p['body'][:600]).lower()
    c = []
    if re.search(r'netwerk|helpdesk|it-trends|applicatie|xelion|vergaderkamer|ict|infrastructuur', t): c.append('netwerk')
    if re.search(r'rtls|lokalisatie|hulpmiddel|tag|sensor|assetguard|track|blyott|docksters|tillift', t): c.append('lokalisatie')
    if re.search(r'veilig|agressie|gevangenis|alarm', t): c.append('veiligheid')
    if re.search(r'argos|elde maasduinen|zgem|spits|ervaring|testimonial|story|dag uit het leven|dag met|aan het woord|reis|anita|achter de schermen|zo.n sensor', t): c.append('praktijk')
    if re.search(r'webinar|beurs|partner|samenwerk|certific|sponsor|estafette|bundelen', p['title'].lower()): c.append('nieuws')
    return c or ['nieuws']


for _p in POSTS:
    _p['cats'] = _cats(_p)


def datum(iso):
    y, m, d = map(int, iso.split('-'))
    return f'{d} {MAANDEN[m-1]} {y}'


def post_card(p, r):
    return (f'<a class="post-card" href="{r}blog/{p["slug"]}/"><span class="thumb"><img src="{esc(p["hero"])}" alt="" loading="lazy"></span>'
            f'<span class="meta">{datum(p["date"])} · {CAT[p["cats"][0]]}</span><h3>{esc(p["title"])}</h3></a>')


def latest(r, n=3, cat=None, slugs=None):
    ps = POSTS
    if slugs:
        ps = [p for s in slugs for p in POSTS if p['slug'] == s]
    elif cat:
        ps = [p for p in POSTS if cat in p['cats']]
    return '<div class="grid-3">' + ''.join(post_card(p, r) for p in ps[:n]) + '</div>'


LOGOS = [('fortinet.png', 'Fortinet'), ('datto.png', 'Datto'), ('topdesk.png', 'TOPdesk'), ('ultimo.png', 'Ultimo'),
         ('evresys.png', 'Evresys'), ('blyott.png', 'Blyott'), ('wiliot.png', 'Wiliot'), ('xelion.png', 'Xelion')]


def logo_strip(r):
    return ('<div class="logos"><span class="wm">HPE Aruba</span>' + ''.join(
        f'<img src="{r}assets/img/partners/{f}" alt="{n}" loading="lazy">' for f, n in LOGOS) + '<span class="wm">RSR</span></div>')


def wp_card(r):
    return (f'<a class="card download wp" href="{r}assets/downloads/whitepaper-netwerkregie-zorg.pdf" download>'
            f'<span class="kicker">Whitepaper · pdf</span><h3>Netwerkregie voor de zorg</h3>'
            f'<p>Van technisch netwerkbeheer naar een veilige, voorspelbare en toekomstbestendige digitale infrastructuur. Vijf uitgangspunten en onze aanpak.</p>'
            f'<span class="btn btn-primary" style="align-self:flex-start">Download de whitepaper</span></a>')


def _md(body):
    out, ul = [], False
    for line in body.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('- '):
            if not ul:
                out.append('<ul>'); ul = True
            out.append(f'<li>{esc(line[2:])}</li>'); continue
        if ul:
            out.append('</ul>'); ul = False
        if line.startswith('### '):
            out.append(f'<h3>{esc(line[4:])}</h3>')
        elif line.startswith('## '):
            out.append(f'<h2>{esc(line[3:])}</h2>')
        elif line.startswith('> '):
            out.append(f'<blockquote>{esc(line[2:])}</blockquote>')
        else:
            out.append(f'<p>{esc(line)}</p>')
    if ul:
        out.append('</ul>')
    return '\n'.join(out)


def _excerpt(body, n=155):
    for line in body.split('\n'):
        if line and not line.startswith(('#', '-', '>')) and len(line) > 60:
            return (line[:n].rsplit(' ', 1)[0] + '…') if len(line) > n else line
    return ''


PARTNERS = [
    ('Netwerk &amp; security', [
        ('Fortinet', 'fortinet.png', 'Next-generation firewalls, Zero Trust Network Access en security-driven networking. Onderdeel van onze standaard doelarchitectuur.', None),
        ('HPE Aruba', None, 'Switching en wifi met centraal beheer. De basis voor betrouwbare, snelle verbindingen op zorglocaties en kantoren.', None),
        ('Datto', 'datto.png', 'Back-up en business continuity, zodat gegevens en systemen snel terug zijn als het nodig is.', None)]),
    ('Service &amp; applicaties', [
        ('TOPdesk', 'topdesk.png', 'Servicemanagement. Wij koppelen lokalisatie aan TOPdesk, zodat meldingen en hulpmiddelen samenkomen.', 'slimmer-sneller-simpeler-de-opbrengsten-van-topdesk-en-rtls-integratie'),
        ('Ultimo', 'ultimo.png', 'Assetmanagement. Integratie in twee richtingen met AssetGuard: onderhoudsdata zichtbaar in de app.', None),
        ('Xelion', 'xelion.png', 'Zakelijke telefonie en communicatie.', 'webinar-xelion-8-1-wat-kan-het-voor-u-toevoegen')]),
    ('Lokalisatie &amp; zorgtechnologie', [
        ('Evresys', 'evresys.png', 'Zorgalarmering, realtime lokalisatie, leefcirkels en medewerkersveiligheid. Het platform achter Lokalisatie &amp; Leefcirkels.', 'samenwerken-aan-zorginnovatie-silvercloud-en-evresys-bundelen-krachten'),
        ('Blyott', 'blyott.png', 'Realtime lokalisatieplatform voor medische hulpmiddelen. Partner sinds 2020.', 'silvercloud-zorgiot-value-added-partner-van-blyott'),
        ('RSR', None, 'Ruim 50 jaar ervaring in mobiliteits- en zorghulpmiddelen. Samen koppelen we lokalisatiedata aan advies over hulpmiddelenbeleid.', 'waarom-we-partneren-met-rsr-van-techniek-naar-nog-meer-toegevoegde-waarde'),
        ('Wiliot', 'wiliot.png', 'Sensortechnologie voor het taggen van hulpmiddelen.', 'unieke-samenwerking-silvercloud-zorg-iot-spits-oosterwolde-blyott-en-wiliot'),
        ('Docksters', 'docksters.png', 'IoT-dataplatform voor actueel data-inzicht. SilverCloud is Solution Integration Partner.', 'docksters-partner')]),
]

REDIRECTS = {
    # oude silvercloudzorgiot.nl-adressen
    'nieuws-blog': 'blog/', 'kennisbank': 'kennis/', 'assetguard': 'zorg/assetguard/', 'realtime-lokalisatie': 'zorg/lokalisatie-leefcirkels/',
    'realtime-lokalisatie-oud-back-up': 'zorg/lokalisatie-leefcirkels/', 'cloud-based-iot-monitoring': 'zorg/lokalisatie-leefcirkels/',
    'intelligente-netwerken': 'zorg/netwerkregie/', 'support': 'contact/', '10-voordelen-realtime-lokalisatie': 'kennis/',
    'slimme-vergaderkamers': 'kennis/', 'iso-9001-27001-nen-7510': 'over-ons/', 'netwerkregie': 'zorg/netwerkregie/', 'caredesk': 'zorg/caredesk/',
}


def _redirect(out, path, target):
    depth = path.count('/') + 1
    t = '../' * depth + target + ('index.html' if target.endswith('/') or target == '' else '')
    d = os.path.join(out, path)
    if os.path.exists(os.path.join(d, 'index.html')):
        return
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
        f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>Doorverwijzing</title><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0; url={t}"></head><body><p>Deze pagina is verhuisd: <a href="{t}">ga verder</a>.</p></body></html>')


def build(page, cta, out):
    # ---------- Blogoverzicht ----------
    r = '../'
    rows = ''.join(
        f'<a class="post-row" href="{r}blog/{p["slug"]}/" data-cat="{" ".join(p["cats"])}" data-search="{esc((p["title"] + " " + p["body"][:400]).lower(), quote=True)}">'
        f'<span class="d">{datum(p["date"])}</span><span class="t">{esc(p["title"])}</span><span class="badge">{CAT[p["cats"][0]]}</span></a>' for p in POSTS)
    chips = '<button class="chip" data-cat="alle" aria-pressed="true">Alles</button>' + ''.join(
        f'<button class="chip" data-cat="{k}" aria-pressed="false">{v}</button>' for k, v in CATS)
    page('blog', 'Blog – SilverCloud Zorg', 'Artikelen van SilverCloud Zorg over netwerkregie, realtime lokalisatie, medewerkersveiligheid en zorg-ICT.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Blog &amp; nieuws</span>
  <h1 class="display" style="margin:16px 0">Inzichten uit de zorgpraktijk</h1>
  <p class="lead">Over netwerken, lokalisatie, veiligheid en de mensen die ermee werken. {len(POSTS)} artikelen sinds {POSTS[-1]["date"][:4]}.</p>
</div></section>
<section class="section mist"><div class="container">{latest(r, 3)}</div></section>
<section class="section"><div class="container">
  <div class="filters" role="group" aria-label="Filter op onderwerp">{chips}<label class="search"><span class="sr-only">Zoek in de blog</span><input id="q" type="search" placeholder="Zoek in {len(POSTS)} artikelen"></label></div>
  <p class="small muted" aria-live="polite"><span id="count">{len(POSTS)}</span> artikelen</p>
  <div class="post-list" id="post-list">{rows}</div>
  <p id="geen" class="muted" hidden>Geen artikelen gevonden.</p>
</div></section>
<script>
(function(){{var l=document.getElementById('post-list'),q=document.getElementById('q'),cs=document.querySelectorAll('.chip'),cat='alle';
function f(){{var t=(q.value||'').toLowerCase().trim(),n=0;l.querySelectorAll('.post-row').forEach(function(a){{var ok=(cat==='alle'||a.dataset.cat.split(' ').indexOf(cat)>-1)&&(!t||a.dataset.search.indexOf(t)>-1);a.hidden=!ok;if(ok)n++}});document.getElementById('count').textContent=n;document.getElementById('geen').hidden=n>0}}
cs.forEach(function(c){{c.addEventListener('click',function(){{cs.forEach(function(x){{x.setAttribute('aria-pressed','false')}});c.setAttribute('aria-pressed','true');cat=c.dataset.cat;f()}})}});q.addEventListener('input',f);
var h=location.hash.slice(1);if(h){{var c=document.querySelector('.chip[data-cat="'+h+'"]');if(c)c.click()}}}})();
</script>
{cta('Liever direct in gesprek?', 'We denken graag mee over uw netwerk, servicedesk of zorgtechnologie.', 'Neem contact op', r + 'contact/', r)}
''', label='zorg', nav='blog')

    # ---------- Artikelen ----------
    r = '../../'
    for i, p in enumerate(POSTS):
        rel = [q for q in POSTS if q is not p and set(q['cats']) & set(p['cats'])][:3]
        tags = ' '.join(f'<a class="badge" href="{r}blog/#{c}">{CAT[c]}</a>' for c in p['cats'])
        prev_ = POSTS[i + 1] if i + 1 < len(POSTS) else None
        next_ = POSTS[i - 1] if i > 0 else None
        nav = (f'<a class="btn-link" href="{r}blog/{prev_["slug"]}/">← Vorig artikel</a>' if prev_ else '') + \
              (f'<a class="btn-link" href="{r}blog/{next_["slug"]}/">Volgend artikel →</a>' if next_ else '')
        page(f'blog/{p["slug"]}', f'{esc(p["title"])} – SilverCloud Zorg', esc(_excerpt(p['body']) or p['title']), f'''
<article>
<section class="hero"><div class="container narrow">
  <p class="small muted"><a href="{r}blog/">Blog</a> · <time datetime="{p["date"]}">{datum(p["date"])}</time></p>
  <h1 style="margin:12px 0 16px">{esc(p["title"])}</h1>
  <div class="tags-row">{tags}</div>
  <figure class="shot post-hero"><img src="{esc(p["hero"])}" alt=""></figure>
</div></section>
<section class="section" style="padding-top:0"><div class="container narrow">
  <div class="prose">{_md(p["body"])}</div>
  <div class="post-nav">{nav}</div>
</div></section>
</article>
<section class="section mist"><div class="container"><div class="section-head"><span class="kicker">Lees ook</span><h2>Meer over dit onderwerp</h2></div>
<div class="grid-3">{"".join(post_card(q, r) for q in rel)}</div></div></section>
{cta('Vragen over dit onderwerp?', 'We denken graag met u mee.', 'Neem contact op', r + 'contact/', r)}
''', label='zorg', nav='blog')
        _redirect(out, p['slug'], f'blog/{p["slug"]}/')

    # ---------- Partners ----------
    r = '../'
    slugs = {p['slug'] for p in POSTS}
    groups = ''
    for g, items in PARTNERS:
        cards = ''
        for n, logo, d, s in items:
            vis = f'<img class="partner-logo" src="{r}assets/img/partners/{logo}" alt="{n}">' if logo else f'<span class="partner-logo wm">{n}</span>'
            more = f'<a class="btn-link" href="{r}blog/{s}/">Lees meer</a>' if s and s in slugs else ''
            cards += f'<div class="card flat">{vis}<h3>{n}</h3><p>{d}</p>{more}</div>'
        groups += f'<div class="section-head" style="margin-top:48px"><span class="kicker">{g}</span></div><div class="grid-3">{cards}</div>'
    page('partners', 'Partners – SilverCloud', 'De technologiepartners van SilverCloud: Fortinet, HPE Aruba, Datto, TOPdesk, Ultimo, Xelion, Evresys, Blyott, RSR, Wiliot en Docksters.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Partners</span>
  <h1 class="display" style="margin:16px 0">Sterke techniek, één regisseur</h1>
  <p class="lead">We kiezen partners op basis van architectuur en kwaliteit, niet andersom. SilverCloud blijft uw aanspreekpunt en zorgt dat alles op elkaar aansluit.</p>
</div></section>
<section class="section mist"><div class="container">{groups}</div></section>
{cta('Benieuwd hoe dit samenkomt in uw omgeving?', 'We laten graag zien hoe we techniek van verschillende partijen tot één geheel maken.', 'Neem contact op', r + 'contact/', r)}
''', nav='over')

    for old, new in REDIRECTS.items():
        _redirect(out, old, new)

    # sitemap
    paths = ['', 'computing/', 'zorg/', 'zorg/netwerkregie/', 'zorg/caredesk/', 'zorg/lokalisatie-leefcirkels/', 'zorg/medewerkersveiligheid/', 'zorg/assetguard/',
             'kennis/', 'blog/', 'partners/', 'over-ons/', 'contact/'] + [f'blog/{p["slug"]}/' for p in POSTS]
    base = 'https://petersminia.github.io/silvercloud-website/'
    open(os.path.join(out, 'sitemap.xml'), 'w', encoding='utf-8').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
        ''.join(f'<url><loc>{base}{u}</loc></url>' for u in paths) + '</urlset>\n')


CERT_URLS = [('NEN 7510', 'Informatiebeveiliging in de zorg', OLD + '2021/01/30265-1-Certificaat-NEN-7510-PDF.pdf'),
             ('ISO 27001', 'Informatiebeveiliging', OLD + '2021/01/30265-1-Certificaat-ISO-27001-NL-PDF.pdf'),
             ('ISO 9001', 'Kwaliteitsmanagement', OLD + '2021/01/30265-1-Certificaat-ISO-9001-NL-PDF1.pdf')]


def certs(r, tekst='Wij werken aantoonbaar zorgvuldig: onze kwaliteit en informatiebeveiliging zijn onafhankelijk gecertificeerd. Voor de zorg betekent NEN 7510 dat we voldoen aan de norm voor informatiebeveiliging in de zorg.'):
    items = ''.join(f'<a class="cert" href="{u}" rel="noopener"><span class="cert-mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg></span><span><strong>{n}</strong><small>{d}</small></span></a>' for n, d, u in CERT_URLS)
    return (f'<section class="section certs-band"><div class="container certs-grid"><div><span class="kicker">Gecertificeerd</span>'
            f'<h2>NEN 7510, ISO 27001 en ISO 9001</h2><p class="muted" style="margin-top:12px">{tekst}</p></div><div class="certs">{items}</div></div></section>')


def afspraak_page(page, r='../'):
    tijden = ''.join(f'<option>{h:02d}:{m:02d}</option>' for h in range(8, 17) for m in (0, 30) if not (h == 8 and m == 0))
    page('afspraak', 'Plan een afspraak – SilverCloud', 'Plan direct een afspraak met SilverCloud: kies een datum en tijd, wij bevestigen per e-mail.', f'''
<section class="hero"><div class="container grid-2" style="align-items:start">
  <div>
    <span class="badge">Afspraak plannen</span>
    <h1 class="display" style="margin:16px 0">Plan een afspraak</h1>
    <p class="lead">Kies een datum en tijd die u uitkomt. We bevestigen de afspraak per e-mail, of stellen een alternatief voor als het moment al bezet is.</p>
    <div class="lijn" style="margin-top:32px"><p>Liever direct contact?<br><a href="tel:+31882560050">088 256 00 50</a> · <a href="mailto:sales@silvercloud.nl">sales@silvercloud.nl</a></p></div>
  </div>
  <form class="form card" action="https://formsubmit.co/sales@silvercloud.nl" method="POST">
    <input type="hidden" name="_subject" value="Afspraakverzoek via de website">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="true">
    <input type="hidden" name="_next" id="next" value="">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="row"><label>Naam<input name="Naam" autocomplete="name" required></label><label>Organisatie<input name="Organisatie" autocomplete="organization"></label></div>
    <div class="row"><label>E-mailadres<input type="email" name="email" autocomplete="email" required></label><label>Telefoon<input type="tel" name="Telefoon" autocomplete="tel"></label></div>
    <div class="row"><label>Datum<input type="date" name="Datum" id="datum" required></label><label>Tijd<select name="Tijd" required>{tijden}</select></label></div>
    <label>Soort afspraak<select name="Soort afspraak"><option>Online (Teams)</option><option>Bij u op locatie</option><option>Bij ons in Nijkerk</option><option>Telefonisch</option></select></label>
    <label>Onderwerp<select name="Onderwerp"><option>Netwerkregie (zorg)</option><option>CareDesk (zorg)</option><option>Lokalisatie &amp; Leefcirkels (zorg)</option><option>Hulpmiddelenbeheer / AssetGuard (zorg)</option><option>ICT voor het mkb (Computing)</option><option>Iets anders</option></select></label>
    <label>Toelichting (optioneel)<textarea name="Toelichting"></textarea></label>
    <p class="small muted">We gebruiken uw gegevens alleen om de afspraak in te plannen.</p>
    <button class="btn btn-primary" type="submit">Afspraak aanvragen</button>
  </form>
</div></section>
<script>
(function(){{var d=document.getElementById('datum'),t=new Date();t.setDate(t.getDate()+1);d.min=t.toISOString().slice(0,10);
d.addEventListener('change',function(){{var w=new Date(d.value).getDay();d.setCustomValidity(w===0||w===6?'Kies een werkdag (ma–vr).':'')}});
document.getElementById('next').value=new URL('bedankt/index.html',location.href.replace(/index\\.html$/,'')).href;}})();
</script>
''', nav='')
    page('afspraak/bedankt', 'Bedankt – SilverCloud', 'Uw afspraakverzoek is verstuurd.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Verstuurd</span>
  <h1 class="display" style="margin:16px 0">Bedankt voor uw aanvraag</h1>
  <p class="lead">We hebben uw afspraakverzoek ontvangen en bevestigen het zo snel mogelijk per e-mail, uiterlijk binnen één werkdag.</p>
  <div class="actions"><a class="btn btn-primary" href="../../">Terug naar de homepage</a><a class="btn btn-secondary" href="../../blog/">Lees de blog</a></div>
</div></section>
''', nav='')
