# Raport P2-INS — integrarea skill-ului consumer-insight (INS)

Agent P2-INS, Faza 2. Skill: `20-skills/consumer-insight/`.

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente | 98 | 95 (98 − 4 comasate + 1 nouă) |
| Note cu `status: growing` | 0 | 95 |
| Note cu 2–6 legături tipizate și cel puțin una spre alt grup de cărți sau alt skill | 76 | 95 |
| Note fără nicio legătură în afara propriului grup Faza 1 (ex. INS-04xx doar spre INS-04xx) | 22 | 0 |
| Lungime corp (`kb.py`) | 282–516 cuvinte | 303–526 cuvinte |

`kb.py check`: nicio problemă în fișierele `consumer-insight` la ultima rulare.

## 2. Comasări (în `merges-INS.txt`)

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| INS-0107 (ELM, Grewal-Levy) | INS-0430 (ELM/HSM, Fennis-Stroebe) | Versiunea de manual a ELM (Laura/Macy's), lectura lui Percy (risc mic: execuția ajunge; risc mare: argumentul trebuie crezut), plus paragraf „unde converg autorii"; surse SRC-012 + SRC-001 + SRC-049. Cele trei tipuri de decizie (extinsă, limitată/impuls, obișnuință) au fost mutate în **INS-0109**, retitlată „Implicarea și diferențele percepute între branduri dau tipul de decizie…". |
| INS-0446 (psihanaliza, Parsons et al.) | INS-0601 (cercetarea motivațională, Fernández Gómez) | Dichter (trei straturi de motive, decapotabila-„amantă", „permisiunea de a te bucura fără vinovăție"), Bernays, critica Packard/Vicary, reabilitarea ca „concepte care sensibilizează" (Williamson, Klein). Notă retitlată și trecută la `kind: debate`; dezacordul explicit: Fernández Gómez (mașină de vânzare) vs. Parsons et al. (vocabular util) vs. Fennis-Stroebe (fără experiment nu e dovadă). Exemplele de sarcini proiective au mers în **INS-1209**. |
| INS-0501 (Braig, „de ce" insistent și fricțiuni) | INS-0702 (McTigue, „ce" → „de ce") | Fricțiunile Braig (KABOOM, Clorox), „de ce contează?" repetat, critica Ford/Jobs; convergența celor trei surse și tensiunea despre focus grupuri (Braig vs. McTigue). Partea despre persona a mers în **INS-1306** (sursă SRC-014 adăugată). |
| INS-0445 (consumul postmodern, Brown via Parsons) | INS-1206 (consumatorul postmodern, Firat & Venkatesh via Batat) | Un singur tabel cu cele două liste de trăsături, linking value, consum solid/lichid, critica Parsons et al. și post-postmodernismul; nivel 3 → 2. |

## 3. Note noi

- **INS-9901** — *Checklist-ul insight-ului — opt verificări înainte ca un „adevăr despre țintă" să intre în brief* (checklist, nivel 2). Golul: pasul final al traseului (verificarea formulării) era împrăștiat în INS-0701, INS-0602, BRF-0715, BRF-0719. Nota strânge testele din SRC-022 (cap. 4: Grand Furniture, Luvs, ambalajul de carne, Stark revizuit), SRC-019 (outil 19, dilema), SRC-025 (cap. 6: Bullmore, Angear, insight fix/dinamic) și SRC-023 (Singleton „helpful insight", triangularea Euro RSCG). Toate pasajele au fost verificate în `90-library/text/`. Face puntea INS → BRF ([[BRF-0702]], [[BRF-0703]]).

## 4. Legături și integrare între autori

Principalul câștig: notele G04 (Fennis & Stroebe), G15 (Percy & Rosenbaum-Elliott), G06 (Milavsky, *La boîte à outils*), G01 (Grewal & Levy), G12 (Batat), G13 (Struhl) și G07 (McTigue) se citează acum reciproc. Convergențe și dezacorduri scrise explicit în corpul notelor:

- **Implicarea** e a persoanei, nu a produsului: Fennis-Stroebe (INS-0401), Grewal-Levy (INS-0109), Percy (INS-1503). INS-1503 `contrazice` ADV-0402: critica Fennis-Stroebe la grila Rossiter-Percy lovește folosirea pe categorii, nu definiția lui Percy.
- **Atitudinea**: Grewal-Levy (ABC, INS-0106) vs. Percy (fără conație, INS-1506) — legătură `contrazice` în ambele sensuri.
- **Subliminal/inconștient**: INS-0439 (efecte mici, condiționate) ↔ INS-1511 (niciun efect) ↔ INS-0402/0412/0414/0421 — `contrazice`, cu paragraf de tensiune.
- **Frica**: INS-0433 (meta-analiza: mai multă frică, mai multă persuasiune) ↔ INS-1507 și ADV-1532 (frică moderată, U inversat).
- **Credibilitatea sursei**: INS-0606 (Milavsky) ≈ INS-0432 (Fennis) ≈ INS-1505 (VisCAP).
- **Focus grupuri și recall**: patru surse converg (INS-1303, INS-0419, INS-0412, ADV-1530, INS-0702).
- **Frâna ca insight**: INS-0417 (alfa/omega) ≈ ADV-0609 (Joannis) ≈ INS-0602 (dilema) ≈ BRF-0714 (Stark).
- **Motivația**: trei tipologii legate `alternativa` (INS-0102, INS-0428, INS-1504).
- **Memoria de lucru și efectul Google**: INS-0411 ↔ INS-1510; INS-0443 ↔ INS-1509.

## 5. Duplicate între skill-uri (legate, necomasate)

| Nota INS | Nota din alt skill | Relație pusă |
|---|---|---|
| INS-0406 (pionierul stabilește agenda atributelor) | BRD-0514 (pionier, urmăritor, intrat târziu) — aceeași cercetare Carpenter & Nakamoto | `vezi` + paragraf în INS-0406 |
| INS-0439, INS-1511 (subliminal) | HIS-0817 (mitul subliminal) | `vezi` în ambele |
| INS-1306 (personas, nu segmente) | DIG-1006 (buyer persona ≠ grup țintă), DIG-0912 | `vezi` |
| INS-0427 (expectanță-valoare) | BRD-1503 (beneficiul de poziționare cu expectanță-valoare) | `aplicare` |
| INS-0417 (alfa/omega) | ADV-0609 (axa psihologică Joannis) | `alternativa` |
| INS-1303, INS-0412 | ADV-1530 (pretestul fără focus grup și fără recall) | `aplicare` |
| INS-0603 (cantitativ vs. calitativ) | MKT-0126 | `vezi` |
| INS-0605 (creierul rapid) | ART-0501 (designul lucrează în Sistemul 1) | `vezi` |

## 6. Goluri rămase

- **Aversiunea la pierdere, teoria perspectivei, efectul de înzestrare**: absente din bibliotecă (grep fără rezultate în SRC-001, 012, 013, 021), deci nu am creat notă.
- **Neuroștiința în cercetarea de brand** (*Kellogg on Branding*, cap. 14): biblioteca o acoperă, dar nu există notă; candidat pentru INS sau AIM.
- **Hărți transversale utile** (pentru `30-maps/`): „Cercetare și măsurare" (INS-05 + ADV pretest + AIM trade-off + DIG A/B) și „Etica persuasiunii" (INS-0420, 0434, 0438, 0105, 1509; CPY-0401; BRD-0402), cum propunea și raportul G04.

## 7. Pentru orchestrator

- Ordinea din „Harta notelor" din `SKILL.md` (6 secțiuni, 18 + 24 + 23 + 10 + 16 + 4 = 95 de note) e ordinea de renumerotare dorită.
- Titluri schimbate (slug-ul de fișier e păstrat până la `renumber`): INS-0109, INS-0601, INS-0702.
- Ținte retrimise deja în notele mele, după `merges-ADV/BRD/EXP.txt`: ADV-0102 → ADV-0401, ADV-0106 → ADV-0604 (în INS am ales ținte mai potrivite: CPY-0403, ADV-1513, ADV-1511), BRD-0104 → BRD-0512, BRD-0205/BRD-0401 → BRD-0606, EXP-0204 → EXP-1210, EXP-1205 → EXP-0901. Dacă alte skill-uri mai comasează după acest raport, redirect-ul final le va acoperi.
- Legături din alte skill-uri spre notele mele comasate (de redirecționat): ADV-0106 și DIG-0104 → INS-0107; ADV-0501 și ADV-0502 → INS-0501; EXP-0401 și MKT-0401 → INS-0445; SRC-001, SRC-013, SRC-014 → notele comasate.
- Secțiunile `<!-- backlinks -->` din notele rescrise au fost golite; `kb.py build` le regenerează.
