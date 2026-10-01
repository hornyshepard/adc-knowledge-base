# Raport P2-IDE — integrarea skill-ului creative-ideation (IDE)

Agent P2-BRF-IDE, Faza 2. Skill: `20-skills/creative-ideation/`. (Același agent a integrat și BRF; vezi `P2-BRF.md`.)

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente | 22 | 25 (22 + 3 noi, nicio comasare) |
| Note cu `status: growing` | 0 | 25 |
| Legături tipizate per notă | 3–5 | 5–6 |
| Note fără nicio legătură tipizată în afara propriului grup Faza 1 și skill | 4 | 0 |
| Note fără secțiunea „Exemplu" | 12 | 0 |
| Lungime corp (`kb.py words`) | 341–493 | 375–497 (nicio notă peste pragul de 650) |

`kb.py check` (ultima rulare): **nicio problemă în fișierele `creative-ideation`**. `renumber --dry-run` (doar afișare) confirmă ordinea din hartă: IDE-0701 → IDE-001 … IDE-0710 → IDE-025.

Nu există comasări IDE, deci nu am creat `merges-IDE.txt`.

## 2. Comasări

Niciuna. Perechile apropiate au rămas separate, cu legături tipizate, pentru că sunt modele sau idei diferite:
- IDE-0702 (16 etape Ingledew) ↔ IDE-0716 (7 pași Ahmed): `alternativa`.
- IDE-0501 (inspirația din afara bulei, Peters + Moffat) ↔ IDE-0712 (banca de inspirație, Ingledew): `extinde` (unde cauți vs. obiceiul de a colecționa).
- IDE-0301 (trei mituri, von Scheel) ↔ IDE-0802 (solitudine/pereche/ședință, clasicii): `contrazice` în ambele sensuri.
- IDE-0708 (inversarea) ↔ IDE-0714 (reîncadrarea): `extinde` — inversarea e un caz particular.

