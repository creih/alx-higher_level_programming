#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            print("{:d}{:d}".format(i, j), end=", ")
print("\n")
