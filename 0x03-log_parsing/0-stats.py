#!/usr/bin/python3
"""
0. Log parsing
"""

import sys

REQUEST_INFO = '] "GET /projects/260 HTTP/1.1" '
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

total_size = 0
count = 0


def printer():
    '''Prints final result'''
    print('File size: {}'.format(total_size))
    statuses = list(status_codes.keys())
    statuses.sort()
    for key in statuses:
        value = status_codes.get(key)
        if value > 0:
            print('{}: {}'.format(key, value))


# read from stdin
try:
    for line in sys.stdin:
        if not line:
            continue
        split_data = (line.split(" "))
        # check input format
        if len(split_data) == 9 and REQUEST_INFO in line:
            try:
                status = int(split_data[-2])
            except ValueError:
                continue
            if status in status_codes.keys():
                total_size += int(split_data[-1])
                status_codes[int(split_data[-2])] += 1
                count += 1
                # print(count)
                if count == 10:
                    printer()
                    count = 0
finally:
    printer()
