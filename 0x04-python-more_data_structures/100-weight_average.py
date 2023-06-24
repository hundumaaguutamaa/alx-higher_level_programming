#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_value = 0
    weigh_value = 0

    for my_tup in my_list:
        num_value += my_tup[0] * my_tup[1]
        weigh_value += my_tup[1]

    return (num_value / weigh_value)

