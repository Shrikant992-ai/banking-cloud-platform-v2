from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body, code = {"status": "UP", "service": "account-service"}, 200
        elif self.path == "/accounts/1001":
            body, code = {"account_id": 1001, "owner": "Demo Customer", "balance": 25000.50}, 200
        else:
            body, code = {"error": "not found"}, 404

        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)


HTTPServer(("0.0.0.0", 5001), Handler).serve_forever()
