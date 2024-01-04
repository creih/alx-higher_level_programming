#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = int(number % 10)
        return (number)
    else:
        number = int((number * -1) % 1)
        return (number * -1)
