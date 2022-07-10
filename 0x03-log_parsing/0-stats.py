#!/usr/bin/python3
"""script that reads stdin line by line"""

import sys


if __name__ == "__main__":
    status_code = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0}
    on_ten = 1
    file_size = 0

    def parse_line(line):
        """parse a line"""
        try:
            parsed_line = line.split()
            code = parsed_line[-2]
            if code in status_code.keys():
                status_code[code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

    def print_stats():
        """display the stats"""
        print("File size: {}".format(file_size))
        for key in sorted(status_code.keys()):
            if status_code[key]:
                print("{}: {}".format(key, status_code[key]))

    try:
        for line in sys.stdin:
            file_size += parse_line(line)
            if on_ten % 10 == 0:
                print_stats()
            on_ten += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
