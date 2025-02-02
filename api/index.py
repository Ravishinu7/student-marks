import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Simulated student marks data
STUDENT_MARKS = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow all origins
        self.end_headers()

        # Parse query parameters
        query = parse_qs(self.path[2:])  # Removing leading "/?"
        names = query.get("name", [])

        # Get marks for requested names
        marks = [STUDENT_MARKS.get(name, 0) for name in names]

        # Send JSON response
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode('utf-8'))
