#!/usr/bin/env python3
"""Module that defines class LIFOCache
"""
BaseCache = __import__('base_caching').BaseCaching


class LIFOCache(BaseCache):
    """Implements a last in first out cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds an item to the cache and replaces the last item
        if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        last_index = len(self.stack) - 1
        if key is None or item is None:
            return

        if key not in self.stack and len(self.cache_data) == super().MAX_ITEMS:
            last_key = self.stack[last_index]
            print('DISCARD: {}'.format(last_key))
            del self.cache_data[last_key]
            self.stack = self.stack[:-1]
        elif key in self.stack:
            self.stack.remove(key)

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key

        Args:
            key: key to get the item
        """
        cache = self.cache_data
        value = None

        if key and key in cache:
            value = cache[key]

        return value
