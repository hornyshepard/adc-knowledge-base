---
id: ADV-008
title: Testată cu date, ierarhia efectelor a ieșit într-o altă ordine decât teoria — de la „ce fac ei" la „ce fac eu"
type: zettel
kind: case
skill: advertising-strategy
also: [consumer-insight, ai-marketing, brand-strategy]
level: 3
tags: [aida, lavidge-steiner, ierarhia-efectelor, loialitate, retele-bayesiene, b2b]
sources:
  - SRC-038 | cap. 7 (Bayes Nets confirm a theoretical model, mostly; Going the next step; Letting the data speak; What next?)
status: growing
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

- **fundament** [[AIM-011-retelele-bayesiene-pornesc-de-la-ideea-ca-atunci-cand|AIM-011]] — metoda care a permis testarea.
- **contrazice** [[ADV-005-ierarhiile-de-efecte-aida-lavidge-steiner-dagmar-ordoneaza|ADV-005]] — ordinea teoretică a ierarhiilor nu s-a confirmat pe date.
- **vezi** [[HIS-010-aida-a-fost-inventata-de-copywriteri-nu-de-psihologi|HIS-010]] — modelele în trepte au pornit ca reguli de scris, nu ca descriere a deciziei.
- **vezi** [[AIM-001-metodele-de-predictie-a-alegerilor-formeaza-patru-familii|AIM-001]] — modelele teoretice ca a patra familie de metode de predicție.
- **aplicare** [[EXP-029-optimizarea-conjoint-a-serviciilor-arata-unde-supra-livrezi|EXP-029]] — pasul următor: optimizarea serviciilor identificate.

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 7

<!-- backlinks:start -->
## Backlinks

- [[ADV-005-ierarhiile-de-efecte-aida-lavidge-steiner-dagmar-ordoneaza|ADV-005]] _exemplu_ — Ierarhiile de efecte (AIDA, Lavidge-Steiner, DAGMAR) ordonează obiectivele „gândește–simte–acționează", dar ordinea lor fixă nu are suport empiric
- [[AIM-001-metodele-de-predictie-a-alegerilor-formeaza-patru-familii|AIM-001]] _vezi_ — Metodele de predicție a alegerilor formează patru familii, fiecare cu o imagine implicită despre om
- [[AIM-011-retelele-bayesiene-pornesc-de-la-ideea-ca-atunci-cand|AIM-011]] _vezi_ — Rețelele bayesiene pornesc de la ideea că, atunci când schimbi o variabilă, se schimbă toate
- [[HIS-010-aida-a-fost-inventata-de-copywriteri-nu-de-psihologi|HIS-010]] _vezi_ — AIDA a fost inventată de copywriteri, nu de psihologi — genealogia modelelor de efect
- [[MAP-002-modele-de-efect-si-customer-journey-comparate|MAP-002]] — Modelele de efect și de customer journey, comparate
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
