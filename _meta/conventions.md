# Convenții ale knowledge base-ului ADC

Acest fișier este „constituția" bazei de cunoștințe. Orice notă nouă — scrisă de un om sau de un agent AI — respectă regulile de aici. `tools/kb.py check` verifică automat cele mai multe dintre ele.

## 1. Metoda: Zettelkasten organizat pe skill-uri

Baza combină două idei:

1. **Zettelkasten** (Niklas Luhmann): note mici, *atomice* (o singură idee per notă), scrise cu cuvintele tale, fiecare cu un ID permanent și legată explicit de alte note. Valoarea nu stă în note, ci în **legături**.
2. **Skill-uri**: fiecare notă are o „casă" — skill-ul principal pe care îl dezvoltă. Un skill este un folder cu un fișier-hub `SKILL.md` (meta-fișier) care spune ce competențe acoperă, în ce ordine se învață notele și cum le folosește un agent AI.

Rezultatul: poți naviga **vertical** (pe skill, ca într-un curs) sau **lateral** (pe legături, ca într-un Zettelkasten).

## 2. Tipuri de note

| Tip (`type`) | Ce este | Unde stă | ID |
|---|---|---|---|
| `fleeting` | Notă rapidă, neprocesată (captură) | `00-inbox/` | fără ID |
| `source` | Notă de lectură: fișa unei cărți | `10-sources/` | `SRC-001` |
| `zettel` | Notă permanentă, atomică | `20-skills/<skill>/notes/` | `BRD-001` |
| `skill` | Hub-ul unui skill (meta-fișier) | `20-skills/<skill>/SKILL.md` | codul skill-ului, ex. `BRD` |
| `map` | Hartă transversală (structure note / MOC) | `30-maps/` | `MAP-001` |

## 3. ID-uri și nume de fișiere

- ID-ul unei note permanente = **codul skill-ului principal + număr**: `BRD-007`. ID-ul nu se schimbă niciodată după publicare, chiar dacă nota își schimbă titlul.
- Codurile de skill sunt în `_meta/skills.json` (MKT, INS, BRD, ADV, BRF, IDE, CPY, ART, STO, DIG, SOC, EXP, AIM, PIT, PRT, CLI, HIS).
- Numele fișierului = `ID-slug.md`, unde slug-ul vine din titlu, cu litere mici, fără diacritice, cu cratime, maxim ~60 caractere. Exemplu: `BRD-007-pozitionarea-un-loc-distinct-in-minte.md`.
- *Temporar*, în faza de construcție, ID-urile pot avea 4 cifre (`BRD-0503` = grupul 05, nota 03). La lansare, `kb.py renumber` le transformă în ID-uri definitive de 3 cifre, în ordinea traseului de învățare din `SKILL.md`.

## 4. Legături

- Sintaxa: wikilink cu ID-ul: `[[BRD-007]]`. `kb.py build` le normalizează în `[[BRD-007-slug|BRD-007]]` ca să funcționeze și în Obsidian, și pentru agenți.
- Link către un skill: `[[BRD]]` (devine link spre `20-skills/brand-strategy/SKILL`).
- Link către o sursă: `[[SRC-014]]`.
- **Fiecare legătură are un motiv.** În secțiunea „Legături" a unei note, fiecare rând are forma:

  `- **relație** [[ID]] — de ce sunt legate (o propoziție)`

  Relațiile permise (vocabular controlat, în `_meta/skills.json`):

  | relație | sens |
  |---|---|
  | `fundament` | nota mea se sprijină pe țintă (citește ținta întâi) |
  | `extinde` | nota mea detaliază / dezvoltă ținta |
  | `aplicare` | nota mea aplică ținta într-un context concret |
  | `exemplu` | nota mea e un caz / exemplu pentru țintă |
  | `contrazice` | nota mea e în tensiune cu ținta |
  | `alternativa` | model alternativ la țintă |
  | `vezi` | legătură tematică generală |

- Legăturile pot apărea și în textul notei (inline), dar cele din „Legături" sunt cele tipizate, folosite pentru graf.
- Backlink-urile (cine trimite spre o notă) se generează automat de `kb.py build`, între markerii `<!-- backlinks:start -->` și `<!-- backlinks:end -->`. Nu le scrie de mână.

## 5. Frontmatter (metadate YAML)

Subset simplu de YAML: `cheie: valoare`, liste inline `[a, b]` și liste cu `- element`. Fără structuri imbricate.

### Notă permanentă (`zettel`)

