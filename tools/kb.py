#!/usr/bin/env python3
"""kb.py — unealta de întreținere a knowledge base-ului ADC (Zettelkasten pe skill-uri).

Fără dependențe externe (Python 3.9+).

Comenzi:
  check                 verifică notele; scrie _meta/health.md
  build [--rename]      normalizează legăturile, backlink-uri, indexuri, catalog, graf, acoperire
  suggest [--skill S] [--top N] [--min X]
                        propune legături între note similare, încă nelegate (TF-IDF)
  merge KEEP DROP       redirecționează toate legăturile DROP→KEEP, unește sursele/tag-urile, șterge DROP
  redirect FILE         aplică redirecționări `DROP KEEP` dintr-un fișier (după comasări manuale)
  renumber [--dry-run]  ID-uri definitive (CODE-001…) în ordinea traseului din SKILL.md
  new CODE "Titlu"      creează o notă permanentă nouă din șablon, cu următorul ID liber
  stats                 statistici pe skill, tip, nivel, status
"""
import csv
import datetime as _dt
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "_meta"
SKIP_DIRS = {"90-library", "tools", "templates", ".obsidian", ".git", ".claude", "reports"}

ID_RE = re.compile(r"^([A-Z]{3}-\d{3,4})\b")
LINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")
TYPED_RE = re.compile(r"^\s*[-*]\s*\*\*([a-zăâîșț]+)\*\*\s*\[\[([^\]|#]+)")
BACK_START, BACK_END = "<!-- backlinks:start -->", "<!-- backlinks:end -->"
AUTO_START, AUTO_END = "<!-- auto:notes:start -->", "<!-- auto:notes:end -->"

SKILLS = json.loads((META / "skills.json").read_text())
SKILL_BY_CODE = {s["code"]: s for s in SKILLS["skills"]}
SKILL_BY_SLUG = {s["slug"]: s for s in SKILLS["skills"]}
DOMAIN_OF = {c: d for d in SKILLS["domains"] for c in d["skills"]}
RELATIONS = set(SKILLS["relations"])
KINDS = set(SKILLS["kinds"])
LEVEL_NAMES = SKILLS["levels"]

REQUIRED = {
    "zettel": ["id", "title", "type", "kind", "skill", "level", "sources", "status"],
    "source": ["id", "title", "type", "authors", "skills", "relevance"],
    "map": ["id", "title", "type"],
    "skill": ["name", "description", "code", "type"],
}


# ---------------------------------------------------------------- parsing

def deaccent(s):
    s = s.replace("ș", "s").replace("ş", "s").replace("ț", "t").replace("ţ", "t")
    s = s.replace("Ș", "S").replace("Ş", "S").replace("Ț", "T").replace("Ţ", "T")
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def slugify(title, maxlen=60):
    s = deaccent(title).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s


