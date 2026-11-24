# Juridische pagina's en kwaliteitspagina, overgenomen van de oude websites
# (silvercloudzorgiot.nl en silvercloud.nl) en aangepast aan deze site.
import os

OLD = 'https://www.silvercloudzorgiot.nl/nijkerk/wp-content/uploads/2021/01/'
PDFS = {
    'beleid': 'silvercloud-kwaliteits-en-informatiebeveiligingsbeleid.pdf',
    'iso9001': 'certificaat-iso-9001.pdf',
    'iso27001': 'certificaat-iso-27001.pdf',
    'nen7510': 'certificaat-nen-7510.pdf',
}


def pdf(out, r, key):
    """Lokale kopie in assets/downloads als die er is, anders de oude site."""
    naam = PDFS[key]
    if os.path.exists(os.path.join(out, 'assets', 'downloads', naam)):
        return f'{r}assets/downloads/{naam}'
    return OLD + naam


def tekstpagina(page, path, title, desc, badge, h1, lead, body, bijgewerkt):
    page(path, title, desc, f'''
<section class="hero"><div class="container narrow">
  <span class="badge">{badge}</span>
  <h1 class="display" style="margin:16px 0">{h1}</h1>
  <p class="lead">{lead}</p>
</div></section>
<section class="section" style="padding-top:0"><div class="container narrow prose">
{body}
<p class="small muted" style="margin-top:2em">{bijgewerkt}</p>
</div></section>
''', nav='')


