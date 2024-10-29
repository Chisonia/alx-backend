#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize class with FIFO cache system """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Adds an item to the cache_data dictionary following FIFO """
        if key is not None and item is not None:

            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Retrieves an item by key from the cache_data dictionary """
        return self.cache_data.get(key, None)
