# Raport P2-DIG — integrarea skill-ului digital-marketing (DIG)

## 1. Bilanț

| | Note |
|---|---|
| Înainte (faza 1) | 87 (G01: 4, G02: 5, G03: 5, G09: 35, G10: 36, G11: 1, G13: 1) |
| Comasate (șterse) | 12 |
| Note noi (faza 2) | 2 (DIG-9901, DIG-9902) |
| **După** | **77** |

Toate cele 77 de note au acum `status: growing`, 4–6 legături tipizate și cel puțin o legătură spre alt grup de cărți sau alt skill. `kb.py check` nu raportează nicio problemă în fișierele DIG (legăturile rupte rămase în KB vin din alte foldere și indică ID-uri comasate de alți agenți sau de mine; vezi §6).

`SKILL.md` e rescris complet: descriere cu situațiile de declanșare, 8 competențe, harta celor 77 de note în 6 secțiuni (strategie → client și journey → media proprii → media plătite → date, confidențialitate și post-cookie → măsurare și atribuire), tabelul surselor cu ★, 12 skill-uri vecine și 6 playbook-uri pentru agenți. Markerii `auto:notes` sunt păstrați.

## 2. Comasări (lista completă în `merges-DIG.txt`)

| DROP → KEEP | Ce s-a integrat, unde converg sau diverg autorii |
|---|---|
| DIG-1013 → **DIG-0918** Ad Rank | Zahay și Sachdev descriu același mecanism; Sachdev adaugă economia cuvintelor (long tail ieftin, CPC real sub maxim), SRC-032 adaugă cuvinte negative, sitelink-uri, Bing. |
| DIG-1029 → **DIG-0922** programatic | Lanțul ad server → rețea → bursă → DSP/SSP/DMP (Zahay) + RTB, 87% programatic, critica Lammenett (date, bugete mari, pierdere de control) din SRC-032. Divergență explicită: standard operațional (Zahay) vs. instrument cu limite (Schwarz-Musch). |
| DIG-1033 → **DIG-0934** atribuire | Acum `debate`: Connors vede multi-touch ca soluție; SRC-032 arată că post-cookie urmărirea etapelor de început devine imposibilă; ambele măsoară corelație → incrementalitate, brand lift. |
| DIG-1035 → **DIG-0924** retargeting | Metoda pe etape (Connors, Zahay) + expunerea post-cookie (SRC-032), cerințele de consimțământ (Sachdev) și contrastul cu „rețeta” Facebook fără consimțământ (Nishad). |
| DIG-1036 → **DIG-0930** publicitate nativă | Acum `debate`: definiție comună (NAI/CMI); SRC-032 laudă ambiguitatea (XXXL Sports), Zahay și Sachdev cer etichetarea (FTC, „impresia netă”). |
| DIG-1017 → **DIG-0910** cookie-uri terțe | Mecanism + ce au făcut posibil + de ce dispar (e-Privacy, GDPR, ATT cu cifre). Divergență: Zahay/Sachdev anunță eliminarea din Chrome, SRC-032 consemnează renunțarea Google din iulie 2024. |
| DIG-0305 → **DIG-1021** strategie first-party | Ciclul celor trei întrebări (SRC-032) + cele cinci practici de colectare cu consimțământ (Ejeke) la întrebarea 3; avertismentul SRC-032 despre datele false din concursuri. |
| DIG-1031 → **DIG-0906** metric vs. KPI | Kaushik (în Zahay) + cele trei trepte și scorul compozit (SRC-032) + scara date → insight (Sachdev). |
| DIG-1005 → **DIG-0905** journey | Sachdev păstrează pâlnia AIDA ca hartă citită neliniar (cazul Seema); Zahay schimbă modelul (decision journey, buclă de loialitate). |
| DIG-0912 → **DIG-1006** persona | Distincția persona/grup țintă (SRC-032) + persona ca unealtă de design, storyboard (Zahay) + dozarea (Sachdev). Divergență: persona biografică vs. persona orientată spre decizie. |
| DIG-1011 → **DIG-0920** landing page | Criteriile MarketingExperiments + greșeala homepage-ului (Zahay, Sachdev) + context matching (SRC-032) + consecvența între canale (Sachdev). |
| DIG-0303 → **DIG-0201** omnicanal | Metoda Kotler (touchpoint-uri, scenarii critice, silozuri) + definiția și măsurarea prin CLV (DX Review) + cifrele Salesforce (Wuebben); cifrele lui Ejeke marcate ca neverificate. |

**Re-atomizare (fără ștergere):** DIG-0907 păstrează doar lanțul obiectiv SMART → metrici → diagnostic; tabelul metricilor pe etape s-a mutat în DIG-1032, care integrează acum și etapa de loialitate din Zahay (fig. 5.6) alături de Aware/Appeal/Ask din SRC-032.

**Tensiuni noi, semnalate prin `contrazice`:** DIG-0926 ↔ DIG-1022 (opt-out „minim acceptabil” la Zahay vs. căsuțe nebifate obligatorii sub GDPR; propoziție adăugată și în corpul DIG-0926), DIG-1001 ↔ MKT-0314 (7A completează 4P vs. EP² îi înlocuiește), DIG-1025 ↔ INS-1503 (implicarea ca atribut de categorie vs. risc perceput), DIG-1101 ↔ DIG-1025 (journey scurt vs. faza lungă la implicare mare), DIG-0933 ↔ ADV-1301 (A/B vs. conjoint), DIG-0932 ↔ EXP-0901 (CRM vs. CX).

