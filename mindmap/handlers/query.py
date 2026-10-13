"""Natural-language query over an existing MindMap."""
from __future__ import annotations

from mindmap.bootstrap import AppContext
from mindmap.models.map import MindMap


def answer(ctx: AppContext, mindmap: MindMap, question: str) -> str:
    """Answer a question grounded in the map's nodes and edges."""
    context = "\n".join(
        f"{e.source} --{e.relation}--> {e.target}" for e in mindmap.edges
    )
    prompt = (
        "You are a mind map assistant. Answer using ONLY the edges below.\n\n"
        f"Edges:\n{context}\n\nQuestion: {question}\nAnswer:"
    )
    return ctx.llm.complete(prompt)