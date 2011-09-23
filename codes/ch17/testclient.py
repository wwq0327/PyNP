#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    testclient.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-24
    :from: Python Network Programming
"""

import xmlrpclib, code

url = 'http://localhost:8765'
s = xmlrpclib.ServerProxy(url)

interp = code.InteractiveConsole({'s': s})
interp.interact("You can now use the object s to interact with the server.")
