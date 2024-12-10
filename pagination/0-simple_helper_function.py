#!/usr/bin/env python3
"""Simple Helper Function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a
    pagination.

    Args:
        page (int): page number
        page_size (int): size of the page
    """
    return((page -1 ) * page_size * page_size)