import http.server
import socketserver

# Define the port the server will run on
PORT = 3135

# Define the directory to serve (relative to this script's location)
DIRECTORY = "ktitan-public"

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    A simple HTTP request handler that adds the CORS header.
    """
    def __init__(self, *args, **kwargs):
        # Set the directory for the server
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 1. Add the CORS Header
        # Allows requests from any origin (*). For a production environment,
        # you should change '*' to your specific client origin (e.g., 'http://localhost:3000')
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        
        # 2. Complete the standard headers
        super().end_headers()

    def do_OPTIONS(self):
        # Handle the pre-flight request used by modern browsers for non-simple requests
        self.send_response(200)
        self.end_headers()

# Start the server
with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Serving directory '{DIRECTORY}' at http://localhost:{PORT}")
    httpd.serve_forever()