# Raport P2-MKT — integrarea skill-ului marketing-fundamentals

Agent P2-MKT, Faza 2. Skill: **MKT — Fundamente și strategie de marketing** (`20-skills/marketing-fundamentals/`).

## 1. Note înainte și după

| | Număr |
|---|---|
| Note la început | 75 (G01: 29, G02: 16, G03: 24, G04: 1, G09: 1, G10: 1, G12: 1, G15: 2) |
| Comasate (șterse) | 4 |
| Note noi (Faza 2) | 2 |
| **Note la final** | **73** |

Toate cele 73 de note au fost revizuite și au `status: growing`. Fiecare are 4–6 legături tipizate în „Legături", cu cel puțin una spre alt grup de cărți sau alt skill. `kb.py check`: zero probleme în fișierele MKT. Cele 8 legături rupte care țintesc ID-uri MKT vin din alte foldere și indică exact cele 4 note comasate (se rezolvă la redirect).

Lungimi: între 339 și 480 de cuvinte în corp. Notele peste 400 de cuvinte au tabele de model sau sunt rezultatul unei comasări (MKT-0127, 0109, 0209, 0301), ori sunt note-ancoră (MKT-0201, 0216).

## 2. Comasări (`merges-MKT.txt`)

| DROP | KEEP | De ce |
|---|---|---|
| MKT-0103 (erele Grewal-Levy: producție → vânzări → piață → valoare) | MKT-0127 | aceeași evoluție descrisă de Kotler-Armstrong ca cinci filozofii; nota KEEP le pune alături și arată unde diferă (istorie liniară vs. opțiuni care coexistă; „valoare" vs. „societal") |
| MKT-0203 (3.0: co-creare, comunitizare, caracter în locul 4P, STP, brand building) | MKT-0209 | aceeași idee la Kotler, în două ediții; KEEP are acum un tabel 4P/STP/poziționare → 3.0 → 4.0 și explică revizuirea |
| MKT-0304 (von Scheel: outside-in și inside-out) | MKT-0109 | e analiza de situație SWOT sub alt nume (piață vs. capabilități); KEEP arată convergența și ce adaugă von Scheel (verificarea presupunerilor, lanțul valoric) |
| MKT-0312 (dezbatere: alegeri în ordine sau simultan) | MKT-0301 | tensiune internă a aceleiași cărți, despre aceleași trei alegeri; integrată ca paragraf și ca test de coerență |

Am analizat și am păstrat separat (legate între ele) perechile care sunt înrudite, dar nu identice: MKT-0106 / 0204 / 0320 (trei ierarhii diferite ale responsabilității sociale), MKT-0113 / 1501 (dezacord explicit despre selecția țintei), MKT-0107 / 0310 (avantaj competitiv la Grewal și la Porter/von Scheel), MKT-0313 / 0401 (concept vs. critică), MKT-0104 / 0314 / 1001 (mixul și alternativele lui), MKT-0302 / 0108 (ciclu strategic vs. plan de marketing).

## 3. Note noi

