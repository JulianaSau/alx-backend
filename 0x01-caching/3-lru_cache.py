#!/usr/bin/env python3
"""Module that defines class LRUCache
"""
BaseCache = __import__('base_caching').BaseCaching


class LRUCache(BaseCache):
    """Implements a least recently used cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache and replaces the least recently used item
        if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        if key is None or item is None:
            return

        if len(self.cache_data) == super().MAX_ITEMS:
            first_key = self.queue[0]

            if key in self.queue:
                self.queue.remove(key)
            else:
                del self.cache_data[first_key]
                self.queue = self.queue[1:]
                print('DISCARD: {}'.format(first_key))

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key

        Args:
            key: key to get the item
        """
        cache = self.cache_data
        value = None

        if key and key in cache:
            self.queue.remove(key)
            self.queue.append(key)
            value = cache[key]

        return value
