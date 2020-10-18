# polybar-inbox-imap-python

A script that shows if there are unread mails in your IMAPs inbox. 

## Configuration

```
email_address = ''
password = ''
imap_server = ''
```

## Module

```
[module/inbox-imap-python]
type = custom/script
exec = path/to/check.py
interval = 60
```
