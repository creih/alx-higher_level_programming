#!/usr/bin/python3
def fizzbuzz():
    for its in range(1, 101):
        if (its % 3 == 0 and its % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (its % 3 == 0):
            print("Fizz", end=' ')
        elif (its % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(its, end=' ')
