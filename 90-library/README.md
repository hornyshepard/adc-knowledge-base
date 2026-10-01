# 90-library — textele integrale (doar local)

Acest folder conține, **doar pe calculatorul tău**, textul extras din copiile cărților (`text/<slug>.txt`) și transcrierea audiobook-ului (`text/audiobook/NN.txt`). Agenții AI le folosesc ca să verifice o notă sau să meargă mai adânc într-un capitol.

Textele **nu sunt în repository** (vezi `.gitignore`): sunt cărți protejate de drepturi de autor. Repository-ul conține doar notele (parafrazate, cu trimiteri la capitole/pagini) și uneltele.

## Cum regenerezi textele

Lucrează pe o **copie** a folderului cu cărți, nu pe originale.

```bash
pip install -r tools/requirements.txt
```

```bash
python tools/extract_texts.py --src "/cale/spre/copia/Books for ADC School" --out 90-library/text
```

Audiobook-ul (Apple Silicon, model Whisper local):

```bash
pip install mlx-whisper
```

```bash
python tools/transcribe_audiobook.py --src "/cale/spre/copia/Audiobook_Strategic Advertising Management 6th Edition"
```

Corespondența dintre ID-urile surselor (`SRC-0XX`) și fișiere este în `_meta/sources.json`.
