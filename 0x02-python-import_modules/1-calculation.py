#!/usr/bin/python3
from calculator_1 as c


if __name__ == "__main__":
    a = 10
    b = 5
    add_result = c.add(a, b)
    sub_result = c.sub(a, b)
    mul_result = c.mul(a, b)
    div_result = c.div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_result))
    print("{:d} - {:d} = {:d}".format(a, b, sub_result))
    print("{:d} * {:d} = {:d}".format(a, b, mul_result))
    print("{:d} / {:d} = {:d}".format(a, b, div_result))
