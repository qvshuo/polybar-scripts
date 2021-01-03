# polybar-inbox-imap-python

A script that shows if there are unread mails in your IMAPs inbox. 

## Font

`yay -S ttf-material-design-icons-git`

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
exec = /path/to/inbox-imap-python.py
interval = 60
```
