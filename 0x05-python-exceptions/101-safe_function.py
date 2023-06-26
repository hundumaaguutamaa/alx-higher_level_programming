#!/usr/bin/python3

def safe_function(fct, *args):
#import "sys" within the function
    import sys
    try:
        result = fct(*args)

#assign the exception object to a variable 'i'
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None

    return (result)
