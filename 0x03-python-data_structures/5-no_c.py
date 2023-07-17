#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Remove all characters c and C from a string."""
 dict = {ord(char): None for char in "cC"}

    # Call the translate string method giving it the mapping table
    new_string = my_string.translate(dict)
    return new_string
