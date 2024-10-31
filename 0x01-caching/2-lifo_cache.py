from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add item to cache with LIFO eviction policy """
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
        """ Retrieve an item from cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
