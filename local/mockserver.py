from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = "localhost"
SERVER_PORT = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{'devText': 'GET request received.'}", "utf-8"))

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{'devText': 'POST request received.'}", "utf-8"))

    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{'devText': 'PUT request received.'}", "utf-8"))

    def do_PATCH(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{'devText': 'PATCH request received.'}", "utf-8"))

    def do_DELETE(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{'devText': 'DELETE request received.'}", "utf-8"))


def run():
    web_server = HTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    print("Server started http://%s:%s" % (HOST_NAME, SERVER_PORT))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    run()
