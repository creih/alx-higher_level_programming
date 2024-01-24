#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            e1 = my_list_1[i]
            e2 = my_list_2[i]

            if type(e1) not in (int, float) or type(e2) not in (int, float):
                    raise TypeError("wrong type")

            result = e1 / e2

        except TypeError as t_e:
            print(t_e)
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)

    return result_list
