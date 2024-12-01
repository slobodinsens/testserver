from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST_NAME = '0.0.0.0'  # Bind to all interfaces
PORT_NUMBER = int(os.environ.get('PORT', 8080))  # Get Heroku's dynamic port

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello, world!", "utf-8"))

if __name__ == '__main__':
    webServer = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    print("Server started on port %s" % PORT_NUMBER)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
