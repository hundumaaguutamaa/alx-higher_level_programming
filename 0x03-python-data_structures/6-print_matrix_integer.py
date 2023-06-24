#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        num_count = len(num)
        for item in range(num_count):
             print("{:d}".format(matrix[num][item]), end='')
        if item < num_count - 1:
                print(" ", end="")
        print("")