def parse_value(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [x.strip().strip("'\"") for x in inner.split(",") if x.strip()] if inner else []
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    return v


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def parse_frontmatter(fm):
    data, key = {}, None
    for line in fm.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(m.group(1).strip().strip("'\""))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, raw = m.group(1), m.group(2)
            raw = re.sub(r"\s+#.*$", "", raw) if not raw.strip().startswith(("'", '"')) else raw
            data[key] = parse_value(raw) if raw.strip() else []
    return data


class Note:
    def __init__(self, path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")
        fm, self.body = split_frontmatter(self.text)
        self.meta = parse_frontmatter(fm) if fm is not None else {}
        self.type = self.meta.get("type", "")
        if self.type == "skill":
            self.id = self.meta.get("code", "")
        else:
            self.id = self.meta.get("id", "") if isinstance(self.meta.get("id", ""), str) else ""
        self.title = self.meta.get("title") or self.meta.get("name") or path.stem
        if isinstance(self.title, list):
            self.title = " ".join(self.title)

    @property
    def rel(self):
        return self.path.relative_to(ROOT).as_posix()

    @property
    def link_target(self):
        return self.path.relative_to(ROOT).with_suffix("").as_posix() if self.type == "skill" else self.path.stem

    def body_without_auto(self):
        b = re.sub(re.escape(BACK_START) + r".*?" + re.escape(BACK_END), "", self.body, flags=re.S)
        return re.sub(re.escape(AUTO_START) + r".*?" + re.escape(AUTO_END), "", b, flags=re.S)

    def links(self):
        """[(target_id, relation_or_None)] din corpul notei (fără secțiunile auto)."""
        out = []
        body = self.body_without_auto()
        typed = {}
        for line in body.splitlines():
            m = TYPED_RE.match(line)
            if m:
                tid = resolve_target(m.group(2))
                if tid:
                    typed.setdefault(tid, m.group(1))
        seen = set()
        for m in LINK_RE.finditer(body):
            tid = resolve_target(m.group(1))
            if tid and tid not in seen:
                seen.add(tid)
                out.append((tid, typed.get(tid)))
        return out

    def words(self):
        b = self.body_without_auto()
        b = re.sub(r"^## (Legături|Surse)\b.*", "", b, flags=re.S | re.M)
        return len(re.findall(r"\w+", b))


def resolve_target(target):
    t = target.strip()
    m = ID_RE.match(t)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Z]{3}", t) and t in SKILL_BY_CODE:
        return t
    m = re.match(r"^(?:20-skills/)?([a-z0-9-]+)/SKILL$", t)
    if m and m.group(1) in SKILL_BY_SLUG:
        return SKILL_BY_SLUG[m.group(1)]["code"]
    return None


def iter_md():
    for p in sorted(ROOT.rglob("*.md")):
        parts = set(p.relative_to(ROOT).parts[:-1])
        if parts & SKIP_DIRS:
            continue
        yield p


def load():
    notes = []
    for p in iter_md():
        n = Note(p)
        if n.type:
            notes.append(n)
    return notes


def index(notes):
    by_id = {}
    dups = defaultdict(list)
    for n in notes:
        if n.id:
            dups[n.id].append(n)
            by_id.setdefault(n.id, n)
    return by_id, {k: v for k, v in dups.items() if len(v) > 1}


def source_ids(n):
    srcs = n.meta.get("sources", [])
    if isinstance(srcs, str):
        srcs = [srcs]
    out = []
    for s in srcs:
        m = re.match(r"\s*(SRC-\d{3})", s)
        if m:
            out.append(m.group(1))
    return out


def as_list(v):
    if isinstance(v, list):
        return v
    return [v] if v else []


# ---------------------------------------------------------------- check

def cmd_check(quiet=False):
    notes = load()
    by_id, dups = index(notes)
    problems = defaultdict(list)
    incoming = Counter()  # doar legături laterale, din alte note permanente
    for n in notes:
        if n.type != "zettel":
            continue
        for tid, _ in n.links():
            if tid != n.id:
                incoming[tid] += 1

    for i, group in dups.items():
        problems["ID duplicat"].append(f"{i}: " + ", ".join(x.rel for x in group))

    for n in notes:
        for f in REQUIRED.get(n.type, []):
            if f not in n.meta or n.meta.get(f) in ("", []):
                problems["Câmp lipsă în frontmatter"].append(f"{n.rel}: `{f}`")
        if n.type == "zettel":
            if not n.path.name.startswith(n.id + "-") and n.path.stem != n.id:
                problems["Nume de fișier ≠ ID"].append(f"{n.rel} (id {n.id})")
            code = n.id[:3]
            sk = SKILL_BY_CODE.get(code)
            if not sk:
                problems["Cod de skill necunoscut"].append(f"{n.rel}: {code}")
            else:
                if n.meta.get("skill") != sk["slug"]:
                    problems["`skill` nu corespunde codului din ID"].append(f"{n.rel}: skill={n.meta.get('skill')} cod={code}")
                if f"20-skills/{sk['slug']}/" not in n.rel:
                    problems["Notă în folderul greșit"].append(n.rel)
            for a in as_list(n.meta.get("also")):
                if a not in SKILL_BY_SLUG:
                    problems["Skill necunoscut în `also`"].append(f"{n.rel}: {a}")
            if n.meta.get("kind") and n.meta.get("kind") not in KINDS:
                problems["`kind` invalid"].append(f"{n.rel}: {n.meta.get('kind')}")
            if str(n.meta.get("level", "")) not in LEVEL_NAMES:
                problems["`level` invalid"].append(f"{n.rel}: {n.meta.get('level')}")
            if n.meta.get("status") and n.meta.get("status") not in SKILLS["statuses"]:
                problems["`status` invalid"].append(f"{n.rel}: {n.meta.get('status')}")
            sids = source_ids(n)
            if not sids:
                problems["Fără sursă"].append(n.rel)
            for s in sids:
                if s not in by_id:
                    problems["Sursă inexistentă"].append(f"{n.rel}: {s}")
            out_links = [t for t, _ in n.links() if t != n.id and not t.startswith("SRC") and len(t) > 3]
            if len(out_links) < 2:
                problems["Sub 2 legături spre alte note"].append(f"{n.rel} ({len(out_links)})")
            if incoming[n.id] == 0:
                problems["Orfan (nicio notă permanentă nu trimite spre ea)"].append(n.rel)
            w = n.words()
            if w < 100 or w > 650:
                problems["Lungime atipică (corp < 100 sau > 650 cuvinte)"].append(f"{n.rel}: {w}")
        for tid, rel in n.links():
            if tid not in by_id:
                problems["Legătură ruptă"].append(f"{n.rel} → {tid}")
        if n.type == "zettel":
            for line in n.body_without_auto().splitlines():
                m = TYPED_RE.match(line)
                if m and m.group(1) not in RELATIONS:
                    problems["Relație necunoscută"].append(f"{n.rel}: **{m.group(1)}**")
                elif not m and re.match(r"^\s*[-*]\s*\*\*", line) and "[[" in line:
                    problems["Relație necunoscută"].append(f"{n.rel}: {line.strip()[:60]}")

    total = sum(len(v) for v in problems.values())
    zettels = [n for n in notes if n.type == "zettel"]
    lines = [
        "# Sănătatea bazei de cunoștințe",
        "",
        f"_Generat de `tools/kb.py check` la {_dt.datetime.now():%Y-%m-%d %H:%M}._",
        "",
        f"- Note totale: **{len(notes)}** (permanente: {len(zettels)}, surse: {sum(n.type == 'source' for n in notes)}, "
        f"skill-uri: {sum(n.type == 'skill' for n in notes)}, hărți: {sum(n.type == 'map' for n in notes)})",
        f"- Probleme: **{total}**",
        "",
    ]
    for k in sorted(problems, key=lambda k: -len(problems[k])):
        lines.append(f"## {k} ({len(problems[k])})")
        lines.append("")
        lines += [f"- {x}" for x in problems[k][:300]]
        if len(problems[k]) > 300:
            lines.append(f"- … încă {len(problems[k]) - 300}")
        lines.append("")
    (META / "health.md").write_text("\n".join(lines), encoding="utf-8")
    if not quiet:
        print(f"{len(notes)} note, {total} probleme → _meta/health.md")
        for k in sorted(problems, key=lambda k: -len(problems[k])):
            print(f"  {len(problems[k]):>4}  {k}")
    return problems


# ---------------------------------------------------------------- build

def normalize_links(text, by_id):
    def rep(m):
        target, anchor, alias = m.group(1), m.group(2) or "", m.group(3)
        tid = resolve_target(target)
        if not tid or tid not in by_id:
            return m.group(0)
        n = by_id[tid]
        label = alias if alias and not ID_RE.match(alias) and alias not in SKILL_BY_CODE else tid
        return f"[[{n.link_target}{anchor}|{label}]]"
    return LINK_RE.sub(rep, text)


def replace_block(text, start, end, content):
    block = f"{start}\n{content}\n{end}"
    if start in text and end in text:
        return re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    return text.rstrip() + "\n\n" + block + "\n"


def md_link(n):
    return f"[[{n.link_target}|{n.id}]]"


def cmd_build(rename=False):
    notes = load()
    by_id, dups = index(notes)
    if dups:
        print("Atenție: ID-uri duplicate — rulează check.", file=sys.stderr)

    if rename:
        for n in notes:
            if n.type == "zettel" and n.id:
                want = f"{n.id}-{slugify(n.title)}.md"
                if n.path.name != want:
                    new = n.path.with_name(want)
                    if not new.exists():
                        n.path.rename(new)
                        n.path = new
        notes = load()
        by_id, _ = index(notes)

    backlinks = defaultdict(list)
    edges = []
    for n in notes:
        for tid, rel in n.links():
            if tid in by_id and tid != n.id:
                backlinks[tid].append((n, rel))
                edges.append({"source": n.id, "target": tid, "relation": rel or "inline"})

    zettels = sorted([n for n in notes if n.type == "zettel"], key=lambda n: n.id)
    by_skill = defaultdict(list)
    for z in zettels:
        by_skill[z.meta.get("skill")].append(z)

    for n in notes:
        text = n.text
        fm, body = split_frontmatter(text)
        body = normalize_links(body, by_id)
        if n.type in ("zettel", "source", "map"):
            bl = sorted(backlinks.get(n.id, []), key=lambda x: (x[0].type != "zettel", x[0].id))
            items = []
            for src, rel in bl:
                if src.type == "skill":
                    continue
                r = f" _{rel}_" if rel else ""
                items.append(f"- {md_link(src)}{r} — {src.title}")
            content = "## Backlinks\n\n" + ("\n".join(items) if items else "_Nicio notă nu trimite încă aici._")
            body = replace_block(body, BACK_START, BACK_END, content)
        if n.type == "skill":
            code = n.id
            slug = SKILL_BY_CODE.get(code, {}).get("slug")
            own = by_skill.get(slug, [])
            also = [z for z in zettels if slug in as_list(z.meta.get("also"))]
            rows = ["| ID | Titlu | Tip | Nivel | Status |", "|---|---|---|---|---|"]
            for z in own:
                rows.append(f"| {md_link(z)} | {z.title} | {z.meta.get('kind', '')} | "
                            f"{LEVEL_NAMES.get(str(z.meta.get('level')), '')} | {z.meta.get('status', '')} |")
            content = f"_{len(own)} note proprii._\n\n" + "\n".join(rows)
            if also:
                content += "\n\n**Note din alte skill-uri, relevante și aici:**\n\n" + "\n".join(
                    f"- {md_link(z)} — {z.title}" for z in also)
            body = replace_block(body, AUTO_START, AUTO_END, content)
        new_text = f"---\n{fm}\n---\n{body}" if fm is not None else body
        if new_text != n.text:
            n.path.write_text(new_text, encoding="utf-8")

    # catalog
    rows = []
    for n in notes:
        rows.append({
            "id": n.id, "type": n.type, "title": n.title, "path": n.rel,
            "skill": n.meta.get("skill", n.meta.get("name", "")) if n.type != "source" else "",
            "also": as_list(n.meta.get("also")), "kind": n.meta.get("kind", ""),
            "level": n.meta.get("level", ""), "status": n.meta.get("status", ""),
            "tags": as_list(n.meta.get("tags")), "sources": source_ids(n),
            "out": [t for t, _ in n.links() if t != n.id], "in": [s.id for s, _ in backlinks.get(n.id, [])],
            "words": n.words(),
        })
    (META / "catalog.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(META / "catalog.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "type", "title", "skill", "kind", "level", "status", "sources", "in", "out", "path"])
        for r in rows:
            w.writerow([r["id"], r["type"], r["title"], r["skill"], r["kind"], r["level"], r["status"],
                        " ".join(r["sources"]), len(r["in"]), len(r["out"]), r["path"]])

    nodes = [{"id": n.id, "title": n.title, "type": n.type,
              "skill": n.meta.get("skill") if n.type == "zettel" else (SKILL_BY_CODE.get(n.id, {}).get("slug") if n.type == "skill" else None),
              "kind": n.meta.get("kind"), "level": n.meta.get("level"), "path": n.rel} for n in notes]
    (META / "graph.json").write_text(json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, indent=1), encoding="utf-8")

    # coverage: skill × source
    srcs = sorted([n for n in notes if n.type == "source"], key=lambda n: n.id)
    cov = defaultdict(Counter)
    for z in zettels:
        for s in source_ids(z):
            cov[z.meta.get("skill")][s] += 1
    lines = ["# Acoperire: skill × sursă", "", f"_Generat de `kb.py build` la {_dt.datetime.now():%Y-%m-%d %H:%M}._", "",
             "Câte note permanente din fiecare skill citează fiecare sursă.", "",
             "## Pe skill", "", "| Skill | Note | Nivel 1/2/3 | Surse folosite | Top surse |", "|---|---|---|---|---|"]
    for s in SKILLS["skills"]:
        own = by_skill.get(s["slug"], [])
        lv = Counter(str(z.meta.get("level")) for z in own)
        top = ", ".join(f"{k} ({v})" for k, v in cov[s["slug"]].most_common(4))
        lines.append(f"| {s['code']} {s['name']} | {len(own)} | {lv['1']}/{lv['2']}/{lv['3']} | {len(cov[s['slug']])} | {top} |")
    lines += ["", "## Pe sursă", "", "| Sursă | Titlu | Note care o citează | Skill-uri |", "|---|---|---|---|"]
    for sn in srcs:
        cnt = sum(cov[k][sn.id] for k in cov)
        sk = sorted({k for k in cov if cov[k][sn.id]})
        lines.append(f"| {sn.id} | {sn.title} | {cnt} | {', '.join(SKILL_BY_SLUG[k]['code'] for k in sk if k in SKILL_BY_SLUG)} |")
    thin = [s for s in SKILLS["skills"] if len(by_skill.get(s["slug"], [])) < 10]
    if thin:
        lines += ["", "## Goluri", ""] + [f"- **{s['code']}** {s['name']}: doar {len(by_skill.get(s['slug'], []))} note." for s in thin]
    (META / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # INDEX auto
    idx = ROOT / "INDEX.md"
    if idx.exists():
        t = idx.read_text(encoding="utf-8")
        parts = []
        for d in SKILLS["domains"]:
            parts.append(f"### {d['code']} · {d['name']}\n")
            for c in d["skills"]:
                s = SKILL_BY_CODE[c]
                own = by_skill.get(s["slug"], [])
                parts.append(f"- [[20-skills/{s['slug']}/SKILL|{c}]] **{s['name']}** — {len(own)} note")
            parts.append("")
        parts.append(f"**Total:** {len(zettels)} note permanente · {len(srcs)} surse · "
                     f"{len([n for n in notes if n.type == 'map'])} hărți · {len(edges)} legături")
        idx.write_text(replace_block(t, AUTO_START, AUTO_END, "\n".join(parts)), encoding="utf-8")

    print(f"build: {len(notes)} note, {len(edges)} legături. Catalog, graf, acoperire actualizate.")


# ---------------------------------------------------------------- suggest

STOP = set("""a ai al ale am ar are as asa asta aceasta acest acesta aceste acestea acei aceia acel acela acele
acolo acum adica ai al alt alta alte altii am apoi ar are as atat atunci au avea b ba c ca cand care cat cate catre
ce cea cei cel cele cele ceva chiar ci cine cum cu d da daca dar de deci decat deja desi despre din dintr dintre doar
dupa e ea ei el ele era este eu fara fi fie fiecare fiind foarte fost fata g h i ia iar ii il imi in inainte inca
intr intre isi j l la le li lor lui m ma mai mult multe multi n ne nici nimic noi nostru nu o ori p pe pentru peste
poate pot prin s sa sau se si sunt spre sub sus t ta tot toata toate toti tu u un una unei unor unde unei unui v va
vor x z the and of to in a is for that on with as by an be or are from this it at not your you can they their more
nota notei note idee ideea exemplu aplicare explicatie intrebari legaturi surse cap p vezi fundament extinde src
""".split())


def tokenize(text):
    t = deaccent(text.lower())
    t = re.sub(r"\[\[[^\]]*\]\]", " ", t)
    return [w for w in re.findall(r"[a-z][a-z0-9-]{2,}", t) if w not in STOP]


def cmd_suggest(skill=None, top=6, min_sim=0.10):
    notes = [n for n in load() if n.type == "zettel"]
    docs = {}
    for n in notes:
        body = n.body_without_auto()
        body = re.split(r"^## (Legături|Surse)\b", body, flags=re.M)[0]
        tags = " ".join(as_list(n.meta.get("tags")))
        docs[n.id] = tokenize((n.title + " ") * 3 + (tags + " ") * 2 + body)
    df = Counter()
    for toks in docs.values():
        df.update(set(toks))
    N = len(docs)
    vecs = {}
    for i, toks in docs.items():
        tf = Counter(toks)
        v = {w: (1 + math.log(c)) * math.log((N + 1) / (df[w] + 0.5)) for w, c in tf.items() if df[w] < N * 0.4}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vecs[i] = {w: x / norm for w, x in v.items()}
    linked = set()
    for n in notes:
        for t, _ in n.links():
            linked.add((n.id, t))
            linked.add((t, n.id))
    by_id = {n.id: n for n in notes}
    postings = defaultdict(list)
    for i, v in vecs.items():
        for w, x in v.items():
            postings[w].append((i, x))
    out = []
    for n in notes:
        if skill and n.meta.get("skill") != skill and skill not in as_list(n.meta.get("also")):
            continue
        scores = Counter()
        for w, x in vecs[n.id].items():
            for j, y in postings[w]:
                if j != n.id:
                    scores[j] += x * y
        cands = [(j, s) for j, s in scores.most_common(40) if s >= min_sim and (n.id, j) not in linked][:top]
        if cands:
            out.append((n, cands))
    lines = ["# Propuneri de legături", "",
             f"_Generat de `kb.py suggest` la {_dt.datetime.now():%Y-%m-%d %H:%M}. Similaritate TF-IDF; "
             "confirmă doar legăturile care au un motiv clar și scrie-le cu relație tipizată._", ""]
    for n, cands in out:
        lines.append(f"## {n.id} — {n.title}")
        for j, s in cands:
            o = by_id[j]
            same = "" if o.meta.get("skill") == n.meta.get("skill") else f" · _{o.meta.get('skill')}_"
            lines.append(f"- {s:.2f} [[{j}]] {o.title}{same}")
        lines.append("")
    name = f"link-suggestions-{skill}.md" if skill else "link-suggestions.md"
    (META / name).write_text("\n".join(lines), encoding="utf-8")
    print(f"suggest: {sum(len(c) for _, c in out)} propuneri pentru {len(out)} note → _meta/{name}")


# ---------------------------------------------------------------- merge / renumber / new

def rewrite_ids(mapping, notes=None):
    """Înlocuiește ID-uri în toate fișierele .md (o singură trecere, fără înlănțuiri)."""
    if not mapping:
        return
    pat = re.compile(r"\b(" + "|".join(re.escape(k) for k in sorted(mapping, key=len, reverse=True)) + r")\b(?!-\d)")
    for p in iter_md():
        t = p.read_text(encoding="utf-8")
        new = pat.sub(lambda m: mapping[m.group(1)], t)
        # legăturile [[OLD-slug|...]] devin [[NEW-slug|...]]; build le reface oricum
        if new != t:
            p.write_text(new, encoding="utf-8")


def set_list_field(text, field, values):
    fm, body = split_frontmatter(text)
    if fm is None:
        return text
    lines = fm.splitlines()
    out, i, done = [], 0, False
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{field}:", line):
            done = True
            i += 1
            while i < len(lines) and re.match(r"^\s+-\s", lines[i]):
                i += 1
            if field == "sources":
                out.append(f"{field}:")
                out += [f"  - {v}" for v in values]
            else:
                out.append(f"{field}: [{', '.join(values)}]")
            continue
        out.append(line)
        i += 1
    if not done:
        out.append(f"{field}: [{', '.join(values)}]" if field != "sources" else f"{field}:\n" + "\n".join(f"  - {v}" for v in values))
    return f"---\n" + "\n".join(out) + f"\n---\n{body}"


def cmd_merge(keep, drop):
    notes = load()
    by_id, _ = index(notes)
    if keep not in by_id or drop not in by_id:
        sys.exit(f"ID inexistent: {keep if keep not in by_id else drop}")
    k, d = by_id[keep], by_id[drop]
    text = k.text
    for field in ("sources", "tags", "also"):
        kv, dv = as_list(k.meta.get(field)), as_list(d.meta.get(field))
        merged = kv + [x for x in dv if x not in kv and not (field == "also" and x == k.meta.get("skill"))]
        if field == "also" and d.meta.get("skill") != k.meta.get("skill") and d.meta.get("skill") not in merged:
            merged.append(d.meta.get("skill"))
        if merged != kv:
            text = set_list_field(text, field, merged)
    k.path.write_text(text, encoding="utf-8")
    d.path.unlink()
    rewrite_ids({drop: keep})
    # elimină auto-legăturile apărute după redirect
    t = k.path.read_text(encoding="utf-8")
    t = re.sub(rf"^\s*[-*]\s*\*\*\w+\*\*\s*\[\[{re.escape(keep)}[^\]]*\]\].*\n", "", t, flags=re.M)
    k.path.write_text(t, encoding="utf-8")
    log = META / "merges.log"
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"{_dt.datetime.now():%Y-%m-%d %H:%M}\t{drop} → {keep}\t{d.title}\n")
    print(f"merge: {drop} → {keep}. Toate legăturile spre {drop} trimit acum la {keep}. Rulează build.")


