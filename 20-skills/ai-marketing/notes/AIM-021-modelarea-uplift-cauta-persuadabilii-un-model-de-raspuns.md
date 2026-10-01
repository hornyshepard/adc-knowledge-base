---
id: AIM-021
title: Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum
type: zettel
kind: concept
skill: ai-marketing
also: [advertising-strategy, digital-marketing, consumer-insight]
level: 3
tags: [uplift-modelling, persuadabili, atribuire, incrementalitate, obama-2012, modele-de-raspuns]
sources:
  - SRC-040 | secț. 2, cap. 3 (Moving From Level 4 to Level 5; Measuring the Right Things)
status: growing
---

# Modelarea uplift caută persuadabilii — un model de răspuns își atribuie și vânzările care ar fi venit oricum

> **Ideea în o frază:** nu contează cine e probabil să cumpere, ci pe cine schimbă mesajul tău; restul e cheltuială sau, mai rău, iritare.

## Explicație

Richards și McLean ajung la această idee explicând de ce motoarele de decizie din call center par mult mai eficiente decât campaniile outbound. Explicația lor are două părți.

**1. Contextul, nu doar predicția.** Clientul care sună e deja implicat; e „la baza pâlniei". Măsurat izolat, motorul de decizie primește toată gloria vânzării, deși drumul până acolo a fost pregătit de multe alte comunicări. A copia modelul în campaniile outbound nu dă aceleași rezultate, pentru că omul e în alt punct al călătoriei.

**2. Tipul de model.** Un **model de răspuns** estimează cine va spune „da". Un **model uplift** estimează pe cine îl *schimbă* contactul. Orice grup se împarte în:

| Grup | Ce face contactul |
|---|---|
| Deja decis să cumpere | nimic; ar fi cumpărat oricum, dar modelul de răspuns îl numără ca succes |
| Hotărât să nu cumpere | nimic |
| Iritat de contact | efect negativ; trebuie lăsat în pace |
| **Persuadabil** | aici e singurul efect real al campaniei |

Exemplul cărții e campania de realegere a lui Barack Obama (2012). Analiștii au construit și testat modele care identificau alegătorii înclinați spre Mitt Romney, dar receptivi la mesajul lui Obama în statele indecise. Modelele au ghidat cumpărările de TV și online, ușile la care băteau voluntarii, apelurile și scrisorile.

Autorii notează și compromisurile: **costul pe conversie crește** (pentru că „sigurii" nu mai sunt numărați), iar munca analitică e mai scumpă. Câștigul: aceleași rezultate cu mai puțină comunicare outbound. Recomandarea lor mai largă: măsoară **angajamentul**, nu doar răspunsul. Caută oamenii care vor cumpăra *doar dacă* primesc încă o bucată de conținut potrivită.

## Aplicare

- Când un raport spune „campania a generat X vânzări", întreabă: câte ar fi apărut fără campanie? Cere un grup de control.
- Exclude din campaniile de retenție sau reduceri clienții care ar rămâne oricum; nu le dai bani degeaba.
- Identifică segmentul „nu deranja" (oameni pe care contactul îi enervează) și scoate-l din liste.

## Exemplu

Pe același principiu, Noil (SRC-037) propune o reducere celor cu „risc de churn". Fără logica uplift, o parte din reduceri ajunge la oameni care oricum nu plecau.

## Întrebări

- De ce un model care „prezice bine" poate fi inutil pentru decizia de a contacta pe cineva?
- Cum ai aplica ideea persuadabililor la planificarea media pentru o campanie de brand?

## Legături

- **contrazice** [[AIM-006-analiza-predictiva-estimeaza-cine-va-cumpara-ce-se-va-vinde|AIM-006]] — utilizările-tip ale analizei predictive ignoră incrementalitatea.
- **vezi** [[AIM-020-o2-vision-motorul-de-decizie-a-dus-conversia-de-la-sub-2-la|AIM-020]] — rezultatele O2, citite prin această lentilă.
- **vezi** [[AIM-014-cota-de-preferinta-nu-e-cota-de-piata-prognoza-trebuie|AIM-014]] — altă capcană: confuzia dintre preferință și piață.
- **vezi** [[INS-081-efectul-unei-reclame-se-dovedeste-prin-experiment-nu-prin|INS-081]] — Fennis & Stroebe: efectul se dovedește doar cu grup de control.
- **vezi** [[DIG-077-modelul-de-atribuire-decide-ce-canal-primeste-meritul|DIG-077]] — modelele de atribuire împart meritul, dar nu arată ce ar fi venit oricum.

## Surse

- [[SRC-040-intelligent-customer-engagement|SRC-040]] Aly Richards & Scott McLean, *Intelligent Customer Engagement*, secț. 2, cap. 3

<!-- backlinks:start -->
## Backlinks

- [[ADV-047-un-big-idea-nu-ajunge-fara-un-long-idea-publicul-trebuie|ADV-047]] _vezi_ — Un Big Idea nu ajunge fără un „Long Idea" — publicul trebuie așteptat la pasul următor (Volvo Trucks, „Epic Split")
- [[AIM-006-analiza-predictiva-estimeaza-cine-va-cumpara-ce-se-va-vinde|AIM-006]] _vezi_ — Analiza predictivă estimează cine va cumpăra, ce se va vinde și ce va funcționa — un ciclu care se verifică continuu, nu un raport
- [[AIM-019-ofera-ce-e-mai-probabil-sa-accepte-clientul-nu-ce-aduce|AIM-019]] _vezi_ — Oferă ce e mai probabil să accepte clientul, nu ce aduce marja cea mai mare — un „da" aduce alt „da"
- [[AIM-020-o2-vision-motorul-de-decizie-a-dus-conversia-de-la-sub-2-la|AIM-020]] _vezi_ — O2 Vision — motorul de decizie a dus conversia de la sub 2% la peste 70%, apoi a venit oboseala audienței
- [[DIG-077-modelul-de-atribuire-decide-ce-canal-primeste-meritul|DIG-077]] _alternativa_ — Modelul de atribuire decide ce canal primește meritul conversiei — iar după cookie-uri urmărirea devine incertă și etapele de început ies dezavantajate
- [[SRC-040-intelligent-customer-engagement|SRC-040]] — Intelligent Customer Engagement: The Future of Content Marketing
<!-- backlinks:end -->
