"""Simple static file server for the Smart ERP dashboard."""

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

HOST = "0.0.0.0"
PORT = 8000


def main() -> None:
    """Run a basic HTTP server for local development."""
    with TCPServer((HOST, PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on http://{HOST}:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
