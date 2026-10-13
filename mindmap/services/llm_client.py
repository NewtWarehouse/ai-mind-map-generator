"""LLM adapter. Routes to OpenAI, Anthropic, or a local llama.cpp model."""
from __future__ import annotations

import json
from collections.abc import Iterable

import httpx

from mindmap.config.settings import Settings
from mindmap.models.edge import MindEdge
from mindmap.models.node import MindNode
from mindmap.utils.logging import get_logger

log = get_logger(__name__)

_EDGE_SCHEMA_HINT = (
    'Return a JSON array of objects: '
    '{"source": "<node id>", "target": "<node id>", "relation": "<verb phrase>", '
    '"weight": <0..1>}. Only reference ids from the provided node list.'
)


class LLMClient:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = httpx.Client(timeout=60.0)

    def complete(self, prompt: str, *, provider: str | None = None, model: str | None = None) -> str:
        p = provider or self._settings.provider
        m = model or self._settings.model
        log.debug("llm.complete provider=%s model=%s", p, m)
        if p == "openai":
            return self._openai(prompt, m)
        if p == "anthropic":
            return self._anthropic(prompt, m)
        if p == "local":
            return self._local(prompt, m)
        raise ValueError(f"unknown provider: {p}")

    def infer_edges(
        self,
        nodes: Iterable[MindNode],
        *,
        provider: str | None = None,
        model: str | None = None,
    ) -> list[MindEdge]:
        node_list = list(nodes)
        payload = json.dumps([{"id": n.id, "label": n.label} for n in node_list], ensure_ascii=False)
        prompt = (
            "You are building a knowledge graph. Given these concept nodes, "
            "infer directional relations between closely related pairs.\n"
            f"{_EDGE_SCHEMA_HINT}\n\nNodes:\n{payload}\n"
        )
        raw = self.complete(prompt, provider=provider, model=model)
        return self._parse_edges(raw, {n.id for n in node_list})

    def _parse_edges(self, raw: str, valid_ids: set[str]) -> list[MindEdge]:
        start, end = raw.find("["), raw.rfind("]")
        if start == -1 or end == -1:
            log.warning("llm returned non-JSON edge payload")
            return []
        try:
            rows = json.loads(raw[start : end + 1])
        except json.JSONDecodeError as exc:
            log.warning("edge JSON malformed: %s", exc)
            return []
        out: list[MindEdge] = []
        for row in rows:
            if row.get("source") in valid_ids and row.get("target") in valid_ids:
                out.append(
                    MindEdge(
                        source=row["source"],
                        target=row["target"],
                        relation=str(row.get("relation", "relates_to")),
                        weight=float(row.get("weight", 0.5)),
                    )
                )
        return out

    def _openai(self, prompt: str, model: str) -> str:
        r = self._client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self._api_key()}"},
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": self._settings.temperature,
                "max_tokens": self._settings.max_tokens,
            },
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    def _anthropic(self, prompt: str, model: str) -> str:
        r = self._client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self._api_key(),
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": model,
                "max_tokens": self._settings.max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        r.raise_for_status()
        return r.json()["content"][0]["text"]

    def _local(self, prompt: str, model: str) -> str:
        r = self._client.post(
            "http://127.0.0.1:8080/completion",
            json={"prompt": prompt, "n_predict": self._settings.max_tokens, "model": model},
        )
        r.raise_for_status()
        return r.json()["content"]

    @staticmethod
    def _api_key() -> str:
        import os

        key = os.environ.get("MMG_API_KEY")
        if not key:
            raise RuntimeError("MMG_API_KEY is not set")
        return key