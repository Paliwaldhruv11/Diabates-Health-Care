"""Load `.env` into os.environ before Streamlit and tab modules import."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def _candidate_roots() -> list[Path]:
    roots: list[Path] = [
        Path(__file__).resolve().parent,
        Path.cwd(),
    ]
    if len(sys.argv) >= 2:
        script = Path(sys.argv[1]).resolve()
        if script.suffix.lower() == ".py":
            roots.append(script.parent)
    seen: set[Path] = set()
    out: list[Path] = []
    for r in roots:
        try:
            r = r.resolve()
        except OSError:
            continue
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def _manual_groq_key() -> None:
    if (os.getenv("GROQ_API_KEY") or "").strip():
        return
    prefix = "GROQ_API_KEY="
    for base in _candidate_roots():
        path = base / ".env"
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        for raw in text.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(prefix):
                val = line[len(prefix) :].strip().strip('"').strip("'")
                if val:
                    os.environ["GROQ_API_KEY"] = val
                    return


def bootstrap() -> None:
    for base in _candidate_roots():
        env_path = base / ".env"
        if env_path.is_file():
            load_dotenv(env_path, override=True, encoding="utf-8")
    _manual_groq_key()


bootstrap()
