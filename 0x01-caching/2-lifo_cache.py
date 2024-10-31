from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.keys_order = []  # Track the order of keys for LIFO

    def put(self, key, item):
        """ Add item to cache with LIFO eviction policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item
            self.cache_data[key] = item
            self.keys_order.remove(key)  # Remove key from current position
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the last item added
                discarded_key = self.keys_order.pop()  # Remove the last key
                del self.cache_data[discarded_key]  # Remove from cache
                print(f"DISCARD: {discarded_key}")

            # Add new item
            self.cache_data[key] = item

        # Add or refresh key in the order list
        self.keys_order.append(key)

    def get(self, key):
        """ Retrieve an item from cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
