---
id: AIM-1314
title: Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
type: zettel
kind: debate
skill: ai-marketing
also: [consumer-insight, client-business]
level: 3
tags: [cutie-neagra, explicabilitate, ansambluri, random-forests, retele-neuronale, control-uman]
sources:
  - SRC-038 | cap. 6 (Random forests, Boosted decision stumps); cap. 8 (Now about neural networks, Thinking about thinking)
status: seed
---

# Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică

> **Ideea în o frază:** cu cât un model AI e mai opac, cu atât e mai greu de verificat dacă face o treabă bună sau doar una mediocră; Struhl preferă deschis metodele pe care le poți confrunta cu bunul-simț.

## Explicație

O descoperire-cheie a învățării automate, explică Struhl, e că **media multor modele slabe bate de obicei orice model individual**. Așa funcționează **ansamblurile** (*ensembles*): pădurile aleatorii (*random forests*) rulează sute de arbori, schimbând aleator oamenii și variabilele, apoi îi pun să „voteze". *Boosting-ul* reia modelul insistând pe cazurile greșit clasificate. Prețul e opacitatea: nu poți vedea ce au făcut 500 de arbori. În cazul croazierelor, Struhl a folosit pădurea doar pentru a alege variabilele sigure, apoi a construit **un singur arbore** care putea fi citit și aplicat.

Rețelele neuronale, „viitorul AI" în presă, sunt cazul extrem. În testul autorului (1.800 de cazuri, 70 de variabile), rețeaua a produs o diagramă de neînțeles și coeficienți cu semne aparent inversate. A prezis mai prost decât celelalte metode și a supra-ajustat datele. Struhl admite că pot străluci cu volume uriașe și antrenament îndelungat, dar ridică o întrebare incomodă: o mașină autonomă proastă se vede imediat, pentru că se lovește. Cum îți dai seama că un sistem automat de recomandări face doar o treabă medie?

## Tensiunea

| Poziția „precizie" | Poziția „transparență" (Struhl) |
|---|---|
| contează doar cât de bine prezice | trebuie să poți verifica dacă modelul are sens |
| modelele complexe captează tipare fine | modelele opace ascund erori de bază |
| automatizarea eliberează oamenii | trebuie să decizi explicit unde cedezi controlul mașinii și furnizorului |

## Aplicare

- Când un furnizor vinde o „cutie neagră", cere validare pe date noi și o explicație a principalelor variabile.
- Folosește modelele opace pentru selecție și explorare, apoi modele explicabile pentru decizie și pentru prezentarea către client.
- Ține minte concluzia autorului: nicio analiză de tranzacții nu-ți dă o idee nouă de produs.

## Exemplu

Psoriazis și depresie: un arbore simplu, aplicabil cu creionul pe hârtie de orice medic, a fost completat de boosting, care a evidențiat două praguri (10% și 20% din suprafața corpului afectată). Ansamblul a servit modelului transparent, nu l-a înlocuit.

## Întrebări

- Ar accepta un director de marketing o recomandare de buget pe care nimeni nu o poate explica?
- Cum se schimbă dezbaterea în era modelelor generative?

## Legături

- **extinde** [[AIM-1313]] — ansamblurile pornesc de la arborii de clasificare.
- **vezi** [[AIM-1305]] — explicabilitatea ca obligație etică și de reglementare.
- **vezi** [[AIM-1306]] — supra-ajustarea, problema clasică a rețelelor neuronale.
- **vezi** [[AIM-1326]] — aceeași întrebare, „unde rămâne omul?", aplicată creației de brand.

## Surse

- [[SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 6 și cap. 8
