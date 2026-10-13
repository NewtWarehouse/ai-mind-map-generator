"""Layered layout for the map canvas. Deterministic given the graph."""
from __future__ import annotations

import math

import networkx as nx


def radial_layout(g: nx.MultiDiGraph, *, radius: float = 320.0) -> dict[str, tuple[float, float]]:
    """Place highest-degree node at origin, others on concentric rings by depth."""
    if g.number_of_nodes() == 0:
        return {}
    root = max(g.nodes, key=lambda n: g.degree(n))
    depths = nx.single_source_shortest_path_length(g.to_undirected(), root)
    rings: dict[int, list[str]] = {}
    for node, depth in depths.items():
        rings.setdefault(depth, []).append(node)

    pos: dict[str, tuple[float, float]] = {root: (0.0, 0.0)}
    for depth, members in rings.items():
        if depth == 0:
            continue
        r = radius * depth
        step = (2.0 * math.pi) / max(1, len(members))
        for i, node in enumerate(sorted(members)):
            angle = i * step
            pos[node] = (r * math.cos(angle), r * math.sin(angle))
    return pos