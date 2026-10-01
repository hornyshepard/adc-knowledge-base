---
id: AIM-010
title: Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
type: zettel
kind: debate
skill: ai-marketing
also: [consumer-insight, client-business]
level: 3
tags: [cutie-neagra, explicabilitate, ansambluri, random-forests, retele-neuronale, control-uman]
sources:
  - SRC-038 | cap. 6 (Random forests, Boosted decision stumps); cap. 8 (Now about neural networks, Thinking about thinking)
status: growing
---

# Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică

> **Ideea în o frază:** cu cât un model AI e mai opac, cu atât e mai greu de verificat dacă face o treabă bună sau doar una mediocră; Struhl preferă deschis metodele pe care le poți confrunta cu bunul-simț.

## Explicație

O descoperire-cheie a învățării automate, explică Struhl, e că **media multor modele slabe bate de obicei orice model individual**. Așa funcționează **ansamblurile** (*ensembles*): pădurile aleatorii (*random forests*) rulează sute de arbori, schimbând aleator oamenii și variabilele, apoi îi pun să „voteze". *Boosting-ul* reia modelul insistând pe cazurile greșit clasificate. Prețul e opacitatea: nu poți vedea ce au făcut 500 de arbori. În cazul croazierelor, Struhl a folosit pădurea doar pentru a alege variabilele sigure, apoi a construit **un singur arbore** care putea fi citit și aplicat.

Rețelele neuronale, „viitorul AI" în presă, sunt cazul extrem. În testul autorului (1.800 de cazuri, 70 de variabile), rețeaua a produs o diagramă de neînțeles și coeficienți cu semne aparent inversate. A prezis mai prost decât celelalte metode și a supra-ajustat datele. Struhl admite că pot străluci cu volume uriașe și antrenament îndelungat, dar ridică o întrebare incomodă: o mașină autonomă proastă se vede imediat, pentru că se lovește. Cum îți dai seama că un sistem automat de recomandări face doar o treabă medie?

## Tensiunea

Poziția opusă o susțin explicit Kotler, Kartajaya și Setiawan: un model de neînțeles e „un lucru bun", pentru că nu mai e limitat de prejudecățile marketerului ([[AIM-006-analiza-predictiva-estimeaza-cine-va-cumpara-ce-se-va-vinde|AIM-006]]).

| Poziția „precizie" (Kotler 5.0) | Poziția „transparență" (Struhl) |
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

- **extinde** [[AIM-009-arborii-de-clasificare-transforma-o-baza-de-date-in-cateva|AIM-009]] — ansamblurile pornesc de la arborii de clasificare.
- **contrazice** [[AIM-006-analiza-predictiva-estimeaza-cine-va-cumpara-ce-se-va-vinde|AIM-006]] — Marketing 5.0 vede opacitatea „cutiei negre" ca pe un avantaj.
- **vezi** [[AIM-030-etica-datelor-in-marketingul-cu-ai-are-patru-reguli-de-baza|AIM-030]] — explicabilitatea ca obligație etică și de reglementare.
- **vezi** [[AIM-007-validarea-pe-un-esantion-de-control-separa-tiparele-reale|AIM-007]] — supra-ajustarea, problema clasică a rețelelor neuronale.
- **vezi** [[AIM-029-poate-ai-ul-crea-identitatea-unui-brand-promisiunea-brand|AIM-029]] — aceeași întrebare, „unde rămâne omul?", aplicată creației de brand.
- **vezi** [[DIG-050-publicitatea-programatica-cumpara-fiecare-afisare-automat|DIG-050]] — publicitatea programatică face același schimb: eficiență automată contra control și transparență.

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 6 și cap. 8

<!-- backlinks:start -->
## Backlinks

- [[AIM-006-analiza-predictiva-estimeaza-cine-va-cumpara-ce-se-va-vinde|AIM-006]] _contrazice_ — Analiza predictivă estimează cine va cumpăra, ce se va vinde și ce va funcționa — un ciclu care se verifică continuu, nu un raport
- [[AIM-009-arborii-de-clasificare-transforma-o-baza-de-date-in-cateva|AIM-009]] _vezi_ — Arborii de clasificare transformă o bază de date în câteva reguli „dacă–atunci" pentru țintire
- [[AIM-032-biasul-in-marketingul-cu-ai-are-doua-surse-datele-din-care|AIM-032]] _vezi_ — Biasul în marketingul cu AI are două surse — datele din care învață modelul și încrederea oarbă a omului în recomandare
- [[MAP-003-etica-reglementare-si-responsabilitate|MAP-003]] — Etică, reglementare și responsabilitate în publicitate
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
