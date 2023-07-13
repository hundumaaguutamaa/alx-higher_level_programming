#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n. 
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    res = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(res[i-1][j-1] + res[i-1][j])

        row.append(1)
        res.append(row)
    return res

