#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    gethostbyaddr.py
    ~~~~~~~~~~~~~~~~~~~~

    反向查询域名
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import sys, socket

try:
    result = socket.gethostbyaddr(sys.argv[1])
    print "Primary looked-up hostname:"
    print ' ' + result[0] # 获取域名

    print "\nAddresses:"
    for item in result[2]:
        print ' ' + item

except socket.herror, e:
    print "Couldn't look up name:", e
