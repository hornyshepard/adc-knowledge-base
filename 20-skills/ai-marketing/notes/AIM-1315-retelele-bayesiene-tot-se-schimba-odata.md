---
id: AIM-1315
title: Rețelele bayesiene pornesc de la ideea că, atunci când schimbi o variabilă, se schimbă toate
type: zettel
kind: concept
skill: ai-marketing
also: [consumer-insight, advertising-strategy]
level: 3
tags: [retele-bayesiene, regresie, driveri, probabilitate-conditionata, sondaj-si-comportament]
sources:
  - SRC-038 | cap. 7 (integral); cap. 8 (Determining the effects of variables)
status: seed
---

# Rețelele bayesiene pornesc de la ideea că, atunci când schimbi o variabilă, se schimbă toate

> **Ideea în o frază:** spre deosebire de regresie, care măsoară efectul unei variabile „ținând restul constant", o rețea bayesiană (*Bayes Net*) modelează felul în care o schimbare se propagă prin toate variabilele legate.

## Explicație

Ideea lui Bayes, spusă simplu: pornești de la o estimare anterioară, o actualizezi cu datele observate și obții o estimare nouă, mai bună. O rețea bayesiană e o diagramă de variabile legate prin săgeți („părinți", „copii"), fără bucle. Fiecare nod conține o tabelă de probabilități condiționate. Rețeaua își poate învăța singură structura din date sau poate fi construită de expert.

Struhl o compară cu metodele clasice:

| | Regresie | Arbore de clasificare | Rețea bayesiană |
|---|---|---|---|
| Relații | linii drepte (corelații) | situații „dacă–atunci" | tot tiparul de valori, inclusiv curbe în S |
| Efectul unei schimbări | restul rămâne constant | doar în anumite combinații | se propagă prin toată rețeaua |
| Variabile corelate | coeficienți instabili, chiar cu semn inversat | puține variabile reținute | le include pe toate |

Rezultatul e o măsură a **sensibilității** țintei la fiecare variabilă, termenul corect pentru ce industria numește „analiză de driveri". Mai poate filtra rapid variabilele relevante („pătura Markov") și include validarea din oficiu.

## Aplicare

- Folosește rețeaua când vrei să legi **răspunsuri din sondaj de comportament real** (cotă, share of wallet), lucru notoriu dificil cu regresia.
- Verifică diagrama: dacă structura nu are sens, nu accepta rezultatul.
- Reține limita: rețeaua îți spune **ce** trebuie schimbat (de exemplu „serviciul de vânzări"), nu **cum**. Pentru „cum" ai nevoie de un experiment.

## Exemplu

Într-un studiu printre clienții unui produs IT, rețeaua a ajuns la 84% predicție corectă a cotei de afaceri reînnoite, cu validare încrucișată. Cel mai bun model de regresie (PLS) ajungea la 11%. Problema Monty Hall (schimbi ușa sau nu?) se rezolvă exact cu o rețea de trei noduri: schimbând, câștigi de două ori mai des.

## Întrebări

- De ce e nerealist, în marketing, să presupui că „restul rămâne constant"?
- Ce public ar respinge un model fără ecuații?

## Legături

- **alternativa** [[AIM-1313-arborii-de-clasificare-transforma-baza-de-date-in-reguli|AIM-1313]] — arborii văd interacțiuni locale, rețelele văd tot tiparul.
- **aplicare** [[ADV-1302-ierarhia-efectelor-testata-cu-date-alta-ordine|ADV-1302]] — rețeaua aplicată unui model teoretic al efectelor publicității.
- **aplicare** [[INS-1305-importanta-unui-atribut-se-schimba-cu-etapa-de-viata|INS-1305]] — rețeaua aplicată driverilor de cumpărare pe segmente de vârstă.
- **fundament** [[AIM-1306-validarea-pe-esantion-de-control-separa-tiparele-reale|AIM-1306]] — validarea, inclusă în rețelele bayesiene.

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 7 și cap. 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-1302-ierarhia-efectelor-testata-cu-date-alta-ordine|ADV-1302]] _fundament_ — Testată cu date, ierarhia efectelor a ieșit într-o altă ordine decât teoria — de la „ce fac ei" la „ce fac eu"
- [[AIM-1306-validarea-pe-esantion-de-control-separa-tiparele-reale|AIM-1306]] _aplicare_ — Validarea pe un eșantion de control separă tiparele reale de supra-ajustare
- [[AIM-1313-arborii-de-clasificare-transforma-baza-de-date-in-reguli|AIM-1313]] _alternativa_ — Arborii de clasificare transformă o bază de date în câteva reguli „dacă–atunci" pentru țintire
- [[INS-1305-importanta-unui-atribut-se-schimba-cu-etapa-de-viata|INS-1305]] _fundament_ — Importanța unui atribut se schimbă cu etapa de viață — „brandul de încredere" contează enorm la 4–8 ani și aproape deloc la preadolescenți
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
