# Raport P2-CPY — integrarea skill-ului Copywriting și mesaj

Agent: P2-CPY-ART-HIS (deține și ART, HIS). Data: 2026-10-01.

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente CPY | 37 | 38 (−1 comasată, +2 noi) |
| Note cu `status: growing` | 0 | 38 |
| Legături tipizate pe notă | 2–5 | 4–6 (toate notele au cel puțin o legătură spre alt grup de cărți sau alt skill) |

`kb.py check`: nicio problemă în fișierele CPY. Singura legătură ruptă legată de CPY e în `10-sources/SRC-027` și `SRC-028` (→ CPY-0802, comasată), care se rezolvă la redirect.

## 2. Comasări (`merges-CPY.txt`)

- **CPY-0802 → CPY-0601** (reason-why). Ambele notele descriau formula „salesmanship in print" a lui Kennedy și metoda Hopkins. CPY-0601 (G06, Fernández Gómez) a păstrat filiația spre copy strategy și USP. Din CPY-0802 (G08, Richards + Watkins) a preluat exemplele Ivory, Pepsodent, Sears și Canada Dry, plus atacul lui MacManus. Sursele sunt acum SRC-018, SRC-027 și SRC-028, iar unghiul e de meșteșug: cum scrii motive concrete. Genealogia istorică rămâne în HIS-0810, legată.

## 3. Note noi (Phase 2)

- **CPY-9901** — Anatomia reclamei tipărite: vizual, titlu, subtitlu, body copy, semnătură (SRC-001 cap. 19, p. 604–605, cu SRC-049 și SRC-021). Lipsea vocabularul de bază al unui copywriter. Nota arată convergența Grewal & Levy, Percy & Rosenbaum-Elliott și Milavsky asupra ordinii imagine → titlu.
- **CPY-9902** — Vocea brandului rămâne constantă, tonul se adaptează (SRC-031 cap. 3 și 8; SRC-016 cap. 7, interviul cu Myra El-Bayoumi; SRC-039 cap. 2). „Ton și voce" era în scope, dar nu avea o notă-concept. Cele trei surse dau aceeași distincție.

## 4. Revizii de conținut

- Convergențe și dezacorduri explicite adăugate: CPY-0401 (Carlsberg: inferență înșelătoare la Fennis & Stroebe vs. ironie modestă la Percy, ADV-1523), CPY-0402 (abordarea refutațională la Percy), CPY-0605 (INS-0410 și BRF-0707), CPY-0806 (meta-analizele despre frică, INS-0433), CPY-0813 (datele despre umor din CPY-0404 și Milavsky), CPY-0817 (perseverența, ADV-0606, și uzura, ADV-0407), CPY-1502 (Milavsky ajunge la aceleași reguli). Sursele noi au fost adăugate în `sources:`.
- CPY-0701 avea secțiunea „Exemplu" lipsă; am adăugat-o.
- Titluri scurtate (prea lungi, nu vagi): CPY-1502, CPY-1001.
- Am tăiat textul la CPY-0605, CPY-1502, CPY-0806 și CPY-0813. Am înlocuit legăturile spre hub-uri (`[[…/SKILL|CPY]]`) cu legături spre note.

## 5. Duplicate între skill-uri (nu am atins notele altora, doar am legat)

| Nota CPY | Nota din alt skill | Relație |
|---|---|---|
| CPY-0601 reason-why | ADV-0603 (copy strategy), ADV-0604 (USP), HIS-0810 (genealogia) | aceeași familie de idei; craft în CPY, strategie în ADV, istorie în HIS |
| CPY-0817 consecvența | ADV-0606 (principiul perseverenței) | aceeași idee, surse diferite (Watkins vs. Fernández Gómez/Milavsky) — candidat la hartă comună |
| CPY-0605 un singur motiv | BRF-0707 (un singur beneficiu), INS-0410 (ușurința reamintirii) | convergență pe trei surse |
| CPY-0806 teama socială | INS-0433 (apelurile la frică) | caz istoric vs. meta-analiză |
| CPY-0404 / CPY-0813 umorul | IDE-0709 (umor, ironie, satiră) | efect vs. istorie vs. tehnică de idee |
| CPY-0607 formatele | INS-1505 (VisCAP), HIS-0821 (personaje vs. celebrități) | alegerea prezentatorului |
| CPY-0401 inferențe înșelătoare | ADV-0108 (puffery), HIS-0808 (FTC) | etica formulării |

## 6. Goluri rămase

- **Scrisul pentru social media** (captions, text peste video, microcopy, UX writing) nu are notă CPY. SRC-034 (*Social Media Storytelling*) are material despre captions. Probabil e acoperit parțial în STO/SOC; de verificat la harta transversală.
- **Naming**: e în BRD (BRD-0524, BRD-0525), dar e și o sarcină de copywriter. Ar ajuta o legătură din harta de identitate.
- **Structuri de text clasice** (PAS, FAB) apar doar în cartea de pitch (SRC-043); n-am scris notă.
- **Etica formulării**: CPY-0401, CPY-0406, CPY-0806 și CPY-0405 sunt candidate pentru harta transversală de etică.

## 7. Pentru orchestrator

- Ordinea de renumerotare e cea din `SKILL.md`: CPY-9901 devine CPY-001, CPY-9902 cade în secțiunea 4.
- Am redirecționat deja, în notele mele, legăturile spre ID-urile comasate de alte skill-uri (ADV-0106 → ADV-0604, DIG-0912 → DIG-1006, DIG-1013 → DIG-0918, DIG-1011 → DIG-0920), după `merges-*.txt` existente la ora rulării.
- Aproximativ 20 de note CPY au 405–445 de cuvinte după metrica din `check` (care numără și titlul H1, tabelele și antetele). Am tăiat doar unde depășirea era mare.
