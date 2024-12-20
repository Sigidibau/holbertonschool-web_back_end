#!/usr/bin/env python3
"""
Type-annotated function concat that takes a string str1 and a string str2
and returns a concatenated string
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
