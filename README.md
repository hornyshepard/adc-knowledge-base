# Baza de cunoștințe ADC

O bază de cunoștințe pentru școala ADC (publicitate, brand, creație, digital), construită din 49 de surse: cărți de marketing, publicitate, psihologia consumatorului, branding, brief și idei creative, istoria publicității, marketing digital, social media, marketing experiențial, AI, pitch, portofoliu și vânzări B2B.

> **Status:** în construcție. Agenții AI citesc cărțile și scriu notele; structura, convențiile și uneltele sunt gata.

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
├── 30-maps/                 # hărți transversale: fluxuri, comparații, curriculum
├── 90-library/              # textele integrale extrase (doar local, nu în git)
├── _meta/
│   ├── conventions.md       # regulile bazei
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

## Cum o folosești

**Ca om (Obsidian sau orice editor Markdown):** deschide folderul ca vault în Obsidian și pornește de la `INDEX.md`. Graful din Obsidian arată legăturile dintre note.

**Cu Claude Code:** deschide o sesiune în acest folder. Claude citește `CLAUDE.md`, pornește de la `SKILL.md`-ul potrivit și citează ID-urile notelor folosite. Exemple de cereri:
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
