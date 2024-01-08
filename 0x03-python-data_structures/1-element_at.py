def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ = "__main__":
    print("Element at index {0} is {1}".format(idx, element_at(my_list, idx)))
