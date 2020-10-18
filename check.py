#!/usr/bin/python

import imaplib

username = ''
password = ''
server = ''

obj = imaplib.IMAP4_SSL(server, 993)
obj.login(username, password)
obj.select()

print("",len(obj.search(None, 'unseen')[1][0].split()))
