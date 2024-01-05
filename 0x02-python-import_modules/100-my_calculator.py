#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if len(argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)

a = int(argv[1])
operator = argv[2]
b = int(argv[3])

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{} {} {} = {}".format(a, operator, b, result))
