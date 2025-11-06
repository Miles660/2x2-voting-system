import http.server
import socketserver
import json
from http import HTTPStatus
import io

class HostHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.METHOD_NOT_ALLOWED)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        input_data = data.get('input', 0)

        # 输出总是+10
        output = input_data + 10

        response = json.dumps({'input': input_data, 'output': output})
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode())

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), HostHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
