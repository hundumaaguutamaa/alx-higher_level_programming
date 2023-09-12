 a file appending function"""


def append_write(filename="", text=""):
    """ Appends file """
    with open(filename, "a", encoding="utf-8") as h:
        """ Appending file in the text"""
        
        return h.write(text)
