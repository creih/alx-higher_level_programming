#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    bara = 0
    try:
        for item in range(x):
            print(my_list[item], end='')
            bara += 1
    except (IndexError, ...):
        pass
    finally:
        print()
    return bara
