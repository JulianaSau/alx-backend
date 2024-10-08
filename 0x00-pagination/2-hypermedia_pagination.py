#!/usr/bin/env python3
"""Module for hyper pagination
"""
import csv
import math
from typing import List
from math import ceil


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets hyper page of the data"""
        hyper_dct = {
                'page_size': page_size,
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': None,
                'prev_page': None,
                'total_pages': 0
                }
        data_size = len(self.dataset())
        total_pages = int(ceil(data_size / page_size))
        hyper_dct['total_pages'] = total_pages
        hyper_dct['prev_page'] = page - 1 if page > 1 else None
        hyper_dct['next_page'] = page + 1 if page < total_pages else None
        hyper_dct['page_size'] = page_size if len(hyper_dct['data']) > 0 else 0

        return hyper_dct


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
