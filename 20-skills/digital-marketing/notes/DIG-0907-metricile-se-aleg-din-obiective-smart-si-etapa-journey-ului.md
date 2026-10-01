---
id: DIG-0907
title: Metricile se aleg pornind de la obiective SMART și de la etapa journey-ului, nu de la ce oferă platforma
type: zettel
kind: method
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [metrici, obiective-smart, trafic, audienta, campanie, ga4]
sources:
  - SRC-029 | cap. 5, p. 130, 137-142
status: seed
---

# Metricile se aleg pornind de la obiective SMART și de la etapa journey-ului, nu de la ce oferă platforma

> **Ideea în o frază:** singura metodă de a pune ordine în mulțimea de metrici este să mapezi explicit fiecare obiectiv SMART pe metricile care îl măsoară, pornind de la o linie de bază și coborând spre detaliu.

## Explicație

Manualul împarte metricile web în trei familii: **trafic** (afișări, page views, sesiuni, click-through), **audiență** (vizitatori unici sau repetați, anonimi sau identificați, pagină de intrare și ieșire, bounce rate, abandonul coșului) și **campanie** (pe canal, pe ofertă, pe cuvânt-cheie). Toate au sens doar pe o perioadă definită. GA4 a înlocuit bounce rate cu **rata de engagement**: cine citește un articol 45 de secunde și pleacă nu e un eșec.

Al doilea filtru este journey-ul (fig. 5.6):

| Etapă | Metrici-exemplu |
|---|---|
| Notorietate | afișări, reach și frecvență, prima vizită, căutare de brand |
| Considerare | abonați la newsletter, vizite repetate, contacte inbound, comentarii, percepția brandului |
| Cumpărare (conversie) | probe gratuite, rată de conversie, ROI pe canal |
| Loialitate | satisfacție, cumpărări repetate, CLV |

Al treilea filtru, decisiv, sunt **obiectivele SMART** (specifice, măsurabile, realizabile, realiste, încadrate în timp). Pentru „crește cu 5% e-mailurile captate în T1" metricile urcă de la vizitatori unici și sursa de trimitere până la înregistrări începute și neterminate și **ultimul câmp completat** — care arată unde se blochează oamenii.

## Aplicare

- Scrie obiectivul în format SMART înainte de a deschide dashboard-ul.
- Pentru fiecare obiectiv, construiește un lanț: linie de bază → comportament intermediar → rezultat → diagnostic (unde se rupe).
- Obiectivele de branding cer cercetare atitudinală (percepție, intenție), nu doar date comportamentale.

## Exemplu

„Reactivează 10.000 de clienți inactivi în T4" cere: e-mailuri trimise, mesaj de reactivare A/B, click-through pe variantă, bounce de pe landing page, oferte acceptate (10% reducere vs. 5 dolari vs. cadou). Fiecare metric răspunde unei întrebări de decizie.

## Întrebări

- De ce e periculos să compari campanii pe metrici de trafic dacă au obiective diferite?
- Care metrici din tabel spun ceva despre brand și care doar despre activitate?

## Legături

- **fundament** [[DIG-0906-un-metric-e-un-numar-un-kpi-arata-progresul-fata-de-obiectiv|DIG-0906]] — distincția metric vs. KPI precede alegerea.
- **fundament** [[DIG-0905-customer-journey-ul-digital-nu-e-palnie-ci-bucla-de-loialitate|DIG-0905]] — etapele journey-ului structurează lista de metrici.
- **aplicare** [[DIG-0908-palnia-de-conversie-arata-unde-pleaca-vizitatorii|DIG-0908]] — pâlnia de conversie e diagnosticul detaliat al etapei de cumpărare.
- **aplicare** [[DIG-0933-testul-ab-o-singura-variabila-si-semnificatie-statistica|DIG-0933]] — obiectivele de reactivare și conversie se ating prin teste A/B.

## Surse

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 5, p. 130, 137-142

<!-- backlinks:start -->
## Backlinks

- [[DIG-0905-customer-journey-ul-digital-nu-e-palnie-ci-bucla-de-loialitate|DIG-0905]] _aplicare_ — Customer journey-ul digital nu e o pâlnie liniară, ci un traseu cu bucle care se închide într-o buclă de loialitate
- [[DIG-0906-un-metric-e-un-numar-un-kpi-arata-progresul-fata-de-obiectiv|DIG-0906]] _aplicare_ — Un metric e doar un număr; un KPI arată cât de aproape ești de obiectiv
- [[DIG-0908-palnia-de-conversie-arata-unde-pleaca-vizitatorii|DIG-0908]] _extinde_ — Pâlnia de conversie arată unde pleacă vizitatorii; treaba marketerului e să afle de ce
- [[DIG-0909-metricile-video-masoara-timpul-brandul-trebuie-sa-apara-devreme|DIG-0909]] _aplicare_ — Metricile video măsoară timpul — brandul trebuie să apară înainte ca privitorul să plece
- [[DIG-0911-site-ul-se-construieste-in-sapte-pasi-marketingul-conduce|DIG-0911]] _vezi_ — Site-ul se construiește în șapte pași, iar marketingul conduce primii — altfel iese tehnologie fără obiectiv
- [[DIG-0914-aplicatia-se-justifica-doar-daca-face-ce-site-ul-nu-poate|DIG-0914]] _vezi_ — O aplicație mobilă se justifică doar dacă face ceva ce un site responsive nu poate face
- [[DIG-0933-testul-ab-o-singura-variabila-si-semnificatie-statistica|DIG-0933]] _aplicare_ — Testul A/B schimbă o singură variabilă, pornește de la o ipoteză și așteaptă semnificația statistică
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
<!-- backlinks:end -->
