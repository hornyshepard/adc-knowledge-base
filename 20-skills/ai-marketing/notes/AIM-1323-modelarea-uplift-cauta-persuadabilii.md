---
id: AIM-1323
title: Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum
type: zettel
kind: concept
skill: ai-marketing
also: [advertising-strategy, digital-marketing, consumer-insight]
level: 3
tags: [uplift-modelling, persuadabili, atribuire, incrementalitate, obama-2012, modele-de-raspuns]
sources:
  - SRC-040 | secț. 2, cap. 3 (Moving From Level 4 to Level 5; Measuring the Right Things)
status: seed
---

# Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum

> **Ideea în o frază:** nu contează cine e probabil să cumpere, ci pe cine schimbă mesajul tău; restul e cheltuială sau, mai rău, iritare.

## Explicație

Richards și McLean ajung la această idee explicând de ce motoarele de decizie din call center par mult mai eficiente decât campaniile outbound. Explicația lor are două părți.

**1. Contextul, nu doar predicția.** Clientul care sună e deja implicat; e „la baza pâlniei". Măsurat izolat, motorul de decizie primește toată gloria vânzării, deși drumul până acolo a fost pregătit de multe alte comunicări. A copia modelul în campaniile outbound nu dă aceleași rezultate, pentru că omul e în alt punct al călătoriei.

**2. Tipul de model.** Un **model de răspuns** estimează cine va spune „da". Un **model uplift** estimează pe cine îl *schimbă* contactul. Orice grup se împarte în:

| Grup | Ce face contactul |
|---|---|
| Deja decis să cumpere | nimic; ar fi cumpărat oricum, dar modelul de răspuns îl numără ca succes |
| Hotărât să nu cumpere | nimic |
| Iritat de contact | efect negativ; trebuie lăsat în pace |
| **Persuadabil** | aici e singurul efect real al campaniei |

Exemplul cărții e campania de realegere a lui Barack Obama (2012). Analiștii au construit și testat modele care identificau alegătorii înclinați spre Mitt Romney, dar receptivi la mesajul lui Obama în statele indecise. Modelele au ghidat cumpărările de TV și online, ușile la care băteau voluntarii, apelurile și scrisorile.

Autorii notează și compromisurile: **costul pe conversie crește** (pentru că „sigurii" nu mai sunt numărați), iar munca analitică e mai scumpă. Câștigul: aceleași rezultate cu mai puțină comunicare outbound. Recomandarea lor mai largă: măsoară **angajamentul**, nu doar răspunsul. Caută oamenii care vor cumpăra *doar dacă* primesc încă o bucată de conținut potrivită.

## Aplicare

- Când un raport spune „campania a generat X vânzări", întreabă: câte ar fi apărut fără campanie? Cere un grup de control.
- Exclude din campaniile de retenție sau reduceri clienții care ar rămâne oricum; nu le dai bani degeaba.
- Identifică segmentul „nu deranja" (oameni pe care contactul îi enervează) și scoate-l din liste.

## Exemplu

Pe același principiu, Noil (SRC-037) propune o reducere celor cu „risc de churn". Fără logica uplift, o parte din reduceri ajunge la oameni care oricum nu plecau.

## Întrebări

- De ce un model care „prezice bine" poate fi inutil pentru decizia de a contacta pe cineva?
- Cum ai aplica ideea persuadabililor la planificarea media pentru o campanie de brand?

## Legături

- **contrazice** [[AIM-1303]] — utilizările-tip ale analizei predictive ignoră incrementalitatea.
- **vezi** [[AIM-1322]] — rezultatele O2, citite prin această lentilă.
- **vezi** [[AIM-1309]] — altă capcană: confuzia dintre preferință și piață.

## Surse

- [[SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, secț. 2, cap. 3
