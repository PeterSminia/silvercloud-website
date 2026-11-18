# SilverCloud website (concept v0.4)

Statische website (HTML en CSS, geen build-stap nodig) op basis van het huisstijlvoorstel *SilverCloud huisstijl* en het document *SilverCloud_Zorg_Websiteconcept_compleet.docx*.

## Pagina's

| Pagina | Bestand |
|---|---|
| Home (moedermerk, keuze mkb of zorg) | `public/index.html` |
| SilverCloud Computing (mkb) | `public/computing/index.html` |
| SilverCloud Zorg, overzicht | `public/zorg/index.html` |
| Netwerkregie | `public/zorg/netwerkregie/index.html` |
| CareDesk | `public/zorg/caredesk/index.html` |
| Lokalisatie & Leefcirkels (Evresys) | `public/zorg/lokalisatie-leefcirkels/index.html` |
| Hulpmiddelenbeheer (AssetGuard) | `public/zorg/assetguard/index.html` |
| Kennis & cases (Argos, ZGEM, downloads) | `public/kennis/index.html` |
| Over ons & werkwijze | `public/over-ons/index.html` |
| Contact | `public/contact/index.html` |

Stijl staat in `public/assets/css/site.css`. Logo's en afbeeldingen staan in `public/assets/img/`, pdf-downloads in `public/assets/downloads/`.

## Lokaal bekijken

Open `public/index.html` in de browser. Alle links zijn relatief, dus dat werkt zonder server.

## Publiceren op GitLab

1. Maak in GitLab een project aan, bijvoorbeeld `silvercloud/website`. Vink **‘Initialize repository with a README’ uit**, anders botst die README met deze.
2. Dubbelklik `deploy.bat`. De eerste keer vraagt het script om de project-URL.
3. GitLab Pages publiceert de map `public/` automatisch (`.gitlab-ci.yml`). De URL vindt u in GitLab onder **Deploy → Pages**.

Volgende wijzigingen: opnieuw `deploy.bat`, eventueel met een omschrijving: `deploy.bat "Teksten CareDesk aangepast"`.

## Bronscript

`tools/build.py` genereert alle pagina's (gedeelde header en footer). Past u HTML direct aan, draai het script dan niet opnieuw: het overschrijft de pagina's.

## Nog in te vullen (gemarkeerd met [ ... ] op de site)

- KvK-nummer (footer). Adres, telefoon en e-mail staan er sinds v0.2 in.
- Teamintroductie en teamfoto (over ons).
- Computing-subpagina's: het bronmateriaal in `1 MKB propositie` kon niet worden gelezen (OneDrive gaf een fout). De Computing-pagina is daarom nog gelijk aan v0.1.
- Doelgroep/marktsegment voor Computing (FAQ op de Computing-pagina).
- Koppeling van het contactformulier (bijv. naar e-mail, HubSpot of Autotask).
- Privacyverklaring en algemene voorwaarden.
- **AVG:** de lettertypes komen nu van Google Fonts. Host ze vóór livegang zelf in `public/assets/fonts/`.
- Toestemming van Argos en ZGEM voor het gebruik van hun namen en citaten op de site (de citaten komen uit de eigen klantcase en blog).
- Het label "Concept v0.2" rechtsonder: verwijderen in `site.css`/HTML bij livegang.

## Wijzigingen in v0.4

- Zorg in **drie proposities**: Netwerkregie, CareDesk en Zorgtechnologie (nieuwe overzichtspagina). Onder Zorgtechnologie: Lokalisatie & Leefcirkels, **Medewerkersveiligheid** (nieuw) en Hulpmiddelenbeheer.
- Blok **"Wij kennen de zorg"** (cultuur, uitdagingen, oplossingen, applicaties, communicatie, sectoren) op Zorg, Over ons en de propositiepagina's. Over ons legt de nadruk op zorgkennis en zorgervaring.
- **CareDesk** herschreven op basis van voorzet, brochure en blueprint; brochure als download.
- **Evresys en Blyott** duidelijk benoemd, met links naar evresys.com en blyott.com.
- **Evresys als aanvulling op een bestaand zorgoproepsysteem**: uitleg wat een zorgoproepsysteem is, wat Evresys toevoegt en wanneer dit logisch is.

## Wijzigingen in v0.3

- **Netwerkregie leidend** voor de zorg: uitgelicht op home en Zorg-overzicht, uitgebreide Netwerkregie-pagina (paradigmaverschuiving, vijf uitgangspunten, architectuur, security by design, bouwblokken per locatietype, transparantie, overstap in twee fases, FAQ). Bron: de Netwerkregie-documenten en -presentaties.
- **Uniciteit en zorgspecifieke eisen** als eigen blokken (open calculatie, gedeelde monitoring, beheer per locatie, segmentatie, 4G/5G-back-up, UPS, NEN 7510).
- **Lokalisatie & Leefcirkels**: SilverCloud als volledige integrator van **Evresys en Blyott**; twee routes met drie Evresys-whitepapers als download.
- **Computing**: herschreven als moderne, ontzorgende MSP (werkplek, veilig netwerk, toegang tot bedrijfsapplicaties, beveiliging & back-up, servicedesk).
- **Blog**: alle 84 artikelen van silvercloudzorgiot.nl, met filter en zoekfunctie (`/blog/`). Oude adressen (`/<blogslug>/`, `/nieuws-blog/`, `/assetguard/` …) sturen door.
- **Partners**-pagina, uitgebreide **cases**, video's, team op Over ons.
- **Certificering** (NEN 7510, ISO 27001, ISO 9001) prominent op home, Zorg, Netwerkregie, Computing en in de footer.
- **Afspraak plannen** (`/afspraak/`): naam, e-mail, datum en tijd; verzonden naar **sales@silvercloud.nl** via FormSubmit. Ook het contactformulier gaat nu naar sales@.

### Eenmalig na livegang
1. **Formulieren activeren:** de eerste inzending stuurt een activatiemail van FormSubmit naar sales@silvercloud.nl. Klik op de link; daarna komen alle aanvragen direct binnen. (FormSubmit verwerkt de formulierdata; neem dit op in de privacyverklaring of vervang later door eigen mail/CRM-koppeling.)
2. **Afbeeldingen lokaal maken:** blogfoto's en certificaat-pdf's verwijzen nog naar silvercloudzorgiot.nl. Draai `python3 tools/download-assets.py` en commit het resultaat voordat de oude site uit gaat.

Bouwen: `python3 tools/build.py` (gebruikt `tools/extra.py` en `tools/posts.json`).

## Wijzigingen in v0.2

- Nieuwe pagina **Hulpmiddelenbeheer (AssetGuard)** onder Zorg, met de modules Snelvinden, Integratie (TOPdesk), Insight en Advies, een echte schermafbeelding van Insight, kerncijfers en vragen en antwoorden.
- Nieuwe pagina **Kennis & cases** met de cases van Argos Zorggroep en Zorggroep Elde Maasduinen en drie pdf-downloads (whitepaper Netwerkregie, 10 voordelen van realtime lokalisatie, klantcase ZGEM).
- Zorg-overzicht toont nu vier oplossingen. Hoofdmenu, submenu Zorg en footer zijn bijgewerkt.
- Contactgegevens (Ohmstraat 18-A, Nijkerk, 088 256 00 50, info@silvercloud.nl) staan in de footer en op de contactpagina.
- Op de homepage staat nu een echt klantcitaat (ZGEM) in plaats van een placeholder.
