#!/usr/bin/python3

class MyList(list):
    """ a sub-class of list"""
    
    def __init__(self):
        
        sorted_l = self.copy()
      
        sorted_l.sort()
        """Print sorted list"""
        print(sorted_l)
