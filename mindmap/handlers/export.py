"""Export a MindMap to JSON, Markdown outline, or GraphViz dot."""
from __future__ import annotations

import json
from pathlib import Path

from mindmap.models.map import MindMap


def to_json(m: MindMap) -> str:
    return json.dumps(m.to_dict(), indent=2, ensure_ascii=False)


def to_markdown(m: MindMap) -> str:
    lines = [f"# {m.title}", ""]
    for node in sorted(m.nodes, key=lambda n: -n.weight):
        lines.append(f"- {node.label}  _(w={node.weight:.2f})_")
    return "\n".join(lines) + "\n"


def to_dot(m: MindMap) -> str:
    out = [f'digraph "{m.title}" {{', "  rankdir=LR;"]
    for n in m.nodes:
        out.append(f'  "{n.id}" [label="{n.label}"];')
    for e in m.edges:
        out.append(f'  "{e.source}" -> "{e.target}" [label="{e.relation}"];')
    out.append("}")
    return "\n".join(out)


def export(m: MindMap, path: str | Path, fmt: str = "json") -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    body = {"json": to_json, "markdown": to_markdown, "dot": to_dot}[fmt](m)
    p.write_text(body, encoding="utf-8")
    return p