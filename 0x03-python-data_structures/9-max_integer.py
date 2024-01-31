#!/usr/bin/python3
def max_integer(my_list=[]):
    maxim = 0
    if len(my_list) == 0:
        return None
    for num in range(len(my_list)):
        if my_list[num] > my_list[num+1]:
            maxim = my_list[num]
            num = num + 1
        else:
            maxim = my_list[num+1]
            num = num + 1
    return maxim

