from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import ollama
import json
import os

HOST = "0.0.0.0"
PORT = 9999


def send_request(question):
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': question,
        },
    ])
    return response['message']['content']


class classHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "r") as file:
                self.wfile.write(bytes(file.read(), "utf-8"))
        elif self.path.startswith("/ask"):
            query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            question = query_components.get("question", ["Why is the sky blue?"])[0]
            response_content = send_request(question)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"response": response_content}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        question = urllib.parse.parse_qs(post_data).get('question', [""])[0]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_content = send_request(question)
        response = {"response": response_content}
        self.wfile.write(bytes(json.dumps(response), "utf-8"))


server = HTTPServer((HOST, PORT), classHTTP)
print('Server running and listening on 127.0.0.1:9999')
server.serve_forever()
server.server_close()
