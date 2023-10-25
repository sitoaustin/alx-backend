#!/usr/bin/python3
""" Basic Class that in herits from
    BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LIFOCache defines:
      - first in first out
      - how to implement FIFOCache
    """

    def __init__(self):
        """Initialize and inheriting
        """
        super().__init__()

    def put(self, key, item):
        """Sets...
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_used_item_key = next(iter(self.cache_data))
            self.cache_data.pop(least_used_item_key)
            self.cache_data[key] = item
            print("DISCARD: {}".format(least_used_item_key))
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets...
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