def build(page, out):
    r = '../'
    contact = ('<p><strong>SilverCloud</strong><br>Ohmstraat 18-A<br>3861 NB Nijkerk<br>'
               '<a href="tel:+31882560050">088 256 00 50</a> · <a href="mailto:info@silvercloud.nl">info@silvercloud.nl</a></p>')

    # ---------- PRIVACYVERKLARING ----------
    tekstpagina(page, 'privacyverklaring', 'Privacyverklaring – SilverCloud',
        'Hoe SilverCloud omgaat met de gegevens die u ons verstrekt.',
        'Privacy', 'Privacyverklaring',
        'SilverCloud hecht veel waarde aan uw privacy. Daarom houden we ons altijd aan de regels rond de privacywet.',
        f'''
<p>Uw gegevens zijn veilig bij ons en worden altijd volgens de geldende richtlijnen opgeslagen en beveiligd. In deze privacyverklaring vindt u alle informatie over het verzamelen, gebruiken en opslaan van de gegevens die u ons verstrekt. Deze verklaring geldt voor SilverCloud Computing en SilverCloud Zorg.</p>
<p>Als u vragen heeft, of wilt weten wat we precies van u bijhouden, neem dan contact met ons op. Onze contactgegevens staan onderaan deze verklaring.</p>

<h2>Contactformulieren en nieuwsbrieven</h2>
<p>U kunt gebruikmaken van het contactformulier of het afsprakenformulier om ons vragen te stellen of aanvragen te doen. Het (factuur)adres, e-mailadres, IP-adres, telefoonnummer en andere NAW-gegevens worden door ons gebruikt en opgeslagen, omdat wij deze informatie nodig kunnen hebben om u van antwoord te voorzien. Wanneer u tevreden bent met onze reactie, worden de gegevens verwijderd.</p>
<p>De formulieren op deze website worden verstuurd via de dienst FormSubmit (formsubmit.co), die uw bericht per e-mail aan ons doorstuurt.</p>
<p>Abonneert u zich op de nieuwsbrief, dan voorzien we u van nieuws, informatie en tips over onze producten en diensten. U kunt de inschrijving op elk gewenst moment opzeggen (we voorzien alle nieuwsbrieven van een link tot uitschrijving). We voegen uw mailadres alleen aan de abonneelijst toe wanneer u hier uitdrukkelijk toestemming voor geeft. Schrijft u zich uit, dan worden uw gegevens gewist.</p>

<h2>Derde partijen</h2>
<p>Wij verstrekken uw gegevens nooit aan derden, tenzij dit nodig is voor de dienstverlening of hier een wettelijke grond voor is. Bij het vermoeden van fraude moeten wij bijvoorbeeld aangifte doen; uw gegevens worden dan verstrekt aan de politie.</p>
<p>Sommige van onze partners bevinden zich buiten de Europese Unie. Maakt u gebruik van social media buttons op onze website of binnen onze dienstverlening, dan worden uw gegevens door deze dienstverleners opgeslagen. We raden u aan de privacyverklaring van deze aanbieders door te nemen voordat u akkoord geeft.</p>

<h2>Reclame en aanbiedingen</h2>
<p>Wij kunnen u reclame en promotionele berichten sturen via post, mail, social media of telefoon. Wanneer u deze berichten niet wilt ontvangen, kunt u dit zelf regelen door op de afmeldlink te klikken die met elk bericht verzonden wordt. Bellen we u en is dit niet gewenst? Geeft u dit dan aan tijdens het gesprek; wij halen dan uw nummer van onze lijst af, zodat u niet nog eens gebeld wordt.</p>

<h2>Cookies</h2>
<p>Deze website plaatst zelf geen cookies en gebruikt geen statistiekdiensten. Op sommige pagina’s staan video’s van Vimeo en de website gebruikt lettertypen van Google Fonts. Hoe dat werkt, leest u in ons <a href="{r}cookiebeleid/">cookiebeleid</a>.</p>

<h2>Beveiliging</h2>
<p>Uw veiligheid is belangrijk voor ons. Daarom maken we gebruik van een versleutelde verbinding (SSL/TLS), zodat alle gegevens die worden uitgewisseld tussen u en onze website zijn afgeschermd.</p>
<p>Deze website maakt gebruik van Google Fonts voor het tonen van web-lettertypen. Daarbij wordt uw IP-adres aan Google doorgegeven. Lees voor meer informatie de privacyverklaring van Google.</p>

<h2>Wijzigingen in de privacyverklaring</h2>
<p>Wij behouden ons het recht voor om de privacyverklaring te wijzigen wanneer dit noodzakelijk of wenselijk is. Controleer daarom met regelmaat of de privacyverklaring aangepast is. Wanneer wij de privacyverklaring aanpassen, communiceren we dit uiteraard naar onze gebruikers.</p>

<h2>Uw gegevens inzien, wijzigen of laten verwijderen</h2>
<p>Wanneer u wilt weten welke gegevens we van u opgeslagen hebben, kunt u altijd contact met ons opnemen. Daarnaast heeft u de volgende rechten met betrekking tot uw gegevens die in ons bezit zijn:</p>
<ul>
<li>Uitleg vragen over welke gegevens we hebben en wat we hiermee doen</li>
<li>Inzage in welke gegevens we exact van u verzameld hebben</li>
<li>Laten wijzigen van persoonlijke informatie</li>
<li>Het laten verwijderen van verouderde of foutieve gegevens</li>
<li>Bezwaar indienen tegen het gebruik van bepaalde gegevens</li>
</ul>
<p>We vragen u duidelijk aan te geven wie u bent wanneer u hier gebruik van maakt, zodat we de wijzigingen op de correcte manier kunnen doorvoeren.</p>

<h2>Hoelang bewaren we uw gegevens?</h2>
<p>Uw gegevens worden zolang bewaard als nodig is, maar niet langer dan strikt noodzakelijk. De volgende bewaartermijnen worden door ons gehanteerd:</p>
<ul>
<li>Informatie met een fiscale achtergrond wordt 7 jaar bewaard.</li>
<li>Na opzegging van onze dienstverlening worden uw gegevens alleen op verzoek of op bepaling van de directie verwijderd.</li>
<li>Informatie van sollicitanten wordt maximaal 1 maand na afloop van de sollicitatie verwijderd.</li>
</ul>

<h2>Een klacht indienen</h2>
<p>Bent u van mening dat wij uw gegevens op een onjuiste manier gebruikt hebben of is uw privacy geschonden? Dan kunt u een klacht indienen bij de Autoriteit Persoonsgegevens, de toezichthouder in dit domein.</p>

<h2>Contact</h2>
{contact}''', 'Deze verklaring is voor het laatst gewijzigd op 24 november 2026.')

    # ---------- COOKIEBELEID ----------
    tekstpagina(page, 'cookiebeleid', 'Cookiebeleid – SilverCloud',
        'Welke cookies en aanverwante technieken deze website gebruikt.',
        'Cookies', 'Cookiebeleid',
        'Dit cookiebeleid is van toepassing op burgers en wettelijk permanente inwoners van de Europese Economische Ruimte en Zwitserland.',
        f'''
<h2>1. Introductie</h2>
<p>Op deze website wordt zo min mogelijk gebruikgemaakt van cookies en aanverwante technieken. (Hierna noemen we al deze technieken voor het gemak “cookies”.) In dit document informeren wij u over wat er op onze site gebeurt.</p>

<h2>2. Wat zijn cookies?</h2>
<p>Een cookie is een klein eenvoudig bestand dat samen met pagina’s van een site wordt verzonden en door uw browser op de harde schijf van uw computer of ander apparaat wordt opgeslagen. De daarin opgeslagen informatie kan tijdens een volgend bezoek terug worden gestuurd naar de servers van de site of van betrokken derde partijen.</p>

<h2>3. Wat zijn scripts?</h2>
<p>Een script is een stukje programmacode dat wordt gebruikt om een site goed te laten functioneren en interactief te maken. Deze code wordt uitgevoerd op de server, of op uw apparatuur.</p>

<h2>4. Wat is een web beacon?</h2>
<p>Een web beacon (ook pixel tag) is een klein, onzichtbaar stukje tekst of afbeelding op een site dat gebruikt wordt om verkeer op een site in kaart te brengen. Deze website gebruikt geen web beacons.</p>

<h2>5. Cookies op deze website</h2>
<h3>5.1 Cookies van SilverCloud</h3>
<p>Deze website plaatst zelf geen cookies: geen functionele cookies, geen statistiekcookies en geen marketingcookies. Daarom tonen we ook geen cookiemelding.</p>
<h3>5.2 Ingesloten video’s (Vimeo)</h3>
<p>Op sommige pagina’s staan video’s van Vimeo. Die laden we met de instelling ‘Do Not Track’, waardoor Vimeo geen gegevens verzamelt om uw gedrag te volgen. Vimeo kan wel technisch noodzakelijke gegevens verwerken om de video af te spelen. Meer hierover leest u in de privacyverklaring van Vimeo.</p>
<h3>5.3 Lettertypen (Google Fonts)</h3>
<p>Voor de weergave van lettertypen gebruiken we Google Fonts. Daarbij worden geen cookies geplaatst, maar wordt uw IP-adres wel aan Google doorgegeven.</p>

<h2>6. Cookies in- of uitschakelen en verwijderen</h2>
<p>U kunt uw internetbrowser gebruiken om cookies automatisch of handmatig te verwijderen. U kunt ook aangeven dat bepaalde cookies niet geplaatst mogen worden, of uw browser zo instellen dat u iedere keer een bericht ontvangt wanneer er een cookie wordt geplaatst. Raadpleeg voor meer informatie de Help-sectie van uw browser.</p>

<h2>7. Uw rechten met betrekking tot persoonsgegevens</h2>
<p>U heeft de volgende rechten met betrekking tot uw persoonsgegevens:</p>
<ul>
<li>U heeft het recht om te weten waarom uw persoonsgegevens nodig zijn, wat ermee gebeurt en hoe lang ze worden bewaard.</li>
<li>Recht op inzage: u kunt een verzoek indienen om inzage in de gegevens die we van u verwerken.</li>
<li>Recht op rectificatie en aanvulling: u heeft het recht om uw persoonlijke gegevens aan te vullen, te corrigeren, te verwijderen of te blokkeren wanneer u maar wilt.</li>
<li>Als u ons toestemming geeft om uw gegevens te verwerken, heeft u het recht om die toestemming in te trekken en uw persoonlijke gegevens te laten verwijderen.</li>
<li>Recht om uw gegevens over te dragen: u heeft het recht om al uw persoonlijke gegevens op te vragen en deze in hun geheel over te dragen aan een andere verwerkingsverantwoordelijke.</li>
<li>Recht op bezwaar: u kunt bezwaar maken tegen de verwerking van uw gegevens. Wij komen hieraan tegemoet, tenzij er gegronde redenen voor verwerking zijn.</li>
</ul>
<p>Om deze rechten uit te oefenen, neemt u contact met ons op. Heeft u een klacht over hoe we met uw gegevens omgaan, dan horen we dat graag. U heeft ook het recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens. Zie ook onze <a href="{r}privacyverklaring/">privacyverklaring</a>.</p>

<h2>8. Contactinformatie</h2>
<p>Voor vragen of opmerkingen over dit cookiebeleid kunt u contact met ons opnemen:</p>
{contact}''', 'Dit cookiebeleid is voor het laatst bijgewerkt op 24 november 2026.')

    # ---------- TOEGANKELIJKHEIDSVERKLARING ----------
    tekstpagina(page, 'toegankelijkheidsverklaring', 'Toegankelijkheidsverklaring – SilverCloud',
        'Hoe SilverCloud werkt aan een toegankelijke website.',
        'Toegankelijkheid', 'Toegankelijkheidsverklaring',
        'Wij streven ernaar om deze website voor iedereen toegankelijk te maken, ook voor mensen met een beperking.',
        f'''
<p>Daarbij volgen we de richtlijnen van de Europese Toegankelijkheidswet (European Accessibility Act) en de Web Content Accessibility Guidelines (WCAG) 2.1 op niveau AA.</p>

<h2>Status van toegankelijkheid</h2>
<p>Deze website is deels toegankelijk. We werken voortdurend aan het verbeteren van de toegankelijkheid en besteden daarbij specifieke aandacht aan:</p>
<ul>
<li>Alternatieve teksten bij afbeeldingen</li>
<li>Voldoende kleurcontrast tussen tekst en achtergrond</li>
<li>Formulieren die goed werken met hulptechnologie</li>
<li>Volledige bediening van de website met alleen het toetsenbord</li>
</ul>

<h2>Heeft u feedback?</h2>
<p>Ervaart u een probleem met de toegankelijkheid van deze website of heeft u suggesties om deze gebruiksvriendelijker te maken? We horen het graag. Wij streven ernaar om binnen 5 werkdagen te reageren.</p>
{contact}''', 'Laatst bijgewerkt: 24 november 2026.')

    # ---------- KWALITEIT & INFORMATIEBEVEILIGING ----------
    page('kwaliteit-informatiebeveiliging', 'Kwaliteit en informatiebeveiliging – ISO 9001, ISO 27001 en NEN 7510 – SilverCloud',
        'SilverCloud is gecertificeerd voor ISO 9001, ISO 27001 en NEN 7510. Lees ons kwaliteits- en informatiebeveiligingsbeleid en bekijk de certificaten.', f'''
<section class="hero"><div class="container narrow">
  <span class="badge">Kwaliteit &amp; informatiebeveiliging</span>
  <h1 class="display" style="margin:16px 0">ISO 9001, ISO 27001 en NEN 7510</h1>
  <p class="lead">Kwaliteit in dienstverlening en een kritisch oog voor informatiebeveiliging en privacy mag u van elke businesspartner verwachten. Bij SilverCloud zit het in ons DNA.</p>
</div></section>
<section class="section" style="padding-top:0"><div class="container narrow prose">
<p>We kijken continu kritisch naar onszelf en naar elkaar, om te controleren dat we hier niet aan tornen. Onze klanten herkennen ons daarin. Toch hebben we bewust de extra stap gezet naar formele certificering voor ISO 9001, ISO 27001 en NEN 7510.</p>
<p>Een formele certificering geeft vertrouwen, omdat die objectief is vastgesteld: vertrouwen in producten, diensten, (management)processen en medewerkers. Met een certificaat toont een organisatie aan dat ze efficiënt en veilig werkt, dat de werkzaamheden en werkprocessen beheerst worden en dat ze duurzaamheid nastreeft.</p>
<p>In 2020 behaalden we onze eerste certificering, met ondersteuning van de consultants van Vos Advies. We hebben ons kwaliteitssysteem aangescherpt, beter verwoord en alle medewerkers opnieuw getraind. In december 2020 slaagden we voor de TÜV-audit op alle drie de normen. Sindsdien zijn we opnieuw gecertificeerd, inmiddels volgens de vernieuwde ISO 27001:2022. De huidige certificaten zijn afgegeven door TÜV NORD Nederland en geldig tot januari 2027.</p>
<p>De certificaten gelden voor zowel SilverCloud Computing als SilverCloud Zorg.</p>

<h2>Wat de normen betekenen</h2>
<ul>
<li><strong>ISO 9001</strong>: kwaliteitsmanagement. Onze processen zijn beheerst en we verbeteren continu.</li>
<li><strong>ISO 27001</strong>: informatiebeveiliging. We gaan aantoonbaar zorgvuldig om met uw gegevens en systemen.</li>
<li><strong>NEN 7510</strong>: informatiebeveiliging in de zorg. De norm voor organisaties die met gezondheidsgegevens werken.</li>
</ul>

<h2>Ons beleid en de certificaten</h2>
<p>De hoofdlijnen van ons kwaliteits- en informatiebeveiligingssysteem delen we graag met u.</p>
<ul>
<li><a href="{pdf(out, r, 'beleid')}">Kwaliteits- en informatiebeveiligingsbeleid</a> (pdf)</li>
<li><a href="{pdf(out, r, 'iso9001')}">Certificaat ISO 9001</a> (pdf)</li>
<li><a href="{pdf(out, r, 'iso27001')}">Certificaat ISO 27001</a> (pdf)</li>
<li><a href="{pdf(out, r, 'nen7510')}">Certificaat NEN 7510</a> (pdf)</li>
</ul>
<p>Meer lezen? In <a href="{r}blog/meer-dan-alleen-een-stempel-onze-hercertificering-met-iso9001-iso27001-en-nen7510/">Meer dan alleen een stempel</a> vertellen we over onze hercertificering.</p>
<p>Vragen over ons kwaliteits- of informatiebeveiligingsbeleid? Neem <a href="{r}contact/">contact</a> met ons op.</p>
</div></section>
''', nav='')
