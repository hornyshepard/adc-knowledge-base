# Raport P2-EXP — integrarea skill-ului experiential-marketing (EXP)

Agent P2-EXP-AIM, Faza 2. Skill: `20-skills/experiential-marketing/`. (Același agent a integrat și AIM; vezi `P2-AIM.md`.)

## 1. Cifre

| | Înainte | După |
|---|---|---|
| Note permanente | 33 | 31 (33 − 2 comasate, 0 noi) |
| Note cu `status: growing` | 0 | 31 |
| Note cu 2–6 legături tipizate | 31 (EXP-1201 avea 9, EXP-1202 avea 8) | 31 |
| Note fără nicio legătură tipizată în afara propriului grup Faza 1 | 7 | 0 |
| Note cu cel puțin o legătură spre alt skill | 26 | 30 |
| Legături tipizate, total | 121 | 162 |
| Lungime corp (numărare tip `kb.py`) | 338–492 | 351–459 |

`kb.py check`: nicio problemă în fișierele EXP la ultima rulare. Legăturile rupte rămase care privesc EXP vin din alte fișiere (SRC-006 → EXP-0204, SRC-036 → EXP-1205, MKT-1201 → EXP-1205) și se rezolvă la redirect.

## 2. Comasări (în `merges-EXP.txt`)

| DROP | KEEP | Ce s-a integrat |
|---|---|---|
| EXP-1205 (CX a depășit CRM-ul, Batat) | EXP-0901 (CX = suma interacțiunilor, Zahay et al.) | O singură notă-definiție: Zahay et al. și Batat converg pe definiția cumulativă și multidimensională (ambii pornesc de la Lemon & Verhoef); Batat adaugă critica CRM-ului, schimbarea scopului consumului și reperele istorice (Holbrook & Hirschman, Pine & Gilmore, Schmitt); Zahay adaugă grila Temkin și distincția „marketingul experiențial e parte din CX, nu CX". Retitlată, `kind: concept`, nivel 1. |
| EXP-0204 (multisenzorial, Kotler 6.0) | EXP-1210 (cinci semnături senzoriale, Batat) | Tabel comun simț × rol × exemplu Batat × exemplu Kotler; „de ce acum" (oboseala digitală) și cei trei pași ai lui Kotler; dezacordul explicit despre Abercrombie & Fitch (model la Batat 2019, parfum „Fierce" prea puternic, înlocuit cu „Ellwood", la Kotler 2024); avertisment despre cifra „80% văz", repetată fără sursă în ambele cărți. |

## 3. Restructurări fără ștergere (suprapunerea Kotler 6.0 ↔ Batat)

Notele Kotler 6.0 (EXP-0202, EXP-0203) amestecau câte două-trei idei care se suprapuneau cu notele Batat și Parsons et al. Le-am făcut atomice, mutând conținutul acolo unde exista deja nota-pereche:

- **EXP-1207** (imersiunea) primește cele cinci elemente ale imersiunii din Kotler 6.0 (multisenzorial, interactiv, participativ, fără fricțiuni, narativ), într-un tabel de corespondență cu cei cinci factori ai lui Batat. Diferențe notate: Batat are factorul cognitiv, Kotler accentuează participarea. Retitlată.
- **EXP-0202** rămâne doar cu cele patru scenarii om–digital (de la casierie la ospitalitate), retitlată; citatul PwC și Ritz-Carlton/Henn-na verificate în text.
- **EXP-0203** devine nota despre **al treilea loc**: Oldenburg (Kotler 6.0) + homeyness (Parsons et al., p. 153–154, care citează Rosenbaum, nu Oldenburg, corectat) + designul spațiului ca poveste (dovezi fizice, proces, oameni). Paragraful despre marketingul spațial a fost scos (e deja în DIG-0205).
- **EXP-1220** (phygital) primește cele cinci moduri de a aduce digitalul în spațiul fizic din Kotler 6.0 (Fig. 6.2), puse alături de instrumentele lui Batat; Timberland apare în ambele cărți.
- **EXP-0401** rămâne doar cu ritul de trecere (Dans le Noir?); partea despre al treilea loc a trecut în EXP-0203. Paginile corectate (p. 152–153, studiul de caz p. 159–160).
- **EXP-0301** (Pine & Gilmore) primește perspectiva lui Batat: cele două axe (absorbție–imersiune, pasiv–activ), transformarea tărâmurilor unul în altul și critica ei, din care se naște ETM. Lista de teme Gottdiener / Schmitt & Simonson a trecut în EXP-1209 (cu SRC-008, cap. 16).
- **EXP-1201** și **EXP-1202**: legăturile spre cele 7 E au trecut inline în tabel, ca să rămână 5–6 legături tipizate; EXP-1201 notează convergența cu EP² (Wuebben).

