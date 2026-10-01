---
id: INS-1302
title: Semnificația statistică nu înseamnă importanță — cu date multe, aproape orice diferență devine „semnificativă"
type: zettel
kind: principle
skill: consumer-insight
also: [ai-marketing, digital-marketing]
level: 2
tags: [semnificatie-statistica, putere-statistica, corelatie, big-data, interpretare]
sources:
  - SRC-038 | cap. 2 (What is significant?, Power versus significance, Significance testing needs to make sense, On to correlations)
status: seed
---

# Semnificația statistică nu înseamnă importanță — cu date multe, aproape orice diferență devine „semnificativă"

> **Ideea în o frază:** „semnificativ" spune doar că probabil nu faci o afirmație falsă; nu spune că efectul e mare, util sau logic.

## Explicație

Struhl clarifică trei confuzii frecvente în rapoartele de cercetare:

1. **Ce înseamnă „semnificativ".** Pragul de 95% încredere e o convenție („pentru că așa"). Spune că ești destul de sigur că nu declari un efect care nu există (eroare de tip I). Nu măsoară dacă ratezi un efect real; asta e **puterea statistică** (eroare de tip II). Cu cât ceri mai multă siguranță, cu atât ratezi mai multe efecte reale, ca observatorul de păsări care, vrând să fie 99% sigur, lasă rațele să treacă nestrigate.
2. **Eșantioanele mari strică testul.** Cu suficiente date, aproape orice diferență trece pragul. Într-un sondaj cu 12.000 de oameni, nativii din zodia Leu păreau să se uite „semnificativ" mai mult la televizor. E un artefact. Cu date mari, semnificația e un **prag minim**, nu o decizie.
3. **Corelația măsoară doar linii drepte.** O curbă de creștere în S (adopția unui brand) poate avea corelație 0,9, deși nu e liniară; alte relații perfect regulate pot avea corelație zero.

Regula lui de bază: orice rezultat trebuie întâi să **aibă sens**. Testul statistic nu poate judeca asta.

## Aplicare

- Când un raport spune „diferență semnificativă", cere și **mărimea** diferenței și întreabă ce decizie schimbă.
- În dashboard-urile digitale, cu milioane de afișări, ignoră „câștigătorii" care diferă cu zecimi de procent și nu au explicație plauzibilă.
- Înlocuiește „corelație semnificativă" cu o întrebare mai bună: ce formă are relația și cât de bine prezice pe date noi?

## Exemplu

Exemplul cu zodia Leu și televizorul e un bun test de seminar: studenții trebuie să explice de ce un rezultat semnificativ statistic poate fi absurd.

## Întrebări

- De ce sunt testele A/B pe volume foarte mari vulnerabile la „câștigători" fără importanță practică?
- Ce e mai grav pentru o campanie: să crezi într-un efect inexistent sau să ratezi unul real?

## Legături

- **vezi** [[AIM-1306]] — validarea pe date noi e alternativa robustă la testul de semnificație.
- **vezi** [[INS-1303]] — eroarea de eșantionare explodează la eșantioane mici.

## Surse

- [[SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 2
