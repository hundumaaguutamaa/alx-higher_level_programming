#!/usr/bin/python3

def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    
    else:
        biggst_int = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[biggst_int]:
                biggst_int = key
        
        return biggst_int

