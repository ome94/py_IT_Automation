# USING PYTHON TO INTERACT WITH THE OPERATING SYSTEM: FINAL PROJECT

This is the repository for the pieces of python code I wrote to complete the second course of Google's IT Automation With Python (Using Python to Interact With The Operating System).
Given a log file - [syslog.log](./syslog.log), I wrote a [python script](./ticky_checky.py) to analyse the log for the events of the `ticky` service, filter the events by type of the `ERROR` encountered (e.g _Tried to add information to closed ticket_, etc.) and by users for each type of event.
The results of the analyses are reported in `error_message.csv` and `user_statistics.csv` for each time the `ticky` service is analysed with [`ticky_checky.py`](./ticky_checky.py).
    
    NOTE: A fresh analyses is reported for every time the `ticky` service is analysed.

The results may be easily visualised as a table by running [`csv_to_html.py`](./csv_to_html.py) and passing both the desired report file (`user_statistics.csv` or `error_message.csv`) and the expected **.html** file as outputs like this
```
    ./csv_to_html.py <report-file> <.html-file>
    that is, for example,
    ./csv_to_html.py user_statistics.csv users_table.html
    # A new user_table is created if it doesn't exist,
    # or overwritten if it already exists.
    # the <.html> file may be named as convenient.
```

The resulting **.html** file can be viewed from a browser by accessing it through its URI.

    NOTE: The `csv_to_html.py` and `syslog.log` files was provided by the course staff and not written by me.
    I wrote every other file myself.