**Rafinări:** IDE-0301 trecută de la `debate` la `principle` (un singur autor contra unor mituri, nu o dispută între autori). IDE-1501 retitlată (titlul vechi conținea două idei; „cel puțin șase idei" a trecut în IDE-9903): „Ideea creativă trebuie întâi să dramatizeze beneficiul-cheie, apoi să atragă atenția, să accelereze procesarea și să susțină multe execuții". Am corectat direcția relațiilor greșite din Faza 1 (de ex. IDE-0701 „extinde" IDE-0702, IDE-0704 „extinde" IDE-0707, IDE-0708 „exemplu" INS-0702).

## 3. Note noi (verificate în `90-library/text/`)

Am căutat întâi ce acoperă deja HIS/CPY (G08) și *Shareworthy*: „big idea" e acoperit de IDE-0801 (+ ADV-1303, CPY-0808, HIS-0810), ideea „shareworthy" de STO-0701/STO-0704, procesul Wallas/Webb Young e menționat în IDE-0703 (biblioteca are doar câteva rânduri despre el, insuficient pentru o notă). Au rămas trei goluri reale:

- **IDE-9901** — *Brainstormingul lui Osborn are patru reguli — cantitate, judecată amânată, idei sălbatice, combinare — și cere ca generarea să fie separată de evaluare* (method, nivel 1). Surse: SRC-025 cap. 6 „The Ideation Process" (`shareworthy-robin-landa.txt` r. 2106–2110, cele patru reguli); SRC-027 cap. 10, p. 207 (Osborn, BBDO, *How to „Think Up"*, 1942 — Braun & Landa dau 1953, *Applied Imagination*: dezacord de datare notat în text); SRC-001 cap. 12, p. 444 (brainstormingul în dezvoltarea de produse, votul la final); SRC-026 cap. 3 și cap. 6 (limită de timp, facilitator); SRC-028 (Campbell's „Soup on the Rocks").
- **IDE-9902** — *Grilele de evaluare a ideilor converg pe trei întrebări — servește strategia, iese din rând, rămâne legată de brand — dar se aplică în momente diferite* (framework, nivel 2). Golul: scope-ul cere „evaluarea ideilor", iar cele cinci grile (Percy Table 14.1, A.L.T.E.R., Milavsky, ADPLAN, matricea Ahmed) erau în patru skill-uri fără comparație. Surse: SRC-049 cap. 14 (`audiobook/28.txt`, inclusiv fraza despre execuția strălucită care nu respectă strategia), SRC-022 cap. 8, SRC-025 cap. 6, SRC-021 cap. 5 și 7, SRC-026 cap. 3 și 7.
- **IDE-9903** — *Volumul precede calitatea — ideea bună iese dintr-un număr mare de încercări, cele mai multe proaste* (principle, nivel 1). Convergență între șase surse independente: SRC-049 („random creativity", cel puțin șase idei), SRC-017 cap. 2 (faza de schiță: „quantity is more important than quality", 50 de schițe), SRC-028 (Spier 40–50 de abordări, Metcalf 25–30 de rescrieri — verificate în text), SRC-022 cap. 8 (echipele generează multe idei, cele mai multe proaste), SRC-025 (regula 1 Osborn), SRC-026 cap. 3.

## 4. Convergențe și dezacorduri scrise explicit în note

- **Mecanismul „aha"**: brainjack-ul lui Ingledew (IDE-0701) = incongruența rezolvată din modelul Kroeber-Riel la Percy (IDE-1501).
- **Big Idea** (IDE-0801): Richards/Watkins + Percy (dramatizează beneficiul) + Braun & Landa (North Star) + Aly Richards & McLean (Long Idea, ADV-1303).
- **Umorul** (IDE-0709): entuziasmul Ingledew `contrazice` datele Fennis & Stroebe (CPY-0404: umorul fură memoria brandului).
- **Șocul** (IDE-0710): + istoria shockvertising-ului (HIS-0818) și meta-analizele despre frică (INS-0433).
- **Locuri neașteptate / word of mouth** (IDE-0711): `contrazice` ADV-0504 (viralitatea vine din difuzarea de masă, nu din bârfă).
- **Clișeul pe dos** (IDE-0706) ≈ metoda Disruption a BDDP (ADV-0619), la nivel de strategie.
- **Incubația** (IDE-0703) confirmată de poveștile clasicilor (Rubicam, Spier — IDE-0802); exemplul Spier verificat în SRC-028.
- **Culture surfing** (IDE-0715): exemplul BlackBerry „May the 4th" din Percy (IDE-1501).
- **Generare separată de evaluare**: Osborn (IDE-9901) ≈ Ahmed (IDE-0716) ≈ strateg convergent / creativ divergent (BRF-1503).

## 5. Duplicate între skill-uri (legate, nu comasate)

| IDE | Alt skill | Natura suprapunerii |
|---|---|---|
| IDE-0801 | CPY-0808, HIS-0810, ADV-1303 | Big Idea: aceeași prefață Watkins în CPY-0808; genealogia în HIS-0810 |
| IDE-0710 | HIS-0818 | șocul ca strategie de atenție |
| IDE-0709 | CPY-0404, CPY-0813 | umorul în reclamă (date experimentale vs. istorie vs. tehnică) |
| IDE-0706 | ADV-0619 | ruperea convenției (execuție vs. strategie) |
| IDE-0802 | HIS-0811 | echipa creativă copywriter–art director |
| IDE-0713 / IDE-9902 | BRF-0712, CPY-0606 | grile de evaluare a ideilor și a execuțiilor |
| tehnicile Ingledew | ART-0702…0706, CPY-0701 | același capitol-sursă (SRC-024), împărțit între IDE (mecanisme) și ART/CPY (limbaj vizual și verbal); harta IDE le listează într-o linie separată |

## 6. Goluri rămase

- **Modelele clasice ale procesului creativ** (Wallas, Webb Young): biblioteca are doar o enumerare a etapelor (SRC-025) și un citat (SRC-024); rămân în IDE-0703 și IDE-9901.
- **Gândirea laterală (de Bono)** apare doar ca tehnică a cuvântului aleator (IDE-0703) și ca cele șase pălării (IDE-0717).
- **AI-ul ca partener de ideație**: nicio notă IDE; posibil subiect pentru AIM (SRC-039 are pasaje despre brainstorming cu ChatGPT).
- **Gândirea divergentă vs. convergentă** ca concept separat: material insuficient (doar Percy/O'Malley în BRF-1503 și o mențiune la Colenso).

## 7. Pentru orchestrator

- Nicio notă IDE nu a fost ștearsă, deci nu e nevoie de redirect pentru IDE.
- IDE-1501 și-a schimbat titlul; fișierul a păstrat vechiul slug (`build --rename` sau `renumber` îl vor alinia).
- Am verificat legăturile spre note comasate de alți agenți (INS-0501 → INS-0702 folosit direct).
