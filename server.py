from http.server import BaseHTTPRequestHandler, HTTPServer

class index(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, index)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()