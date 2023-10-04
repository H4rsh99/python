import http.server
import socketserver

# Set the port you want the server to listen on
PORT = 8080

# Define the request handler
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving atttttt port {PORT}")
    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
