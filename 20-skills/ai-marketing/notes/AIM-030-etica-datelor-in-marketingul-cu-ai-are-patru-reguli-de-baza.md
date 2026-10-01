---
id: AIM-030
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
status: growing
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

Biasul algoritmic apare ca risc separat, tratat în [[AIM-032-biasul-in-marketingul-cu-ai-are-doua-surse-datele-din-care|AIM-032]].

Najafov ([[SRC-039-chatgpt-for-marketing|SRC-039]]) ajunge la aceeași listă din direcția opusă, a designului. Principiile lui de **confidențialitate prin design** (*privacy by design*) pentru personalizare adaugă trei elemente: anonimizarea, **controlul utilizatorului** (vede, editează, șterge, refuză personalizarea) și auditul periodic al practicilor de date. Convergența celor două cărți arată că lista e deja standard de industrie, nu opinia unui autor. Aceeași listă apare și la juristul Raj Sachdev ([[DIG-065-zece-practici-de-confidentialitate-pentru-marketeri-de-la|DIG-065]]).

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

- **vezi** [[AIM-016-personalizarea-cu-ai-lucreaza-in-patru-registre-in-timp|AIM-016]] — supra-personalizarea e varianta comercială a aceleiași probleme.
- **vezi** [[AIM-033-declara-cand-folosesti-ai-o-trusa-de-transparenta-si-un|AIM-033]] — transparența față de public privind conținutul generat cu AI.
- **vezi** [[AIM-032-biasul-in-marketingul-cu-ai-are-doua-surse-datele-din-care|AIM-032]] — biasul algoritmic, tratat pe larg.
- **vezi** [[AIM-023-chatbotul-bun-stie-cand-sa-predea-conversatia-unui-om|AIM-023]] — chatbotul e locul unde răspunderea pentru erorile AI devine vizibilă.
- **vezi** [[DIG-065-zece-practici-de-confidentialitate-pentru-marketeri-de-la|DIG-065]] — zece practici de confidențialitate pentru marketeri, aceeași listă văzută de un jurist.
- **vezi** [[DIG-063-consimtamantul-valid-se-cere-activ-si-se-poate-retrage-la|DIG-063]] — cum arată un consimțământ valid în practică.

## Surse

- [[SRC-037-ai-driven-marketing|SRC-037]] Karen Noil, *AI-Driven Marketing*, cap. 12 (12.1-12.5)
- [[SRC-039-chatgpt-for-marketing|SRC-039]] Eldar Najafov, *ChatGPT for Marketing*, cap. 3, p. 73–74

<!-- backlinks:start -->
## Backlinks

- [[AIM-010-precizie-sau-transparenta-ansamblurile-si-retelele|AIM-010]] _vezi_ — Precizie sau transparență — ansamblurile și rețelele neuronale prezic, dar nu explică
- [[AIM-016-personalizarea-cu-ai-lucreaza-in-patru-registre-in-timp|AIM-016]] _vezi_ — Personalizarea cu AI lucrează în patru registre — în timp real, comportamental, micro-segment și predictiv
- [[AIM-023-chatbotul-bun-stie-cand-sa-predea-conversatia-unui-om|AIM-023]] _vezi_ — Chatbotul bun știe când să predea conversația unui om
- [[AIM-028-ascultarea-vizuala-gaseste-brandul-in-imagini-acolo-unde-nu|AIM-028]] _vezi_ — Ascultarea vizuală găsește brandul în imagini, acolo unde nu e numit în text
- [[AIM-032-biasul-in-marketingul-cu-ai-are-doua-surse-datele-din-care|AIM-032]] _vezi_ — Biasul în marketingul cu AI are două surse — datele din care învață modelul și încrederea oarbă a omului în recomandare
- [[AIM-033-declara-cand-folosesti-ai-o-trusa-de-transparenta-si-un|AIM-033]] _extinde_ — Declară când folosești AI — o trusă de transparență și un checklist etic în opt puncte
- [[DIG-062-strategia-de-date-first-party-porneste-de-la-intrebarea-ce|DIG-062]] _vezi_ — Strategia de date first-party pornește de la întrebarea „ce date ne cresc vânzările?” și obține datele prin invitație și schimb de valoare, nu prin colectare ascunsă
- [[DIG-063-consimtamantul-valid-se-cere-activ-si-se-poate-retrage-la|DIG-063]] _vezi_ — Consimțământul valid se cere activ și se poate retrage la fel de ușor — butoane egale, căsuțe nebifate, scopuri explicate, dovadă păstrată
- [[DIG-065-zece-practici-de-confidentialitate-pentru-marketeri-de-la|DIG-065]] _vezi_ — Zece practici de confidențialitate pentru marketeri, de la consimțământul cu valoare arătată până la minimizarea datelor
- [[HIS-020-reclama-politica-a-invatat-de-la-cea-comerciala-de-la|HIS-020]] _vezi_ — Reclama politică a învățat de la cea comercială — de la spoturile lui Eisenhower la „Daisy"
- [[MAP-003-etica-reglementare-si-responsabilitate|MAP-003]] — Etică, reglementare și responsabilitate în publicitate
- [[SRC-037-ai-driven-marketing|SRC-037]] — AI-Driven Marketing: Harnessing Artificial Intelligence to Personalize Customer Experiences
- [[SRC-039-chatgpt-for-marketing|SRC-039]] — ChatGPT for Marketing: Learn Practical Applications of ChatGPT for Marketing
<!-- backlinks:end -->
