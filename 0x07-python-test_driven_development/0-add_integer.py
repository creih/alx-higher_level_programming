#!/usr/bin/python3
def add_integer(a, b=98):
    """this is a python function to add 2 ints"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")
    return (a + b)

# # Test cases
# try:
#     result1 = add_integer(5, 3)
#     print(f"Test Case 1: {result1}")  # Output: 8
# except TypeError as e:
#     print(f"Test Case 1: {e}")

# try:
#     result2 = add_integer(2.5, 3)
#     print(f"Test Case 2: {result2}")  # Output: 5
# except TypeError as e:
#     print(f"Test Case 2: {e}")

# try:
#     result3 = add_integer("10", 5)
#     print(f"Test Case 3: {result3}")  # TypeError will be raised
# except TypeError as e:
#     print(f"Test Case 3: {e}")

# try:
#     result4 = add_integer(7, "abc")
#     print(f"Test Case 4: {result4}")  # TypeError will be raised
# except TypeError as e:
#     print(f"Test Case 4: {e}")
