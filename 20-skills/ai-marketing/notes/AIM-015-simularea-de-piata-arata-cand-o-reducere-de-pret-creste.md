---
id: AIM-015
title: Simularea de piață arată când o reducere de preț crește cota, dar scade veniturile
type: zettel
kind: case
skill: ai-marketing
also: [marketing-fundamentals, client-business]
level: 2
tags: [simulator-de-piata, pret, razboi-al-preturilor, alegere-discreta, curba-s]
sources:
  - SRC-038 | cap. 4 (Market simulations, Case study: The power of simulations – mobile phone towers, The price is right, Utility and share)
status: growing
---

# Simularea de piață arată când o reducere de preț crește cota, dar scade veniturile

> **Ideea în o frază:** un simulator construit dintr-un studiu de alegere discretă îți permite să joci mutarea ta și răspunsul concurenței înainte de a le face în piață.

## Explicație

Rezultatul cel mai valoros al unui studiu de alegere discretă, spune Struhl, este **simulatorul de piață**: un fișier Excel cu controale pentru caracteristicile și prețurile fiecărui produs. Se schimbă o setare și se vede imediat cum se mută cotele de preferință. Un simulator bun are:

- un **scenariu de referință** (piața de azi), cu care se compară orice modificare;
- controale de ajustare pentru notorietate și distribuție;
- pe lângă cotă, **veniturile** (de exemplu la 100 de vânzări), pentru că cota maximă nu e întotdeauna profitul maxim.

Referința e necesară pentru că utilitatea nu se transformă liniar în cotă. Relația are forma unei **curbe în S**: un brand mic trebuie să adune multă valoare ca să iasă din zgomot; în zona de mijloc, mici îmbunătățiri mută mult; la cote foarte mari, convertești greu clienții fideli altor branduri. Același câștig de utilitate are efecte diferite în funcție de punctul de plecare. Curba e apropiată de cea din teoria perspectivei (Kahneman).

Struhl adaugă reguli de preț: patru niveluri de preț ajung pentru aproape orice formă a curbei preț-cotă. Nu extrapola dincolo de prețurile testate, pentru că poate exista un „cot" sau un **preț de rezervă**, peste care vânzările se prăbușesc.

## Aplicare

- Când clientul vrea să scadă prețul „ca să ia cotă", cere scenariul în care concurenții răspund la fel.
- Prezintă rezultatele în limbajul deciziei. Un director din carte a cerut, iritat, nu elasticități, ci câte vânzări pierde dacă urcă prețul cu un dolar.
- Folosește simulatorul în ateliere cu clientul: e un instrument de dialog strategic, nu doar un raport.

## Exemplu

**Turnurile de telefonie mobilă (Ace T&T).** Liderul pieței, cu 38% cotă la prețul mediu de 68.000 $, a simulat o scădere la 52.000 $. Singur, ar fi urcat la 46%, dar cu venituri puțin mai mici. Dacă și concurenții urmau, ajungea înapoi la ~39%, cu venituri cu ~22% mai mici. Doar cel mai mic jucător ar fi ieșit aproape nevătămat. Conducerea a ordonat **încuierea rapoartelor**, de teama unei scurgeri. O creștere de preț făcută doar de Ace aducea un mic câștig de venit.

## Întrebări

- De ce cota de piață e un obiectiv înșelător pentru un lider?
- Ce limită are simulatorul dacă piața se schimbă radical după studiu?

## Legături

- **fundament** [[AIM-012-metodele-de-trade-off-alegere-discreta-conjoint-maxdiff-q|AIM-012]] — alegerea discretă e metoda din spatele simulatorului.
- **vezi** [[AIM-014-cota-de-preferinta-nu-e-cota-de-piata-prognoza-trebuie|AIM-014]] — simulatorul dă cotă de preferință, care trebuie ajustată.
- **vezi** [[BRD-060-in-modelele-de-alegere-brandul-e-un-container-de-atribute|BRD-060]] — brandul apare în model ca valoare reziduală.
- **vezi** [[MKT-024-pretul-este-sacrificiul-total-al-clientului-si-se-fixeaza|MKT-024]] — prețul se fixează și după concurență, exact ce simulează scenariul „răspund și ceilalți".

## Surse

- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] Steven Struhl, *Artificial Intelligence Marketing and Predicting Consumer Choice*, cap. 4

<!-- backlinks:start -->
## Backlinks

- [[AIM-012-metodele-de-trade-off-alegere-discreta-conjoint-maxdiff-q|AIM-012]] _vezi_ — Metodele de trade-off — alegere discretă, conjoint, MaxDiff, Q-Sort — răspund la întrebări diferite
- [[AIM-014-cota-de-preferinta-nu-e-cota-de-piata-prognoza-trebuie|AIM-014]] _vezi_ — Cota de preferință nu e cotă de piață — prognoza trebuie ajustată pentru notorietate, înțelegere și distribuție
- [[BRD-060-in-modelele-de-alegere-brandul-e-un-container-de-atribute|BRD-060]] _vezi_ — În modelele de alegere, brandul e un „container" de atribute, iar valoarea lui se vede în ce rămâne după atribute
- [[MKT-024-pretul-este-sacrificiul-total-al-clientului-si-se-fixeaza|MKT-024]] _vezi_ — Prețul este sacrificiul total al clientului și se fixează prin cele 5C — obiective, clienți, costuri, concurență, canal
- [[SRC-038-artificial-intelligence-marketing-and-predicting-consumer-choice|SRC-038]] — Artificial Intelligence Marketing and Predicting Consumer Choice: An Overview of Tools and Techniques
<!-- backlinks:end -->