| ID | Titlu | Sursa verificată în `90-library/text/` |
|---|---|---|
| MKT-9901 | Cele cinci forțe ale lui Porter arată cine îți poate lua din marjă | SRC-007 cap. 3, p. 64 și 78 (lista forțelor); SRC-031 anexa 2A, p. 428; SRC-002 cap. 7, p. 215-216 (aplicare pe piața rurală) |
| MKT-9902 | Strategia globală de marketing decide, P cu P, cât standardizezi și cât adaptezi | SRC-001 cap. 8, p. 264-270 și glosarul („glocalization") |

Motivul: scope-ul skill-ului numește explicit „5 forțe", dar nicio notă nu le trata. Marketingul global (standardizare vs. adaptare a mixului) e un fundament evident pentru campaniile pe mai multe piețe și era acoperit doar din unghiul comunicării (ADV-1521) și al brandului (BRD-0516). Atenție: biblioteca nu conține cartea lui Porter. MKT-9901 se sprijină pe enumerări și aplicări din trei surse și marchează explicit ce e sinteza notei.

Am adăugat și conținut nou în note existente, din surse verificate: Value Proposition Canvas și dezacordul Zahay vs. Grewal-Levy (propunerea de valoare nu e o declarație de poziționare) în MKT-0116, din SRC-029 p. 77-79.

## 4. Alte revizii

- **Titluri schimbate** (fișierele păstrează vechiul slug; `renumber` le redenumește): MKT-0127, 0109, 0209, 0301 (comasări), MKT-0309 (menționează acum că modelul e Cynefin, necitat de sursă).
- **Nivel**: MKT-0207 1→2, MKT-1001 1→2, MKT-1201 2→3. **Kind**: MKT-0315 framework → case.
- **Convergențe și dezacorduri** scrise explicit în aproape toate notele, de exemplu: definiția AMA reluată de Kotler 5.0 și contestată de Wuebben (0101); CLV ca retenție vs. loialitatea ca recomandare în 5A (0105 ↔ 0210); Percy vs. Grewal despre selecția țintei (1501 ↔ 0113); Trout & Ries, Barre & Gayrard-Carrera și Kotler 4.0 despre poziționare (0115); planul anual vs. marketingul agil (0108 ↔ 0214); ciclul de viață vs. cicluri scurtate (0118); Rogers vs. curba 5/15/80 necitată a lui von Scheel (0119 ↔ 0308); avantajul pionierului, mai mare în INS-0406 decât în manual (0119); purpose ca diferențiator (3.0), ca igienă (5.0) sau inutil pentru unele branduri (0213, BRD-0510); greenwashingul numit de Grewal-Levy, ocolit de Viturino (0323).
- Relațiile tipizate au fost corectate acolo unde direcția era inversată (de ex. o notă de bază care „extindea" o notă derivată).

## 5. Cărțile slabe din G03: ce am păstrat și de ce

| Sursă | Rating | Ce rămâne |
|---|---|---|
| SRC-007 von Scheel | ★★☆☆☆ | 10 note (0301, 0302, 0303, 0305-0311), după comasarea 0304 → 0109 și 0312 → 0301. Le-am păstrat pentru că sunt instrumente de predat care nu există altundeva în bibliotecă (trei alegeri, Can–Want–Should, niveluri de trend, driver/forță, 80-15-5, Cynefin). Fiecare notă spune acum explicit ce e nesusținut (procente fără metodă, Cynefin și Rogers necitați, atribuirea „cu Steve Jobs") și cere folosirea lor ca euristici. |
| SRC-008 Wuebben | ★★★☆☆ | 6 note (0313-0318) + contribuții în 0319, 0323. Valoroase: prosumatorul, EP², generativele lui Kelly, Carrotmob, verificarea retrospectivă a prognozelor. |
| SRC-009 DX Review | ★☆☆☆☆ | doar ca exemplu negativ în 0319. |
| SRC-010 Ejeke | ★★☆☆☆ | doar ca sursă secundară în 0319, 0320, 0323. |
| SRC-011 Viturino | ★★☆☆☆ | 5 note (0320-0324). Le-am păstrat pentru vocabular și checklist-uri (materialitate, scope 1-2-3, design circular). Valoarea lor vine din încadrarea critică a notelor (0323 critică explicit sursa). |

SRC-002 Policarpio (★★☆☆☆) rămâne sursă secundară; erorile ei sunt semnalate în notele unde apare (0101, 0114, 0121, 0127, 0129).

## 6. Duplicate între skill-uri (nu le-am atins; sunt legate)

- **Declarația de poziționare / propunerea de valoare**: MKT-0116 ↔ BRD-0503 (Kellogg, cu motivul de a crede), BRF-0705 (în brief), BRF-1502 (Percy, trei variabile), DIG-1004 (formula digitală). Aceeași formulă apare în cinci note. Propun BRD-0503 ca locul canonic al *declarației*. MKT-0116 rămâne nota despre *conceptul* de propunere de valoare (cercurile, Value Proposition Canvas).
- **Harta perceptuală / poziționarea**: MKT-0115 ↔ BRD-0607 (aceeași hartă în patru pași + șase teste), BRD-0605, ADV-0610.
- **Ecuația valorii**: MKT-0102 ↔ BRD-0506.
- **Calitativ vs. cantitativ**: MKT-0126 ↔ INS-0603 (aproape identice ca idee centrală); INS-1303 nuanțează focus-grupul.
- **Greenwashing / purpose-washing**: MKT-0323 ↔ BRD-0402, STO-0707.
- **Customer journey**: MKT-0210 (5A) ↔ DIG-0905, ADV-0501, DIG-1032 (KPI pe etapele 5A).
- **Persona vs. segment**: MKT-0113 / 1501 ↔ DIG-1006, INS-1306.
- **Segmentul de unu**: MKT-0114 ↔ DIG-0204.
- **Planul**: MKT-0108 ↔ DIG-1002, ADV-1506.
- **Mixul alternativ**: MKT-0104 / 0128 ↔ EXP-1201 (7E), DIG-1001 (7A). Sunt alternative, nu duplicate.
- **Pionierul**: MKT-0119 ↔ INS-0406, BRD-0514.
- **Global**: MKT-9902 ↔ ADV-1521, BRD-0516.
- **Servicii**: MKT-0123 ↔ BRD-0520.

## 7. Goluri rămase

- **Porter** e acoperit doar indirect (fără textul original). MKT-9901 e o notă modestă și ar câștiga dintr-o sursă primară.
- **Marketingul B2B** (Grewal cap. 7 citit doar la nivel de cuprins) nu are notă MKT; o parte e în CLI.
- **Metricile de marketing** (ROMI, cotă de piață, NPS) sunt împrăștiate între ADV, DIG și MKT-0322; nu există o notă MKT de sinteză.
- **Strategiile competitive după poziția pe piață** (lider, challenger, urmăritor, nișă) lipsesc; nu am verificat dacă biblioteca le acoperă.
- **Glocalizare/grobalizare (Ritzer)** din SRC-013, semnalate de G04, nu au fost notate.
- Reglementarea și etica marketingului în context UE/RO (semnalate de G01) rămân fără casă.

## 8. Pentru orchestrator

- Legăturile din alte foldere spre ID-urile comasate (SRC-001 → MKT-0103; SRC-003, BRD-0201, BRD-0203, SOC-0201 → MKT-0203; SRC-007, ADV-0611 → MKT-0304; SRC-007 → MKT-0312) se rezolvă cu `merges-MKT.txt`.
- În legăturile noi am folosit deja ID-urile KEEP din listele de comasare ale celorlalți agenți, așa cum erau la momentul lucrului (ADV-1506, BRD-0512, ADV-0604, SOC-1115, ADV-1533, BRD-0606, DIG-0930, DIG-0905, EXP-0901, INS-1206). Dacă alți agenți comasează după acest moment, `redirect` trebuie rulat și pe folderul MKT.
- `SKILL.md` conține toate cele 73 de note, în ordinea traseului (6 secțiuni). `renumber` va produce MKT-001 = MKT-0101 … MKT-073 = MKT-0318.
- Copii de siguranță ale notelor dinaintea Fazei 2 sunt în scratchpad-ul agentului (`P2-MKT/backup/`).
