---
id: AIM-1303
title: Analiza predictivă este un ciclu în cinci pași, nu un raport
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, marketing-fundamentals]
level: 1
tags: [analiza-predictiva, churn, clv, lead-scoring, modele]
sources:
  - SRC-037 | cap. 5 (5.1-5.6)
status: seed
---

# Analiza predictivă este un ciclu în cinci pași, nu un raport

> **Ideea în o frază:** analiza descriptivă spune ce s-a întâmplat; analiza predictivă (*predictive analytics*) estimează ce urmează și se îmbunătățește doar dacă predicțiile sunt comparate continuu cu realitatea.

## Explicație

Noil prezintă analiza predictivă ca pe un proces în cinci etape:

1. **Colectarea datelor** — comportamentale, tranzacționale, demografice, psihografice.
2. **Curățarea și pregătirea** — eliminarea dublurilor, completarea golurilor, structurarea.
3. **Construirea modelului** — algoritmul învață din istoric relațiile dintre variabile și rezultat.
4. **Generarea predicțiilor** — cine va cumpăra, cine va pleca, cine va răspunde la o campanie.
5. **Evaluarea și optimizarea** — modelul se rafinează pe măsură ce sosesc date noi (bucla de feedback).

Cartea listează cinci utilizări-tip în marketing: valoarea clientului pe durata relației (*customer lifetime value*, CLV), scorarea predictivă a lead-urilor (*predictive lead scoring*), recomandările de produs, predicția și prevenirea renunțării (*churn*), optimizarea campaniilor (ce canal funcționează pentru ce segment).

Limitele semnalate: calitatea datelor (date proaste → predicții proaste), complexitatea modelelor (firmele mici depind de furnizori) și confidențialitatea.

## Aplicare

- Când un client spune „avem date", întreabă despre pasul 2: cât de curate și cât de legate sunt?
- Cere întotdeauna pasul 5: cum verificăm dacă predicția a fost corectă? Fără el, modelul e o opinie automatizată.
- Folosește predicția pentru a alege **pe cine** și **când** (cine e pe cale să plece), apoi lasă strategia și creația să decidă **ce** îi spui.

## Exemplu

Sala de fitness din carte observă scăderea frecvenței de vizite la unii membri, îi marchează ca „risc de renunțare" și le oferă o ședință gratuită cu un antrenor înainte să-și anuleze abonamentul.

## Întrebări

- O predicție de churn corectă garantează că oferta de retenție e profitabilă? (Poate îi plătești pe unii care ar fi rămas oricum.)
- Ce lipsește din această schemă simplă față de o abordare riguroasă (validare pe date noi, supra-ajustare)?

## Legături

- **extinde** [[AIM-1306]] — Struhl arată de ce un model trebuie validat pe date pe care nu le-a văzut.
- **aplicare** [[AIM-1302]] — segmentarea predictivă folosește direct aceste modele.
- **vezi** [[AIM-1301]] — personalizarea predictivă e consumatorul final al predicțiilor.

## Surse

- [[SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 5 (5.1-5.6)
