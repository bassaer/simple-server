import SimpleHTTPServer
import SocketServer
import socket

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler
print 'running'
SocketServer.TCPServer(("", 8000), Handler).serve_forever()
