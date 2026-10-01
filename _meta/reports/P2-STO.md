# Raport P2-STO — Faza 2: integrarea skill-ului storytelling-content

Agent: P2-SOC-STO (deține și SOC; vezi `P2-SOC.md`). Data: 2026-10-01.

## 1. Bilanț

| | Înainte | După |
|---|---|---|
| Note proprii STO | 41 | **41** (40 păstrate + 1 nouă) |
| Comasări (DROP → KEEP) | — | 1 (`merges-STO.txt`) |
| Note noi | — | 1 (STO-9901) |
| Status | 41 seed | 41 growing |
| Niveluri | — | 10 × 1, 30 × 2, 1 × 3 |
| `SKILL.md` | hub provizoriu | rescris: 7 competențe, hartă în 6 secțiuni (toate cele 41 de note), surse cu ★, vecini, 5 playbook-uri |

Toate notele au 2–6 legături tipizate și cel puțin una spre alt skill sau alt grup de cărți. `kb.py check`: nicio problemă în fișierele STO.

## 2. Comasări și restructurări

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| STO-0903 | STO-0202 | Ciclul strategiei de content marketing: cei opt pași Kotler (4.0) + cei patru pași Zahay + varianta în șase pași Barre & Gayrard-Carrera. Nota spune unde converg (bucla evaluare–reluare) și unde diferă (ordinea: obiective înainte de idee la Kotler, creația întâi la Zahay; amplificarea prin influenceri vs. curatorierea). Principiul „conținutul conține ce vrea clientul să folosească" s-a mutat în STO-0901, studiul Google despre reclamele nesărite în STO-1104. |

**Clusterul „călătoria eroului".** Indicația din sarcină numea STO-0902, dar STO-0902 e matricea de conținut Chaffey, nu o notă despre erou. Clusterul real: STO-1201, STO-1303, STO-0702, STO-1101, STO-1103 (plus STO-0501 și STO-0905, apropiate). Nicio notă nu era un duplicat curat, așa că am făcut **o notă-nucleu și note de aplicare**, fără să șterg nimic:

- **STO-1201** a devenit nota-nucleu (nivel 1): Campbell/Vogler, versiunile din cinci cărți (Batat, Mueller & Rajaram, Braun & Landa, Richards & McLean, Sawhney), de ce funcționează (transport narativ, transformarea prin brand) și dezbaterea „cine e eroul" (clientul pentru Richards & McLean, Sawhney, Braun & Landa; și fondatorul pentru Batat; ghidul în loc de erou pe social, la Mueller & Rajaram).
- Aplicații, cu `fundament` spre nucleu: **STO-0702** (spotul: C.O.W. + B → T și trei acte), **STO-1303** (conținutul: actele ca ciclu de cumpărare, varianta B2B), **STO-1103** (social: cele șapte cotituri ca întrebări); **STO-1101** rămâne `debate` și `contrazice` nucleul.
- Cele patru ingrediente ale poveștii din Batat s-au mutat în **STO-0905**, comparate cu grila Kindra Hall și cu modelul Kotler 3.0 (STO-0201).

**Alte integrări:** STO-1112 (UGC) adună acum Mueller & Rajaram, Barre & Gayrard-Carrera, Labrecque (5C), Nishad și Glenister, cu dezbaterea „apel implicit vs. mecanică explicită"; STO-0601 a pierdut lista de pași (duplicat cu STO-0202) și păstrează regulile de legitimitate și reînnoire.

## 3. Verificarea STO-0702 („C.O.W.")

