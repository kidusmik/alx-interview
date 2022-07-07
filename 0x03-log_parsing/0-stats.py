#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import re
from datetime import datetime


status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
file_size = 0
on_ten = 0


def check_ip(ip):
    """validate ip address"""
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"\
        r"{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if (re.search(pattern, ip)):
        return True
    return False


def display_metrics():
    """display the metrics"""
    print(f'File size: {file_size}')
    for k, v in status_code.items():
        if v:
            print(f'{k}: {v}')


try:
    for lines in sys.stdin:
        line = lines.split(' ')
        ip = line[0]
        dates = line[2][1:] + line[3][:-1]
        dates = datetime.strptime(dates, "%Y-%m-%d%H:%M:%S.%f")
        minus = line[1]
        method = line[4][1:]
        path = line[5]
        http = line[6][:-1]
        code = line[7]
        size = line[-1].split('\\')[0]
        if minus == '-' and code in status_code and \
                http == 'HTTP/1.1' and method == 'GET' and \
                    check_ip(ip) and isinstance(dates, datetime) \
                        and path == '/projects/260':
            if on_ten == 10:
                display_metrics()
                on_ten = 0
            status_code[code] += 1
            file_size += int(size)
            on_ten += 1
        else:
            print(ip, dates, minus, method, path, http, code, size)
except KeyboardInterrupt:
    display_metrics()
    sys.exit(1)
else:
    display_metrics()
