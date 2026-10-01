---
id: DIG-035
title: În e-mail, click-to-open rate spune mai mult decât open rate
type: zettel
kind: concept
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [email, open-rate, ctr, ctor, bounce-rate, dezabonare, metrici]
sources:
  - SRC-029 | cap. 11, p. 299, 312-315, 317
status: growing
---

# În e-mail, click-to-open rate spune mai mult decât open rate

> **Ideea în o frază:** rata de deschidere e zgomotoasă și doar orientativă; rata de clic față de deschideri (*click-to-open rate, CTOR*), bazată pe clicuri unice, arată mai bine câți oameni au răspuns efectiv la mesaj.

## Explicație

Furnizorii de e-mail (MailChimp, HubSpot, Constant Contact) oferă dashboard-uri cu șase metrici de bază:

| Metric | Formula | Ce spune |
|---|---|---|
| Open rate | deschideri ÷ e-mailuri livrate | orientativ; numără și deschiderile accidentale sau repetate |
| CTR | clicuri ÷ e-mailuri trimise | engagementul total; umflat de clicuri multiple, firewall-uri care testează linkuri, redirecționări |
| CTOR | clicuri unice ÷ deschideri | câți dintre cei care au deschis au acționat — metricul preferat de mulți manageri |
| Unsubscribe rate | dezabonări ÷ trimise | semnal de relevanță sau de frecvență prea mare |
| Hard bounce | adresă invalidă | calitatea listei |
| Soft bounce | nelivrat temporar (problemă de sistem) | probleme tehnice |

Exemplul de calcul din carte: 8.000 de abonați, 2.570 deschid, 825 dau clic → open rate 32,1%, CTR 10,3%, CTOR circa 32%. O rată de dezabonare de 10,1% (808 oameni) ar trebui să alarmeze. Autorii mai notează că majoritatea deschiderilor au loc în primele 24 de ore (față de 48 de ore cu câțiva ani înainte), deci reacția rapidă e esențială. Mediile pe industrie sunt modeste: în jur de 21,5% open rate, 2,3% CTR și 10,5% CTOR (Campaign Monitor, 2022).

**Atenție la carte:** CTR e definit într-un loc ca „clicuri ÷ deschideri" (p. 299), iar în altul ca „clicuri ÷ trimise" (p. 315), iar dashboard-ul exemplului arată CTOR 26%, nu 32%. Verificați întotdeauna definiția folosită de platforma voastră.

## Aplicare

- Folosește open rate pentru a testa subiectul, CTOR pentru a testa conținutul și oferta.
- Compară rata de dezabonare după fiecare schimbare de frecvență sau de ton.
- Raportează clientului mereu în raport cu media industriei, nu în cifre absolute.

## Exemplu

Dashboard-ul MailChimp cu mai multe campanii (fig. 11.16) compară segmente care primesc mesaje diferite; diferența dintre deschideri totale și unice arată câți oameni revin la același e-mail, de exemplu după o primă citire în grabă.

## Întrebări

- De ce a devenit open rate și mai puțin fiabil odată cu protecția confidențialității pe e-mail (deschideri automate)?
- Poate un e-mail cu CTOR mic să fie totuși un succes de brand?

## Legături

- **fundament** [[DIG-072-un-metric-e-doar-un-numar-devine-kpi-cand-e-ales-pentru-ca|DIG-072]] — metricile devin KPI doar legate de un obiectiv.
- **aplicare** [[DIG-034-e-mailul-promotional-bun-are-o-singura-oferta-un-termen|DIG-034]] — elementele de design se evaluează prin aceste metrici.
- **aplicare** [[DIG-076-testul-a-b-schimba-o-singura-variabila-porneste-de-la-o|DIG-076]] — subiectul și oferta se compară prin teste A/B.
- **vezi** [[DIG-036-in-e-mailul-cu-ai-momentul-si-frecventa-trimiterii-se|DIG-036]] — optimizarea orei de trimitere se bazează pe istoricul deschiderilor fiecărui abonat.

## Surse

- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 11, p. 299, 312-315, 317

<!-- backlinks:start -->
## Backlinks

- [[DIG-034-e-mailul-promotional-bun-are-o-singura-oferta-un-termen|DIG-034]] _vezi_ — E-mailul promoțional bun are o singură ofertă, un termen-limită și un subiect sub 50 de caractere
- [[DIG-076-testul-a-b-schimba-o-singura-variabila-porneste-de-la-o|DIG-076]] _vezi_ — Testul A/B schimbă o singură variabilă, pornește de la o ipoteză și așteaptă semnificația statistică
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
<!-- backlinks:end -->
