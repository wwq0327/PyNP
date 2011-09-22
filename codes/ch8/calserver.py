#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    calserver.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import calendar, SimpleXMLRPCServer

class Calendar:
    def getMonth(self, year, month):
        return calendar.month(year, month)

    def getYear(self, year):
        return calendar(year)

calendar_object = Calendar()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_instance(calendar_object)
print "Linstening on port 8888"
server.serve_forever()