Alte convergențe scrise explicit: girafa Joshie de la Ritz-Carlton apare și în Kotler 4.0 (EXP-0201), și în Zahay et al. (EXP-0901); markerul „cumulativ" al lui Batat = definiția CX a lui Zahay (EXP-1203); ruptura de la livrare/despachetare apare și la Batat (EXP-1215), și la Pereira/Kellogg (EXP-0501).

## 4. Note noi

Niciuna. Am căutat în bibliotecă material pentru planificarea și măsurarea evenimentelor (hors-média, événementiel, street marketing, activation, peak-end): există doar mențiuni scurte în cărțile franceze (SRC-019, SRC-020), iar regula peak-end e deja în PIT-1417, pe care am legat-o din EXP-1204 și EXP-1223.

## 5. Duplicate între skill-uri (nu le-am atins; legate)

| Nota EXP | Nota din alt skill | Relația |
|---|---|---|
| EXP-1220, EXP-0203 | DIG-0205 (marketing contextual și spațial, Kotler 5.0 + 6.0) | suprapunere parțială pe marketingul spațial; scos din EXP-0203, legat `vezi` |
| EXP-1220 | DIG-0201 (omnichannel) | aceeași idee din designul experienței vs. din canale; `vezi` |
| EXP-1210 | ART-0502 (12 indicii senzoriale, Kellogg) | convergență: toate indiciile trebuie să declanșeze aceleași asocieri; `vezi` |
| EXP-1206 | DIG-0905, MKT-0210, ADV-0501 | modele alternative ale parcursului clientului; `alternativa` |
| EXP-1214 | SOC-1005 (concursuri după efortul cerut) | aceeași logică a nivelului de participare; `vezi` |
| EXP-1213 | MKT-0401 (co-creația ca muncă neplătită) | `contrazice` |
| EXP-1201 | MKT-0128 (7P servicii), MKT-0314 (EP²) | `alternativa` |
| EXP-1212 | MKT-0124 (decalajele de serviciu, aceiași autori ca SERVQUAL) | `fundament` |
| EXP-0901 | DIG-1010 (DCX, fagurele Morville) | înrudite, nelegate direct (EXP-0901 are deja 6 legături) |

## 6. Ce trebuie să știe orchestratorul

- **Legături din alte skill-uri al căror motiv s-a mutat:** SOC-0202 → EXP-0202 („cinci elemente ale imersiunii") ar trebui să ducă acum la **EXP-1207**; DIG-0205 → EXP-0203 („spațiul fizic augmentat") ar fi mai exact spre **EXP-1220**. MKT-0215 → EXP-0202 și MKT-0216 → EXP-0203 rămân corecte.
- Numele de fișiere nu au fost schimbate, deși titlurile EXP-0202, EXP-0203, EXP-0401, EXP-0901, EXP-1207, EXP-1210 și EXP-1220 s-au schimbat; slug-urile se pot regenera la `renumber`.
- În notele mele, legăturile spre note comasate de alți agenți au fost deja redirecționate (INS-0445 → INS-1206) pe baza fișierelor `merges-*.txt` existente la final. Dacă apar comasări noi după mine, redirect-ul global le prinde.
- EXP-1301 (conjoint de servicii, Struhl) a rămas în EXP, ca notă de măsurare; ar putea sta și la AIM sau CLI.

## 7. Goluri rămase

- Planificarea și producția unui eveniment sau a unei activări (buget, logistică, riscuri de execuție) — biblioteca nu are o sursă dedicată; doar SOC-1129 (Fyre Festival) ca avertisment.
- Rezultate măsurate ale campaniilor experiențiale: cazurile lui Batat sunt descriptive, fără efecte asupra vânzărilor sau brandului.
- Experiența angajatului (EX) ca subiect separat, accesibilitatea și incluziunea în designul experienței, experiențele B2B și târgurile.
- Instrumentul EXQUAL nu poate fi reprodus: tabelul cu itemi lipsește din copia text (semnalat în EXP-1212).
