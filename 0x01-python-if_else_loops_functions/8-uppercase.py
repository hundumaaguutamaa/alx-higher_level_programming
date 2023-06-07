#!/usr/bin/python3

def uppercase(str):
    for a in str:
        b = ord(a)
        if b >= 97 and b <= 122:
            b = b - 32
            a = chr(b)
        print('{}'.format(a), end="")
        
    print()

