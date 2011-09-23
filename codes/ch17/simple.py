#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    simple.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-24
    :from: Python Network Programming
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from SocketServer import ForkingMixIn

class Math:
    def pow(self, x, y):
        return x ** y

    def hex(self, x):
        return "%x" % x

class ForkingServer(ForkingMixIn, SimpleXMLRPCServer):
    pass

serveraddr = ('', 8765)
srvr = ForkingServer(serveraddr, SimpleXMLRPCRequestHandler)
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.serve_forever()
