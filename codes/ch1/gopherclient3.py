#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    gopherclient3.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
"""

import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fd = s.makefile('rw', 0)

fd.write(filename+'\r\n')

for line in fd.readlines():
    sys.stdout.write(line)
