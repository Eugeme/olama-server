from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 9999


class classHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_content = {"response": "____________"}

        self.wfile.write(bytes(str(response_content), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_content = {"response": "____________"}

        self.wfile.write(bytes(str(response_content), "utf-8"))



server = HTTPServer((HOST, PORT), classHTTP)
print('sever running')
server.serve_forever()
server.server_close()
