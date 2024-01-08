#!/usr/bin/python3
def no_c(my_string):
    new_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return new_string


if __name__ == "__main__":
    no_c(my_string)
