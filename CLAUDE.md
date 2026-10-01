# CLAUDE.md — cum lucrează un agent AI cu această bază de cunoștințe

Aceasta este baza de cunoștințe a școlii ADC: un Zettelkasten în română, organizat pe 17 skill-uri, construit din 49 de surse (cărți de marketing, publicitate, brand, creație, digital, AI, pitch, portofoliu). Regulile complete sunt în `_meta/conventions.md`.

## Navigare

1. Intrarea: `INDEX.md` → domenii → skill-uri.
2. Fiecare skill: `20-skills/<slug>/SKILL.md` — competențe, traseu de învățare, playbook-uri pentru agenți.
3. Notele permanente: `20-skills/<slug>/notes/<ID>-<slug>.md`. Un link `[[BRD-007]]` sau `[[BRD-007-…|BRD-007]]` = fișierul care începe cu `BRD-007-`. Găsește-l cu `ls 20-skills/*/notes/BRD-007-*`.
4. Fișele cărților: `10-sources/SRC-0XX-*.md`. Textul integral (copie extrasă) e în `90-library/text/` — folosește-l pentru a verifica o afirmație sau a merge mai adânc (caută cu `grep -n`).
5. Hărți transversale (fluxuri de lucru, comparații de modele, curriculum): `30-maps/`.
6. Metadate generate: `_meta/catalog.csv` (toate notele), `_meta/graph.json` (legături), `_meta/coverage.md`.

## Când răspunzi la o întrebare sau faci un task (strategie, brief, idei, pitch…)

- Pornește de la `SKILL.md` relevant și urmează playbook-ul din secțiunea „Cum folosește un agent AI acest skill".
- Fundamentează-te pe note, nu pe memorie generală. **Citează ID-urile** notelor folosite (ex. „conform [[BRD-007]] și [[INS-012]]"), ca răspunsul să fie verificabil.
- Urmează legăturile tipizate: `fundament` = ce trebuie înțeles înainte; `contrazice` = unde autorii nu sunt de acord (menționează tensiunea).
- Dacă baza nu acoperă subiectul, spune asta explicit și propune o notă nouă în `00-inbox/`.

## Când adaugi cunoștințe (fluxul CEQRC)

1. **Capture** — notă rapidă în `00-inbox/` (șablon `_meta/templates/fleeting.md`).
2. **Explain** — `python3 tools/kb.py new <COD> "Titlu-afirmație"` creează nota permanentă cu ID-ul următor; scrie-o cu cuvintele tale, după șablon.
3. **Question** — secțiunea „Întrebări": unde nu se aplică, cine contrazice.
4. **Refine** — titlu precis, o singură idee, sursă cu pagină, `status: growing`.
5. **Connect** — 2–6 legături tipizate; adaug-o în harta din `SKILL.md`; rulează:

```bash
python3 tools/kb.py suggest --skill <slug>   # legături candidate
python3 tools/kb.py build                    # backlink-uri, indexuri, catalog, graf
python3 tools/kb.py check                    # sănătate → _meta/health.md
```

## Reguli

- ID-urile sunt permanente: nu renumerota după lansare; comasează cu `kb.py merge KEEP DROP`.
- Nu edita de mână secțiunile dintre markerii `<!-- backlinks:… -->` și `<!-- auto:… -->`.
- Nu copia pasaje din cărți: parafrazează; cel mult un citat scurt (< 15 cuvinte) per notă.
- Româna cu diacritice corecte (ș, ț cu virgulă).
