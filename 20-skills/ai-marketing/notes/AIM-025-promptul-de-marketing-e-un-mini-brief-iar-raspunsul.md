---
id: AIM-025
title: Promptul de marketing e un mini-brief, iar răspunsul modelului e o ciornă, nu un livrabil
type: zettel
kind: method
skill: ai-marketing
also: [copywriting, creative-brief, art-direction]
level: 1
tags: [prompting, ai-generativ, chatgpt, midjourney, brief, ciorna, variante, curatorie]
sources:
  - SRC-039 | cap. 1 (Real-World Use Cases, p. 10–14); cap. 2 (Tailoring Content for Target Audiences, Conducting A/B Testing for Messaging, p. 26–27); cap. 4 (Case Studies, p. 80–81; Demystifying Analytics, p. 94)
  - SRC-025 | cap. 6 „The North Star" (cazul Jardim Sonoro „Blended with Nature")
status: growing
---

# Promptul de marketing e un mini-brief, iar răspunsul modelului e o ciornă, nu un livrabil

> **Ideea în o frază:** un prompt bun pentru o sarcină de marketing conține aceleași elemente ca un brief (scop, conținut, public, ton, exemple), iar ce iese trebuie revizuit, ales și adaptat de un om.

## Explicație

Biblioteca e săracă la acest capitol, și merită spus deschis: singura carte despre ChatGPT (Najafov) nu propune o metodă de prompting, ci doar cinci scenarii simple. Toate au însă aceeași structură în trei pași: **prompt inițial → revizuire și editare → utilizare**. Din exemplele lui se pot extrage elementele unui prompt de marketing:

| Element | Exemplul din carte |
|---|---|
| **Scopul** comunicării | e-mail care anunță o întârziere a livrării |
| **Punctele-cheie** | scuze + promisiunea unei livrări accelerate |
| **Detaliile de produs** | sticlă eco din materiale reciclate, ține rece 24 de ore |
| **Formatul și numărul de variante** | „o serie de trei postări" |
| **Publicul și tonul** | blog tech despre AI; ton specificat pentru social |
| **Exemple din conținutul existent** | articole vechi date modelului, pentru că primele ciorne nu aveau tonul brandului |

Autorul mai recomandă variante multiple pentru teste A/B și întrebări analitice în limbaj natural, cu rezervele din [[AIM-027-un-model-de-limbaj-rezuma-bine-text-dar-nu-dovedeste-cauze|AIM-027]].

Un caz din *Shareworthy* arată cum arată promptul într-o echipă creativă. Pentru festivalul Jardim Sonoro, Dentsu Creative Portugal a dat programului Midjourney numele artiștilor din program și cuvinte precum păsări, fluturi, frunze, copaci. Echipa a rafinat apoi rezultatele. Ingredientele promptului veneau din conceptul „Blended with Nature", iar în credite apare un „A.I. prompt master", alături de art directori și copywriter. Promptul e deci o meserie în echipă, nu un substitut pentru idee.

## Aplicare

- Scrie promptul ca pe un brief scurt: *ce* (sarcina și formatul), *pentru cine*, *de ce* (obiectiv), *ce trebuie să conțină* (fapte, beneficii), *cum să sune* (ton, exemple aprobate).
- Pune în prompt cuvintele conceptului, nu doar descrierea produsului. Ideea vine înaintea promptului.
- Cere mai multe variante, apoi selectează și combină. Verifică faptele: modelul poate inventa caracteristici de produs.

## Exemplu

Postările generate în carte pentru sticla eco sunt corecte, dar previzibile: emoji, hashtaguri generice („#EcoFriendly"), beneficii listate. Sunt o ciornă care are nevoie de o idee și de vocea brandului ca să devină comunicare.

## Întrebări

- Ce element al unui brief creativ (insight-ul, propoziția unică) lipsește din aproape toate exemplele de prompt din carte?
- Când e mai rapid să scrii textul singur decât să corectezi o ciornă generată?

## Legături

- **fundament** [[BRF-016-brief-ul-get-to-by-pune-toata-strategia-intr-o-fraza-cu|BRF-016]] — Get/To/By, scheletul cel mai scurt al unui brief, deci și al unui prompt.
- **vezi** [[CPY-029-vocea-brandului-nu-se-obtine-din-prompt-ci-dintr-un-ciclu|CPY-029]] — ciclul de supraveghere umană a vocii, care urmează după prompt.
- **vezi** [[AIM-027-un-model-de-limbaj-rezuma-bine-text-dar-nu-dovedeste-cauze|AIM-027]] — limita întrebărilor analitice „și de ce?" adresate modelului.
- **vezi** [[AIM-026-in-campaniile-premiate-cu-ai-ideea-vine-din-insight-ul-uman|AIM-026]] — cazurile premiate în care AI-ul execută o idee formulată de oameni.
- **vezi** [[AIM-024-ipoteza-o-formuleaza-omul-ai-ul-o-ruleaza-omul-o|AIM-024]] — împărțirea muncii om–AI în testare și generare de lead-uri.

## Surse

- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, cap. 1, p. 10–14; cap. 2, p. 26–27; cap. 4, p. 80–81, 94
- [[SRC-025-shareworthy|SRC-025]] Robin Landa, *Shareworthy*, cap. 6 „The North Star" (Jardim Sonoro, Dentsu Creative Portugal)

<!-- backlinks:start -->
## Backlinks

- [[AIM-026-in-campaniile-premiate-cu-ai-ideea-vine-din-insight-ul-uman|AIM-026]] _vezi_ — În campaniile premiate cu AI, ideea vine din insight-ul uman, iar AI-ul îi dă scară — Cadbury, Nike „Never Done Evolving", Jardim Sonoro
- [[AIM-027-un-model-de-limbaj-rezuma-bine-text-dar-nu-dovedeste-cauze|AIM-027]] _vezi_ — Un model de limbaj rezumă bine text, dar nu dovedește cauze — „de ce a crescut conversia?" nu e o întrebare pentru chatbot
- [[BRF-001-brief-ul-creativ-este-planul-de-arhitect-al-executiei-harta|BRF-001]] _vezi_ — Brief-ul creativ este planul de arhitect al execuției — hartă pentru creație și criteriu de evaluare
- [[CPY-029-vocea-brandului-nu-se-obtine-din-prompt-ci-dintr-un-ciclu|CPY-029]] _fundament_ — Vocea brandului nu se obține din prompt, ci dintr-un ciclu exemple → ciornă → editare umană → feedback → control final
- [[SRC-039-chatgpt-for-marketing|SRC-039]] — ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
