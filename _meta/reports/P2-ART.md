# Raport P2-ART — integrarea skill-ului Direcție artistică și identitate vizuală

Agent: P2-CPY-ART-HIS (deține și CPY, HIS). Data: 2026-10-01.

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente ART | 27 | 29 (+2 noi, nicio comasare) |
| Note cu `status: growing` | 0 | 29 |
| Legături tipizate pe notă | 3–6 | 4–6 (toate au cel puțin o legătură spre alt grup de cărți sau alt skill) |

`kb.py check`: nicio problemă în fișierele ART.

## 2. Comasări

Niciuna (`merges-ART.txt` conține doar un comentariu). Notele de identitate (G05, Peters/Calder) și cele de idee vizuală (G07, Ingledew) sunt înrudite, dar nu duplicate. Le-am legat cu relații tipizate.

## 3. Traseu coerent pentru un skill amestecat

Skill-ul combina trei familii: identitate și logo (*Logos That Last*, Calder), tehnici de idee vizuală (Ingledew, Milavsky) și tactici vizuale din cercetare (Percy, ART-15xx). Plus lecții istorice (G08) și un banner (G10). Harta din `SKILL.md` le ordonează așa:

1. cum e privită o reclamă (imagine, culoare, tipografie, privire);
2. ideea vizuală de campanie;
3. identitatea: de la asociații la semn;
4. sistemul de identitate în timp: consecvență, redesign, ambalaj;
5. lecții din istorie;
6. avansat: canale, culturi, persuasiune implicită.

## 4. Note noi (Phase 2)

- **ART-9901** — Culoarea spune povestea, diferențiază și motivează; saturația contează mai mult decât nuanța. Surse: SRC-017 „Color Palette", SRC-016 interviul cu Laura Guido-Clark, SRC-049 cap. 13, SRC-031 cap. 3, SRC-014 cap. 7. „Culoarea" era în scope fără notă proprie. Nota arată și dezacordul: tabelele populare de semnificații (Sachdev) față de saturație și luminozitate (Guido-Clark).
- **ART-9902** — Ambalajul se proiectează și pentru viața de după cumpărare: forma ca indiciu, beneficiul repetat la fiecare folosire. Surse: SRC-049 cap. 15, SRC-014 cap. 7. Golul fusese semnalat în rapoartele G03 și G15. **Atenție:** agentul ADV a scris în paralel **ADV-9901** (ambalajul la raft), din același pasaj Percy. Am rescris ART-9902 pe unghiul de design (reclama după cumpărare, Rossiter & Bellman; forma ca indiciu, Calder), cu ADV-9901 ca `fundament`. Suprapunerea rămasă e mică, dar perechea e de verificat.

## 5. Revizii de conținut

- Au primit secțiunea „Exemplu", care lipsea: ART-0703 (Pearson, *Penguin by Design*), ART-0704 (Fukuda, *Sea Cannot Be Cut Apart*), ART-0705 (seria HSBC), ART-0706 (felicitările johnson banks). Exemplele au fost mutate din explicație, nu dublate.
- ART-0503: am adăugat SRC-049 (aceeași scădere Tropicana de circa 20%, citată de Percy): două surse independente confirmă cazul.
- Am tăiat ART-1503 (de la 560 la circa 430 de cuvinte) și ART-1501. Am scurtat titlul la ART-1001.
- Am adăugat legături spre alte grupuri, mai ales pentru notele G05, care aveau doar legături interne: ART-0505/0506 → IDE-0704/0705/0707, ART-0509 → BRD-1505, STO-1108, ART-0511 → BRD-1505, CPY-0817.

## 6. Duplicate între skill-uri

| Nota ART | Nota din alt skill | Relație |
|---|---|---|
| ART-9902 ambalajul după cumpărare | ADV-9901 ambalajul la raft | aceeași sursă (SRC-049 cap. 15); unghiuri diferite, legate cu `fundament` |
| ART-0511 hardware/software, ART-0509, ART-0701 | BRD-1505 (look & feel consecvent, Percy) | aceeași idee de consecvență vizuală din trei surse |
| ART-1001 bannerul | DIG-0921 (evoluția display) | execuție vs. evoluția formatului |
| ART-0702/0703/0704 | IDE-0705/0706/0707 | tehnicile Ingledew împărțite între ART (limbaj vizual) și IDE (mecanismul ideii) |
| ART-0401 privirea | DIG-0104 (mobil, fețe), DIG-0913 (convenții web) | compoziție vs. format |

## 7. Goluri rămase

- **Compoziție și ierarhie tipografică** (grid, contrast, aliniere): acoperite doar indirect (ART-1503, ART-0801, ART-0508). Cărțile de portofoliu (SRC-046, SRC-048) ar putea da o notă de bază.
- **Design pentru social și video vertical**: doar ART-1001 și, în DIG, DIG-0104. Ar merita o notă dedicată dacă biblioteca o permite.
- **Fotografia și ilustrația ca alegeri de direcție artistică**: lipsesc ca note proprii.
- **Audio branding**: semnalat de G15; nu se potrivește în ART (vizual) și nici în CPY. Propun o hartă sau o notă BRD/EXP.

## 8. Pentru orchestrator

- Ordinea de renumerotare e cea din `SKILL.md`: ART-1503 devine ART-001, ART-9901 devine ART-002.
- În notele mele am redirecționat deja legăturile BRD-0105 → BRD-0508 și DIG-1011 → DIG-0920.
