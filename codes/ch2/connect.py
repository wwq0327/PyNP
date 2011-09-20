#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    connect.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
"""

import socket

print "Creating socket...",
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'done.'

print "Connecting to remote host...",
s.connect(("www.google.com", 80))
print "done."
