#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_stats(size, list_count_stat):
    "Log prasing after 10 lines or key interrupt"
    print("File size:", size)
    for code in sorted(list_count_stat.keys()):
        print(f"{code}: {list_count_stat[status_code]}")


if __name__ == "__main__":
    size = 0
    list_count_stat = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                       404: 0, 405: 0, 500: 0}
    nb_lines = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                if len(parts) >= 7:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    size += file_size
                    if status_code in list_count_stat:
                        list_count_stat[status_code] += 1
                    nb_lines += 1

                    if nb_lines % 10 == 0:
                        print_stats(size, list_count_stat)
            except (ValueError, IndexError):
                pass
    except KeyboardInterrupt:
        print_stats(size, list_count_stat)
