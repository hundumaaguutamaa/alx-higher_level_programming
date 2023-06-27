def safe_print_list(my_list=[], x=0):
    count_inlist = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            count_inlist += 1
        except IndexError:
            break
    print()
    return count_inlist

