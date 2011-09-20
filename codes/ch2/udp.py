#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    udp.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
"""

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
print "Enter data to transmit: "
data = sys.stdin.readline().strip()
s.sendall(data)
print "Looking for replies; press Ctrl-C or Ctrl-Break to stop."
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
