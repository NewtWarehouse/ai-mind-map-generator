"""CLI entrypoint. `mmg` and `python -m mindmap` land here."""
from __future__ import annotations

import argparse
import sys

from mindmap.bootstrap import bootstrap
from mindmap.utils.logging import get_logger

log = get_logger(__name__)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mmg", description="AI mind map generator")
    p.add_argument("input", nargs="?", help="Path to a .txt, .md, or .pdf source document")
    p.add_argument("--out", "-o", default="exports/map.mmg.json", help="Output path for the map")
    p.add_argument("--provider", default="openai", help="LLM provider name")
    p.add_argument("--model", default=None, help="Override model id for the provider")
    p.add_argument("--gui", action="store_true", help="Launch the desktop UI instead of CLI")
    p.add_argument("--verbose", "-v", action="count", default=0)
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    ctx = bootstrap(verbose=args.verbose)

    if args.gui or args.input is None:
        from mindmap.app import run

        return run(ctx)

    from mindmap.handlers.generate import generate_from_path

    try:
        result = generate_from_path(ctx, args.input, provider=args.provider, model=args.model)
    except Exception as exc:  # noqa: BLE001 — top-level CLI guard
        log.error("generation failed: %s", exc)
        return 2

    result.save(args.out)
    log.info("wrote %d nodes / %d edges to %s", len(result.nodes), len(result.edges), args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())