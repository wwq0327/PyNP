#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    getaddrinfo-basic.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import sys, socket

result = socket.getaddrinfo(sys.argv[1], None)

print result[0][4]
## print result
