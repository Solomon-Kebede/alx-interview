#!/usr/bin/python3

'''
Write a script that reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET \
    /projects/260 HTTP/1.1" <status code> <file size>\
     (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),\
     print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>\
         (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an\
             integer, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order
'''

import sys


method_and_path = '] "GET /projects/260 HTTP/1.1" '
status_list = [200, 301, 400, 401, 403, 404, 405, 500]
status_dict = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total_size = 0
count = 1

stats = "----STATS-----"


def printer():
    # print(stats)
    print('File size: {}'.format(total_size))
    for key, value in status_dict.items():
        if value > 0:
            print('{}: {}'.format(key, value))

try:
    for line in sys.stdin:
        print(repr(line))
        if count == 10:
            printer()
            count = 0
        line_clean = line.splitlines()[0]
        total_size += int(line_clean.split(" ")[-1])
        status = line_clean.split(" ")[-2]
        status_dict[status] += 1
        print(line_clean)
        count += 1

except KeyboardInterrupt:
    printer()
