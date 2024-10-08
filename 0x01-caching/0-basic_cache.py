#!/usr/bin/python3
"""Module that defines class BasicCache
"""
BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """Defines a basic cache behavior"""

    def put(self, key, item):
        """Sets a key and value pair in the cache

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        if key and item:
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
