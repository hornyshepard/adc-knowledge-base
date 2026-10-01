---
id: AIM-1306
title: Validarea pe un eșantion de control separă tiparele reale de supra-ajustare
type: zettel
kind: method
skill: ai-marketing
also: [consumer-insight, digital-marketing]
level: 2
tags: [validare, overfitting, hold-out, modele-predictive, evaluare]
sources:
  - SRC-038 | cap. 2 (How do I plan to evaluate the results?, Results and validation), cap. 7
status: seed
---

# Validarea pe un eșantion de control separă tiparele reale de supra-ajustare

> **Ideea în o frază:** un model predictiv pare întotdeauna mai bun pe datele pe care a fost construit; abia testat pe date pe care nu le-a văzut arată cât valorează în piață.

## Explicație

Steven Struhl insistă ca orice proiect de predicție să decidă **de la început** cum va fi judecat rezultatul. Criteriile uzuale: procentul de clasificări corecte (*correct classification*), varianța explicată (R²), criteriile informaționale AIC/BIC (doar pentru a compara modele între ele) și eroarea pătratică medie (*RMSE*).

Cel mai important pas este **validarea**: pui deoparte o parte din date (*hold-out sample*), construiești modelul pe rest și îl testezi pe partea păstrată. Orice model prinde și „denivelări" întâmplătoare, specifice setului de date; fenomenul se numește **supra-ajustare** (*overfitting*). Rezultatul validat e aproape mereu mai slab, dar mai realist. Exemplu din carte: o rețea bayesiană prezicea corect 93% din comportament fără validare și 84% cu validare încrucișată.

Struhl adaugă trei nuanțe de bun-simț:

- „Toate modelele sunt greșite, dar unele sunt utile" (George Box): nu există un prag universal de „suficient de bun"; organizațiile își impun praguri arbitrare (70% varianță explicată, „două treimi"), pe care trebuie să le afli înainte.
- **Un rezultat slab poate fi informație.** La un producător de medicamente, rememorarea mesajului de vânzare explica cel mult 28% din vânzări; conducerea a acceptat, în cele din urmă, că problema nu era la forța de vânzare.
- Cu cât ai mai multe date, cu atât validarea e mai necesară și mai ușor de făcut.

## Aplicare

- Când o agenție sau un furnizor de AI prezintă un model de țintire, întreabă: „Cât de bine prezice pe date pe care nu le-a văzut?"
- Stabilește cu clientul, înainte de analiză, ce înseamnă „rezultat bun" și ce decizie se ia dacă modelul e slab.
- Tratează un model care „explică totul" pe datele vechi ca pe un semnal de alarmă, nu de succes.

## Exemplu

În studiul despre produsul IT din capitolul 7, un model de regresie complex (*PLS path model*) prezicea corect doar 11% din cota de afaceri; rețeaua bayesiană, validată încrucișat, ajungea la 84%. Comparația are sens doar pentru că ambele au fost evaluate cu aceeași regulă.

## Întrebări

- De ce un model care se potrivește perfect cu trecutul poate fi mai prost decât unul imperfect?
- Ce ar însemna „validare" pentru o campanie creativă testată pe un singur pre-test?

## Legături

- **fundament** [[AIM-1303]] — ciclul predictiv simplu are nevoie de acest pas de verificare.
- **vezi** [[INS-1302]] — semnificația statistică, celălalt criteriu adesea prost înțeles.
- **aplicare** [[AIM-1315]] — rețelele bayesiene includ validarea din oficiu.

## Surse

- [[SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 2 și cap. 7
