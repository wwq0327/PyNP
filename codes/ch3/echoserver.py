#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    echoserver.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import socket, traceback

host = ''
port = 51423

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    # Process the connetion
    try:
        print "Got connection from", clientsock.getpeername()
        while 1:
            data = clientsock.recv(4096) ## 获取来自客户端的数据
            if not len(data):
                break
            clientsock.sendall(data)  ## 将所获得数据发送到客户端
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close the connection

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        
