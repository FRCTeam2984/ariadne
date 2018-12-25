#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes
import json
from cairosvg import svg2png
from PIL import Image
import os
from io import BytesIO
from shutil import copyfileobj
from base64 import b64encode

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('favicon.ico'):
            return
        root = os.path.dirname(os.path.abspath(__file__))
        if self.path == "/":
            self.path = "/index.html"
        filename = root + self.path

        file = open(filename, "rb")
        self.send_response(200)
        self.send_header("Content-type", mimetypes.guess_type(filename)[0]+"; charset=utf-8")
        self.end_headers()
        copyfileobj(file, self.wfile)
        file.close()

    def do_POST(self):
        pass

def main():

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    main()
