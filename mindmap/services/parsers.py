"""Document parsers. Plain text, markdown, and PDF (via pypdf)."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mindmap.utils.logging import get_logger

log = get_logger(__name__)


@dataclass(frozen=True, slots=True)
class ParsedDocument:
    title: str
    text: str
    source: Path


def parse_document(path: Path) -> ParsedDocument:
    if not path.exists():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md", ".markdown"}:
        text = path.read_text(encoding="utf-8")
        return ParsedDocument(_title_from(text, path), text, path)
    if suffix == ".pdf":
        return _parse_pdf(path)
    raise ValueError(f"unsupported document type: {suffix}")


def _title_from(text: str, path: Path) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line:
            return line[:80]
    return path.stem


def _parse_pdf(path: Path) -> ParsedDocument:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(pages)
    return ParsedDocument(path.stem, text, path)