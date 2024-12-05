#!/usr/bin/env python3
"""
Type-annotated function add that takes a float a and a float as arguments
and returns their sum as a float
"""

def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenation of `str1` and `str2`.
    """
    return str1 + str2
