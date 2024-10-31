#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a caching system with LIFO discard policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None  # Track the last added key

    def put(self, key, item):
        """ Assign the item to the cache with the key """
        if key is None or item is None:
            return

        # Update the cache with the new key and item
        self.cache_data[key] = item
        self.last_key = key

        # If cache exceeds MAX_ITEMS, discard the last added item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last key added before the current key was set
            discarded_key = self.last_key
            if discarded_key in self.cache_data:
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Return the value linked to key in the cache """
        return self.cache_data.get(key, None)
