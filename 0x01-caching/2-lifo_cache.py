#!/usr/bin/python3
""" LIFOCache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache implements a caching system
    with LIFO discard policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.keys_order = []  # Track the order of keys

    def put(self, key, item):
        """ Assign the item to the cache with the key """
        if key is None or item is None:
            return

        # If key already exists, update its value
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update the order list
            self.keys_order.remove(key)
        else:
            # Eviction if over capacity
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the last item added
                last_key = self.keys_order.pop()  # Remove the last key
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            # Insert new item
            self.cache_data[key] = item

        # Add the key to the order list
        self.keys_order.append(key)

    def get(self, key):
        """ Return the value linked to key in the cache """
        return self.cache_data.get(key, None)
