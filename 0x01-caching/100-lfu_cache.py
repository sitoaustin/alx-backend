#!/usr/bin/python3
""" Basic Class that in herits from
    BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Least frequently used
      - how to implement LFUCache
    """

    def __init__(self):
        """Initialize and inheriting
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Sets...
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            for d_key, value in self.frequency.items():
                if value == min_frequency:
                    self.cache_data.pop(d_key)
                    self.frequency.pop(d_key)
                    self.cache_data[key] = item
                    self.frequency[key] = 1
                    print("DISCARD: {}".format(d_key))
                    return
        self.cache_data[key] = item
        self.frequency[key] = 1

    def get(self, key):
        """gets...
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            reference_value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = reference_value
            self.frequency[key] += 1
        return self.cache_data[key]
