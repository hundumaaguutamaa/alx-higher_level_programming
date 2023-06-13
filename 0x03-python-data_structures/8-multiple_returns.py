#!/usr/bin/python3

def multiple_returns(sentence):
    length_str = len(sentence)
    if length_str == 0:
        return (0, None)
    else:
        first_char = sentence[0]
        return (length_str, first_char)

