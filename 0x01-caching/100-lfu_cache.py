#!/usr/bin/python3
""" LFUCache module """

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache implements a caching system with LFU discard policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.usage_frequency = defaultdict(int)  # Track frequency of each key
        self.usage_order = {}  # Track the order of usage for LFU and LRU
        self.time = 0  # Monotonic counter to track recency

    def put(self, key, item):
        """ Assign the item to the cache with the key """
        if key is None or item is None:
            return

        # Update cache and usage tracking
        if key in self.cache_data:
            self.usage_frequency[key] += 1
        else:
            # Handle eviction if over capacity
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key(s)
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k, v in self.usage_frequency
                            .items() if v == min_freq]

                # If more than one key has the lowest frequency, apply LRU
                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                    del self.cache_data[lru_key]
                    del self.usage_frequency[lru_key]
                    del self.usage_order[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    # Discard the LFU key
                    lfu_key = lfu_keys[0]
                    del self.cache_data[lfu_key]
                    del self.usage_frequency[lfu_key]
                    del self.usage_order[lfu_key]
                    print(f"DISCARD: {lfu_key}")

            # Insert the new item with initial usage tracking
            self.cache_data[key] = item
            self.usage_frequency[key] = 1

        # Update usage order for recency tracking
        self.usage_order[key] = self.time
        self.time += 1

    def get(self, key):
        """ Return the value linked to key in the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update usage frequency and order since this key is now accessed
        self.usage_frequency[key] += 1
        self.usage_order[key] = self.time
        self.time += 1
        return self.cache_data[key]
