#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    trad_gen_simple.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-23
    :from: Python Network Programming
"""

from email.MIMEText import MIMEText
from email import Utils

message = """Hello,
This is a test message from Chapter 9. I hope you enjoy it!

-- Anonymous"""

msg = MIMEText(message)
msg['To'] = 'wwq0327@gmail.com'
msg['From'] = 'wwq0327@gmail.com'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Date'] = Utils.formatdate(localtime=1)
msg['Message-ID'] = Utils.make_msgid()

print msg.as_string()
