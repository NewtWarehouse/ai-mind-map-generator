"""Main window: input pane, map canvas, export toolbar."""
from __future__ import annotations

from mindmap.bootstrap import AppContext
from mindmap.handlers.export import to_json
from mindmap.handlers.generate import generate_from_path
from mindmap.utils.logging import get_logger

log = get_logger(__name__)


class MainWindow:
    """Thin façade. Real implementation subclasses QMainWindow at import time."""

    def __init__(self, ctx: AppContext) -> None:
        from PySide6.QtWidgets import QMainWindow, QTextEdit, QToolBar, QFileDialog, QMessageBox

        self._ctx = ctx
        self._win = QMainWindow()
        self._editor = QTextEdit()
        self._win.setCentralWidget(self._editor)

        bar = QToolBar("Main")
        bar.addAction("Open", self._open)
        bar.addAction("Generate", self._generate)
        bar.addAction("Export JSON", self._export)
        self._win.addToolBar(bar)

    # Qt duck-typing: forward the surface used by app.run().
    def resize(self, w: int, h: int) -> None:
        self._win.resize(w, h)

    def show(self) -> None:
        self._win.show()

    def _open(self) -> None:
        from PySide6.QtWidgets import QFileDialog

        path, _ = QFileDialog.getOpenFileName(
            self._win, "Open document", "", "Documents (*.txt *.md *.pdf)"
        )
        if path:
            self._editor.setPlainText(open(path, encoding="utf-8", errors="replace").read())

    def _generate(self) -> None:
        from PySide6.QtWidgets import QMessageBox

        QMessageBox.information(self._win, "Generate", "Pick a file via Open, then File > Generate.")

    def _export(self) -> None:
        m = getattr(self, "_last_map", None)
        if m is None:
            return
        path, _ = QFileDialog.getSaveFileName(self._win, "Export", "map.mmg.json", "JSON (*.json)")
        if path:
            open(path, "w", encoding="utf-8").write(to_json(m))