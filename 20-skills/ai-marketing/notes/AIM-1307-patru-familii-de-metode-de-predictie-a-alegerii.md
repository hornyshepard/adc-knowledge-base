---
id: AIM-1307
title: Metodele de predicție a alegerilor formează patru familii, fiecare cu o imagine implicită despre om
type: zettel
kind: framework
skill: ai-marketing
also: [consumer-insight, marketing-fundamentals]
level: 1
tags: [predictie, metode-de-cercetare, machine-learning, definitie-ai, biasuri-implicite]
sources:
  - SRC-038 | Prefață; cap. 1 (Some definitions we need, The methods we will be discussing, Implicit views of people and biases); cap. 8
status: seed
---

# Metodele de predicție a alegerilor formează patru familii, fiecare cu o imagine implicită despre om

> **Ideea în o frază:** înainte să alegi o metodă (sau un instrument AI), întreabă ce presupune ea despre felul în care oamenii decid, pentru că acolo se ascund erorile.

## Explicație

Struhl definește pragmatic inteligența artificială: orice face o mașină ca să răspundă mediului și să-și maximizeze succesul. Pentru marketing, mediul sunt **datele**, iar succesul înseamnă găsirea tiparelor pe care noi nu le vedem. Decizia rămâne la om. Mai precizează că nu „prezicem", ci **prognozăm** (*forecasting*), ca meteorologii. Iar AI „se ascunde la vedere" de decenii în metodele de cercetare (arbori de clasificare, analiză bayesiană ierarhică).

Metodele de predicție a alegerilor se împart în patru familii:

| Familie | Ce presupune despre oameni | Limita tipică |
|---|---|---|
| Experimentale / de trade-off (alegere discretă, conjoint, MaxDiff) | produsul e un pachet de atribute care se pot cântări | atributele măsurabile nu sunt mereu cele importante |
| Întrebări și răspunsuri (sondaje) | oamenii spun corect ce gândesc | biasuri de răspuns, ratinguri umflate |
| Date stocate / istorice (data mining, machine learning) | vei face ce ai făcut; vei cumpăra ce cumpără cei asemănători ție | eșuează când piața se schimbă sau când ești pus în grupul greșit |
| Modele teoretice (ierarhii de tip AIDA) | oamenii trec prin etape psihologice | adesea fără bază empirică |

Struhl le așază pe două axe: **efortul de a planifica interacțiunea cu consumatorii** (inevitabil) și **complexitatea analitică** (uneori negociabilă). Alegerea discretă e sus pe ambele axe; datele istorice cer multă analiză, dar aproape deloc contact cu oamenii.

## Aplicare

- Pune fiecărei surse de „insight" întrebarea: ce imagine despre om stă în spatele ei?
- Combină familiile: datele istorice spun *cine*, sondajele sugerează *de ce*, experimentele arată *ce s-ar întâmpla dacă*.
- Fii sceptic față de metodele susținute doar de site-ul unui vânzător. Struhl acceptă doar ce are și experiență practică, și validare academică.

## Exemplu

Ipoteza „cumperi ce cumpără cei asemănători ție" stă la baza motoarelor de recomandare: dacă femeile în ultimul trimestru de sarcină cumpără multă vată, sistemul presupune că și Thisbe, aflată în aceeași situație, va cumpăra.

## Întrebări

- Ce imagine despre om are un brief care spune „targetul vrea calitate la preț bun"?
- Ce familie folosește un instrument de social listening? Ce poate și ce nu poate spune?

## Legături

- **extinde** [[AIM-1308-datele-istorice-prezic-repetarea-nu-noutatea|AIM-1308]] — limita datelor istorice, dezvoltată.
- **extinde** [[AIM-1310-metodele-de-trade-off-cand-folosesti-fiecare|AIM-1310]] — familia experimentală, pe larg.
- **vezi** [[ADV-1302-ierarhia-efectelor-testata-cu-date-alta-ordine|ADV-1302]] — un model teoretic (ierarhia efectelor) testat cu date.
- **aplicare** [[AIM-1316-ce-metoda-pentru-ce-intrebare-de-marketing|AIM-1316]] — matricea „ce metodă pentru ce sarcină".

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, Prefață, cap. 1, cap. 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-1302-ierarhia-efectelor-testata-cu-date-alta-ordine|ADV-1302]] _vezi_ — Testată cu date, ierarhia efectelor a ieșit într-o altă ordine decât teoria — de la „ce fac ei" la „ce fac eu"
- [[AIM-1308-datele-istorice-prezic-repetarea-nu-noutatea|AIM-1308]] _fundament_ — Datele istorice prezic repetarea, nu noutatea — nu răspund la „ce-ar fi dacă" și nu arată percepțiile
- [[AIM-1316-ce-metoda-pentru-ce-intrebare-de-marketing|AIM-1316]] _fundament_ — Alegi metoda de analiză după întrebarea de marketing, nu după moda tehnologică
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
