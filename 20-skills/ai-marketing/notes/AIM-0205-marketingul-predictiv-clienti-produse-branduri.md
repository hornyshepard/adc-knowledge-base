---
id: AIM-0205
title: Marketingul predictiv anticipează piața în trei zone — clienți, produse și branduri — cu regresie, filtrare colaborativă și rețele neuronale
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, advertising-strategy]
level: 3
tags: [predictive-analytics, clv, next-best-action, recomandari, regresie, retele-neuronale, moneyball]
sources:
  - SRC-005 | cap. 9 „Predictive Marketing"
status: seed
---

# Marketingul predictiv anticipează piața în trei zone — clienți, produse și branduri — cu regresie, filtrare colaborativă și rețele neuronale

> **Ideea în o frază:** în loc să explice trecutul și să ghicească viitorul din intuiție, marketerul folosește modele care învață din datele istorice ca să prezică cine va cumpăra, ce se va vinde și ce campanie va funcționa, înainte de a investi.

## Explicație

Metafora cărții e *Moneyball*: Oakland Athletics și apoi Liverpool FC au construit echipe câștigătoare pe baza analizei statistice, nu a intuiției. Analitica predictivă depășește statistica descriptivă (ce s-a întâmplat) și analitica în timp real (reacția imediată). Ea caută tipare subtile și recomandă acțiunea următoare.

**Trei aplicații** (Fig. 9.1):

| Zona | Model | Ce prezice |
|---|---|---|
| **Clienți** | modelul de *customer equity*: valoarea pe viață a clientului (CLV), inclusiv upsell, cross-sell și riscul de abandon | pe cine merită să cucerești și să păstrezi; permite **next-best-action** (un plan pas cu pas pentru fiecare client) și niveluri de clienți după CLV |
| **Produse** | analiza atributelor care au funcționat, sisteme de recomandare, modele de propensiune, afinitate între produse | ce produs nou are șanse; ce să oferi fiecărui client |
| **Branduri** | profiluri de audiență, ingredientele campaniilor reușite, analiză de sentiment | ce combinație de copy și vizual va funcționa; ce conținut se potrivește cu ce public; site dinamic, cu „următorul conținut potrivit" |

**Trei tehnici**, pe care marketerul trebuie să le înțeleagă conceptual, chiar dacă le construiesc specialiștii în date:

- **Regresia** — relația dintre variabilele independente (momentul campaniei, copy, demografie) și cele dependente (click-uri, vânzări). Regresia logistică dă probabilitatea unui rezultat binar (cumpără/nu cumpără, rămâne/pleacă).
- **Filtrarea colaborativă** — colectezi preferințe (ratinguri sau acțiuni), grupezi clienții și produsele similare și prezici ratingul pentru ce n-au văzut încă (Netflix, Amazon).
- **Rețelele neuronale** — straturi ascunse care descoperă singure relații în date nestructurate. Sunt precise, dar opace („cutie neagră").

Pentru autori, opacitatea e un avantaj: modelul nu e limitat de prejudecățile și presupunerile marketerului. Totuși, marketerul trebuie să ghideze alegerea datelor și să interpreteze rezultatul.

## Aplicare

- Înainte de un pre-test clasic, verifică dacă există date istorice de campanie din care să extragi „ingredientele" care au funcționat.
- Pentru clienții B2B sau din servicii (bănci, telecom), argumentează bugetul de achiziție prin CLV, nu prin prima vânzare.
- Folosește regresia când problema e simplă și structurată, rețelele neuronale când factorii sunt necunoscuți.

## Exemplu

Netflix a decis să producă *House of Cards* pe baza unei predicții: combinația Kevin Spacey, David Fincher și o dramă politică inspirată din serialul britanic avea șanse mari de succes (cap. 9).

## Întrebări

- „Opacitatea e un avantaj" — ce se întâmplă când modelul reproduce prejudecăți și nu poți explica de ce?
- Poate predicția să descurajeze ideile cu adevărat noi, pentru care nu există date istorice?

## Legături

- **fundament** [[DIG-0204]] — modelele predictive se construiesc pe ecosistemul de date.
- **vezi** [[ADV-0202]] — PAR și BAR măsurau retrospectiv; predicția încearcă să estimeze înainte de lansare.
- **vezi** [[AIM-0203]] — omul rămâne responsabil de interpretare și de decizia finală.
- **aplicare** [[AIM-0204]] — recomandările și prognozele apar în checklistul martech.

## Surse

- [[SRC-005]] Kotler, Kartajaya, Setiawan, *Marketing 5.0*, cap. 9 „Predictive Marketing: Anticipating Market Demand with Proactive Action" (Fig. 9.1, 9.2)
