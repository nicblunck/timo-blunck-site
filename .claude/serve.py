import functools, http.server, socketserver

DIRECTORY = "/Users/nicolasblunck/Documents/Github/Timo Blunck Site"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
with socketserver.TCPServer(("127.0.0.1", 4321), Handler) as httpd:
    print("serving on 4321")
    httpd.serve_forever()
