#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_inlist = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except:
            print("Not in the list")
        else:
            count_inlist += 1
    print()
    return (count_inlist)
