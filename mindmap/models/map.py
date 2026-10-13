from __future__ import annotations

from typing import Any
import networkx as nx
from pydantic import BaseModel, Field

from mindmap.models.edge import MindEdge
from mindmap.models.node import MindNode


class MindMap(BaseModel):
    title: str
    nodes: list[MindNode] = Field(default_factory=list)
    edges: list[MindEdge] = Field(default_factory=list)

    @classmethod
    def from_graph(cls, g: nx.MultiDiGraph, *, title: str) -> "MindMap":
        nodes = [
            MindNode(id=n, label=g.nodes[n].get("label", n), kind=g.nodes[n].get("kind", "concept"),
                     weight=float(g.nodes[n].get("weight", 0.5)))
            for n in g.nodes
        ]
        edges = [
            MindEdge(source=u, target=v, relation=d.get("relation", "relates_to"),
                     weight=float(d.get("weight", 0.5)))
            for u, v, d in g.edges(data=True)
        ]
        return cls(title=title, nodes=nodes, edges=edges)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "nodes": [n.model_dump() for n in self.nodes],
            "edges": [e.model_dump() for e in self.edges],
        }