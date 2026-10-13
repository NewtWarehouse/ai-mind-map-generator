"""Build a NetworkX graph from concept spans + LLM-suggested relations."""
from __future__ import annotations

from collections.abc import Iterable

import networkx as nx

from mindmap.core.extractor import ConceptSpan
from mindmap.models.node import MindNode
from mindmap.models.edge import MindEdge


def build_graph(
    nodes: Iterable[MindNode],
    edges: Iterable[MindEdge],
) -> nx.MultiDiGraph:
    """Assemble a multigraph. Duplicate (u, v, label) triples collapse."""
    g: nx.MultiDiGraph = nx.MultiDiGraph()
    for n in nodes:
        g.add_node(n.id, label=n.label, kind=n.kind, weight=n.weight)
    seen: set[tuple[str, str, str]] = set()
    for e in edges:
        key = (e.source, e.target, e.relation)
        if key in seen or e.source not in g or e.target not in g:
            continue
        seen.add(key)
        g.add_edge(e.source, e.target, key=e.relation, relation=e.relation, weight=e.weight)
    return g


def spans_to_nodes(spans: Iterable[ConceptSpan], *, prefix: str = "n") -> list[MindNode]:
    from mindmap.utils.ids import stable_id

    return [
        MindNode(
            id=stable_id(prefix, span.text),
            label=span.text,
            kind="concept",
            weight=span.weight,
        )
        for span in spans
    ]