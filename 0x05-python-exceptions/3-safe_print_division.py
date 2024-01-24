#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        subizo = a / b
    except (ZeroDivisionError, TypeError):
        return None
    finally:
        print("Inside result: {}".format(subizo))
