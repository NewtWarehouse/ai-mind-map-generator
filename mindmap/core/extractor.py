"""Concept extraction: turn raw text into candidate concept spans."""
from __future__ import annotations

import re
from dataclasses import dataclass

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
_STOPWORDS = frozenset(
    """a an the and or but if then than that this these those of in on at to for
    with by from is are was were be been being it its as into over under""".split()
)


@dataclass(frozen=True, slots=True)
class ConceptSpan:
    text: str
    start: int
    end: int
    weight: float


def _score(phrase: str) -> float:
    """Length-normalized frequency proxy. Longer phrases carry more signal."""
    words = [w for w in phrase.lower().split() if w not in _STOPWORDS]
    if not words:
        return 0.0
    return min(1.0, len(words) / 6.0) * (1.0 + 0.1 * len(phrase))


def extract_concepts(text: str, *, min_len: int = 3, max_len: int = 64) -> list[ConceptSpan]:
    """Extract candidate concept spans from a document.

    Returns spans in document order. Deterministic: same input -> same output.
    """
    spans: list[ConceptSpan] = []
    cursor = 0
    for sentence in _SENT_SPLIT.split(text):
        if not sentence.strip():
            cursor += len(sentence) + 1
            continue
        head = sentence.split(",", 1)[0].strip()
        if min_len <= len(head) <= max_len:
            spans.append(ConceptSpan(head, cursor, cursor + len(head), _score(head)))
        cursor += len(sentence) + 1
    return spans