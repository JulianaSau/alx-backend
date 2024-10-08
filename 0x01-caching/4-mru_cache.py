#!/usr/bin/env python3
"""Module that defines class MRUCache
"""
BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """Implements a most recently used cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.stack = []
        self.index = 0
        self.lru_index = 0

    def put(self, key, item):
        """Adds an item to the cache and replaces the most recently used item
        if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        if key is None or item is None:
            return

        if len(self.cache_data) == super().MAX_ITEMS:
            last_index = len(self.stack) - 1
            last_key = self.stack[last_index]

            if key in self.stack:
                self.stack.remove(key)
            else:
                del self.cache_data[last_key]
                self.stack = self.stack[:-1]
                print('DISCARD: {}'.format(last_key))

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
            self.stack.remove(key)
            self.stack.append(key)
            value = cache[key]

        return value
