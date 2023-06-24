#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div_result = []
    for n in my_list:
        if n % 2 == 0:
            div_result.append(True)
        else:
            div_result.append(False)
    return div_result

