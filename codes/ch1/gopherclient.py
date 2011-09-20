#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    gopherclient.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
    :usage: Python gopherclient.py quux.org /
"""

import socket, sys

if len(sys.argv) != 3:
    print __doc__
    sys.exit()

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(filename+"\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
    
