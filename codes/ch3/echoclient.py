#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    echoclient.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""
import socket, sys
host = 'localhost'
port = 51423

data = "x" * 10485760  ## 10MB of data

s = socket.socket()
s.connect((host, port))

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data))
    byteswritten += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
    sys.stdout.flush()

s.shutdown(1)

print "All date sent."
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
