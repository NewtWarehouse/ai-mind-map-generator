"""Typed settings loaded from TOML + environment overrides."""
from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from platformdirs import user_config_dir

from mindmap.utils.logging import get_logger

log = get_logger(__name__)

Provider = Literal["openai", "anthropic", "local"]


class Settings(BaseModel):
    provider: Provider = "openai"
    model: str = "gpt-4o-mini"
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int = Field(default=2048, ge=128, le=32_768)
    bridge_port: int = Field(default=8765, ge=1024, le=65535)
    cache_dir: Path = Field(default_factory=lambda: Path(".mindmap_cache"))
    max_nodes: int = Field(default=200, ge=8, le=2000)
    api_key_env: str = "MMG_API_KEY"


def _config_path() -> Path:
    return Path(user_config_dir("ai-mind-map-generator", "PotatoLabs")) / "config.toml"


def load_settings() -> Settings:
    path = _config_path()
    raw: dict[str, object] = {}
    if path.exists():
        try:
            raw = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            log.warning("config at %s is malformed, using defaults: %s", path, exc)

    env_override = os.environ.get("MMG_PROVIDER")
    if env_override:
        raw["provider"] = env_override
    env_model = os.environ.get("MMG_MODEL")
    if env_model:
        raw["model"] = env_model

    return Settings.model_validate(raw)