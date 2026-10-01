---
id: AIM-1324
title: Oferă ce e mai probabil să accepte clientul, nu ce aduce marja cea mai mare — un „da" aduce alt „da"
type: zettel
kind: principle
skill: ai-marketing
also: [digital-marketing, client-business]
level: 2
tags: [decision-engine, next-best-action, propensitate, arbitraj, strategie-de-contact, interest-cloud]
sources:
  - SRC-040 | secț. 4, cap. 4 (Decision Engines – What They Do, arbitration, Technology Notes); cap. 2 (Contact Strategy); cap. 3 (Engagement Decision Engine – Build Persona Interest Clouds)
status: seed
---

# Oferă ce e mai probabil să accepte clientul, nu ce aduce marja cea mai mare — un „da" aduce alt „da"

> **Ideea în o frază:** în deciziile automate despre ce ofertă să faci, regula „cea mai mare marjă" pierde pe termen lung în fața regulii „cea mai mare probabilitate de acceptare".

## Explicație

Richards și McLean explică pas cu pas anatomia unui **motor de decizie** din call center, folosind exemplul unei bănci:

1. **Modele de propensitate**: câte un model pentru fiecare produs estimează probabilitatea de cumpărare.
2. **Acțiuni pe segmente de propensitate**: de exemplu, oferta se face doar peste 70%. Un client cu propensitate mică ar avea nevoie de un stimulent.
3. **Reguli de eligibilitate**, verificate primele: înainte de un credit ipotecar rulezi verificarea de credit, ca să nu vinzi ceva ce omul nu poate primi.
4. **Arbitraj** între produse: de exemplu „propensitate × marjă", eventual împărțit la timpul de vânzare.
5. **Comutator de prioritate**: când coada de apeluri e lungă, câștigă produsele rapide.

După fiecare răspuns al clientului, motorul rulează din nou și propune următoarea cea mai bună acțiune (*next-best-action*).

Observația contraintuitivă vine din proiectele autorilor:

| | Produs A | Produs B |
|---|---|---|
| Propensitate | 55% | 85% |
| Marjă | 100 £ | 50 £ |

Cu regula de marjă, motorul oferă A, la care omul spune mai des „nu". Fără ea, oferă B. Rezultatul: mai multe oferte acceptate și, mai ales, **primul „da" crește probabilitatea unui al doilea**. Pe termen lung, câștigi mai mult.

Două idei complementare din carte:

- **Strategia de contact**: reguli care împiedică suprasolicitarea (de exemplu, minimum șase săptămâni între apelurile pentru asigurări, doar miercuri seara între 19:00 și 20:30). Strategul de audiență trebuie să aibă autoritate în fața managerilor de produs.
- **„Norii de interes"**: conținutul e etichetat automat (NLP), iar interesul unui om pentru un subiect crește când revine la el și scade când nu mai revine. E o anticipare a recomandărilor de conținut de azi.

## Aplicare

- În briefurile de CRM, cere explicit regula de arbitraj și pune la îndoială optimizarea pe marjă imediată.
- Propune o strategie de contact scrisă, cu frecvențe maxime pe canal, înainte de orice program automatizat.
- Pentru copywriter: scenariile de next-best-action au nevoie de texte scurte, modulare, pentru fiecare ofertă și fiecare răspuns posibil.

## Exemplu

Secvența din carte: clientul sună pentru o asigurare de clădire (o cumpără), apoi i se propune asigurarea bunurilor (refuză), apoi un card de credit. Fiecare ofertă e recalculată după răspunsul anterior.

## Întrebări

- Ce se întâmplă cu încrederea clientului dacă simte că fiecare apel devine o vânzare?
- E regula „un da aduce alt da" valabilă și în e-commerce, nu doar în call center?

## Legături

- **fundament** [[AIM-1321-modelul-de-maturitate-ice-zece-principii-cinci-niveluri|AIM-1321]] — motorul de decizie definește nivelul 4 de maturitate.
- **vezi** [[DIG-1301-ai-in-e-mail-moment-si-frecventa-pe-individ|DIG-1301]] — optimizarea frecvenței, rudă cu strategia de contact.
- **vezi** [[AIM-1323-modelarea-uplift-cauta-persuadabilii|AIM-1323]] — tipul de model contează la fel de mult ca regulile.

## Surse

- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, secț. 4, cap. 2, 3 și 4

<!-- backlinks:start -->
## Backlinks

- [[AIM-1321-modelul-de-maturitate-ice-zece-principii-cinci-niveluri|AIM-1321]] _extinde_ — Modelul de maturitate ICE — zece principii și cinci niveluri, de la tranzacție la angajament inteligent
- [[DIG-1301-ai-in-e-mail-moment-si-frecventa-pe-individ|DIG-1301]] _vezi_ — În e-mailul cu AI, momentul și frecvența trimiterii se optimizează pe individ, nu pe listă
- [[SRC-040-intelligent-customer-engagement|SRC-040]] — Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
