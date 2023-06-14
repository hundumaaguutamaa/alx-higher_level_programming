#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = []
    for i in my_list:
        if i not in unique_list:
            sum = 0
            sum += i
            unique_list.append(i)

    return sum

