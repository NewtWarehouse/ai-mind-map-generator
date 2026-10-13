# Contributing to ai-mind-map-generator

Thanks for wanting to grow the tater. This is a Windows-first desktop
mind map generator that turns text, PDFs, and markdown into navigable
maps of concepts, then lets you edit, export, and re-query them.

## Ground rules

- Python 3.11+ only. We use `match` statements, tomllib, and `StrEnum`.
- One feature, one handler module under `mindmap/handlers/`.
- Core algorithms live under `mindmap/core/`. Handlers orchestrate,
  core computes. No business logic in `ui/`.
- Every new public function gets a docstring and a type signature.
- Tests go in `tests/` and mirror the source tree.

## Dev setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pre-commit install
pytest -q
```

## Style

- `ruff` handles lint + format. Line length 100.
- `mypy --strict` on `mindmap/core` and `mindmap/models`.
- No `print()` in library code — use the `mindmap.utils.logging` logger.

## Pull requests

- Branch from `main`, name it `feat/<topic>` or `fix/<topic>`.
- Include a short demo (screenshot or transcript) for UI changes.
- CI must pass: lint, types, tests, and a headless smoke import.

## Reporting bugs

Open an issue with the OS build, Python version, the input document
(if shareable), and the full traceback. Redact anything private.