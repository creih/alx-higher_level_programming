#!/usr/bin/python3
from sys import argv

def main():
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_args))

    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, argv[i]))

if __name__ == "__main__":
    main()
