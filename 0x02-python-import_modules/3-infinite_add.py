#!/usr/bin/python3
from sys import argv

def main():
    args = argv[1:]
    result = sum(map(int, args))
    print(result)

if __name__ == "__main__":
    main()
