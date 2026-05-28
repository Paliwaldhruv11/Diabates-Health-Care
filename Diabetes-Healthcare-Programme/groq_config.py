"""Groq API key, model name, and chat completion (OpenAI-compatible endpoint)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from streamlit.errors import StreamlitSecretNotFoundError

_PROJECT_ROOT = Path(__file__).resolve().parent
_GROQ_BASE_URL = "https://api.groq.com/openai/v1"
_DEFAULT_GROQ_MODEL = "llama-3.3-70b-versatile"


def _candidate_roots() -> list[Path]:
    roots: list[Path] = [_PROJECT_ROOT, Path.cwd()]
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


def _load_project_env() -> None:
    """Load `.env` from the repo root, cwd, and Streamlit script directory. Use override so a stale empty env var does not block the file."""
    for base in _candidate_roots():
        path = base / ".env"
        if path.is_file():
            load_dotenv(path, override=True, encoding="utf-8")


def _read_env_key_manual(name: str) -> str | None:
    """Read `NAME=value` from `.env` without relying on python-dotenv (handles BOM, odd line endings)."""
    for base in _candidate_roots():
        path = base / ".env"
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        prefix = f"{name}="
        for raw in text.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(prefix):
                val = line[len(prefix) :].strip().strip('"').strip("'")
                return val or None
    return None


def get_groq_model() -> str:
    _load_project_env()
    name = (os.getenv("GROQ_MODEL") or "").strip()
    if name:
        return name
    try:
        val = st.secrets["GROQ_MODEL"]
        if val is not None and str(val).strip():
            return str(val).strip()
    except (StreamlitSecretNotFoundError, KeyError):
        pass
    return _DEFAULT_GROQ_MODEL


def get_groq_api_key() -> str | None:
    _load_project_env()
    key = (os.getenv("GROQ_API_KEY") or "").strip()
    if not key:
        key = (_read_env_key_manual("GROQ_API_KEY") or "").strip()
        if key:
            os.environ["GROQ_API_KEY"] = key
    if key:
        return key
    try:
        val = st.secrets["GROQ_API_KEY"]
        return (str(val).strip() or None) if val is not None else None
    except (StreamlitSecretNotFoundError, KeyError):
        return None


def groq_chat_completion(messages: list[dict[str, str]]) -> str:
    """Run a chat completion on Groq. Raises if the API key is missing."""
    key = get_groq_api_key()
    if not key:
        raise ValueError("GROQ_API_KEY is not set")
    client = OpenAI(api_key=key, base_url=_GROQ_BASE_URL)
    response = client.chat.completions.create(
        model=get_groq_model(),
        messages=messages,
    )
    content = response.choices[0].message.content
    return (content or "").strip()
