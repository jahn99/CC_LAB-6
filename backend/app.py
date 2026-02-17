from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f"Served by backend: {hostname}".encode())

PORT = 8080
server = HTTPServer(('', PORT), Handler)
print("Server running on port", PORT)
server.serve_forever()
