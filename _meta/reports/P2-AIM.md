# Raport P2-AIM — integrarea skill-ului ai-marketing (AIM)

Agent P2-EXP-AIM, Faza 2. Skill: `20-skills/ai-marketing/`. (Același agent a integrat și EXP; vezi `P2-EXP.md`.)

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente | 33 | 34 (33 − 1 comasată + 2 noi) |
| Note cu `status: growing` | 0 | 34 |
| Note cu 2–6 legături tipizate | 33 | 34 |
| Note fără nicio legătură tipizată în afara propriului grup Faza 1 | 11 | 0 |
| Note cu cel puțin o legătură spre alt skill | 22 | 34 |
| Legături tipizate, total | 108 | 178 |
| Lungime corp (numărare tip `kb.py`) | 304–485 | 305–490 |

`kb.py check`: nicio problemă în fișierele AIM la ultima rulare (singura „relație necunoscută", o legătură inline într-un rând cu bold din AIM-0206, a fost corectată). Legătura ruptă SRC-005 → AIM-0205 se rezolvă la redirect.

Am corectat și direcția relațiilor: multe note G02/G13 foloseau `aplicare`/`extinde`/`exemplu` în sens invers (de exemplu, nota-concept „aplicare" spre nota care o aplică). Le-am trecut pe `vezi` sau le-am inversat unde era cazul.

## 2. Comasări (în `merges-AIM.txt`)

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| AIM-0205 (marketingul predictiv, Kotler 5.0) | AIM-1303 (analiza predictivă ca ciclu, Noil) | Un tabel comun: cele trei zone ale lui Kotler (clienți, produse, branduri) × utilizările-tip ale lui Noil (CLV, lead scoring, churn, recomandări, optimizare de campanie); ciclul în cinci pași (Noil) și cele trei tehnici (regresie, filtrare colaborativă, rețele neuronale, Kotler). Dezacordul explicit: Kotler et al. văd opacitatea „cutiei negre" ca avantaj, Struhl nu (AIM-1314, acum cu legătură `contrazice` în ambele sensuri); niciuna dintre cele două surse nu cere validare pe date nevăzute sau incrementalitate. Nivel 1. |

Alte integrări între autori: AIM-0301 primește dovada empirică din Fennis & Stroebe (ADV-0410) și convergența cu Zahay et al. (DIG-0929); AIM-0206 notează că Noil (AIM-1304) și Najafov (AIM-1320) ajung la același model hibrid om–bot; AIM-1305 notează convergența cu lista lui Sachdev (DIG-1015) și trimite biasul în nota nouă; AIM-1326 adaugă poziția lui Kotler 5.0 și cazurile reale; AIM-0202 adaugă saltul AI-ului lingvistic din Marketing 6.0 (SRC-006).

## 3. Note noi

- **AIM-9901** — *În campaniile premiate cu AI, ideea vine din insight-ul uman, iar AI-ul îi dă scară — Cadbury, Nike „Never Done Evolving", Jardim Sonoro* (case, nivel 2). Golul: secțiunea „AI generativ în creație" nu avea niciun caz real (cărțile de AI nu dau cazuri). Surse verificate în text: SRC-006, cap. 5 (Cadbury #NotJustACadburyAd, 130.000 de reclame, 94 mil. vizualizări); SRC-025, cap. 6 (Nike/AKQA, Jardim Sonoro cu Midjourney și „A.I. prompt master" în credite, Area 23 „Sick Beats") și cap. 8 (Guan Hin Tay).
- **AIM-9902** — *Biasul în marketingul cu AI are două surse — datele din care învață modelul și încrederea oarbă a omului în recomandare* (concept, nivel 2). Golul: biasul era doar o frază în AIM-1305, deși traseul cerut se încheie cu „etică, bias, confidențialitate". Surse verificate: SRC-037 cap. 12 (12.1.2, 12.3), SRC-039 cap. 2 (p. 20–22), SRC-005 cap. 4 (automation bias) și cap. 7 (David Dao), SRC-038 cap. 1 (imaginile implicite despre om).

**Prompting.** Am verificat dacă biblioteca susține note mai bine fundamentate despre prompting. Nu le susține: Najafov are cinci exemple simple (cap. 1) și capitole generice despre ton și multilingvism; Noil doar listează unelte (Jasper, Persado, Phrasee); Zahay et al. au un paragraf despre DALL-E. Nu am scris note noi de prompting. Am îmbogățit AIM-1317 cu singurul exemplu de prompting într-o echipă creativă reală (Jardim Sonoro, SRC-025) și cu legătura spre Get/To/By (BRF-0716), iar SKILL.md spune deschis că tehnica de prompting e un gol.

## 4. Duplicate între skill-uri (nu le-am atins; legate)

| Nota AIM | Nota din alt skill | Relația |
|---|---|---|
| AIM-0301, AIM-1301 | DIG-0929 (personalizare și reactanță), ADV-0410 (potrivire + intruziune) | aproape aceeași limită a personalizării; `vezi`, convergența scrisă în text |
| AIM-1305 | DIG-1015 (zece practici de confidențialitate), DIG-1022 (consimțământ valid) | liste care se suprapun în mare; `vezi` |
| AIM-1303 | DIG-1020 (targetarea predictivă) | același principiu aplicat în media; `vezi` |
| AIM-1302 | DIG-0204 (segmentul de unu) | aceeași idee dusă la limită; `vezi` |
| AIM-1317 | CPY-1301 (vocea brandului cu AI) | complementare (prompt → ciclul de voce) |
| AIM-1320, AIM-1306 | DIG-0933 (testul A/B) | aceeași disciplină experimentală; `vezi` |
| AIM-1325 | SOC-1116 (verificarea influencerilor, include SOC-1301 comasată) | `vezi` |
| AIM-9902 | STO-0709, ADV-0302 (verificarea reprezentării) | aceeași vigilență, pe imagini și texte; `vezi` |
| AIM-1314 | DIG-0922 (programatic: eficiență vs. control) | `vezi` |

## 5. Ce trebuie să știe orchestratorul

- În notele mele am redirecționat deja legăturile spre note comasate de alți agenți (DIG-0305 → DIG-1021, SOC-1301 → SOC-1116; pentru programatic am legat direct DIG-0922, nu DIG-1029, care a fost comasată), pe baza fișierelor `merges-*.txt` existente la final.
- EXP-1301 (conjoint de servicii, Struhl) e în EXP, nu în AIM; e legat din AIM-1310.
- G13 recomanda marcarea notelor AIM-1310–1315 ca traseu „avansat/planning": în SKILL.md ele stau grupate în secțiunea 2, iar AIM-1314, AIM-1315, AIM-1323 au nivel 3.

## 6. Goluri rămase

- O metodă riguroasă de prompting (text și imagine) — biblioteca nu o conține.
- Instrumentele și fluxurile generative actuale; reglementarea AI (de exemplu, AI Act); dreptul de autor asupra conținutului generat; acordul pentru chip și voce sintetice dincolo de cazul Cadbury.
- Măsurarea eficienței creației generate cu AI și a „uzurii" creative când toate brandurile folosesc aceleași modele.
- Cifrele din Noil, Najafov, James și Iroegbu rămân neverificabile; notele le semnalează ca atare.
