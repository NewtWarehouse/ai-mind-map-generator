from __future__ import annotations

from mindmap.core.extractor import extract_concepts


def test_extract_basic_sentences() -> None:
    text = "Graphs are useful. Mind maps show relations. AI helps extract concepts."
    spans = extract_concepts(text)
    assert len(spans) == 3
    assert spans[0].text == "Graphs are useful"


def test_extract_is_deterministic() -> None:
    text = "Cats sleep. Dogs bark. Birds sing."
    a = extract_concepts(text)
    b = extract_con