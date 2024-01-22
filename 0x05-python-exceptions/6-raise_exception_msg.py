#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        undefined_variable
    except NameError:
        print(f"Name exception raised: {message}")
    finally:
        print("Inside finally block")
