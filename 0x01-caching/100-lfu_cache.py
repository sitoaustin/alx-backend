#!/usr/bin/python3
""" Basic Class that in herits from
    BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - first in first out
      - how to implement FIFOCache
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
            self.least_value_key = 0
            least_number_holder = self.frequency[next(iter(self.frequency))][1]
            for key, value in self.frequency.items():
                if value[1] < least_number_holder:
                    least_number_holder = value[1]
                    self.least_value_key = key
            least_used_item_key = self.least_value_key
            self.cache_data.pop(least_used_item_key)
            self.cache_data[key] = item
            print("DISCARD: {}".format(least_used_item_key))
            return
        self.cache_data[key] = item
        self.frequency[key] = [item, 1]

    def get(self, key):
        """gets...
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            reference_value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = reference_value
            self.frequency[key][1] += 1
        return self.cache_data[key]
