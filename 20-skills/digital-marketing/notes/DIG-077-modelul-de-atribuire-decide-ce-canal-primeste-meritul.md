---
id: DIG-077
title: Modelul de atribuire decide ce canal primește meritul conversiei — iar după cookie-uri urmărirea devine incertă și etapele de început ies dezavantajate
type: zettel
kind: debate
skill: digital-marketing
also: [advertising-strategy]
level: 2
tags: [atribuire, last-click, first-touch, linear, multi-touch, utm, post-view, brand-lift, incrementalitate, roi]
sources:
  - SRC-030 | cap. 4, cap. 5
  - SRC-029 | cap. 9, p. 262-263; cap. 13, p. 381-382
  - SRC-032 | cap. 2.1, p. 39; cap. 3.3, p. 108-109; cap. 3.4.3.1, p. 119-120; cap. 4.3, p. 145
status: growing
---

# Modelul de atribuire decide ce canal primește meritul conversiei — iar după cookie-uri urmărirea devine incertă și etapele de început ies dezavantajate

> **Ideea în o frază:** când omul atinge brandul de cinci ori înainte să cumpere, modelul de atribuire (*attribution model*) hotărăște cât merit primește fiecare touchpoint, deci și unde se mută bugetul; alegerea lui e o decizie strategică, nu una tehnică.

## Explicație

Connors (SRC-030) numește atribuirea una dintre cele mai mari provocări ale marketingului multicanal: omul vede o reclamă pe Facebook, apoi un banner de retargeting, primește un newsletter și cumpără după o recenzie. Cine a „vândut”?

| Model | Cum împarte meritul | Ce favorizează |
|---|---|---|
| Last-touch / last-click | totul la ultima interacțiune | search de brand, e-mail, retargeting |
| First-touch | totul la prima interacțiune | canalele de descoperire (social, display) |
| Linear | egal între toate | o imagine echilibrată, dar naivă |
| Multi-touch | după contribuția estimată | pentru Connors, cel mai cuprinzător |

Zahay et al. (SRC-029) dau infrastructura: **parametrii UTM** (sursă, mediu, campanie; opțional termen și conținut) fac vizibil fiecare clic în analytics. În B2B, ei arată că lead-urile din canale diferite au și costuri, și rate de conversie diferite.

**Tensiunea.** Connors tratează modelul multi-touch ca pe o soluție. Schwarz-Musch et al. (SRC-032) arată că, în era post-cookie, urmărirea omului de la prima reclamă la cumpărare devine tot mai grea, mai ales pentru etapele de început. Last-touch supraevaluează search-ul și retargetingul, first-touch supraevaluează awareness-ul. Soluția lor, KPI separați pe etape, ocolește problema fără s-o rezolve: nu spune câți bani valorează o campanie de notorietate. Firmele fac încă, în paralel, studii clasice prin sondaj (*brand lift*). Toate modelele măsoară corelație, nu cauzalitate.

## Aplicare

- Întreabă clientul ce model folosește înainte să accepți KPI-urile; o campanie de notorietate judecată pe last-click „pierde” mereu.
- Pune UTM-uri pe fiecare link distribuit și raportează cu cel puțin două modele, discutând diferența.
- Completează atribuirea cu teste de incrementalitate (zone sau grupuri fără campanie) și cu sondaje de brand lift.

## Exemplu

O campanie de retargeting arată spectaculos în raportul last-touch, pentru că prinde oameni deja hotărâți. Dar acei oameni au intrat în journey datorită unui video văzut cu două săptămâni înainte, pe care modelul nu îl creditează deloc.

## Întrebări

- Ar trebui agențiile creative să fie plătite după un model de atribuire? După care?
- Cum atribui efectul unei campanii TV sau outdoor într-un model digital?

## Legături

