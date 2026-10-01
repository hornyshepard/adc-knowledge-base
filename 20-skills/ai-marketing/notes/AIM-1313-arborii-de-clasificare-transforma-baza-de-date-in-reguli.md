---
id: AIM-1313
title: Arborii de clasificare transformă o bază de date în câteva reguli „dacă–atunci" pentru țintire
type: zettel
kind: method
skill: ai-marketing
also: [digital-marketing, consumer-insight]
level: 2
tags: [chaid, arbori-de-clasificare, tintire, lift, interactiuni, segmentare]
sources:
  - SRC-038 | cap. 6 (integral)
status: seed
---

# Arborii de clasificare transformă o bază de date în câteva reguli „dacă–atunci" pentru țintire

> **Ideea în o frază:** un arbore de clasificare (CHAID, CART) împarte repetat populația în grupuri tot mai diferite față de un comportament-țintă și produce reguli simple care descoperă combinații de factori la care nu te-ai fi gândit.

## Explicație

Arborele pornește de la întreaga bază de date și caută variabila care o împarte cel mai bine în grupuri cu niveluri diferite ale comportamentului urmărit. Apoi reîmparte fiecare grup și tot așa, până la un prag de semnificație sau la o mărime minimă de grup. Struhl numește câteva calități:

- **Interacțiuni vizibile**: arată când doi factori împreună produc mai mult decât fiecare separat (CHAID = *chi-squared automatic interaction detector*).
- **Recodare optimă** (*optimal recoding*): găsește singur cum să grupeze categoriile; testarea e atât de sofisticată încât a fost prezentată prima dată la o conferință de AI.
- **Reguli simple**, ușor de programat într-o bază de date: „DACĂ suburbie ȘI 5+ copii ATUNCI 27,5% cumpără".
- **Analiza de câștig** (*gains / lift chart*): ordonează grupurile după concentrația de cumpărători și ajută la alegerea pragului de țintire.

Limita: arborele e un **algoritm lacom** (*greedy*). Alege la fiecare pas varianta cea mai bună local, iar mici variații în date pot produce arbori foarte diferiți. Recomandarea lui Struhl: lasă programul să crească arborele, apoi verifică și ghidează-l după ce e util strategic.

## Aplicare

- Folosește arborele ca să găsești **cui** să-i vorbești și ce combinații de trăsături definesc un segment. Apoi testează **ce** să-i spui cu metodele de trade-off.
- Cere regulile finale, nu doar „acuratețea": un model ușor de explicat clientului valorează mai mult decât un punct în plus la scor.

## Exemplu

**SoggyOs vs. Kardboard Krunchies** (nume fictive): din datele de casă ale unui lanț, arborele a arătat că 28% dintre familiile din suburbii cu cinci sau mai mulți copii cumpără concurentul, de trei ori mai mult decât familiile suburbane cu 1–3 copii. Insight-ul a dus la un ambalaj „economic" uriaș. La o companie de croaziere de lux (rată de bază 0,6%), 15 reguli cu doar 10 variabile au clasificat peste 340.000 de oameni. Primele 11 grupuri cuprindeau 20% din bază și 70% dintre cumpărători, adică o țintire de ~17,5 ori mai eficientă.

## Întrebări

- De ce un model care descrie milioane de oameni cu 10 variabile poate părea suspect clientului?
- Ce nu îți spune arborele despre mesajul care va convinge segmentul găsit?

## Legături

- **aplicare** [[AIM-1302-segmentele-construite-cu-ai-sunt-dinamice|AIM-1302]] — arborele e un instrument concret de micro-segmentare.
- **vezi** [[AIM-1314-precizie-sau-transparenta-ansamblurile-si-retelele-neuronale|AIM-1314]] — pădurile aleatorii și boosting-ul, extensiile de tip ansamblu.
- **alternativa** [[AIM-1315-retelele-bayesiene-tot-se-schimba-odata|AIM-1315]] — rețelele bayesiene văd tot tiparul, nu doar situații „dacă–atunci".

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 6

<!-- backlinks:start -->
## Backlinks

- [[AIM-1314-precizie-sau-transparenta-ansamblurile-si-retelele-neuronale|AIM-1314]] _extinde_ — Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
- [[AIM-1315-retelele-bayesiene-tot-se-schimba-odata|AIM-1315]] _alternativa_ — Rețelele bayesiene pornesc de la ideea că, atunci când schimbi o variabilă, se schimbă toate
- [[AIM-1316-ce-metoda-pentru-ce-intrebare-de-marketing|AIM-1316]] _aplicare_ — Alegi metoda de analiză după întrebarea de marketing, nu după moda tehnologică
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
