---
id: ADV-1302
title: Testată cu date, ierarhia efectelor a ieșit într-o altă ordine decât teoria — de la „ce fac ei" la „ce fac eu"
type: zettel
kind: case
skill: advertising-strategy
also: [consumer-insight, ai-marketing, brand-strategy]
level: 3
tags: [aida, lavidge-steiner, ierarhia-efectelor, loialitate, retele-bayesiene, b2b]
sources:
  - SRC-038 | cap. 7 (Bayes Nets confirm a theoretical model, mostly; Going the next step; Letting the data speak; What next?)
status: seed
---

# Testată cu date, ierarhia efectelor a ieșit într-o altă ordine decât teoria — de la „ce fac ei" la „ce fac eu"

> **Ideea în o frază:** modelele în trepte (AIDA, Lavidge-Steiner) sunt utile ca ipoteze; când le lași să fie verificate de date, secvența reală poate fi alta, iar asta schimbă ce măsori și ce comunici.

## Explicație

Struhl amintește că modelele ierarhice domină gândirea despre publicitate: **AIDA** (Attention, Interest, Desire, Action), atribuit lui E. St Elmo Lewis (1898), și modelul în șase trepte al lui **Lavidge și Steiner** (1961), de la notorietate la cumpărare, urcat ca pe o scară. Multe sisteme de măsurare (urmărirea notorietății, apoi a preferinței) presupun implicit o astfel de ierarhie. Mult timp, ierarhiile au rezistat și din motive tehnice: regresia nu putea lega ratingurile de vânzări, pentru că relațiile nu sunt liniare.

Cazul: o firmă de servicii pentru brokeri comerciali avea un model teoretic construit manual. Acțiunile firmei alcătuiau „satisfacția", sentimentele clientului alcătuiau „relația", amândouă duceau la „loialitate", iar loialitatea la cota de afaceri. Modelul (o regresie PLS) prezicea cota cu doar **18%** acuratețe. O rețea bayesiană lăsată să învețe din aceleași date a găsit o ierarhie diferită, cu **62%** predicție corectă validată:

**Ce fac ei (obiectiv) → Cum mă tratează → Ce simt → Ce fac eu → Cota**

Deci acțiunile nu lucrează separat de relație. Felul în care clientul *percepe* acțiunile îi formează sentimentele, iar sentimentele îi explică comportamentul.

## Aplicare

- Tratează orice model de efecte din manual ca pe o **ipoteză de testat** pe datele clientului, nu ca pe o lege.
- În strategia de comunicare B2B, lucrează pe veriga „cum mă tratează". Acțiunile operaționale contează prin felul în care sunt trăite.
- Leagă măsurătorile de brand de comportament real (cotă, share of wallet), nu doar de alte ratinguri.

## Exemplu

Din aceeași analiză au ieșit acțiuni concrete importante: persoană de contact desemnată pe tot parcursul relației, comunicare la actualizări, sistem de meniu vocal, o persoană dedicată rezolvării problemelor. Clientul a testat apoi *cum* să le îmbunătățească printr-un conjoint de servicii.

## Întrebări

- Ce ar însemna această ierarhie pentru un brand de consum, nu B2B?
- Dacă oamenii acționează adesea fără să treacă prin etape, mai e AIDA util la seminar? Pentru ce?

## Legături

- **fundament** [[AIM-1315]] — metoda care a permis testarea.
- **vezi** [[AIM-1307]] — modelele teoretice ca a patra familie de metode.
- **aplicare** [[EXP-1301]] — pasul următor: optimizarea serviciilor identificate.

## Surse

- [[SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 7
