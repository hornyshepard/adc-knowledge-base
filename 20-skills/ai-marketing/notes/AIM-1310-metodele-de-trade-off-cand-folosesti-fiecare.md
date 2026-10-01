---
id: AIM-1310
title: Metodele de trade-off — alegere discretă, conjoint, MaxDiff, Q-Sort — răspund la întrebări diferite
type: zettel
kind: framework
skill: ai-marketing
also: [consumer-insight, marketing-fundamentals]
level: 2
tags: [alegere-discreta, conjoint, maxdiff, q-sort, experiment, hierarchical-bayes]
sources:
  - SRC-038 | cap. 3 (integral); cap. 4 (The Bayesian advantage); cap. 8 (Finding what is most valuable in a list)
status: seed
---

# Metodele de trade-off — alegere discretă, conjoint, MaxDiff, Q-Sort — răspund la întrebări diferite

> **Ideea în o frază:** toate obligă oamenii să aleagă între atribute, dar fiecare răspunde la altă întrebare; alegerea greșită a metodei produce răspunsuri precise la întrebarea greșită.

## Explicație

Metodele de trade-off pornesc de la ideea că un produs, un serviciu sau un mesaj e un pachet de atribute, fiecare cu **niveluri** (de exemplu prețuri de 2.000, 4.500, 6.800 și 9.000 de lire). Valoarea fiecărui nivel se măsoară în **utilități**, o unitate contabilă abstractă. Metodele nu pretind să reproducă gândirea, ci **rezultatul** deciziei.

| Metodă | Ce arată participantului | Răspunde la |
|---|---|---|
| Alegere discretă (*discrete choice modelling*) | piețe simulate cu produse concurente + „niciunul" | ce se întâmplă cu cotele dacă schimb produsul, prețul sau concurența (inclusiv canibalizarea) |
| Conjoint (*full-profile*) | un produs sau mesaj întreg, evaluat | cea mai bună configurație pentru un produs fără concurență directă sau cu cotă mică; optimizarea mesajelor |
| MaxDiff | seturi de 2–6 itemi dintr-o listă de 8–35; „cel mai/cel mai puțin important" | ierarhia unei liste de beneficii, mesaje, cadouri; date pentru fiecare individ |
| Q-Sort / Thurstone Case 5 | listă lungă (până la ~100); ordonezi primii și ultimii | ierarhia unei liste foarte lungi, doar la nivel de grup |

Forța lor vine din **experimentul planificat** (*designed experiment*): atributele variază necorelat între ele (design ortogonal). Astfel, 18 profiluri pot estima valoarea a 4.374 de combinații, iar 20 pot acoperi 262.144.

Componenta AI e **analiza bayesiană ierarhică** (*Hierarchical Bayes, HB*): completează datele lipsă ale fiecărui respondent „împrumutând" repetat estimări de la ceilalți, de zeci de mii de ori, până când valorile se stabilizează. Cu HB poți măsura de 2–4 ori mai multe atribute fără eșantion mai mare și obții rezultate la nivel individual. Oamenii obosesc după 6–12 ecrane; inginerii și fermierii rezistă până la ~21.

## Aplicare

- Lista de beneficii pentru brief? MaxDiff, nu ratinguri.
- Lansare într-o piață aglomerată, cu reacții posibile ale concurenților? Alegere discretă.
- Ce combinație de titlu, imagine și ofertă funcționează? Conjoint.

## Exemplu

Struhl dă exemplul unei vitrine frigorifice pentru vin, cu funcții propuse de echipa de produs, unele „ușor exagerate": la ratinguri, aproape toate ies foarte importante. Un MaxDiff sau un conjoint pe aceleași funcții le-ar fi separat clar.

## Întrebări

- De ce nu poate MaxDiff să compare „valabil 3 luni" cu „valabil 6 luni"?
- Ce pierzi dacă testezi atributele separat, nu în contextul produsului întreg?

## Legături

- **fundament** [[INS-1304]] — eșecul ratingurilor directe e motivul existenței acestor metode.
- **extinde** [[AIM-1311]] — alegerea discretă și simulatorul de piață în acțiune.
- **aplicare** [[ADV-1301]] — conjoint-ul aplicat mesajelor publicitare.
- **vezi** [[AIM-1312]] — regulile practice pentru un studiu de alegere bine construit.

## Surse

- [[SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 3, 4 și 8
