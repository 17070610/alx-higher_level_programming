#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print("{}".format(" "), end="")
            print("{}".format(num))
        print("{}".format(""))