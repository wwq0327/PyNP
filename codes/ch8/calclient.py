#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    calclient.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""
import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")
month = server.getMonth(2002, 8)
print month
