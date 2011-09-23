#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    connect.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-23
    :from: Python Network Programming
"""

from ftplib import FTP

f = FTP('ftp.ibiblio.org')
print "Welcome:", f.getwelcome()
f.login()

print "CWD:", f.pwd()
f.quit()
