# Raport P2-BRF — integrarea skill-ului creative-brief (BRF)

Agent P2-BRF-IDE, Faza 2. Skill: `20-skills/creative-brief/`. (Același agent a integrat și IDE; vezi `P2-IDE.md`.)

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente | 26 | 27 (26 − 1 comasată + 2 noi) |
| Note cu `status: growing` | 0 | 27 |
| Legături tipizate per notă | 3–5 | 5–6 |
| Note fără nicio legătură tipizată în afara propriului grup Faza 1 și skill | 7 | 0 |
| Note fără secțiunea „Exemplu" | 9 | 0 |
| Lungime corp (`kb.py words`) | 345–465 | 386–527 (tabelele umflă numărătoarea; nicio notă peste pragul de 650) |

`kb.py check` (ultima rulare): **nicio problemă în fișierele `creative-brief`**. Singura legătură ruptă legată de BRF este `10-sources/SRC-032 → BRF-1001`, așteptată până la redirect. Am rulat o dată `kb.py renumber --dry-run` (doar afișare, fără scriere) ca să verific că ordinea din harta `SKILL.md` e cea dorită: BRF-0701 → BRF-001 … BRF-0708 → BRF-027.

## 2. Comasări (în `merges-BRF.txt`)

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| BRF-1001 (brief-ul campaniei digitale, Schwarz-Musch et al., SRC-032) | BRF-1501 (documentul de briefing, Percy & Rosenbaum-Elliott, SRC-049) | Am verificat în text: SRC-032 (cap. 2.2.1, p. 40–41) își construiește explicit cele patru blocuri pe Percy & Rosenbaum-Elliott. KEEP-ul are acum ambele surse: tabelul celor cinci arii Percy, rearanjarea în patru blocuri, adaosul digital (buyer persona, customer journey, obiective pe fiecare fază), citatul Davis („atâtea metode de briefing câți oameni"), exemplul e-mountain bike. Retitlată: „Documentul de briefing precede strategia — produs, piață, sursă de business, concurență și obiective, plus persona și journey-ul ei în digital"; `also` + digital-marketing. |

**Păstrate separat, legate ca `alternativa`** (modele diferite, nu aceeași idee):
- BRF-0705 (poziționare în patru piese, McTigue–Rucker) ↔ BRF-1502 (trei variabile, Percy). Ambele au acum un paragraf de comparație: aceeași formulă la Tybout & Calkins (BRD-0503); Percy renunță la RTB și înlocuiește cadrul de referință cu nevoia de categorie; diferență de școală („de ce m-ar alege?" vs. „ce este? / ce oferă?").
- BRF-0702 (șase componente) ↔ BRF-1503 (trei blocuri Percy).
- BRF-0601 (brief client vs. brief creativ, Barre) ↔ BRF-1501 (documentul de briefing).

## 3. Note noi

- **BRF-9901** — *Primirea brief-ului — îl reduci la esență, îl verifici pe componente, pui întrebările naive și agreezi în scris orice schimbare* (method, nivel 2). Golul: scope-ul skill-ului cere „cum primești un brief, debriefing", dar nicio notă nu privea brief-ul din partea celui care îl primește. Surse verificate în `90-library/text/`: SRC-024, „Strategies for solving a creative brief", etapele 1–2 (`a-to-z-visual-ideas.txt` r. 520–600: întrebări naive, livrabile, brief de 10 pagini redus la 15 cuvinte); SRC-022 cap. 1 Myths (brief-ul ca hartă, nu contract, r. 143–145) și cap. 8 (account-ul recitește brief-ul în ședință, r. 851–857); SRC-019 outil 1–2 (triajul, brief de 50 de pagini care omite informația crucială, fluxul Publicis cu „débrief créatif", r. 1028–1034, 1314–1330); SRC-025 cap. 6 („Don't Forget the Insight", „Reframing").
- **BRF-9902** — *Zece semnale de alarmă într-un brief — de la obiectivul care nu poate fi infirmat la măsurarea decisă după campanie* (checklist, nivel 2). Golul: greșelile tipice erau împrăștiate în șapte note; lipsea instrumentul de evaluare rapidă a unui brief (competența C6). Surse verificate: SRC-022, toate secțiunile „Why Brands Fail and How to Succeed" (cap. 1–7, r. 109–128, 217–224, 321–334, 423–438, 545–554, 663–686, 769–792); SRC-049 cap. 14 (brief pe o pagină, acceptat de toți, `audiobook/28.txt`); SRC-019 outil 1.

## 4. Convergențe și dezacorduri scrise explicit în note

- **Obiectivul de comunicare** (BRF-0703): McTigue–Rucker (bariera) ≈ Barre (o singură problemă de comunicare, ADV-0613) ≈ Percy (patru efecte, ADV-1502; ținte cifrice, ADV-1505).
- **Ținta** (BRF-0704): nevoi / Own–Attract–Accept (McTigue) vs. grupuri de cumpărători după relația cu brandul (Percy, ADV-1507, MKT-1501).
- **Beneficiul** (BRF-0706): scara „și ce dacă?" la McTigue ≈ Milavsky (ADV-0624, plus eliminarea beneficiilor de categorie) vs. modelul expectanță-valoare (Percy, BRD-1503).
- **Un singur beneficiu** (BRF-0707): convergența formularelor + dovezi empirice noi: ușurința reamintirii (INS-0410, Fennis & Stroebe) și „maximum trei argumente" (CPY-0605, Milavsky).
- **Emoțional vs. funcțional** (BRF-0708): Fennis & Stroebe (CPY-0403) dau dreptate lui McTigue–Rucker; forma istorică a disputei, Reeves–Ogilvy (ADV-0607); exemplul „Loretta" verificat în text.
- **Măsurarea** (BRF-0710): McTigue acceptă focus grupul pentru „de ce" vs. Percy, care îl exclude din pretest (ADV-1530, `contrazice`); Struhl (INS-1303) e de partea lui McTigue.
- **Feedback-ul** (BRF-0711): regulile lui Milavsky (CPY-0606) sunt aproape identice cu cele McTigue–Rucker, din partea agenției.
- **ADPLAN** (BRF-0712) extinde strategia în trei pași a lui Sternthal (ADV-0503), tot de la Kellogg.
- **Obligatoriile** (BRF-0709): Percy (logo și tagline neatinse, manuale de stil suspecte) ≈ McTigue (obligatoriile care scriu reclama).
- **Formularele** (BRF-0720): pe lângă cele cinci, comparația menționează brief-ul Percy (BRF-1503) și formularul Publicis din Barre (BRF-0601). Singleton O&M (dovada senzorială) e susținut de ierarhia promisiunilor Milavsky (ADV-0623).

## 5. Duplicate între skill-uri (legate, nu comasate)

| BRF | Alt skill | Natura suprapunerii |
|---|---|---|
| BRF-0705 | BRD-0503 | aceeași declarație de poziționare în patru piese (școala Kellogg); BRF-0705 e versiunea „din brief" |
| BRF-0706 | ADV-0624 | scara atribut → beneficiu final cu testul „și ce dacă?" (Milavsky vs. McTigue) |
| BRF-0712 | ADV-0503 | ADPLAN conține cei trei pași Sternthal (atenție, amplificare, legătură) |
| BRF-0601 | ADV-0603 | copy strategy-ul e inima brief-ului creativ; suprapunere parțială |
| BRF-0716 | PIT-1407 | gândește/simte/fă ≈ Know/Feel/Do/Why now |
| BRF-1101 | SOC-1117, SOC-1133 | brief-ul pentru creatori stă la granița BRF–SOC |
| (componenta insight) | INS-0701, INS-0702 | capitolul „Insights" din SRC-022 a fost scris în INS; harta BRF trimite explicit acolo, fără notă dublă |

## 6. Goluri rămase

- **Briefing-ul ca prezentare** (cum „vinzi" brief-ul echipei creative, ședința de briefing) apare doar ca paragraf în BRF-1503 (Percy) și în BRF-9901; biblioteca nu are mai mult material.
- **Contra-brief-ul / brief-ul inversat** (agenția îi trimite clientului propria reformulare) nu are sursă în bibliotecă dincolo de „débrief créatif" (Barre) și de recomandarea McTigue de a rescrie și aproba brief-ul; nu am scris notă.
- **Brief pentru alte tipuri de proiecte** (activări, produse, parteneriate) rămâne întrebare deschisă în BRF-0720.

## 7. Pentru orchestrator

- Redirect necesar: `BRF-1001 → BRF-1501` (trimiteri din SRC-032, DIG-1004, DIG-1006, DIG-1024 — în backlinks — și din `digital-marketing/SKILL.md`).
- Am înlocuit legăturile mele spre ADV-0614 (comasată de P2-ADV în ADV-1502) și INS-0501 (comasată în INS-0702) cu KEEP-urile.
- Problemă globală observată, nu doar la BRF: multe note din Faza 1 au wikilink-uri în celule de tabel; după `build`, forma `[[ID-slug|ID]]` introduce un `|` care sparge tabelul Markdown (de ex. BRF-0702). Ar merita ca `normalize_links` să scape pipe-ul (`\|`) în rândurile de tabel. În notele noi am evitat link-urile în tabele.
- `SKILL.md`: competențele nu conțin ID-uri proprii, ca ordinea pentru `renumber` să fie dată numai de hartă.
