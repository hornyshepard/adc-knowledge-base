# Raport P2-PIT — Faza 2: pitch-presentation

Agent: P2-PIT-PRT-CLI · skill: `pitch-presentation` (PIT) · data: 2026-10-01

## 1. Note înainte / după

| | Număr |
|---|---|
| Note înainte | 35 (32 din G14 — Colenso, Nishad; PIT-0501 din G05 — Peters; PIT-0601, PIT-0602 din G06) |
| Comasări (DROP) | 0 |
| Note noi | 1 (PIT-9901) |
| Note după | **36** |
| `status: growing` | 35 (toate, cu excepția PIT-1432, verificată și lăsată `seed`) |

`merges-PIT.txt` e gol: nu am găsit duplicate reale în skill. Perechile apropiate sunt concept + aplicare sau surse care se completează și au rămas separate, legate între ele: PIT-1424 (nervii, Colenso) / PIT-1432 (dezbaterea Colenso–Nishad), PIT-1420 (etapele repetiției) / PIT-1431 (bucla video), PIT-0602 (frazarea, Muller) / PIT-1425 (energia și vocea, Colenso).

## 2. Ce am făcut

- **Legături:** am adăugat 47 de legături tipizate în 34 de note. Aproape toate notele Colenso aveau doar legături interne PIT. Acum fiecare notă are 3–6 legături, iar 33 din 36 au cel puțin una spre alt skill sau alt grup (INS, CPY, STO, BRF, ADV, ART, MKT, CLI, PRT, IDE).
- **Convergențe și dezacorduri scrise în text** (cu sursa adăugată în `sources`):
  - PIT-1408 — regula celor trei mesaje la Colenso și Nishad, plus Milavsky (SRC-021, CPY-0605);
  - PIT-1422 — formula P + + – P are temei în mesajul bilateral (Fennis & Stroebe, SRC-012, CPY-0402);
  - PIT-1423 — pasul „Relate", sprijinit de Milavsky (SRC-021, INS-0607);
  - PIT-1407 — Know–Feel–Do în tensiune cu critica ierarhiilor de efecte (SRC-012, ADV-0401, `contrazice`);
  - PIT-1416 — „eroul e clientul" la Colenso și la Richards & McLean (SRC-040, STO-1303);
  - PIT-0602 — diagnosticul comun Muller–Colenso (SRC-043).
- **Legături repuse după comasările altor agenți:** PIT-0601 → ADV-1506 (înlocuiește ADV-0612) și PIT-1407 → ADV-1502 (înlocuiește ADV-0614), conform `merges-ADV.txt`.
- **SKILL.md** scris complet: 7 competențe, traseu în 6 secțiuni (Fundamente → Discover → Distil & Design → Drill & Debrief → Deliver → Prezentarea muncii creative la client), 7 surse cu rating, 6 skill-uri vecine, 6 playbook-uri. Am verificat cu `kb.py renumber --dry-run` că ordinea viitoarelor ID-uri urmează traseul (PIT-1401 → PIT-001 … PIT-0501 → PIT-036).

## 3. Notă nouă

| ID | Titlu | Surse |
|---|---|---|
| PIT-9901 | Prezentarea muncii creative la client are un ritual — strategia recitită, ideea dezvăluită, întrebări în loc de soluții, pasul următor cerut | SRC-021 cap. 7–8 (p. 125–135); SRC-022 cap. 8; SRC-017 cap. 2; SRC-025 cap. 1 (Greg Hahn) |

De ce: brief-ul cerea un traseu clar pentru „prezentarea muncii creative la client", iar G14 semnalase lipsa lui. Nota pune cap la cap patru perspective (managerul de la client, clientul, designerul, directorul de creație) în cinci mișcări. Ea deschide secțiunea 6 a hărții, alături de PIT-0601 și PIT-0501 și de lecturile din alte skill-uri: BRF-0711, BRF-0712, CPY-0606, CLI-0602, CLI-0701, CLI-9905.

## 4. Duplicate și suprapuneri cu alte skill-uri (neatinse, doar legate)

| Nota mea | Nota din alt skill | Natura suprapunerii |
|---|---|---|
| PIT-0501 | ART-0507 | Amândouă descriu prima prezentare a celor 15 semne (Peters). PIT păstrează vânzarea și feedback-ul, ART procesul. Legate prin `fundament`. |
| PIT-1416 | STO-1303 | „Eroul e clientul, nu brandul", din surse diferite (Colenso/Miller vs. Richards & McLean). Legate prin `vezi`. |
| PIT-1407 | ADV-0401, ADV-1502, BRF-0719 | Know–Feel–Do față de gândește–simte–acționează și efectele de comunicare. Modele înrudite, nu duplicate. |
| PIT-1408 | CPY-0605, BRF-0707 | Regula celor trei mesaje sau argumente și beneficiul unic. Principii convergente. |
| PIT-1412 | INS-0440 | Dovada socială (Cialdini). |
| PIT-9901 | BRF-0711 | Aceeași ședință de creație văzută din cele două părți. Complementare. |

## 5. Goluri rămase

- Nicio sursă despre **pitch-ul de new business al agenției** ca format: credentials, chemistry meeting, pitch-ul condus de achiziții. Colenso îl atinge doar în treacăt (PIT-1403, PIT-1413, PIT-1414).
- **Prezentarea datelor** (grafice, cifre spuse pe scenă) e doar în PIT-1418, principiul 2.
- Regula peak-end și studiul despre prima impresie în 33 ms vin indirect, prin Colenso; în INS nu există o notă-sursă pentru ele.
- Nishad (SRC-044) e subțire: pare transcrierea unui curs video. Notele bazate pe el (PIT-1431, PIT-1432) îl folosesc doar ca a doua voce.

## 6. Pentru orchestrator

- `kb.py check`: 0 probleme în `20-skills/pitch-presentation/`.
- În rădăcina KB există două fișiere goale (0 octeți), probabil create din greșeală: `ADV-0603.md` și `PRT-0501.md`. `kb.py` le ignoră (nu au frontmatter), dar ar trebui șterse. Nu le-am atins, pentru că sunt în afara folderelor mele.
- Harta din SKILL.md conține și ID-uri din alte skill-uri, pe rânduri „Din alte skill-uri…". `renumber` le ignoră; am verificat.
