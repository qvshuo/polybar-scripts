# polybar-scripts

## inbox-imap-python.py

A script that shows if there are unread mails in your IMAPs inbox. Inspired by [this](https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/inbox-imap-pythongpg) script.

### Configuration

```
email_address = ''
password = ''
imap_server = ''
```

### Module

```
[module/inbox-imap-python]
type = custom/script
exec = /path/to/inbox-imap-python.py
interval = 60
label-maxlen = 20
```

## openweathermap-mini.sh

A script that displays temperatures for the current weather.

### Module

```
[module/openweathermap-mini]
type = custom/script
exec = /path/to/openweathermap-mini.sh
interval = 600
label-maxlen = 20
```

## player-cmus.sh

A script that displays information about the current track, copyed from [this](https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/player-cmus) scripts.

### Module

[module/player-cmus]
type = custom/script
exec = /path/to/player-cmus.sh
interval = 1
click-left = cmus-remote -n &
click-right = cmus-remote -r &
click-middle = cmus-remote -u &
label-maxlen = 50
