#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import sys
import Adafruit_DHT

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        params = 't: {0:0.1f},  u: {1:0.1f}'.format(temperature, humidity)
        json = 'callback({ %s });' % (params)
        self.request.sendall(json)

def run(server_class=HTTPServer, handler_class=S, port=3001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
