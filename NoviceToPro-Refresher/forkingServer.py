#A Forking Server
import socketserver
from socketserver import TCPServer

class Server(socketserver.TCPServer., TCPServer): pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from ',addr)
        self.wfile.write('Thankyou for connecting')

server = Server(('',1234),Handler)
server.serve_forever()
