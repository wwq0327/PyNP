#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    connect2.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
"""

import socket

print 'Creating socket...',
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'done.'

print "Looking up port number...",
port = socket.getservbyname('http', 'tcp')
print 'done.'

print "Connecting to remote host on port %d..." % port,
s.connect(("www.google.com", port))
print "done."
