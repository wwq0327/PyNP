#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    syslogsample.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

import syslog, sys, StringIO, traceback, os

def logexception(includetraceback=0):
    '''traceback激活时，则收集所有错误信息，否则只是简单的记录异常的类型和它的信息.
    '''
    
    exctype, exception, exctraceback = sys.exc_info()
    excclass = str(exception.__class__)
    message = str(exception)

    if not includetraceback:
        syslog.syslog(syslog.LOG_ERR, "%s: %s" % (excclass, message))
    else:
        excfd = StringIO.StringIO()
        traceback.print_exception(exctype, exception, exctraceback, None,
                                  excfd)
        for line in excfd.getvalue().split("\n"):
            syslog.syslog(syslog.LOG_ERR, line)

def initsyslog():
    '''初始化syslog系统，程序名+ID作为日志名称。并记一条信息，说明服务器启动了
    '''
    
    syslog.openlog("%s[%d]" % (os.path.basename(sys.argv[0]),
                                                os.getpid()), 0,
                   syslog.LOG_DAEMON)
    syslog.syslog("Started.")

if __name__ == '__main__':
    initsyslog()

    try:
        raise RuntimeError, "Exception 1"
    except:
        logexception(0)

    try:
        raise RuntimeError, "Exception 2"
    except:
        logexception(1)

    syslog.syslog("I'm termination.")
    
