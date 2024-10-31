#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache implements a caching system with LRU discard policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # Track the order of usage for LRU

    def put(self, key, item):
        """ Assign the item to the cache with the key """
        if key is None or item is None:
            return

        # Update cache and manage order of usage
        if key in self.cache_data:
            self.order.remove(key)  # Remove key if it already exists
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Insert item and update usage order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Return the value linked to key in the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order since this key is now recently accessed
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