def cmd_redirect(path):
    """Aplică redirecționări dintr-un fișier: pe fiecare rând `DROP KEEP` (sau `DROP → KEEP`)."""
    mapping = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        ids = re.findall(r"[A-Z]{3}-\d{3,4}", line)
        if len(ids) >= 2 and not line.lstrip().startswith("#"):
            mapping[ids[0]] = ids[1]
    # rezolvă lanțurile A→B, B→C
    for k in list(mapping):
        seen = {k}
        while mapping[k] in mapping and mapping[k] not in seen:
            seen.add(mapping[k])
            mapping[k] = mapping[mapping[k]]
    rewrite_ids(mapping)
    with open(META / "merges.log", "a", encoding="utf-8") as f:
        for a, b in mapping.items():
            f.write(f"{_dt.datetime.now():%Y-%m-%d %H:%M}\t{a} → {b}\t(redirect)\n")
    print(f"redirect: {len(mapping)} ID-uri redirecționate. Rulează build.")


def skill_order(skill_note, own_ids):
    body = skill_note.body_without_auto()
    order = []
    for m in LINK_RE.finditer(body):
        tid = resolve_target(m.group(1))
        if tid in own_ids and tid not in order:
            order.append(tid)
    return order


def cmd_renumber(dry=False):
    notes = load()
    by_id, dups = index(notes)
    if dups:
        sys.exit("ID-uri duplicate; rezolvă-le întâi (kb.py check).")
    mapping = {}
    for s in SKILLS["skills"]:
        own = sorted([n for n in notes if n.type == "zettel" and n.id.startswith(s["code"] + "-")],
                     key=lambda n: (int(n.meta.get("level", 9) or 9), n.id))
        own_ids = [n.id for n in own]
        hub = by_id.get(s["code"])
        order = skill_order(hub, set(own_ids)) if hub else []
        order += [i for i in own_ids if i not in order]
        for k, old in enumerate(order, 1):
            new = f"{s['code']}-{k:03d}"
            if new != old:
                mapping[old] = new
    if dry:
        for a, b in mapping.items():
            print(f"{a} → {b}")
        return
    rewrite_ids(mapping)
    for n in load():
        if n.type == "zettel":
            want = f"{n.id}-{slugify(n.title)}.md"
            if n.path.name != want:
                n.path.rename(n.path.with_name(want))
    (META / "renumber-map.json").write_text(json.dumps(mapping, indent=1), encoding="utf-8")
    print(f"renumber: {len(mapping)} ID-uri schimbate → _meta/renumber-map.json. Rulează acum build.")


