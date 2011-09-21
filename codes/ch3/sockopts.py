#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    sockopts.py
    ~~~~~~~~~~~~~~~~~~~~

    打印Python所支持系统的 socket 选项列表
    
    :date: 2011-09-21
    :from: Python Network Programming
"""

import socket

solist = [x for x in dir(socket) if x.startswith('SO_')]

solist.sort()

for x in solist:
    print x
