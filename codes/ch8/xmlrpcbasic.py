#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    xmlrpcbasic.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import xmlrpclib

url = 'http://www.oreillynet.com/meerkat/xml-rpc/server.php'
#url = 'http://www.xmlrpc.com/directory/1568/services'
s = xmlrpclib.ServerProxy(url)
catdata = s.meerkat.getCategories()
cattitles = [item['title'] for item in catdata]
cattitles.sort()
for item in cattitles:
    print item
