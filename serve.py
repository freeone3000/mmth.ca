from http.server import SimpleHTTPRequestHandler, HTTPServer

class AlwaysGetIndexHandler(SimpleHTTPRequestHandler):
    """
    Custom request handler that serves index.html for all GET requests.
    """
    def do_GET(self):
        # Serve the index.html file for all GET requests
        self.path = 'index.html'
        return super().do_GET()

def main():
    # set up a simple HTTP server that responds to all requests with the contents of index.html
    server_address = ('', 8000)  # Serve on all addresses, port 8000
    httpd = HTTPServer(server_address, AlwaysGetIndexHandler)
    print(f'Serving on http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()


if __name__ == '__main__':
    main()