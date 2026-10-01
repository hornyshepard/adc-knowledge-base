---
id: AIM-032
title: Biasul în marketingul cu AI are două surse — datele din care învață modelul și încrederea oarbă a omului în recomandare
type: zettel
kind: concept
skill: ai-marketing
also: [consumer-insight, advertising-strategy, digital-marketing]
level: 2
tags: [bias-algoritmic, automation-bias, etica-ai, audit, incluziune, discriminare, david-dao]
sources:
  - SRC-037 | cap. 12 (12.1.2, 12.3.1–12.3.2)
  - SRC-039 | cap. 2 („Addressing Bias in AI-Driven Campaigns", „Frameworks for Bias Mitigation", p. 20–22)
  - SRC-005 | cap. 4 „Digital Divide" (efectele comportamentale); cap. 7 „The New CX" (cazul David Dao)
  - SRC-038 | cap. 1 („Implicit views of people and biases")
status: growing
---

# Biasul în marketingul cu AI are două surse — datele din care învață modelul și încrederea oarbă a omului în recomandare

> **Ideea în o frază:** un model repetă nedreptățile din datele lui și din obiectivul pe care îl optimizează, iar oamenii le amplifică atunci când acceptă recomandarea fără să judece; de aceea biasul se caută în rezultatele pe grupuri, nu în intenții.

## Explicație

Sursele din bibliotecă descriu trei mecanisme diferite, care se adună.

| Sursa biasului | Ce se întâmplă | Exemplul din carte |
|---|---|---|
| **Datele de antrenament** (Noil, Najafov) | modelul învață tiparele din istoric, inclusiv inegalitățile, și le poate accentua | o platformă imobiliară ale cărei reclame ocolesc anumite grupuri după rasă, gen sau statut; recomandări de modă după stereotipuri de gen; un model de limbaj care subreprezintă unele grupuri |
| **Obiectivul optimizat** (Kotler 5.0) | algoritmul face exact ce i s-a cerut și ignoră ce nu vede | United (2017): algoritmul de maximizare a veniturilor l-a ales pe David Dao drept pasagerul „cel mai puțin valoros" după statut și tarif, fără să știe că era medic cu pacienți a doua zi |
| **Automation bias** (Kotler 5.0) | omul își suspendă judecata și se bazează pe ce sugerează algoritmul | aceeași poveste: nimeni n-a contrazis recomandarea |

Struhl adaugă un nivel mai adânc: fiecare metodă de predicție poartă o imagine implicită despre om ([[AIM-001-metodele-de-predictie-a-alegerilor-formeaza-patru-familii|AIM-001]]). „Vei cumpăra ce cumpără cei asemănători ție" e deja o presupunere care poate pune pe cineva în grupul greșit.

Remediile propuse converg. Noil cere audit al surselor de date (reprezentative, diverse) și testarea periodică a modelelor pentru efecte nedorite. Najafov adaugă instrumente de detecție, echipe de revizuire diverse, monitorizare continuă, instruire și politici scrise. Kotler cere ca omul să poată anula decizia mașinii.

## Aplicare

- Înainte de lansare, întreabă: cine e exclus sau supra-țintit? Citește rezultatele pe grupuri (vârstă, gen, regiune), nu doar totalul.
- Scrie ce optimizează modelul și ce nu are voie să sacrifice (de exemplu, accesul egal la o ofertă).
- Pentru deciziile cu miză (preț, credit, excludere), păstrează o regulă clară de intervenție umană.

## Exemplu

Cazul David Dao arată cum biasul de obiectiv și cel de automatizare se combină: o regulă de venituri, aplicată fără empatie, a produs o criză de imagine pe care niciun model nu o „costase".

## Întrebări

- Optimizarea creației după CTR e și ea un bias, spre ce e ușor de apăsat? Ce pierde brandul?
- Cine auditează biasul într-o agenție: echipa de date, strategul sau creativul care alege imaginile?

## Legături

- **fundament** [[AIM-001-metodele-de-predictie-a-alegerilor-formeaza-patru-familii|AIM-001]] — imaginea implicită despre om din fiecare metodă e prima formă de bias.
- **vezi** [[AIM-030-etica-datelor-in-marketingul-cu-ai-are-patru-reguli-de-baza|AIM-030]] — explicabilitatea și răspunderea, regulile etice care fac biasul vizibil.
- **vezi** [[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]] — modelele opace sunt cele mai greu de auditat.
- **vezi** [[AIM-004-in-noul-cx-masinile-sunt-cool-dar-oamenii-sunt-calzi-ai|AIM-004]] — cazul David Dao, în argumentul despre înțelepciunea umană.
- **vezi** [[STO-040-checklist-ul-de-responsabilitate-pentru-reprezentare|STO-040]] — checklist-ul de reprezentare aplică aceeași vigilență imaginilor și textelor.
- **vezi** [[ADV-051-reclama-incluziva-se-verifica-pe-trei-axe-ton-limbaj|ADV-051]] — reclama incluzivă se verifică pe ton, limbaj și reprezentare.

## Surse

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 12 (12.1.2, 12.3.1–12.3.2)
- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, cap. 2, p. 20–22
- [[SRC-005-marketing-5-0-philip-kotler|SRC-005]] Kotler, Kartajaya & Setiawan, *Marketing 5.0*, cap. 4 și cap. 7
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 1

<!-- backlinks:start -->
## Backlinks

- [[AIM-004-in-noul-cx-masinile-sunt-cool-dar-oamenii-sunt-calzi-ai|AIM-004]] _vezi_ — În noul CX mașinile sunt „cool", dar oamenii sunt „calzi" — AI preia datele și convergența, omul păstrează insight-ul, înțelepciunea și empatia
- [[AIM-030-etica-datelor-in-marketingul-cu-ai-are-patru-reguli-de-baza|AIM-030]] _vezi_ — Etica datelor în marketingul cu AI are patru reguli de bază — consimțământ, acces și ștergere, transparență, minimizare
- [[AIM-034-decalajul-digital-real-e-intre-sustinatorii-si-criticii|AIM-034]] _vezi_ — Decalajul digital real e între susținătorii și criticii digitalizării — tehnologia câștigă încredere când e personală, socială și experiențială
- [[MAP-003-etica-reglementare-si-responsabilitate|MAP-003]] — Etică, reglementare și responsabilitate în publicitate
<!-- backlinks:end -->
