#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    trad_parse.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-23
    :from: Python Network Programming
"""

import sys, email

msg = email.message_from_file(sys.stdin)

print msg

print " *** Headers in message:"
for header, value in msg.items():
    print header + ':'
    print " " + value

if msg.is_multipart():
    print "This program cannot handle MIME multipart messages; exiting."
    sys.exit(1)

print "-" * 78
if 'subject' in msg:
    print "Subject: ", msg['subject']
    print "-" * 78

print "message Body:"
print
print msg.get_payload()
