"""Static server for the orb page that also saves POSTed frames to ./frames/<n>.png."""
import http.server
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
FRAMES = ROOT / "frames"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def do_POST(self):
        name = self.path.rsplit("/", 1)[-1]
        if not (name.endswith(".png") and name[:-4].isdigit()):
            self.send_error(400)
            return
        body = self.rfile.read(int(self.headers["Content-Length"]))
        (FRAMES / name).write_bytes(body)
        self.send_response(204)
        self.end_headers()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), Handler).serve_forever()
