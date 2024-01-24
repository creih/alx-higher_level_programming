#!/usr/bin/python3
def safe_print_division(a, b):
    subiza = 0
    try:
        subiza = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        subiza = None
    finally:
        print("Inside result: {}".format(subiza))
        return subiza
