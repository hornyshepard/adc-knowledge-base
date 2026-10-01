---
id: AIM-027
title: Un model de limbaj rezumă bine text, dar nu dovedește cauze — „de ce a crescut conversia?" nu e o întrebare pentru chatbot
type: zettel
kind: debate
skill: ai-marketing
also: [consumer-insight, digital-marketing]
level: 2
tags: [analiza-de-date, llm, sentiment, cauzalitate, halucinatii, social-listening]
sources:
  - SRC-039 | cap. 4 (Analytics Tools, Demystifying Analytics, p. 94–95); cap. 5 (Data Collection and Preprocessing, NLP, Summarization and Insights Generation, Case Studies, p. 109–114)
  - SRC-038 | cap. 2 (These methods show what will happen but not why, Results and validation); cap. 8 (Thinking about thinking)
status: growing
---

# Un model de limbaj rezumă bine text, dar nu dovedește cauze — „de ce a crescut conversia?" nu e o întrebare pentru chatbot

> **Ideea în o frază:** ChatGPT e util pentru a citi și sintetiza volume mari de text nestructurat; dar o explicație fluentă a cifrelor nu e o analiză cauzală validată.

## Explicație

Najafov descrie un flux de analiză cu ChatGPT în patru pași: **colectare și pregătire** (curățare, transformare, integrare), **procesarea limbajului natural** (*NLP*: sentiment, identificarea temelor, extragerea expresiilor-cheie), **rezumare și insight-uri**, apoi **vizualizare și raportare**. Partea solidă a propunerii e lucrul cu text: recenzii, comentarii, răspunsuri deschise. De exemplu, modelul observă că un produs e lăudat pentru calitate, dar criticat pentru preț.

Problema apare când autorul extinde promisiunea la cifre și cauze. Exemplele lui de „după integrare" arată modelul spunând că paginile de blog au trafic mare *datorită* articolelor pe teme la modă, sau că rata de conversie a crescut cu 15% „în principal datorită" noii campanii de e-mail. Studiile de caz (un „gigant e-commerce", o „firmă de servicii financiare") sunt anonime și fără metodă.

## Tensiunea

| Najafov (SRC-039) | Struhl (SRC-038) |
|---|---|
| modelul transformă date brute în concluzii acționabile, rapid | un model trebuie validat pe date noi, altfel supra-ajustează |
| poate spune *de ce* s-a schimbat un indicator | chiar metodele riguroase arată *ce* se întâmplă mai ușor decât *de ce* |
| tiparele apar din date | „tiparele descoperite spontan" sunt adesea legende (scutece și bere) |

Struhl nu discută modelele generative (cartea lui e din 2017), dar criteriile lui se aplică direct. O explicație cauzală cere design (experiment, grup de control) sau un model validat, nu doar o propoziție convingătoare.

## Aplicare

- Folosește modelul pentru **sinteză de text** (teme din 2.000 de recenzii, rezumatul unui focus grup transcris), apoi verifică pe un eșantion citit de om.
- Pentru întrebări de tip „ce a cauzat?", cere un test (A/B, grup de control) sau un analist; tratează răspunsul modelului ca **ipoteză**.
- Nu lăsa modelul să „curețe" singur baza de clienți fără reguli verificabile.

## Exemplu

Cazul anonim al producătorului de bunuri de consum care a „descoperit" cererea de produse eco și a lansat o linie de succes ilustrează exact riscul: povestea e plauzibilă, dar nu știm ce date, ce metodă și ce alternative au existat.

## Întrebări

- Cum ai verifica dacă temele extrase de model din recenzii sunt reale și nu inventate?
- Ce întrebări de cercetare poți delega în siguranță unui model de limbaj?

## Legături

- **contrazice** [[AIM-005-datele-istorice-prezic-repetarea-nu-noutatea-nu-raspund-la|AIM-005]] — Struhl: datele nu produc singure insight-uri sau idei noi.
- **vezi** [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] — validarea, pasul lipsă din fluxul propus de Najafov.
- **vezi** [[AIM-025-promptul-de-marketing-e-un-mini-brief-iar-raspunsul|AIM-025]] — întrebările analitice ca tip de prompt.
- **vezi** [[INS-081-efectul-unei-reclame-se-dovedeste-prin-experiment-nu-prin|INS-081]] — un efect cauzal se dovedește prin experiment cu grup de control.
- **vezi** [[AIM-028-ascultarea-vizuala-gaseste-brandul-in-imagini-acolo-unde-nu|AIM-028]] — analiza automată de sentiment, pe text și pe imagini, are aceleași limite.

## Surse

- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, cap. 4, p. 94–95; cap. 5, p. 109–114
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 2 și cap. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-005-datele-istorice-prezic-repetarea-nu-noutatea-nu-raspund-la|AIM-005]] _vezi_ — Datele istorice prezic repetarea, nu noutatea — nu răspund la „ce-ar fi dacă" și nu arată percepțiile
- [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] _vezi_ — Validarea pe un eșantion de control separă tiparele reale de supra-ajustare
- [[AIM-024-ipoteza-o-formuleaza-omul-ai-ul-o-ruleaza-omul-o|AIM-024]] _vezi_ — Ipoteza o formulează omul, AI-ul o rulează, omul o interpretează — împărțirea muncii în testare și lead-uri
- [[AIM-025-promptul-de-marketing-e-un-mini-brief-iar-raspunsul|AIM-025]] _vezi_ — Promptul de marketing e un mini-brief, iar răspunsul modelului e o ciornă, nu un livrabil
- [[AIM-028-ascultarea-vizuala-gaseste-brandul-in-imagini-acolo-unde-nu|AIM-028]] _vezi_ — Ascultarea vizuală găsește brandul în imagini, acolo unde nu e numit în text
- [[DIG-075-palnia-de-conversie-arata-unde-pleaca-vizitatorii-treaba|DIG-075]] _vezi_ — Pâlnia de conversie arată unde pleacă vizitatorii; treaba marketerului e să afle de ce
- [[SRC-039-chatgpt-for-marketing|SRC-039]] — ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