Note scurtate ușor (detalii redundante): DIG-0103, 0202, 0204, 0205, 0926, 0931; DIG-1019 a primit o propoziție de convergență cu Zahay.

## 3. Note noi

| ID | Titlu (scurt) | Surse verificate în `90-library/text/` |
|---|---|---|
| DIG-9901 | Accesibilitatea digitală — condiție de UX și risc legal (alt text, subtitrări, culoare, cititoare de ecran) | SRC-031 cap. 4 p. 122-123, cap. 7 p. 238, cap. 8 p. 283, cap. 11 p. 375-377; SRC-029 cap. 6 p. 176 (cazul Target, 6 mil. $) |
| DIG-9902 | Proprietatea intelectuală în conținutul digital — mărci, domenii, copyright, fair use, Creative Commons | SRC-031 cap. 4 p. 122, cap. 11 p. 370-375 (cazul NCAA / UDRP) |

DIG-9902 e completată de STO-9901 (agentul STO), care dă regulile de producție pe social; cele două note se leagă reciproc.

## 4. Duplicate între skill-uri (nu le-am atins; legate prin `vezi` / `alternativa`)

| DIG | Alt skill | Observație |
|---|---|---|
| DIG-0925 owned/earned/paid | ADV-0617 (acum include PESO, după comasarea ADV-1101) | aceeași tipologie; candidat la comasare sau la o hartă comună |
| DIG-0930 publicitate nativă | ADV-0408, HIS-0820 | trei unghiuri (digital, psihologic, istoric) ale aceleiași forme |
| DIG-0929 personalizare și reactanță | AIM-0301, ADV-0410 | aceeași tensiune; AIM-0301 e cel mai apropiat |
| DIG-1015 zece practici de confidențialitate | AIM-1305 | AIM-1305 e o versiune scurtă a aceleiași liste |
| DIG-1006 persona ≠ grup țintă | INS-1306 | aceeași teză, altă sursă (SRC-040) |
| DIG-0921 display | ART-1001 | formate IAB în ambele; ART-1001 are regulile de design |
| DIG-0905 journey | MKT-0210 (5A), ADV-0501 | trei modele de journey, legate ca alternative |
| DIG-0931 demand generation / DIG-1007 buying center | CLI-9902 | centrul de cumpărare B2B apare în ambele skill-uri |

## 5. Goluri rămase

- **Incrementalitate și marketing mix modeling**: doar menționate (DIG-0934, cu trimitere la AIM-1323 și INS-0419); biblioteca nu are un capitol dedicat.
- **Retail media, social commerce, TikTok ads, afiliere**: neacoperite de surse.
- **SEO pentru motoarele de răspuns cu AI** (căutare fără clic): doar întrebări de seminar în DIG-0302, DIG-0917.
- **Configurarea analytics** (evenimente GA4, tag manager): doar la nivel de concepte (DIG-0907, DIG-0934).
- **Legislația UE recentă** (DSA, actul european privind accesibilitatea): nu e în surse; notele citează GDPR, e-Privacy, ADA, FTC.
- Publicitatea pe Meta/Facebook stă în SOC (SOC-1004, SOC-1006); DIG trimite acolo din DIG-0919 și DIG-0924.

## 6. Pentru orchestrator

- `merges-DIG.txt` are 12 rânduri. Note din alte foldere care încă trimit spre ID-urile DIG comasate (de redirecționat): AIM-0301, ART-1001, BRD-0301, CPY-1001, MKT-1001, SOC-0901, SOC-1002/SOC-1118, SOC-1004, SOC-1008, STO-0903/STO-0202 și fișele SRC-029, SRC-031.
- În notele DIG am redirecționat deja legăturile spre ID-urile comasate de alți agenți, după `merges-*.txt` existente la final (ex. ADV-0102→ADV-0401, ADV-1001→ADV-0103, ADV-1101→ADV-0617, AIM-0205→AIM-1303, BRF-1001→BRF-1501, EXP-1205→EXP-0901, INS-0107→INS-0430, SOC-0101→SOC-1115, SOC-1002→SOC-1118, STO-0903→STO-0202). Dacă alți agenți mai comasează după mine, redirecționarea automată le acoperă.
- Fișierele KEEP își păstrează numele vechi chiar unde titlul s-a schimbat; `renumber` le va redenumi. Blocurile backlinks și `auto:notes` din SKILL.md conțin încă intrări vechi până la `build`.
- Paginile din notele G09/G10 sunt pagini PDF (marcajele `=== [page N] ===`); la SRC-029 tipărit = PDF − 14, la SRC-031 tipărit ≈ PDF − 19.
- Sugestie de hărți `30-maps/`: „Date, confidențialitate și lege în publicitate” (DIG-0910, 1015, 1016, 1021, 1022, 9902, AIM-1305, SOC-1118, STO-9901) și „Măsurare și eficiență” (DIG-0906, 0934, 1032, ADV-0103, ADV-1528, INS-0419, AIM-1323), cum propuneau și rapoartele G09/G10.
