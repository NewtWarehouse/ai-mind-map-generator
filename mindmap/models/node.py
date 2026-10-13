from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

NodeKind = Literal["concept", "entity", "topic", "note"]


class MindNode(BaseModel):
    id: str
    label: str
    kind: NodeKind = "concept"
    weight: float = Field(default=0.5, ge=0.0, le=1.0)
    note: str = ""