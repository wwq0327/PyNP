#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    DNS-basic.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import sys
import DNS as dns

query = sys.argv[1]
dns.DiscoverNameServers()

reqobj = dns.Request()

answerobj = reqobj.req(name=query, qtype=dns.Type.ANY)
if not len(answerobj.answers):
    print "Not found."
for item in answerobj.answers:
    print "%-5s %s" % (item['typename'], item['data'])
