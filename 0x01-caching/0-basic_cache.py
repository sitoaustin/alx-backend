#!/usr/bin/python3
""" Basic Class that in herits from
    BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Assigns keys and values to BaseCashing dictionary
      - Gets the value of the key passed
    """


    def __init__(self, cache_data):
        """Initialize and ingerits
        """
        super().__init__(cache_data)

    def put(self, key, item):
        """Sets the key-value pair
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets the value of the key
        """ 
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
