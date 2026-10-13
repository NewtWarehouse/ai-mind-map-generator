from __future__ import annotations

import logging
import sys

_CONFIGURED = False
_LEVEL = logging.INFO


def set_verbosity(verbose: int) -> None:
    global _LEVEL
    _LEVEL = logging.DEBUG if verbose >= 2 else logging.INFO


def get_logger(name: str) -> logging.Logger:
    global _CONFIGURED
    if not _CONFIGURED:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        root = logging.getLogger("mindmap")
        root.addHandler(handler)
        root.setLevel(_LEVEL)
        _CONFIGURED = True
    return logging.getLogger(name)