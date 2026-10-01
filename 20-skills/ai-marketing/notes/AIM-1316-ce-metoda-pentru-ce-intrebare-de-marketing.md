---
id: AIM-1316
title: Alegi metoda de analiză după întrebarea de marketing, nu după moda tehnologică
type: zettel
kind: checklist
skill: ai-marketing
also: [consumer-insight, client-business]
level: 2
tags: [alegerea-metodei, cercetare, predictie, planificarea-proiectului]
sources:
  - SRC-038 | cap. 2 (At the beginning, Know what sensible goals might look like); cap. 8 (The tasks the methods do)
status: seed
---

# Alegi metoda de analiză după întrebarea de marketing, nu după moda tehnologică

> **Ideea în o frază:** fiecare tip de întrebare are metoda lui potrivită; trusa completă combină metode noi, bazate pe învățare automată, cu metode clasice.

## Explicație

În capitolul de sinteză, Struhl reorganizează cartea după **sarcină**, nu după metodă. Înainte de orice proiect pune șase întrebări:

1. Ce se poate schimba în urma acestei analize?
2. Ce trebuie să știu ca schimbarea să se întâmple?
3. Ce date sau ce oameni îmi trebuie?
4. Care e maximul pe care îl pot obține de la sursa asta?
5. Cum voi ști că am ajuns la un răspuns bun?
6. Înțeleg utilizatorii rezultatului ce vor primi?

Apoi potrivește întrebarea cu metoda:

| Întrebarea | Metoda recomandată |
|---|---|
| Cine sunt cei mai buni prospecți? Ce caracterizează un grup? | arbori de clasificare (+ păduri aleatorii, boosting); clustering, analiză discriminantă |
| Care element dintr-o listă (beneficii, cadouri, mesaje) e cel mai valoros? | MaxDiff (cu HB), Q-Sort/Case 5 pentru liste foarte lungi |
| Ce influențează un rezultat (cotă, intenție)? | rețele bayesiene |
| Care e cea mai bună combinație pentru un mesaj, o reclamă, un produs individual? | conjoint |
| Ce se întâmplă cu un produs nou sau modificat într-o piață competitivă? | alegere discretă + simulator |
| Ce structuri ascunse sunt în date? | rețele bayesiene, arbori |
| Recunoaștere de tipare în volume uriașe | rețele neuronale, cu prudență |

Struhl adaugă un avertisment despre așteptări. E rezonabil să folosești tranzacțiile ca să estimezi răspunsul la o ofertă similară cu una recentă. Nu e rezonabil să aștepți de la ele o idee de produs nou.

## Aplicare

- Folosește cele șase întrebări ca preambul în orice brief de cercetare sau de date.
- Când clientul cere „un model AI", traduce cererea într-un rând din tabel. Adesea răspunsul e o metodă clasică.
- Explică dinainte stakeholderilor cum va arăta un rezultat rezonabil. Oamenii ocupați uită repede ce s-a convenit.

## Exemplu

Cazul croazierelor arată combinarea: arborele a găsit *cine* poate cumpăra croaziera de lux, dar Struhl notează că trăsăturile și mesajele care i-ar convinge trebuiau testate separat, cu metode de trade-off.

## Întrebări

- Ce metodă ai alege pentru a decide între trei propoziții de poziționare? De ce nu un focus grup?
- Unde intră modelele generative de azi în acest tabel din 2017?

## Legături

- **fundament** [[AIM-1307-patru-familii-de-metode-de-predictie-a-alegerii|AIM-1307]] — cele patru familii de metode.
- **aplicare** [[AIM-1313-arborii-de-clasificare-transforma-baza-de-date-in-reguli|AIM-1313]] — metoda pentru „cine".
- **aplicare** [[AIM-1310-metodele-de-trade-off-cand-folosesti-fiecare|AIM-1310]] — metodele pentru „ce" și „ce-ar fi dacă".
- **vezi** [[AIM-1306-validarea-pe-esantion-de-control-separa-tiparele-reale|AIM-1306]] — întrebarea 5, cum judeci rezultatul.

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 2 și cap. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-1307-patru-familii-de-metode-de-predictie-a-alegerii|AIM-1307]] _aplicare_ — Metodele de predicție a alegerilor formează patru familii, fiecare cu o imagine implicită despre om
- [[AIM-1312-checklist-pentru-un-studiu-de-alegere-bine-construit|AIM-1312]] _aplicare_ — Un studiu de alegere bun se construiește înainte de chestionar — checklist în zece puncte
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
