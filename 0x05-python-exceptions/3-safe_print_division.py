#!/usr/bin/python3
def safe_print_division(a, b):
    subizo = 0
    try:
        subizo = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(subizo))
