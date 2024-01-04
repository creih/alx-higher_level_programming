#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digits = int(number % 10)
print(number)
if digits > 5:
    print(f"Last digit of {number} is {digits} and is greater than 5")
elif digits == 0:
    print(f"Last digit of {number} is {digits} and is 0")
else:
    print(f"Last digit of {number} is {digits} and is less than 6 and not 0")
