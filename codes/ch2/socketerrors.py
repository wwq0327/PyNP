#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    socketerrors.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-20
    :from: Python Network Programming
"""

import sys, socket

host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

## socket 对象创建失败时产生的异常
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating socket: %s" % e
    sys.exit(1)

## 端口处理失败时产生的异常
try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)

## 连接到服务器失败时产生异常
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)

## 发送数据失败时异常
try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)

while 1:
    ## 获取数据失败时异常
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)

