#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    se1.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-21
    :from: Python Network Programming
"""
import sys

print "Welcome."
print "Please enter a string:"
sys.stdout.flush()
line = sys.stdin.readline().strip()
print "You entered %d characters" % len(line)
