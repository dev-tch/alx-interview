#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_stats(size, list_count_stat):
    "Log prasing after 10 lines or key interrupt"
    print("File size: {:d}".format(size))
    for statusCode, times in sorted(list_count_stat.items()):
        if times:
            print("{:d}: {:d}".format(statusCode, times))


if __name__ == "__main__":
    size = 0
    list_count_stat = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                       404: 0, 405: 0, 500: 0}
    nb_lines = 0

    try:
        for line in sys.stdin:
            if nb_lines != 0 and nb_lines % 10 == 0:
                print_stats(size, list_count_stat)
            nb_lines += 1
            try:
                parts = line.split()
                if len(parts) >= 7:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    size += file_size
                    if status_code in list_count_stat:
                        list_count_stat[status_code] += 1
            except:
                pass
        print_stats(size, list_count_stat)
    except KeyboardInterrupt:
        print_stats(size, list_count_stat)
        raise
