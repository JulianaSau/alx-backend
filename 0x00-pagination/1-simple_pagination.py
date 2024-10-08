#!/usr/bin/env python3
"""Module for simple pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page of the data"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        indx_range = index_range(page, page_size)
        data = self.dataset()[indx_range[0]: indx_range[1]]

        return data


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
