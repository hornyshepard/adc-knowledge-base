---
id: AIM-012
title: Metodele de trade-off — alegere discretă, conjoint, MaxDiff, Q-Sort — răspund la întrebări diferite
type: zettel
kind: framework
skill: ai-marketing
also: [consumer-insight, marketing-fundamentals]
level: 2
tags: [alegere-discreta, conjoint, maxdiff, q-sort, experiment, hierarchical-bayes]
sources:
  - SRC-038 | cap. 3 (integral); cap. 4 (The Bayesian advantage); cap. 8 (Finding what is most valuable in a list)
status: growing
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

- **fundament** [[INS-078-intrebati-direct-ce-conteaza-oamenii-spun-totul-ratingurile|INS-078]] — eșecul ratingurilor directe e motivul existenței acestor metode.
- **vezi** [[AIM-015-simularea-de-piata-arata-cand-o-reducere-de-pret-creste|AIM-015]] — alegerea discretă și simulatorul de piață în acțiune.
- **vezi** [[AIM-013-un-studiu-de-alegere-bun-se-construieste-inainte-de|AIM-013]] — regulile practice pentru un studiu de alegere bine construit.
- **vezi** [[ADV-080-elementele-unei-reclame-se-pot-testa-ca-un-experiment|ADV-080]] — conjoint-ul aplicat mesajelor publicitare.
- **vezi** [[BRD-060-in-modelele-de-alegere-brandul-e-un-container-de-atribute|BRD-060]] — în aceleași modele, valoarea brandului apare ca diferență rămasă după atribute.
- **vezi** [[EXP-029-optimizarea-conjoint-a-serviciilor-arata-unde-supra-livrezi|EXP-029]] — conjoint-ul aplicat pachetului de servicii.

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 3, 4 și 8

<!-- backlinks:start -->
## Backlinks

- [[ADV-080-elementele-unei-reclame-se-pot-testa-ca-un-experiment|ADV-080]] _fundament_ — Elementele unei reclame se pot testa ca un experiment — conjoint-ul de mesaj bate testul A/B
- [[AIM-001-metodele-de-predictie-a-alegerilor-formeaza-patru-familii|AIM-001]] _vezi_ — Metodele de predicție a alegerilor formează patru familii, fiecare cu o imagine implicită despre om
- [[AIM-008-alegi-metoda-de-analiza-dupa-intrebarea-de-marketing-nu|AIM-008]] _vezi_ — Alegi metoda de analiză după întrebarea de marketing, nu după moda tehnologică
- [[AIM-013-un-studiu-de-alegere-bun-se-construieste-inainte-de|AIM-013]] _fundament_ — Un studiu de alegere bun se construiește înainte de chestionar — checklist în zece puncte
- [[AIM-014-cota-de-preferinta-nu-e-cota-de-piata-prognoza-trebuie|AIM-014]] _fundament_ — Cota de preferință nu e cotă de piață — prognoza trebuie ajustată pentru notorietate, înțelegere și distribuție
- [[AIM-015-simularea-de-piata-arata-cand-o-reducere-de-pret-creste|AIM-015]] _fundament_ — Simularea de piață arată când o reducere de preț crește cota, dar scade veniturile
- [[BRD-059-brandul-este-un-activ-nu-o-cheltuiala-iar-puterea-lui-nu-e|BRD-059]] _vezi_ — Brandul este un activ, nu o cheltuială, iar puterea lui nu e performanța lui
- [[BRD-060-in-modelele-de-alegere-brandul-e-un-container-de-atribute|BRD-060]] _fundament_ — În modelele de alegere, brandul e un „container" de atribute, iar valoarea lui se vede în ce rămâne după atribute
- [[EXP-029-optimizarea-conjoint-a-serviciilor-arata-unde-supra-livrezi|EXP-029]] _vezi_ — Optimizarea conjoint a serviciilor arată unde supra-livrezi și unde sub-livrezi
- [[INS-078-intrebati-direct-ce-conteaza-oamenii-spun-totul-ratingurile|INS-078]] _extinde_ — Întrebați direct ce contează, oamenii spun „totul" — ratingurile de importanță nu prezic comportamentul
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
