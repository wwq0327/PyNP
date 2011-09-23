#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    firstfork.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-24
    :from: Python Network Programming
"""

import os, time

print "Before the fork, my PID is", os.getpid()

if os.fork():
    print "hello from the parent. My PID is", os.getpid()
else:
    print "Hello from the child. My PID is", os.getpid()

time.sleep(1)
print "hello from both of us."
