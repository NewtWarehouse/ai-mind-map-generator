from __future__ import annotations

import hashlib


def stable_id(prefix: str, text: str) -> str:
    """Deterministic short id for a concept. Same text -> same id."""
    digest = hashlib.blake2s(text.strip().lower().encode("utf-8"), digest_size=6).hexdigest()
    return f"{prefix}_{digest}"