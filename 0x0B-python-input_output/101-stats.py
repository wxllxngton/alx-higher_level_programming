#!/usr/bin/python3

"""
This is the 'metrics' script.

It reads stdin line by line and computes metrics as described.
"""

import signal
import sys

def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

def print_metrics():
    total_size = sum([int(line.split()[-1]) for line in lines])
    print("Total file size:", total_size)

    status_codes = {}
    for line in lines:
        status_code = line.split()[8]
        if status_code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

    for status_code in sorted(status_codes):
        print(status_code + ":", status_codes[status_code])

lines = []
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        lines.append(line.strip())
        if len(lines) == 10:
            print_metrics()
            lines = []
except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)