```yaml
---
id: BRD-007
title: Poziționarea este un loc distinct în mintea consumatorului
type: zettel
kind: concept            # concept | framework | principle | method | case | checklist | debate
skill: brand-strategy    # slug-ul skill-ului principal (folderul în care stă)
also: [advertising-strategy, consumer-insight]   # alte skill-uri unde e relevantă (opțional)
level: 1                 # 1 Fundament | 2 Practică | 3 Avansat
tags: [pozitionare, diferentiere]
sources:
  - SRC-014 | cap. 2, p. 31-40
  - SRC-003 | cap. 4
status: seed             # seed | growing | evergreen
---
```

### Notă de lectură (`source`)

```yaml
---
id: SRC-014
title: Kellogg on Branding in a Hyper-Connected World
type: source
authors: [Alice M. Tybout, Tim Calkins]
year: 2019
language: en
file: Kellogg on Branding.pdf
text: 90-library/text/kellogg-on-branding.txt
skills: [brand-strategy, marketing-fundamentals]
relevance: 5             # 1-5, cât de utilă e cartea pentru o școală de publicitate
level: 2
---
```

## 6. Cum arată o notă permanentă bună

1. **Titlul este o afirmație sau un concept precis**, nu un subiect vag. Bine: „Brief-ul bun are o singură propoziție centrală". Rău: „Despre brief".
2. **Atomicitate**: o idee per notă. Dacă te prinzi scriind „și de asemenea…", sparge nota în două și leagă-le.
3. **Cu cuvintele tale**: parafrazează, nu copia. Cel mult un citat scurt (sub 15 cuvinte) per notă, între ghilimele, cu sursa.
4. **Autonomă**: nota se înțelege fără să fi citit cartea.
5. **Aplicabilă**: secțiunea „Aplicare" spune ce face un student / un creativ / un strateg concret cu ideea.
6. **Ancorată în surse**: fiecare notă citează cel puțin o sursă (`SRC-…`), cu capitol sau pagină unde se poate.
7. **Legată**: cel puțin 2 legături tipizate (nicio notă orfană).
8. Lungime: 150–400 de cuvinte în corpul notei. Modelele complexe pot avea un tabel.

Șablonul complet: `_meta/templates/zettel.md`.

## 7. Limbă și stil

- Notele sunt scrise în **română**, cu diacritice corecte (ă, â, î, ș, ț — cu virgulă, nu cu sedilă).
- Termenii de specialitate se dau în română + termenul original la prima apariție: „poziționare (*positioning*)", „propoziție unică de vânzare (*USP*)". Când termenul englezesc e standard în industrie (brief, insight, pitch, big idea, KPI), se păstrează.
- Numele modelelor rămân cele originale: „Grila Rossiter-Percy", „Piramida CBBE (Keller)".
- Ton: clar, direct, util pentru un student care vrea să lucreze într-o agenție.

## 8. Fluxul de lucru CEQRC (cum crește baza)

| Pas | Ce faci | Unde |
|---|---|---|
| **C**apture | Notezi rapid ideea / citatul / pagina | `00-inbox/` (notă `fleeting`) |
| **E**xplain | O rescrii cu cuvintele tale, ca notă atomică | `20-skills/<skill>/notes/` |
| **Q**uestion | Adaugi întrebări: unde nu se aplică? cine contrazice? | secțiunea „Întrebări" |
| **R**efine | Scurtezi, clarifici titlul, verifici sursa, ridici `status` | nota însăși |
| **C**onnect | Adaugi legături tipizate, o pui în harta din `SKILL.md` | „Legături" + `SKILL.md` |

Apoi rulezi `python3 tools/kb.py build` (backlink-uri, indexuri, graf) și `python3 tools/kb.py suggest` (propuneri de legături pe care nu le-ai făcut încă).

## 9. Meta-fișiere generate automat (nu le edita de mână)

| Fișier | Conținut |
|---|---|
| `_meta/catalog.json`, `_meta/catalog.csv` | toate notele cu metadatele lor |
| `_meta/graph.json` | graful: noduri (note) + muchii (legături tipizate) |
| `_meta/coverage.md` | matricea skill × sursă și golurile de acoperire |
| `_meta/link-suggestions.md` | perechi de note similare, încă nelegate |
| `_meta/health.md` | raportul `check`: legături rupte, orfani, câmpuri lipsă |
| secțiunile `<!-- auto:... -->` din `SKILL.md` și `INDEX.md` | liste de note generate |
