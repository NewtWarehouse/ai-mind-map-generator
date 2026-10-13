"""Bootstrap: load config, wire services, hand back a ready AppContext."""
from __future__ import annotations

from dataclasses import dataclass

from mindmap.config.settings import Settings, load_settings
from mindmap.services.llm_client import LLMClient
from mindmap.services.bridge import LocalBridge
from mindmap.utils.logging import get_logger, set_verbosity

log = get_logger(__name__)


@dataclass(slots=True)
class AppContext:
    settings: Settings
    llm: LLMClient
    bridge: LocalBridge


def bootstrap(*, verbose: int = 0) -> AppContext:
    set_verbosity(verbose)
    settings = load_settings()
    log.info("bootstrap: provider=%s model=%s", settings.provider, settings.model)

    llm = LLMClient(settings)
    bridge = LocalBridge(settings.bridge_port)
    return AppContext(settings=settings, llm=llm, bridge=bridge)