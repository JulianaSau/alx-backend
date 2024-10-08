#!/usr/bin/env python3
"""Module that defines class LFUCache
"""
BaseCache = __import__('base_caching').BaseCaching


class LFUCache(BaseCache):
    """Implements a least frequently used cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.queue = []
        self.freq = {}

    def put(self, key, item):
        """Adds an item to the cache and replaces the least frequently used
        item if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        frq = self.freq
        if key is None or item is None:
            return

        if len(self.cache_data) == super().MAX_ITEMS:
            least_frq = 1000
            for k, v in frq.items():
                if least_frq > v:
                    least_frq = v
            lfu_key = [k for k, v in frq.items() if frq[k] == least_frq][0]

            del_key = lfu_key

            if key in self.queue:
                self.queue.remove(key)
            else:
                del self.cache_data[del_key]
                del frq[del_key]
                self.queue.remove(del_key)
                print('DISCARD: {}'.format(del_key))

        self.queue.append(key)
        frq[key] = frq[key] + 1 if key in frq.keys() else 1
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
            self.freq[key] += 1
            value = cache[key]

        return value
