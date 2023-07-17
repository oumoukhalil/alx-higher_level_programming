#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return a tuple with the length of a string
# and its first character
# -----------------------------------------------------------

def multiple_returns(sentence):
    """
    Args:
        sentence: this is a string argument

    Returns:
        tuple with the length of a string and its first character
    """

    str_len, first_char = len(sentence), sentence[0]
    return (str_len, first_char)
