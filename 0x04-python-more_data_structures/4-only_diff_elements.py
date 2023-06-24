#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    setellement = []
    for letters in set_1:
        if letters not in set_2:
            setellement.append(letters)

    for letters in set_2:
        if letters not in set_1:
            setellement.append(letters)

    return setellement

