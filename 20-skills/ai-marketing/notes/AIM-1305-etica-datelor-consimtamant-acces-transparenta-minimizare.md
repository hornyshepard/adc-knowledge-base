---
id: AIM-1305
title: Etica datelor în marketingul cu AI are patru reguli de bază — consimțământ, acces și ștergere, transparență, minimizare
type: zettel
kind: checklist
skill: ai-marketing
also: [digital-marketing, brand-strategy]
level: 1
tags: [etica, gdpr, confidentialitate, explicabilitate, responsabilitate]
sources:
  - SRC-037 | cap. 12 (12.1-12.5)
  - SRC-039 | cap. 3 (Privacy-by-Design Principles for Personalized Marketing, p. 73–74)
status: seed
---

# Etica datelor în marketingul cu AI are patru reguli de bază — consimțământ, acces și ștergere, transparență, minimizare

> **Ideea în o frază:** personalizarea cu AI se plătește în încredere; patru reguli de date, plus explicabilitatea și asumarea răspunderii, fac diferența între relevant și abuziv.

## Explicație

Noil rezumă principiile din reglementări precum GDPR (UE) și CCPA (California) în patru reguli:

| Regulă | Ce înseamnă |
|---|---|
| Consimțământ (*consent*) | acord explicit înainte de colectare și folosire în marketing |
| Acces și ștergere (*right to access and erasure*) | omul poate vedea ce date ai și poate cere ștergerea lor |
| Transparență | explici clar ce colectezi și la ce folosești |
| Minimizare (*data minimization*) | colectezi doar ce îți trebuie |

Peste ele, capitolul adaugă trei obligații specifice AI:

- **Explicabilitate** (*explainability*): modelele complexe sunt „cutii negre"; dacă nu poți explica de ce cineva a văzut o reclamă sau a fost refuzat la un credit, ai o problemă de încredere și de conformitate.
- **Responsabilitate** (*accountability*): dacă un chatbot dă o informație greșită, răspunde firma, nu „algoritmul".
- **Anonimizare** (*tokenization*, agregare): folosești datele pentru tipare fără să expui indivizi.

Biasul algoritmic apare ca risc separat: un model antrenat pe date părtinitoare poate exclude grupuri de la reclame imobiliare sau poate repeta stereotipuri de gen în recomandări.

Najafov ([[SRC-039-chatgpt-for-marketing|SRC-039]]) ajunge la aceeași listă din direcția opusă, a designului. Principiile lui de **confidențialitate prin design** (*privacy by design*) pentru personalizare adaugă trei elemente: anonimizarea, **controlul utilizatorului** (vede, editează, șterge, refuză personalizarea) și auditul periodic al practicilor de date. Convergența celor două cărți arată că lista e deja standard de industrie, nu opinia unui autor.

## Aplicare

- Înainte de o campanie personalizată, verifică cele patru reguli ca pe o listă de control.
- Formulează o frază pe care ai putea-o spune clientului final: „Vezi asta pentru că…". Dacă sună jenant, regândește mecanismul.
- Pentru strategie de brand: transparența despre date poate fi ea însăși un mesaj de diferențiere.

## Exemplu

Exemplul din carte: o platformă imobiliară care țintește reclame cu AI trebuie să-și auditeze datele și rezultatele, ca algoritmul să nu favorizeze sau excludă oameni după rasă, gen sau statut socio-economic.

## Întrebări

- Consimțământul obținut printr-un banner de cookie pe care nimeni nu-l citește e un consimțământ real?
- Unde se termină „personalizare utilă" și începe manipularea?

## Legături

- **extinde** [[AIM-1301-personalizarea-cu-ai-are-patru-registre|AIM-1301]] — supra-personalizarea e varianta comercială a aceleiași probleme.
- **vezi** [[AIM-1304-chatbotul-bun-stie-cand-sa-predea-unui-om|AIM-1304]] — chatbotul e locul unde răspunderea pentru erorile AI devine vizibilă.
- **extinde** [[AIM-1318-declara-cand-folosesti-ai-trusa-de-transparenta|AIM-1318]] — transparența față de public privind conținutul generat cu AI.

## Surse

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 12 (12.1-12.5)
- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, cap. 3, p. 73–74

<!-- backlinks:start -->
## Backlinks

- [[AIM-1301-personalizarea-cu-ai-are-patru-registre|AIM-1301]] _vezi_ — Personalizarea cu AI lucrează în patru registre — în timp real, comportamental, micro-segment și predictiv
- [[AIM-1304-chatbotul-bun-stie-cand-sa-predea-unui-om|AIM-1304]] _vezi_ — Chatbotul bun știe când să predea conversația unui om
- [[AIM-1314-precizie-sau-transparenta-ansamblurile-si-retelele-neuronale|AIM-1314]] _vezi_ — Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
- [[AIM-1318-declara-cand-folosesti-ai-trusa-de-transparenta|AIM-1318]] _extinde_ — Declară când folosești AI — o trusă de transparență și un checklist etic în opt puncte
- [[AIM-1325-ascultarea-vizuala-gaseste-brandul-in-imagini|AIM-1325]] _vezi_ — Ascultarea vizuală găsește brandul în imagini, acolo unde nu e numit în text
- [[SRC-037-ai-driven-marketing|SRC-037]] — AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
- [[SRC-039-chatgpt-for-marketing|SRC-039]] — ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
