#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        import sys
        print(f"Exception: {e}", file=sys.stderr)
        return False
