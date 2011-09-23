#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    advbinarydl.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-23
    :from: Python Network Programming
"""

from ftplib import FTP
import sys

f = FTP('ftp.kernel.org')
f.login()

f.cwd('/pub/linux/kernel/v1.0')
f.voidcmd("TYPE I")

datasock, estsize = f.ntransfercmd("RETR linux-1.0.tar.gz")
transbytes = 0
fd = open('linux-1.0.tar.gz', 'wb')
while 1:
    buf = datasock.recv(2048)
    if not len(buf):
        break
    fd.write(buf)
    transbytes += len(buf)
    sys.stdout.write("Received %d" % transbytes)

    if estsize:
        sys.stdout.write("os %d bytes (%.1f%%)\r"\
                         (estsize, 100.0 * float(transbytes)/float(estsize)))
    else:
        sys.stdout.write("bytest\r")
    sys.stdout.flush()
sys.stdout.write("\n")
fd.close()
datasock.close()
f.voidresp()

    
