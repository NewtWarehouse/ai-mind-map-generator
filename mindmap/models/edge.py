from __future__ import annotations

from pydantic import BaseModel, Field


class MindEdge(BaseModel):
    source: str
    target: str
    relation: str = "relates_to"
    weight: float = Field(default=0.5, ge=0.0, le=1.0)