Am căutat în `90-library/text/shareworthy-robin-landa.txt` (rândurile ~1712–1729, cap. 5, p. ~104). Cartea dă harta „Protagonist (represents the target audience) → Obstacle (conflict) → Want or need or desire + Brand (facilitator) → Transformation → Resolution and call-to-action" și scrie imediat sub ea **„C.O.W. + B→T"**, dar **nu explică nicio literă**. Nota rescrisă spune doar ce reiese din text: O, W, B și T corespund termenilor cu majusculă din hartă (*Obstacle, Want, Brand, Transformation*); pentru C cartea nu dă nicio cheie (primul element se numește *Protagonist*), deci formula se folosește ca prescurtare a hărții. Titlul nu mai sugerează că C = protagonist. Am verificat în text și cele trei acte (25/50/25%), apoteoza, Orchard Thieves și Reddit (p. 103–118).

## 4. Notă nouă

- **STO-9901** — *Pe social media, conținutul altora se preia prin funcția de distribuire sau cu acord scris, iar oamenii filmați își păstrează dreptul la propria imagine* (SRC-034, cap. 2.5, pro tip D. Mrkaja, p. 82–85 în paginarea PDF folosită de G11). Golul fusese semnalat de G11 (§4). În paralel, agentul DIG a scris **DIG-9902** (Sachdev: mărci, copyright, fair use, CC); am restrâns STO-9901 la regulile de producție socială (distribuire vs. repostare, acord scris, muzică, dreptul la imagine, minori) și am legat-o `fundament` → DIG-9902.

## 5. Duplicate între skill-uri (legate, neatinse)

- **STO-0709** (checklist de reprezentare, *Shareworthy*) ↔ **ADV-0302** (reclama incluzivă pe trei axe, Ejeke) — liste paralele; `alternativa`.
- **STO-9901** ↔ **DIG-9902** — suprapunere parțială pe licențele Creative Commons (vezi §4).
- **STO-0601** ↔ **BRD-1201** (de la brand content la brand culture, Batat).
- **STO-0901** ↔ **ADV-0301** (dezbaterea conținut vs. reclamă, Wuebben) — `contrazice`.
- **STO-1115** ↔ **ADV-0504** (viralul vine din difuzare de masă) — `contrazice`.
- **STO-0701 / STO-0704 / STO-1115** ↔ **INS-0444** (emoțiile cu activare mare se distribuie) — `fundament`.
- **STO-1201 / STO-1101** ↔ **PIT-1416** (în pitch, eroul e clientul).
- **STO-0707 / STO-1114** ↔ **BRD-0402**, **BRD-0509** (purpose, greenwashing).
- **STO-1109** ↔ **ART-0705** (cuvântul și imaginea se tensionează, nu se repetă); **STO-1102** ↔ **ART-0803**.
- **STO-1105** ↔ **CPY-0815** (Burma-Shave, copy serial).

## 6. Goluri rămase

- **Producția de conținut cu smartphone-ul** (cadraj, sunet, montaj, aspect ratio) — o parte mare din SRC-034, tutorială, între STO și ART; fără notă.
- **Storytelling audio/podcast** și **povestea în B2B** dincolo de STO-1303.
- **Cele șapte intrigi ale lui Booker** apar doar în STO-0501; „story spine"-ul Pixar e doar în PRT-1416.
- **Dreptul românesc** (drepturi de autor, dreptul la imagine): STO-9901 descrie regulile germane din carte și cere verificarea legii locale.

## 7. Pentru orchestrator

- Legături din alte skill-uri spre STO-0903 (de redirecționat la STO-0202): DIG-0925, DIG-0930 (DIG-0912 a fost comasată de DIG), plus SRC-029.
- În fișierele mele am redirecționat deja legăturile spre comasările altor agenți (BRD-0205→BRD-0606, DIG-0912→DIG-1006). Rulează totuși `redirect` pentru comasările ulterioare.
- `SKILL.md` nu citează ID-uri în „Competențe", ca `renumber` să urmeze harta (STO-0701, STO-1201, STO-0702 … STO-0710).
- STO-0202, STO-0702 și STO-1201 au 440–445 de cuvinte după contorul `kb.py` (titlu H1 lung + tabele); proza e în jur de 400.
