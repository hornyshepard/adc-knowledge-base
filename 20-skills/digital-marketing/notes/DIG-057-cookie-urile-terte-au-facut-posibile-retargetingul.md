---
id: DIG-057
title: Cookie-urile terțe au făcut posibile retargetingul, lookalike-urile și profilurile cross-site, iar legea și browserele le scot din joc — puterea trece la datele first-party
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy, ai-marketing]
level: 1
tags: [cookies, cookie-uri-terte, first-party-data, third-party-data, tracking, gdpr, ccpa, e-privacy, att, safari, chrome, post-cookie]
sources:
  - SRC-029 | cap. 5, p. 135-137; cap. 8, p. 218-219; cap. 10, p. 278, 282-283
  - SRC-032 | cap. 1.2.1-1.2.2, p. 15-18
  - SRC-031 | cap. 11, p. 391; cap. 12, p. 408
status: growing
---

# Cookie-urile terțe au făcut posibile retargetingul, lookalike-urile și profilurile cross-site, iar legea și browserele le scot din joc — puterea trece la datele first-party

> **Ideea în o frază:** o tehnologie invizibilă pentru public a stat la baza publicității digitale personalizate, iar dispariția ei obligă industria să-și regândească targetarea și măsurarea pe datele proprii ale brandului.

## Explicație

Un **tag** (pixel) e un fragment de cod care înregistrează comportamentul pe pagină. Un **cookie** e fișierul text din browser care recunoaște utilizatorul. Cookie-urile au fost inventate la Netscape ca să nu se golească coșul de cumpărături.

| | First-party | Third-party |
|---|---|---|
| Cine îl pune | site-ul vizitat | un alt domeniu (ad server, rețea) |
| Unde funcționează | doar pe acel site | pe orice site care încarcă acel cod |
| La ce servește | logare, coș, analytics | profiluri cross-site, retargeting |

**La ce au servit** cookie-urile terțe (SRC-032): retargeting, targetare după situația financiară, modelare *lookalike* și optimizare în timpul campaniei, nu doar după.

**De ce dispar:** Directiva e-Privacy (2002/2009) și GDPR (2018) cer consimțământ; CCPA dă californienilor dreptul de a ști, de a șterge și de a refuza vânzarea datelor. Safari și Firefox blochează sau limitează cookie-urile terțe din 2019–2020. Apple ATT (iOS 14.5) cere acordul pentru urmărirea între aplicații: sub jumătate acceptă, de la circa 20% în Germania la aproape 50% în Emiratele Arabe Unite.

**Unde se contrazic sursele.** Zahay et al. și Sachdev scriu ca și cum Google ar urma să elimine cookie-urile din Chrome. Schwarz-Musch et al. consemnează că, în iulie 2024, Google a renunțat la eliminare și a lăsat alegerea utilizatorului. Lecția: termenele din manuale se învechesc repede, direcția nu.

Alternativele discutate de Zahay et al. sunt un ID universal, publicitatea contextuală, e-mailul criptat ireversibil (*hashed*) și, mai ales, datele first-party.

## Aplicare

- Fă inventarul tacticilor clientului care depind de cookie-uri terțe: retargeting, lookalike, plafon de frecvență, atribuire. Notează pentru fiecare alternativa.
- Orice strategie nouă răspunde: ce date proprii colectăm și în schimbul a ce valoare?

## Exemplu

Magnolia Bakery (SRC-029, cap. 11) și-a construit liste proprii printr-un pop-up cu 10% reducere și o tombolă de ziua de naștere. Abonații petreceau cu 35% mai mult timp pe site decât ceilalți.

## Întrebări

- Este targetarea comportamentală incompatibilă cu respectul pentru client sau doar trebuie făcută transparent?
- Ce pierd brandurile mici, fără baze de date mari, în lumea post-cookie?

## Legături

- **fundament** [[DIG-001-marketingul-digital-inseamna-interactiune-engagement-si|DIG-001]] — definiția Zahay pune deja datele proprii în centrul marketingului digital.
- **vezi** [[DIG-058-fara-cookie-uri-terte-raman-cinci-familii-de-targetare-iar|DIG-058]] — ce familii de targetare rămân fără cookie-uri terțe.
- **vezi** [[DIG-062-strategia-de-date-first-party-porneste-de-la-intrebarea-ce|DIG-062]] — cum se construiește strategia de date first-party care le înlocuiește.
- **vezi** [[DIG-063-consimtamantul-valid-se-cere-activ-si-se-poate-retrage-la|DIG-063]] — consimțământul valid devine condiția oricărei urmăriri.
- **vezi** [[DIG-052-retargetingul-functioneaza-doar-segmentat-pe-etapa-din|DIG-052]] — retargetingul, tactica cea mai afectată.
- **vezi** [[AIM-031-paradoxul-personalizarii-cu-cat-reclama-stie-mai-mult|AIM-031]] — paradoxul personalizării explică presiunea publică din spatele reglementării.

## Surse

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 5, p. 135-137; cap. 8, p. 218-219; cap. 10, p. 278, 282-283
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 1.2.1-1.2.2 (p. 15-18)
- [[SRC-031-digital-marketing-manual|SRC-031]] Raj Sachdev, *Digital Marketing*, cap. 11 (p. 391) și cap. 12 (p. 408)

<!-- backlinks:start -->
## Backlinks

- [[DIG-001-marketingul-digital-inseamna-interactiune-engagement-si|DIG-001]] _vezi_ — Marketingul digital înseamnă interacțiune, engagement și măsurare, nu doar canale noi
- [[DIG-033-permisiunea-in-e-mail-marketing-are-patru-niveluri-de-la|DIG-033]] _vezi_ — Permisiunea în e-mail marketing are patru niveluri, de la opt-out la double opt-in
- [[DIG-052-retargetingul-functioneaza-doar-segmentat-pe-etapa-din|DIG-052]] _fundament_ — Retargetingul funcționează doar segmentat pe etapa din journey, dozat și consimțit — tactica cea mai eficientă a erei cookie e și cea mai expusă după ea
- [[DIG-056-targetarea-contextuala-urmareste-pagina-cea-comportamentala|DIG-056]] _vezi_ — Targetarea contextuală urmărește pagina, cea comportamentală urmărește omul
- [[DIG-058-fara-cookie-uri-terte-raman-cinci-familii-de-targetare-iar|DIG-058]] _fundament_ — Fără cookie-uri terțe rămân cinci familii de targetare, iar profilul pe cookie descria oricum un dispozitiv, nu un om
- [[DIG-063-consimtamantul-valid-se-cere-activ-si-se-poate-retrage-la|DIG-063]] _vezi_ — Consimțământul valid se cere activ și se poate retrage la fel de ușor — butoane egale, căsuțe nebifate, scopuri explicate, dovadă păstrată
- [[DIG-064-identitatea-fara-cookie-uri-are-trei-trepte-de-reach|DIG-064]] _vezi_ — Identitatea fără cookie-uri are trei trepte de reach — canalele proprii sau o singură „grădină închisă", camerele curate de date (data clean rooms) și ID-urile universale
- [[MAP-003-etica-reglementare-si-responsabilitate|MAP-003]] — Etică, reglementare și responsabilitate în publicitate
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-031-digital-marketing-manual|SRC-031]] — Digital Marketing
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
