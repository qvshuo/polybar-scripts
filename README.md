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

A script that displays temperatures for the current weather. Inspired by [this](https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/openweathermap-simple) script.

## Configuration

If `CITY` is left empty, the location is retrieved via the Mozilla Location API. `CITY` can either be a city ID (e.g. ID of Berlin is `2950159`), city name (e.g. `Berlin`) or city name + country code (e.g. `Berlin,DE`).

Change these values:

```
KEY=""
CITY=""
UNITS="metric"
SYMBOL="°"
```

### Module

```
[module/openweathermap-mini]
type = custom/script
exec = /path/to/openweathermap-mini.sh
interval = 600
label-maxlen = 20
```
