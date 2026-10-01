---
id: AIM-006
title: Analiza predictivă estimează cine va cumpăra, ce se va vinde și ce va funcționa — un ciclu care se verifică continuu, nu un raport
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, marketing-fundamentals, advertising-strategy]
level: 1
tags: [analiza-predictiva, predictive-marketing, clv, churn, lead-scoring, next-best-action, recomandari, regresie, retele-neuronale, moneyball]
sources:
  - SRC-037 | cap. 5 (5.1-5.6)
  - SRC-005 | cap. 9 „Predictive Marketing" (Fig. 9.1, 9.2)
status: growing
---

# Analiza predictivă estimează cine va cumpăra, ce se va vinde și ce va funcționa — un ciclu care se verifică continuu, nu un raport

> **Ideea în o frază:** analiza descriptivă spune ce s-a întâmplat; analiza predictivă (*predictive analytics*) învață din istoric ca să estimeze ce urmează și devine utilă doar dacă predicțiile sunt comparate permanent cu realitatea.

## Explicație

*Marketing 5.0* și Karen Noil descriu același instrument din două unghiuri. Kotler, Kartajaya și Setiawan pornesc de la *Moneyball*: Oakland Athletics a construit o echipă câștigătoare pe statistici, nu pe intuiție. Ei împart aplicațiile în trei zone; Noil dă utilizările-tip din fiecare.

| Zona (Kotler 5.0) | Ce prezice | Utilizări-tip (Noil) |
|---|---|---|
| **Clienți** | valoarea pe viață (CLV), upsell, cross-sell, riscul de abandon | CLV, scorarea lead-urilor, predicția *churn*; plan de *next-best-action* pentru fiecare client |
| **Produse** | ce produs nou are șanse, ce să oferi fiecăruia | sisteme de recomandare, modele de propensiune |
| **Branduri** | ce combinație de copy și vizual va funcționa, pentru ce public | optimizarea campaniilor pe canale și segmente |

Noil adaugă procesul, în cinci pași: colectarea datelor, curățarea și pregătirea, construirea modelului, generarea predicțiilor, evaluarea și optimizarea (bucla de feedback). Kotler adaugă tehnicile pe care marketerul trebuie să le înțeleagă conceptual: **regresia** (cea logistică dă probabilitatea unui da/nu), **filtrarea colaborativă** (ce le-a plăcut oamenilor asemănători) și **rețelele neuronale** (precise, dar opace).

Aici sursele se despart. Kotler et al. văd opacitatea „cutiei negre" ca pe un avantaj: modelul nu mai e limitat de prejudecățile marketerului. Struhl susține opusul ([[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]]). Și nici Kotler, nici Noil nu vorbesc despre validarea pe date nevăzute sau despre vânzările care ar fi venit oricum.

## Aplicare

- Când un client spune „avem date", întreabă despre pasul 2: cât de curate și cât de legate sunt?
- Cere întotdeauna pasul 5: cum verificăm dacă predicția a fost corectă? Fără el, modelul e o opinie automatizată.
- Folosește predicția ca să alegi **pe cine** și **când**, apoi lasă strategia și creația să decidă **ce** îi spui. În B2B și servicii, argumentează bugetul de achiziție prin CLV, nu prin prima vânzare.

## Exemplu

Netflix a decis să producă *House of Cards* pe baza unei predicții despre combinația Kevin Spacey, David Fincher și o dramă politică (Kotler 5.0). La scară mică, sala de fitness din cartea lui Noil marchează membrii care vin tot mai rar ca „risc de renunțare" și le oferă o ședință gratuită cu un antrenor.

## Întrebări

- O predicție de churn corectă garantează că oferta de retenție e profitabilă? Poate îi plătești pe unii care ar fi rămas oricum.
- Poate predicția să descurajeze ideile cu adevărat noi, pentru care nu există istoric?

## Legături

- **fundament** [[DIG-061-marketingul-bazat-pe-date-tinteste-segmentul-de-unu-si|DIG-061]] — modelele predictive se construiesc pe ecosistemul de date al „segmentului de unu".
- **vezi** [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] — validarea pe date nevăzute, pasul pe care ciclul îl presupune, dar nu-l explică.
- **contrazice** [[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]] — Struhl respinge ideea că opacitatea modelului e un avantaj.
- **vezi** [[AIM-021-modelarea-uplift-cauta-persuadabilii-un-model-de-raspuns|AIM-021]] — modelarea uplift: nu cine va cumpăra, ci pe cine schimbă contactul.
- **vezi** [[DIG-060-targetarea-predictiva-muta-intrebarea-de-la-cine-a-fost|DIG-060]] — targetarea predictivă aplică același principiu în media.
- **vezi** [[AIM-016-personalizarea-cu-ai-lucreaza-in-patru-registre-in-timp|AIM-016]] — personalizarea predictivă e consumatorul final al predicțiilor.

## Surse

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 5 (5.1-5.6)
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]] Kotler, Kartajaya & Setiawan, *Marketing 5.0*, cap. 9 „Predictive Marketing: Anticipating Market Demand with Proactive Action" (Fig. 9.1, 9.2)

<!-- backlinks:start -->
## Backlinks

- [[AIM-003-martech-are-sapte-cazuri-de-utilizare-pe-calea-clientului|AIM-003]] _vezi_ — Martech are șapte cazuri de utilizare pe calea clientului — de la publicitate și conținut la service CRM
- [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] _fundament_ — Validarea pe un eșantion de control separă tiparele reale de supra-ajustare
- [[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]] _contrazice_ — Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
- [[AIM-016-personalizarea-cu-ai-lucreaza-in-patru-registre-in-timp|AIM-016]] _vezi_ — Personalizarea cu AI lucrează în patru registre — în timp real, comportamental, micro-segment și predictiv
- [[AIM-017-segmentele-construite-cu-ai-sunt-dinamice-clientul-migreaza|AIM-017]] _aplicare_ — Segmentele construite cu AI sunt dinamice — clientul migrează între ele după comportament
- [[AIM-019-ofera-ce-e-mai-probabil-sa-accepte-clientul-nu-ce-aduce|AIM-019]] _vezi_ — Oferă ce e mai probabil să accepte clientul, nu ce aduce marja cea mai mare — un „da" aduce alt „da"
- [[AIM-021-modelarea-uplift-cauta-persuadabilii-un-model-de-raspuns|AIM-021]] _contrazice_ — Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum
- [[DIG-060-targetarea-predictiva-muta-intrebarea-de-la-cine-a-fost|DIG-060]] _vezi_ — Targetarea predictivă mută întrebarea de la „cine a fost omul" la „ce va face probabil" și poate folosi declanșatori de context precum vremea, locul și ora
- [[DIG-061-marketingul-bazat-pe-date-tinteste-segmentul-de-unu-si|DIG-061]] _aplicare_ — Marketingul bazat pe date țintește „segmentul de unu" și începe cu un obiectiv îngust, nu cu un proiect IT
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]] — Marketing 5.0: Technology for Humanity
- [[SRC-037-ai-driven-marketing|SRC-037]] — AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
<!-- backlinks:end -->
