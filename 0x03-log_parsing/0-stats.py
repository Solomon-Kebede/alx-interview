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
count = 0


def printer():
    print('File size: {}'.format(total_size))
    '''Print metrics'''
    for item in status_list:
        key = str(item)
        value = status_dict[key]
        if value != 0:
            print('{}: {}'.format(key, value))


def checker(ip, date, status_code):
    '''Checks validity of log data'''
    try:
        import ipaddress
        import datetime
        ipaddress.ip_address(ip)
        datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if status_code in status_dict.keys():
            status_dict[status_code] += 1
        total_size += int(file_size)
    except Exception:
        pass


try:
    for line in sys.stdin:
        line = line.splitlines()[0]
        if method_and_path in line:
            ip_date_status_size = line.split(method_and_path)
            ip, date = ip_date_status_size[0].split(" - [")
            status_code, file_size = ip_date_status_size[1].split(" ")
            # print(ip, ' & ', date, ' & ', status_code, ' & ', file_size)
            if status_code in status_dict.keys():
                status_dict[status_code] += 1
            total_size += int(file_size)
            count += 1
            if count == 10:
                count = 0
                printer()
except KeyboardInterrupt:
    printer()
