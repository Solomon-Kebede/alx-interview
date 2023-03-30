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
    for key, value in status_codes.items():
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
            if int(split_data[-2]) in status_codes.keys():
                # print(split_data)
                total_size += int(split_data[-1])
                status_codes[int(split_data[-2])] += 1
                count += 1
                # print(count)
                if count == 10:
                    printer()
                    count = 0
finally:
    printer()
