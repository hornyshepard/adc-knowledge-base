# Raport P2-PRT — Faza 2: portfolio

Agent: P2-PIT-PRT-CLI · skill: `portfolio` (PRT) · data: 2026-10-01

## 1. Note înainte / după

| | Număr |
|---|---|
| Note înainte | 27 (26 din G14 — Fenn, Kubišová, Morgan; PRT-0501 din G05 — Peters) |
| Comasări (DROP) | 0 |
| Note noi | 0 |
| Note după | **27** |
| `status: growing` | 22; lăsate `seed` după verificare (erau deja bine legate): PRT-1401, PRT-1406, PRT-1417, PRT-1418, PRT-1423 |

`merges-PRT.txt` e gol. Perechile cele mai apropiate sunt principiu + metodă și au rămas separate, legate între ele:

- PRT-1405 (calitatea bate volumul) / PRT-1422 (metoda DA–NU–POATE);
- PRT-1402 (două documente) / PRT-1423 (trei tipuri de portofoliu);
- PRT-1409 (structura studiului de caz) / PRT-1424 (textul pe pagină);
- PRT-1417 (CV-ul vizual, Morgan) / PRT-1426 (CV-ul funcțional, Kubišová) — două filozofii, cu tensiunea notată în PRT-1418.

## 2. Ce am făcut

- **Legături:** am adăugat 24 de legături tipizate în 22 de note (23 din 27 de note au acum cel puțin o legătură spre alt skill sau alt grup de cărți). Fiecare notă are acum 3–6 legături; skill-urile țintă sunt PIT, CLI, ART, CPY, STO, BRD, MKT, IDE, SOC, HIS și BRF.
- **Convergență scrisă în text:** PRT-0501 — Peters (proiectele personale) și Fenn (arată doar munca pe care vrei s-o faci) spun același lucru. Am adăugat SRC-048 în `sources`.
- **SKILL.md** scris complet: 7 competențe, traseu în 6 secțiuni (Fundamente → Materia primă și selecția → Structură, ritm, format → Scrisul și designul paginii → Pachetul de aplicare → Distribuție, brand personal, critică), 5 surse cu rating, 6 skill-uri vecine, 6 playbook-uri. Ordinea de renumerotare e verificată cu `renumber --dry-run` (PRT-1401 → PRT-001 … PRT-1413 → PRT-027).

## 3. Note noi

Niciuna. Skill-ul acoperă bine construcția portofoliului. Golurile reale (mai jos) nu au acoperire în bibliotecă.

## 4. Duplicate și suprapuneri cu alte skill-uri (neatinse, doar legate)

| Nota mea | Nota din alt skill | Natura suprapunerii |
|---|---|---|
| PRT-1419 | CLI-1402 | Lista „Dream 10" de agenții e Dream 100 aplicat carierei. Legate. |
| PRT-1403 | IDE-0712 | Jurnalul de lucru și banca de inspirație: aceeași disciplină a colecționării. |
| PRT-1402 | PIT-1418 (principiul 6) | Deck-ul de prezentare ≠ documentul lăsat. Aceeași regulă, la Fenn și la Colenso. |
| PRT-1409 | PIT-1416 | Brief–Ce am făcut–Rezultate față de SOLVE: structuri alternative pentru un caz. `alternativa` în ambele sensuri. |
| PRT-0501 | IDE-0501 | Proiectele personale de inspirație ale lui Peters. Înrudite, nu duplicate. |
| PRT-1414 | BRD-0503 | Fraza lui Hoffman e o declarație de poziționare. Nu există altă notă de branding personal în BRD. |

## 5. Goluri rămase

- **Nicio sursă specifică publicității** pentru portofoliu: book-ul de copywriter sau art director, case film-ul de festival, portofoliul de strateg. Notele transferă din UX și arhitectură, iar întrebările din note semnalează explicit transferul (PRT-1407, PRT-1409).
- **Interviul propriu-zis** (întrebări tipice, negocierea salariului, proba practică) nu e acoperit.
- **Producția fizică a portofoliului tipărit** (SRC-046, pașii 5–7) nu a fost transformată în note. E tehnică și ține mai degrabă de ART.
- Morgan (SRC-047, 2014) are date și platforme învechite (Google+, Klout). Notele le semnalează, iar dezbaterea PRT-1418 le pune în context.

## 6. Pentru orchestrator

- `kb.py check`: 0 probleme în `20-skills/portfolio/`.
- Câteva note au 450–520 de cuvinte după numărătoarea `kb.py` (PRT-1407, PRT-1411, PRT-1412, PRT-1418, PRT-1426): peste ținta de 400, sub pragul de 650. Le-am lăsat întregi, pentru că fiecare rămâne atomică.
- Fișierul gol `PRT-0501.md` din rădăcina KB (0 octeți) nu e nota reală, care se află în `20-skills/portfolio/notes/`. Ar trebui șters.
- Sugestie de taxonomie, preluată de la G14: scopul PRT din `skills.json` ar putea menționa explicit „carieră și angajabilitate" (CV, LinkedIn, rețea), pentru că PRT-1414, PRT-1419, PRT-1420 și PRT-1426 țin de asta.
