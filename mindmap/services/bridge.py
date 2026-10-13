"""Local HTTP bridge for plugins/browser extensions. Binds 127.0.0.1 only."""
from __future__ import annotations

import threading

from mindmap.utils.logging import get_logger

log = get_logger(__name__)


class LocalBridge:
    def __init__(self, port: int = 8765) -> None:
        self.port = port
        self._server: threading.Thread | None = None

    def start(self) -> None:
        from http.server import BaseHTTPRequestHandler, HTTPServer

        port = self.port

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self) -> None:  # noqa: N802
                if self.path == "/health":
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"ok")
                else:
                    self.send_response(404)
                    self.end_headers()

            def log_message(self, fmt: str, *args: object) -> None:
                log.debug("bridge: " + fmt, *args)

        srv = HTTPServer(("127.0.0.1", port), Handler)
        t = threading.Thread(target=srv.serve_forever, daemon=True, name="mmg-bridge")
        t.start()
        self._server = t
        log.info("local bridge listening on 127.0.0.1:%d", port)