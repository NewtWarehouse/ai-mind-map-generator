"""End-to-end: source document -> MindMap. The CLI and GUI both call this."""
from __future__ import annotations

from pathlib import Path

from mindmap.bootstrap import AppContext
from mindmap.core.extractor import extract_concepts
from mindmap.core.graph_builder import build_graph, spans_to_nodes
from mindmap.models.map import MindMap
from mindmap.services.parsers import parse_document
from mindmap.utils.logging import get_logger

log = get_logger(__name__)


def generate_from_path(
    ctx: AppContext,
    path: str | Path,
    *,
    provider: str | None = None,
    model: str | None = None,
) -> MindMap:
    """Read a document, extract concepts, ask the LLM for edges, return a map."""
    doc = parse_document(Path(path))
    log.info("parsed %d chars from %s", len(doc.text), path)

    spans = extract_concepts(doc.text)
    nodes = spans_to_nodes(spans)[: ctx.settings.max_nodes]
    log.info("extracted %d candidate nodes", len(nodes))

    edges = ctx.llm.infer_edges(nodes, provider=provider, model=model)
    g = build_graph(nodes, edges)
    return MindMap.from_graph(g, title=doc.title or Path(path).stem)