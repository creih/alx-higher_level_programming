#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        digi = number % 10
    else:
        digi = (-number % 10)
    print(digi, end='')
    return (digi)
