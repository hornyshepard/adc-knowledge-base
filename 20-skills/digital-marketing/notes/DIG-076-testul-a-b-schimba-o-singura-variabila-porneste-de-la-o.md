---
id: DIG-076
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
status: growing
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

- **aplicare** [[DIG-073-metricile-se-aleg-pornind-de-la-obiectivul-smart-nu-de-la|DIG-073]] — obiectivele SMART de conversie și reactivare se ating prin teste.
- **aplicare** [[DIG-075-palnia-de-conversie-arata-unde-pleaca-vizitatorii-treaba|DIG-075]] — fiecare ipoteză de abandon din pâlnie devine un test.
- **aplicare** [[DIG-045-reclama-e-doar-atat-de-buna-cat-pagina-pe-care-aterizeaza|DIG-045]] — optimizarea landing page-ului e o succesiune de teste.
- **fundament** [[INS-080-semnificatia-statistica-nu-inseamna-importanta-cu-date|INS-080]] — cu date multe, aproape orice diferență devine „semnificativă”, dar nu neapărat importantă.
- **contrazice** [[ADV-080-elementele-unei-reclame-se-pot-testa-ca-un-experiment|ADV-080]] — conjoint-ul de mesaj testează mai multe elemente deodată și bate testul A/B.
- **vezi** [[DIG-035-in-e-mail-click-to-open-rate-spune-mai-mult-decat-open-rate|DIG-035]] — subiectul și oferta e-mailului se compară prin metricile de e-mail.

## Surse

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, cap. 1
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 5, p. 140; cap. 8, p. 238

<!-- backlinks:start -->
## Backlinks

- [[ADV-080-elementele-unei-reclame-se-pot-testa-ca-un-experiment|ADV-080]] _alternativa_ — Elementele unei reclame se pot testa ca un experiment — conjoint-ul de mesaj bate testul A/B
- [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] _vezi_ — Validarea pe un eșantion de control separă tiparele reale de supra-ajustare
- [[AIM-024-ipoteza-o-formuleaza-omul-ai-ul-o-ruleaza-omul-o|AIM-024]] _vezi_ — Ipoteza o formulează omul, AI-ul o rulează, omul o interpretează — împărțirea muncii în testare și lead-uri
- [[CPY-017-perturba-apoi-reincadreaza-o-ciudatenie-mica-in-formularea|CPY-017]] _vezi_ — „Perturbă, apoi reîncadrează" — o ciudățenie mică în formularea prețului, urmată de o concluzie persuasivă, crește vânzarea
- [[CPY-025-scoala-mail-order-cuponul-a-transformat-copywritingul-intr|CPY-025]] _vezi_ — Școala mail-order — cuponul a transformat copywritingul într-un experiment măsurabil
- [[CPY-027-anuntul-de-cautare-se-scrie-ca-un-set-de-piese|CPY-027]] _vezi_ — Anunțul de căutare se scrie ca un set de piese interschimbabile, iar fiecare trebuie să funcționeze singură
- [[DIG-035-in-e-mail-click-to-open-rate-spune-mai-mult-decat-open-rate|DIG-035]] _aplicare_ — În e-mail, click-to-open rate spune mai mult decât open rate
- [[DIG-044-campania-de-paid-search-si-paid-social-are-cinci-etape-de|DIG-044]] _aplicare_ — Campania de paid search și paid social are cinci etape — de la cercetarea cuvintelor-cheie la testare
- [[DIG-073-metricile-se-aleg-pornind-de-la-obiectivul-smart-nu-de-la|DIG-073]] _aplicare_ — Metricile se aleg pornind de la obiectivul SMART, nu de la ce oferă platforma — într-un lanț care merge de la linia de bază până la diagnostic
- [[DIG-075-palnia-de-conversie-arata-unde-pleaca-vizitatorii-treaba|DIG-075]] _aplicare_ — Pâlnia de conversie arată unde pleacă vizitatorii; treaba marketerului e să afle de ce
- [[INS-080-semnificatia-statistica-nu-inseamna-importanta-cu-date|INS-080]] _vezi_ — Semnificația statistică nu înseamnă importanță — cu date multe, aproape orice diferență devine „semnificativă"
- [[INS-081-efectul-unei-reclame-se-dovedeste-prin-experiment-nu-prin|INS-081]] _aplicare_ — Efectul unei reclame se dovedește prin experiment, nu prin sondajul „înainte și după"
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]] — Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
<!-- backlinks:end -->
