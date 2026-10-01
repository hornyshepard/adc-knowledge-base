# Raport P2-HIS — integrarea skill-ului Istoria și cultura publicității

Agent: P2-CPY-ART-HIS (deține și CPY, ART). Data: 2026-10-01.

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente HIS | 28 | 29 (+1 nouă, nicio comasare) |
| Note cu `status: growing` | 0 | 29 |
| Legături tipizate pe notă | 3–6 | 5–6 (toate au cel puțin o legătură spre alt grup de cărți sau alt skill) |

`kb.py check`: nicio problemă în fișierele HIS.

## 2. Comasări

Niciuna (`merges-HIS.txt` conține doar un comentariu). 27 de note vin dintr-un singur grup (G08: Richards + Watkins), deci erau deja coerente între ele, dar legate aproape numai între ele. Am adăugat pentru fiecare legături spre ADV, INS, CPY, ART, DIG, SOC, STO, MKT, CLI, PRT, AIM.

## 3. Etica și reglementarea — grupate într-o singură secțiune

Rapoartele G01, G04, G06, G07, G08, G09, G10 și G11 au semnalat că etica și reglementarea n-au casă. În `SKILL.md`, **secțiunea 6, „Etică, reglementare și limitele publicității"**, adună cele nouă note HIS pe temă, în ordinea unui raționament: HIS-0806 (leacurile-minune), HIS-0807 (autoreglementarea), HIS-0808 (standardul FTC), HIS-0825 (demonstrația reală), HIS-0820 (reclama deghizată), HIS-0817 (subliminalul), HIS-0818 (șocul), HIS-0824 (tutunul), HIS-0823 (diversitatea). Secțiunea începe cu lista notelor înrudite din alte skill-uri (CPY-0401, ADV-0108, SOC-1118, DIG-0930, STO-0709, ADV-0302, INS-0420, AIM-1305), ca punct de plecare pentru harta transversală de etică.

## 4. Notă nouă (Phase 2)

- **HIS-9901** — Fiecare mediu nou refuză întâi reclama, apoi trăiește din ea, până când aglomerația naște tehnologia de evitare. Surse: SRC-027 cap. 11, p. 242–243; cap. 14, p. 302–304; cap. 15, p. 347–354; SRC-032 pentru CTR-ul de azi. Golul era epoca radio–TV–internet: skill-ul se oprea practic la anii '60–'90. Nota leagă HIS-0804 (presa), HIS-0820 (native), ART-1001 (bannerul) și ADV-1528 (scepticismul lui Percy față de digital).

## 5. Revizii de conținut

- **HIS-0810** (genealogia stilurilor): l-am păstrat pe unghiul istoric, cum s-a cerut. Nota trimite explicit spre CPY-0601 și CPY-0803 pentru meșteșug și spre ADV-0607 și ADV-0604 pentru strategie (USP vs. imagine).
- **HIS-0817** (subliminalul): am adăugat dezacordul dintre surse. Percy & Rosenbaum-Elliott (INS-1511) îl declară mit inventat. Fennis & Stroebe (INS-0439) admit un efect îngust, la oameni care au deja scopul. Am notat și că cifrele lui Vicary apar inversate de la o carte la alta. Am adăugat SRC-012 și SRC-049 la surse.
- HIS-0601: legat de ADV-1519, unde Percy susține același lucru: jargonul nou nu schimbă mecanismul.
- Am înlocuit legăturile spre hub-uri cu legături spre note. Am corectat relațiile folosite invers (de exemplu `exemplu`/`aplicare` puse din perspectiva țintei).

## 6. Duplicate între skill-uri

| Nota HIS | Nota din alt skill | Relație |
|---|---|---|
| HIS-0817 subliminalul (istorie) | INS-0439 (efect îngust), INS-1511 (mit), INS-0601 (cercetarea motivațională) | același subiect, trei poziții; legate cu `contrazice` / `vezi` |
| HIS-0815 AIDA (genealogie) | ADV-0401, ADV-1302, ADV-1503, MKT-0210 | istoria modelului vs. critica și alternativele lui |
| HIS-0820 reclama deghizată | DIG-0930 (DIG-1036 comasată în ea), ADV-0408, SOC-1118 | istorie vs. reguli actuale |
| HIS-0810 stilurile de copy | ADV-0607 (Reeves vs. Ogilvy), CPY-0601, CPY-0803 | istorie / strategie / craft |
| HIS-0818 shockvertising | IDE-0710 (dezbaterea despre șoc) | cazuri istorice pentru dezbatere |
| HIS-0823 diversitatea | ADV-0302, STO-0709, ADV-0411 | istorie vs. checklist-uri actuale |
| HIS-0601 invenția recurentă | ADV-1519 | aceeași teză, surse diferite |
| HIS-0816 account planning | ADV-0620 (planning strategic) | istorie vs. metodă |

## 7. Goluri rămase

- **Context european și românesc**: biblioteca e centrată pe SUA (Richards, Watkins). Lipsesc istoria publicității în România, ARPP/RAC și legislația UE (UCPD, consumatorul mediu). HIS-0807 și HIS-0808 menționează doar în treacăt Codul RAC și standardul UE.
- **Istoria televiziunii ca mediu creativ** (spotul, anii '80–'90) și **istoria agențiilor holding**: acoperite doar tangențial.
- **Critica publicității** (Packard, Galbraith, materialismul): doar prin HIS-0817 și INS-0420.

## 8. Pentru orchestrator

- Ordinea de renumerotare e cea din `SKILL.md`: HIS-0801 devine HIS-001, HIS-9901 devine HIS-005, secțiunea de etică ocupă ultimele nouă poziții.
- În notele mele am redirecționat deja DIG-1036 → DIG-0930. Duplicatul de legătură rezultat în HIS-0820 a fost eliminat.
