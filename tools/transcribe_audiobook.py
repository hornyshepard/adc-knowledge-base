"""Transcrie local un audiobook (folder cu NN.mp3) cu mlx-whisper (Apple Silicon).

Utilizare:
    pip install mlx-whisper
    python tools/transcribe_audiobook.py --src "/cale/spre/copia/Audiobook_..." --out 90-library/text/audiobook

Rezultat: un fișier <out>/NN.txt per capitol. Reia de unde a rămas dacă e întrerupt.
"""
import argparse
import time
from pathlib import Path

import mlx_whisper

ap = argparse.ArgumentParser()
ap.add_argument("--src", required=True, help="folderul cu COPIILE fișierelor mp3")
ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "90-library" / "text" / "audiobook"))
ap.add_argument("--model", default="mlx-community/whisper-large-v3-turbo")
ap.add_argument("--language", default="en")
args = ap.parse_args()

out = Path(args.out)
out.mkdir(parents=True, exist_ok=True)
files = sorted(Path(args.src).glob("*.mp3"), key=lambda p: int(p.stem) if p.stem.isdigit() else p.stem)
for f in files:
    dst = out / (f"{int(f.stem):02d}.txt" if f.stem.isdigit() else f"{f.stem}.txt")
    if dst.exists():
        continue
    t = time.time()
    r = mlx_whisper.transcribe(str(f), path_or_hf_repo=args.model, language=args.language)
    dst.write_text(r["text"].strip())
    print(f"{f.name}: {time.time() - t:.0f}s, {len(r['text'].split())} cuvinte", flush=True)
