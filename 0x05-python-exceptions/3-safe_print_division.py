def safe_print_division(a, b):
    try:
        subizo = a / b
    except ZeroDivisionError:
        return None
    else:
        return subizo
    finally:
        print("Inside result: {}".format(subizo))
