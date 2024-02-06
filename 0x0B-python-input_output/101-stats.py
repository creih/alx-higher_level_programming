#!/usr/bin/python3
"""this is an advanced task responce."""
import sys


def print_metrics(total_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            parts = line.strip().split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)
                print()
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
