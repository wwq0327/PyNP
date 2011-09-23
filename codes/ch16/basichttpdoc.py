#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    basichttpdoc.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-23
    :from: Python Network Programming
"""

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time

starttime = time.time()

class RequestHandler(BaseHTTPRequestHandler):
    """Definintion of the request handler."""
    def _writeheaders(self, doc):
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _getdoc(self, filename):
        global starttime
        if filename == '/':
            return """<html><head><title>Sample Page</title></head>
            <body>this is a sample page.You can also look at the <a href="stats.html">server statistics</a>.</body></html>
            """
        elif filename == '/stats.html':
            return """This server has been running for %d seconds.""" % \
                   int(time.time() - starttime)
        else:
            return None

    def do_HEAD(self):
        doc = self._getdoc(self.path)
        self._writeheaders(doc)

    def do_GET(self):
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
        if doc is None:
            self.wfile.write("""The requested documnet '%s' was not found.""" %\
                             self.path)
        else:
            self.wfile.write(doc)

serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()
