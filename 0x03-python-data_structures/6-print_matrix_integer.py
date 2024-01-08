#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != len(row) - 1:
                # Print the number with a space after it
                print("{:d}".format(num), end=" ")
            else:
                # Print the last number in the row with a newline
                print("{:d}".format(num))
    if not matrix:
        print()


if __name__ == "__main__":
    print_matrix_integer(matrix)
