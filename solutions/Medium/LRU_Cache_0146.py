from collections import OrderedDict


class LRUCache:
    """
    Class: LRUCache
    Description: Implements a Least Recently Used (LRU) cache using an OrderedDict for O(1) operations.

    Methods:
    - get(key): Retrieves the value if the key exists, otherwise returns -1.
    - put(key, value): Inserts/updates a key-value pair. If capacity is exceeded, removes the LRU entry.

    Time Complexity:
    - get: O(1)
    - put: O(1)
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with the given capacity.

        Parameters:
        - capacity (int): The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the given key if it exists.

        Parameters:
        - key (int): The key to retrieve.

        Returns:
        - int: The value associated with the key, or -1 if the key does not exist.
        """
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark the key as recently used
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the key-value pair in the cache.
        If the capacity is exceeded, the least recently used item is removed.

        Parameters:
        - key (int): The key to insert or update.
        - value (int): The associated value.
        """
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark the key as recently used
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used entry
            self.cache.popitem(last=False)


# Example Test Cases
if __name__ == "__main__":
    lRUCache = LRUCache(2)

    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))  # Expected output: 1

    lRUCache.put(3, 3)  # Evicts key 2
    print(lRUCache.get(2))  # Expected output: -1

    lRUCache.put(4, 4)  # Evicts key 1
    print(lRUCache.get(1))  # Expected output: -1
    print(lRUCache.get(3))  # Expected output: 3
    print(lRUCache.get(4))  # Expected output: 4

# Test case 1: Capacity of 1
    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)
    print(lRUCache.get(2))  # Expected output: 1

    lRUCache.put(3, 2)  # Evicts key 2
    print(lRUCache.get(2))  # Expected output: -1
    print(lRUCache.get(3))  # Expected output: 2

# Test case 2: Capacity of 3
    lRUCache = LRUCache(3)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    lRUCache.put(3, 3)
    print(lRUCache.get(1))  # Expected output: 1

    lRUCache.put(4, 4)  # Evicts key 2
    print(lRUCache.get(2))  # Expected output: -1
    print(lRUCache.get(1))  # Expected output: 1
    print(lRUCache.get(3))  # Expected output: 3
    print(lRUCache.get(4))  # Expected output: 4

# Test case 3: Capacity of 0
    lRUCache = LRUCache(0)
    lRUCache.put(1, 1)
    print(lRUCache.get(1))  # Expected output: -1

    lRUCache.put(2, 2)  # Evicts key 1
    print(lRUCache.get(1))  # Expected output: -1
    print(lRUCache.get(2))  # Expected output: -1

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(1) for both get and put operations since the OrderedDict provides O(1) time complexity for these operations.
# Space Complexity: O(N) where N is the capacity of the cache. The space complexity is determined by the capacity of the cache.
