---
id: DIG-0933
title: Testul A/B schimbă o singură variabilă, pornește de la o ipoteză și așteaptă semnificația statistică
type: zettel
kind: method
skill: digital-marketing
also: [copywriting, art-direction]
level: 2
tags: [ab-testing, experiment, ipoteza, multivariat, optimizare, conversie]
sources:
  - SRC-030 | cap. 1
  - SRC-029 | cap. 5, p. 140
  - SRC-029 | cap. 8, p. 238
status: seed
---

# Testul A/B schimbă o singură variabilă, pornește de la o ipoteză și așteaptă semnificația statistică

> **Ideea în o frază:** testul A/B (*split test*) este un experiment controlat: arăți aleatoriu varianta A unui grup și varianta B altuia, schimbând un singur element, și declari un câștigător doar după ce ai atins eșantionul și pragul de încredere stabilite dinainte.

## Explicație

Zahay et al. (SRC-029) definesc testul A/B ca experiment controlat pentru optimizarea conținutului web: două sau mai multe variante (e-mail, promoție, landing page), grupuri alocate aleatoriu, testul statistic potrivit. Capitolul de paid social repetă refrenul „TEST, TEST, TEST": testarea e „sângele" marketingului digital. Connors (SRC-030) dă pașii:

1. **Alege ce testezi** — elementele cu cel mai mare impact asupra rezultatului dorit (titlul, CTA-ul, lungimea formularului; la e-mail, subiectul, textul, ora trimiterii).
2. **Formulează o ipoteză** specifică, măsurabilă, bazată pe date („butonul roșu crește CTR-ul pentru că atrage mai mult atenția"), nu pe capriciu.
3. **Creează varianta de control (A) și varianta (B)**, care diferă printr-un **singur** element — altfel nu poți atribui diferența.
4. **Stabilește eșantionul și durata** cu un calculator statistic; țintește cel puțin 95% încredere.
5. **Nu trage cu ochiul**: oprirea testului la jumătate produce fals-pozitive.
6. **Analizează** pe metrica-cheie; un rezultat neconcludent e tot o informație (elementul contează mai puțin decât credeai).
7. **Documentează și reia**: arhiva testelor devine memoria echipei.

Variante avansate: **testul multivariat** (combinații de titluri, imagini și butoane deodată; cere mult trafic), **testul secvențial** (analiză în etape stabilite, ca să oprești devreme fără fals-pozitive) și testele pe segmente (ce merge la tineri poate să nu meargă la seniori). Connors adaugă etica: transparență și conformitate GDPR.

## Aplicare

- Folosește testele ca să rezolvi discuțiile creative „pe gust": două titluri bune, un test, o decizie bazată pe date.
- Scrie ipoteza în brief-ul de testare, cu motivul psihologic; altfel nu înveți nimic chiar dacă B câștigă.
- Nu testa detalii minore pe trafic mic; testează ofertele și mesajele, care au impact mare.

## Exemplu

Campania de reactivare din SRC-029 (fig. 5.7) testează mesajul de reactivare A/B și stimulentul (10% reducere vs. 5 dolari la prima comandă vs. cadou), măsurând click-through-ul, bounce-ul de pe landing page și ofertele acceptate pentru fiecare variantă.

## Întrebări

- Poate un test A/B să optimizeze o campanie spre un „maxim local" banal și să omoare ideile curajoase?
- De ce nu e un test A/B pe clicuri o dovadă despre efectul pe termen lung asupra brandului?

## Legături

- **aplicare** [[DIG-0907-metricile-se-aleg-din-obiective-smart-si-etapa-journey-ului|DIG-0907]] — obiectivele SMART de conversie și reactivare se ating prin teste.
- **aplicare** [[DIG-0908-palnia-de-conversie-arata-unde-pleaca-vizitatorii|DIG-0908]] — fiecare ipoteză de abandon din pâlnie devine un test.
- **aplicare** [[DIG-0920-reclama-e-doar-atat-de-buna-cat-landing-page-ul-ei|DIG-0920]] — optimizarea landing page-ului e o succesiune de teste.
- **vezi** [[DIG-0928-in-email-click-to-open-rate-spune-mai-mult-decat-open-rate|DIG-0928]] — subiectul și oferta e-mailului se compară prin metricile de e-mail.

## Surse

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, cap. 1
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 5, p. 140; cap. 8, p. 238

<!-- backlinks:start -->
## Backlinks

- [[DIG-0907-metricile-se-aleg-din-obiective-smart-si-etapa-journey-ului|DIG-0907]] _aplicare_ — Metricile se aleg pornind de la obiective SMART și de la etapa journey-ului, nu de la ce oferă platforma
- [[DIG-0908-palnia-de-conversie-arata-unde-pleaca-vizitatorii|DIG-0908]] _aplicare_ — Pâlnia de conversie arată unde pleacă vizitatorii; treaba marketerului e să afle de ce
- [[DIG-0919-campania-de-paid-search-si-paid-social-are-cinci-etape|DIG-0919]] _aplicare_ — Campania de paid search și paid social are cinci etape — de la cercetarea cuvintelor-cheie la testare
- [[DIG-0928-in-email-click-to-open-rate-spune-mai-mult-decat-open-rate|DIG-0928]] _aplicare_ — În e-mail, click-to-open rate spune mai mult decât open rate
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]] — Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
<!-- backlinks:end -->
