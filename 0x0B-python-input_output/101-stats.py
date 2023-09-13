#!/usr/bin/python3
import sys
import signal

""" Initialize counters"""
t_size = 0
status_cs = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0

def print_stats():
    """Function to  print status"""
    print("File size: {}".format(t_size))
    for code in sorted(status_cs.keys()):
        if status_cs[code] > 0:
            print("{}: {}".format(code, status_cs[code]))

def signal_handler(sig, frame):
    """Function to handle signals"""
    print_stats()
    sys.exit(0)

"""Register signal handler for CTRL+C"""
signal.signal(signal.SIGINT, signal_handler)

try:
    for l in sys.stdin:
        parts = l.split(" ")
        if len(parts) > 6:
            size = parts[-1]
            code = parts[-2]
            t_size += int(size)
            if code in status_cs:
                status_cs[code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass

"""Print final stats at end of file ascending order"""
print_stats()
