"""Desktop entrypoint. Wires the Qt application to the main window."""
from __future__ import annotations

import sys

from mindmap.bootstrap import AppContext, bootstrap
from mindmap.utils.logging import get_logger

log = get_logger(__name__)


def run(ctx: AppContext | None = None) -> int:
    """Launch the PySide6 desktop shell. Returns process exit code."""
    from PySide6.QtWidgets import QApplication

    from mindmap.ui.main_window import MainWindow

    ctx = ctx or bootstrap()
    app = QApplication.instance() or QApplication(sys.argv)
    app.setApplicationName("AI Mind Map Generator")

    window = MainWindow(ctx)
    window.resize(1280, 820)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(run())