def cmd_new(code, title):
    s = SKILL_BY_CODE.get(code)
    if not s:
        sys.exit(f"Cod necunoscut: {code}")
    notes = load()
    nums = [int(n.id.split("-")[1]) for n in notes if n.type == "zettel" and n.id.startswith(code + "-")]
    nid = f"{code}-{(max(nums) + 1 if nums else 1):03d}"
    tpl = (META / "templates" / "zettel.md").read_text(encoding="utf-8")
    tpl = tpl.replace("XXX-000", nid, 1).replace("skill-slug", s["slug"])
    tpl = tpl.replace("Titlul este o afirmație sau un concept precis", title)
    p = ROOT / "20-skills" / s["slug"] / "notes" / f"{nid}-{slugify(title)}.md"
    p.write_text(tpl, encoding="utf-8")
    print(p.relative_to(ROOT))


def cmd_stats():
    notes = load()
    z = [n for n in notes if n.type == "zettel"]
    print(f"Note: {len(notes)} · permanente: {len(z)} · surse: {sum(n.type == 'source' for n in notes)} · hărți: {sum(n.type == 'map' for n in notes)}")
    by = Counter(n.meta.get("skill") for n in z)
    for s in SKILLS["skills"]:
        print(f"  {s['code']} {s['slug']:24} {by[s['slug']]:>4}")
    print("kind:", dict(Counter(n.meta.get("kind") for n in z)))
    print("level:", dict(Counter(str(n.meta.get("level")) for n in z)))
    print("status:", dict(Counter(n.meta.get("status") for n in z)))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, args = argv[0], argv[1:]

    def opt(name, default=None, cast=str):
        if name in args:
            i = args.index(name)
            return cast(args[i + 1])
        return default

    if cmd == "check":
        cmd_check()
    elif cmd == "build":
        cmd_build(rename="--rename" in args)
    elif cmd == "suggest":
        cmd_suggest(skill=opt("--skill"), top=opt("--top", 6, int), min_sim=opt("--min", 0.10, float))
    elif cmd == "merge" and len(args) == 2:
        cmd_merge(args[0], args[1])
    elif cmd == "redirect" and len(args) == 1:
        cmd_redirect(args[0])
    elif cmd == "renumber":
        cmd_renumber(dry="--dry-run" in args)
    elif cmd == "new" and len(args) == 2:
        cmd_new(args[0], args[1])
    elif cmd == "stats":
        cmd_stats()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
