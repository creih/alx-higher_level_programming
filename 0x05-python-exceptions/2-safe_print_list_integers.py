#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    bara = 0
    try:
        for ins in range(x):
            value = my_list[ins]
            if type(value) is int:
                print("{:d}".format(value), end="")
                bara += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
    return bara
