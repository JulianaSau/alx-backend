#!/usr/bin/env python3
"""Module that defines function index_range
"""


def index_range(page: int, page_size: int) -> tuple:
    """Gets an index range of pages

    Args:
        page: page number
        page_size: the size of a page

    Returns:
        index range of the pages
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size

    return (start_index, end_index)
