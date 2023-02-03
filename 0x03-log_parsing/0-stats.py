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
import re
import ipaddress
import datetime


'''
line = '192.8.12.16 - [2023-02-03 13:53:31.507501]\
 "GET /projects/260 HTTP/1.1" 405 843'
'''
# sys_stdin = [line, line, 'sdfgbgfb'] * 7
logRegex = re.compile(
    r'(.*) - \[(.*)\] ("GET /projects/260 HTTP/1.1") (.*) (.*)'
)
chkstr = '"GET /projects/260 HTTP/1.1"'
status_list = [200, 301, 400, 401, 403, 404, 405, 500]
status_record = {}
count = 0
results = []
total_size = 0
# for line in sys_stdin:
for line in sys.stdin:
    # print(count)
    if count == 10:
        count = 0
        print('File size: {}'.format(total_size))
        for status in status_list:
            if status in status_record.keys():
                print('{}: {}'.format(status, status_record.get(status)))
        # print(results)
        # results = []
        total_size = 0
        status_record = {}
    parsed_logs = logRegex.search(line)
    if parsed_logs is not None:
        ip, date, request_info, status_code, file_size = parsed_logs.groups()
        if chkstr == request_info:
            if status_code in status_list:
                total_size += int(file_size)
            if status_code in status_record.keys():
                status_record[status_code] += 1
            else:
                status_record[status_code] = 1
            results.append(
                [
                    ipaddress.ip_address(ip),
                    datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f'),
                    status_code,
                    file_size
                ]
            )
    count += 1
