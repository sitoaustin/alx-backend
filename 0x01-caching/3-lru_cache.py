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
            last_dict_key = list(self.cache_data)[-1]
            self.cache_data.pop(last_dict_key)
            self.cache_data[key] = item
            print("DISCARD: {}".format(last_dict_key))
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets...
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
