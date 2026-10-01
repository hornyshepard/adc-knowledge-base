# Baza de cunoștințe ADC

O bază de cunoștințe pentru școala ADC (publicitate, brand, creație, digital), construită din 49 de surse: cărți de marketing, publicitate, psihologia consumatorului, branding, brief și idei creative, istoria publicității, marketing digital, social media, marketing experiențial, AI, pitch, portofoliu și vânzări B2B.

**În cifre:** 49 de surse · 778 de note permanente · 17 skill-uri în 6 domenii · 6 hărți transversale · ~7.700 de legături · 52 de note-dezbatere (unde autorii nu sunt de acord).

## Metoda: Zettelkasten + skill-uri + AI

| Idee | Cum e aplicată aici |
|---|---|
| **Note atomice, legate** (Zettelkasten) | O idee per notă, scrisă în română cu cuvintele noastre, cu ID permanent (`BRD-007`) și legături tipizate care au motiv (`fundament`, `extinde`, `contrazice`…). |
| **Organizare pe skill-uri** | 17 skill-uri în 6 domenii. Fiecare skill are un hub `SKILL.md` (meta-fișier): competențe, traseu de învățare, surse, playbook-uri pentru agenți. |
| **Legare automată** | `tools/kb.py suggest` propune legături între note similare (TF-IDF), pe care un om sau un agent le confirmă. |
| **Fluxul CEQRC** | Capture → Explain → Question → Refine → Connect, descris în `_meta/conventions.md` și `CLAUDE.md`. |
| **Execuție agentică** | Claude Code citește folderul: `CLAUDE.md` îi spune cum să navigheze, iar fiecare `SKILL.md` e compatibil cu formatul de skill Claude. |

## Structura

```
ADC-Knowledge-Base/
├── INDEX.md                 # punctul de intrare: domenii → skill-uri
├── CLAUDE.md                # instrucțiuni pentru agenți AI
├── 00-inbox/                # note rapide, neprocesate (Capture)
├── 10-sources/              # o fișă de lectură per carte (SRC-001 … SRC-049)
├── 20-skills/
│   └── <skill>/
│       ├── SKILL.md         # hub-ul skill-ului (meta-fișier + skill Claude)
│       └── notes/           # note permanente atomice (BRD-001-….md)
├── 30-maps/                 # 6 hărți transversale (vezi mai jos)
├── 90-library/              # textele integrale extrase (doar local, nu în git)
├── .claude/skills/          # legături spre cele 17 skill-uri, pentru Claude Code
├── _meta/
│   ├── conventions.md       # regulile bazei
│   ├── reports/             # rapoartele agenților care au citit cărțile
│   ├── skills.json          # taxonomia: domenii, skill-uri, tipuri, relații
│   ├── sources.json         # registrul surselor
│   ├── templates/           # șabloane: zettel, source, skill, map, fleeting
│   ├── catalog.json/.csv    # generat: toate notele
│   ├── graph.json           # generat: noduri + legături tipizate
│   ├── coverage.md          # generat: acoperire skill × sursă
│   └── health.md            # generat: legături rupte, orfani, câmpuri lipsă
└── tools/
    ├── kb.py                # check, build, suggest, merge, redirect, renumber, new, stats
    ├── extract_texts.py     # PDF/EPUB/AZW3/DOCX → text
    └── transcribe_audiobook.py
```

## Skill-urile

| Domeniu | Skill-uri |
|---|---|
| D1 Gândire strategică | MKT Fundamente de marketing · INS Psihologia consumatorului și insight · BRD Strategie de brand · ADV Strategie de publicitate · BRF Brief-ul creativ |
| D2 Creație | IDE Ideație · CPY Copywriting · ART Direcție artistică și identitate vizuală · STO Storytelling și conținut |
| D3 Canale | DIG Marketing digital · SOC Social media și influenceri · EXP Marketing experiențial |
| D4 AI | AIM AI în marketing și publicitate |
| D5 Profesie | PIT Pitch și prezentare · PRT Portofoliu · CLI Client, vânzări și business |
| D6 Cultură | HIS Istoria publicității |

## Hărțile transversale

| Hartă | La ce folosește |
|---|---|
| MAP-001 Fluxul agenției | drumul unui proiect, de la problema de business la pitch și măsurare — coloana vertebrală a cursului |
| MAP-002 Modele de efect și customer journey | AIDA, FCB, Rossiter-Percy, 5A, journey digital, 7A… comparate, cu limitele lor |
| MAP-003 Etică și reglementare | adevăr și dovadă, limitele persuasiunii, publicitate nativă, date și AI, reprezentare, drepturi |
| MAP-004 Dezbateri | toate notele în care autorii se contrazic — material de seminar |
| MAP-005 Ghidul bibliotecii | cele 49 de surse ordonate după relevanță (★1–5), cu ce să citești integral și ce să eviți |
| MAP-006 Traseul de curs ADC | patru module + skill-urile profesionale în paralel, cu punctul de start în fiecare skill |

## Cum o folosești

**Ca om (Obsidian sau orice editor Markdown):** deschide folderul ca vault în Obsidian și pornește de la `INDEX.md`. Graful din Obsidian arată legăturile dintre note.

**Cu Claude Code:** deschide o sesiune în acest folder. Claude citește `CLAUDE.md`, iar cele 17 skill-uri sunt expuse în `.claude/skills/`, deci se activează singure când cererea se potrivește cu descrierea lor. Claude pornește de la `SKILL.md`-ul potrivit și citează ID-urile notelor folosite. Exemple de cereri:
- „Scrie un brief creativ pentru … folosind skill-ul creative-brief."
- „Compară modelele de customer journey din bază și spune unde nu sunt de acord autorii."
- „Pregătește structura unui pitch de 10 minute pentru …"

**Întreținere:**

```bash
python3 tools/kb.py check
```

```bash
python3 tools/kb.py build
```

```bash
python3 tools/kb.py suggest --skill brand-strategy
```

## Drepturi de autor

Notele sunt rezumate și sinteze proprii, cu trimiteri la capitol și pagină. Repository-ul nu conține cărțile și nici textul lor integral. Textele se regenerează local din copiile proprii ale cărților (vezi `90-library/README.md`).
