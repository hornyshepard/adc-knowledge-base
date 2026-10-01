# Raport P2-SOC — Faza 2: integrarea skill-ului social-influencer

Agent: P2-SOC-STO (deține și STO; vezi `P2-STO.md`). Data: 2026-10-01.

## 1. Bilanț

| | Înainte | După |
|---|---|---|
| Note proprii SOC | 53 | **49** |
| Comasări (DROP → KEEP) | — | 4 (`merges-SOC.txt`) |
| Note noi (`SOC-99NN`) | — | 0 |
| Status | 53 seed | 46 growing, 3 seed (SOC-1006, SOC-1109, SOC-1130 — neatinse, aveau deja legături bune) |
| Niveluri | — | 13 × 1, 32 × 2, 4 × 3 (SOC-1121 coborât de la 3 la 2) |
| `SKILL.md` | hub provizoriu | rescris: 7 competențe, hartă în 6 secțiuni (toate cele 49 de note, în ordinea de învățare), surse cu ★, vecini, 5 playbook-uri |

Toate notele păstrate au 2–6 legături tipizate și cel puțin una spre alt skill sau alt grup de cărți. `kb.py check`: nicio problemă în fișierele SOC.

## 2. Comasări

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| SOC-0101 | SOC-1115 | Cele două modele „4R" (Grewal-Levy: relevanță, reach, răspuns, randament; Onalytica la Glenister: relevanță, rezonanță, referință, reach) într-o singură notă comparativă: unde converg (relevanța primul criteriu) și unde diferă (selecție înainte vs. evaluare după campanie). Tipologia Grewal-Levy cu costuri și cazul LaCroix au trecut în SOC-1114; etica (fraudă, declarare, sinceritate) în SOC-1116 și SOC-1118. |
| SOC-1002 | SOC-1118 | Disclosure-ul din Sachdev (relația materială FTC, „clear and conspicuous", răspunderea pentru pseudo-sfaturi, cazul Teami) + Grewal-Levy (sinceritatea, cererea în căsătorie „spontană") + Glenister (ASA/CMA/EASA, etichete acceptate și riscante, Molly-Mae). Trei surse converg aproape cuvânt cu cuvânt. |
| SOC-1301 | SOC-1116 | Criteriile AI pentru selecție (Iroegbu, SRC-042; ascultarea vizuală, SRC-041) unite cu checklistul de fraudă al lui Glenister: aceleași semnale; diferența e insistența lui Glenister pe statistici reale și verificare manuală. |
| SOC-1126 | SOC-1007 | Rolul platformelor în influencer marketing (Glenister, Sbai) unit cu testul celor patru întrebări pentru social ads (Schwarz-Musch): un singur tabel platformă × rol × specific publicitar. |

## 3. Note noi

Niciuna. Lipsurile identificate (§5) sunt acoperite parțial de note din alte skill-uri sau sunt prea tutoriale.

## 4. Duplicate între skill-uri (nu le-am atins; sunt legate)

- **SOC-1112** (hashtag viral fără potrivire de valori) ↔ **IDE-0715** („culture surfing" doar când valorile brandului îi dau voie) — aceeași regulă din două cărți; legate `alternativa`.
- **SOC-0906** (plan de criză pe social) ↔ **ADV-0622** (comunicarea de criză: recunoaște, nu nega) — suprapunere parțială; legate.
- **SOC-0901** (POST) ↔ **DIG-0103** (ascultă–analizează–acționează, campania socială în cinci pași) — cadre alternative.
- **SOC-0902** (cei 5C) ↔ **DIG-0102** (roata implicării) — explicații alternative ale implicării.
- **SOC-0401 / SOC-1102** ↔ **BRD-0519** (comunitatea de brand ideală) — aceeași temă din trei cărți.
- **SOC-1125** (ER, CPE, CPM) ↔ **DIG-1012** (modele de plată media) — aceleași acronime.
- **SOC-1113 / SOC-1114** ↔ **INS-0432**, **INS-1505**, **HIS-0821** (celebritatea ca sursă) — perspective complementare.
- **SOC-1118** ↔ **DIG-0930** (publicitatea nativă marcată clar) și **DIG-9902** (drepturi în conținutul digital, notă nouă a agentului DIG, care trimite încă spre SOC-1002 → redirect la SOC-1118).
- Brief-ul pentru influenceri stă în **BRF-1101**; SOC trimite spre el din SOC-1110, SOC-1118, SOC-1133 și din playbook.

## 5. Goluri rămase

- **Social listening** ca metodă de sine stătătoare (azi apare doar în SOC-0903, SOC-1133 și în DIG-0103, INS-0203).
- **Social commerce și live shopping**: doar ca micro-trend în SOC-0201.
- **Reglementarea din România/UE** pentru disclosure și promoții: notele spun doar „verifică regulile locale"; biblioteca nu are o sursă românească.
- **Influencerii virtuali și creatorii generați cu AI**: doar mențiuni (SOC-1114, SOC-1132).
- **Brand lift** ca metodă de măsurare: apare doar în cazuri (SOC-1130).

## 6. Pentru orchestrator

- Note din alte skill-uri care trimit spre ID-urile mele comasate (de redirecționat): ADV-0109, DIG-0102, MKT-0119 → SOC-0101; DIG-1016, DIG-9902 (și DIG-1036, comasată de DIG) → SOC-1002; AIM-1318, AIM-1325 → SOC-1301; plus notele-sursă SRC-001, SRC-031, SRC-034, SRC-035, SRC-041, SRC-042.
- În fișierele mele am redirecționat deja legăturile spre ID-urile comasate de alți agenți, după `merges-*.txt` existente la final (ADV-1101→ADV-0617, BRD-0401→BRD-0606, DIG-0912→DIG-1006, DIG-1031→DIG-0906, DIG-1035→DIG-0924, DIG-1036→DIG-0930). Rulează totuși `redirect` pentru comasările făcute după mine.
- `SKILL.md` nu citează ID-uri în „Competențe", ca `renumber` să urmeze ordinea din hartă.
- Câteva note comasate au 420–490 de cuvinte după contorul `kb.py` (care include titlul H1 lung și tabelele); proza e în jur de 400.
- Scripturile folosite (aplicarea rescrierilor cu păstrarea backlink-urilor, legături, redirect) sunt în `scratchpad/P2-SOC-STO/`, cu un backup al folderelor înainte de modificare.