- **fundament** [[DIG-072-un-metric-e-doar-un-numar-devine-kpi-cand-e-ales-pentru-ca|DIG-072]] — KPI-urile pe canal depind de modelul de atribuire.
- **vezi** [[DIG-074-fiecare-etapa-a-journey-ului-are-kpi-urile-ei-reach-net-si|DIG-074]] — KPI-urile separate pe etape, răspunsul parțial al SRC-032.
- **vezi** [[DIG-052-retargetingul-functioneaza-doar-segmentat-pe-etapa-din|DIG-052]] — retargetingul, câștigătorul clasic al atribuirii last-click.
- **alternativa** [[AIM-021-modelarea-uplift-cauta-persuadabilii-un-model-de-raspuns|AIM-021]] — modelarea uplift caută efectul incremental, nu doar cine a fost atins.
- **fundament** [[INS-081-efectul-unei-reclame-se-dovedeste-prin-experiment-nu-prin|INS-081]] — numai experimentul controlat dovedește că reclama a produs efectul.
- **vezi** [[SOC-039-valid-metrics-framework-succesul-pe-social-media-se-termina|SOC-039]] — și pe social impactul asupra vânzărilor e greu de atribuit, de aceea cadrul se oprește la advocacy.

## Surse

- [[SRC-030-digital-marketing-strategies|SRC-030]] K. Connors, *Advanced Digital Marketing Strategies*, cap. 4, cap. 5
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] Zahay et al., *Digital Marketing: Foundations and Strategy*, cap. 9, p. 262-263; cap. 13, p. 381-382
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] Schwarz-Musch, Tauchhammer, Guetz, *Digital Advertising in the Post-cookie Era*, cap. 2.1 (p. 39), 3.3 (p. 108-109), 3.4.3.1 (p. 119-120), 4.3 (p. 145)

<!-- backlinks:start -->
## Backlinks

- [[ADV-082-trackingul-continuu-masoara-campania-pe-aceiasi-patru-pasi|ADV-082]] _vezi_ — Trackingul continuu măsoară campania pe aceiași patru pași ai secvenței de răspuns, iar uzura se diagnostichează de la plan spre execuție
- [[ADV-085-eficienta-publicitatii-digitale-ramane-nedovedita-iar|ADV-085]] _vezi_ — Eficiența publicității digitale rămâne nedovedită, iar cartea vede rețelele sociale ca un mediu „negociat", afectat de fraudă și de vizibilitate slabă
- [[AIM-021-modelarea-uplift-cauta-persuadabilii-un-model-de-raspuns|AIM-021]] _vezi_ — Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum
- [[DIG-020-omnicanalul-inseamna-canale-care-se-intaresc-reciproc-se|DIG-020]] _vezi_ — Omnicanalul înseamnă canale care se întăresc reciproc — se construiește pe scenariile critice de cumpărare, cu silozurile sparte, și se măsoară prin valoarea clientului, nu prin clicuri pe canal
- [[DIG-072-un-metric-e-doar-un-numar-devine-kpi-cand-e-ales-pentru-ca|DIG-072]] _vezi_ — Un metric e doar un număr; devine KPI când e ales pentru că arată progresul față de un obiectiv — iar un KPI poate combina mai multe metrici
- [[DIG-074-fiecare-etapa-a-journey-ului-are-kpi-urile-ei-reach-net-si|DIG-074]] _vezi_ — Fiecare etapă a journey-ului are KPI-urile ei — reach net și frecvență în Aware, intrarea în setul evocat în Appeal, clicuri și conversii în Ask, retenție și CLV după cumpărare
- [[MAP-001-fluxul-agentiei-de-la-problema-de-business-la-pitch|MAP-001]] — Fluxul agenției — de la problema de business la pitch și înapoi
- [[MAP-002-modele-de-efect-si-customer-journey-comparate|MAP-002]] — Modelele de efect și de customer journey, comparate
- [[SRC-029-digital-marketing-foundations-and-strategy|SRC-029]] — Digital Marketing: Foundations and Strategy (5th ed.)
- [[SRC-030-digital-marketing-strategies|SRC-030]] — Advanced Digital Marketing Strategies: Mastering SEO, Social Media, Content Marketing, and AI for Maximum Online Growth
- [[SRC-032-digital-advertising-in-post-cookies-era|SRC-032]] — Digital Advertising in the Post-cookie Era: Strategic Campaign Planning Across the Customer Journey
<!-- backlinks:end -->
