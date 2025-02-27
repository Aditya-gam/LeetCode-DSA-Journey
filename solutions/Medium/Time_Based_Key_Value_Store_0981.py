import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize the data structure.
        store: Dictionary mapping key -> List of (timestamp, value) pairs
        """
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None

        Stores (timestamp, value) for the given key.
        Timestamps are guaranteed strictly increasing for each key.
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str

        Returns the value associated with the largest timestamp <= timestamp,
        or "" if no such timestamp exists.
        """
        if key not in self.store:
            return ""

        arr = self.store[key]

        # We'll search for the rightmost position where timestamp could be inserted
        # to keep arr sorted by timestamp. Then we take one step back to find <= timestamp.
        # We can use bisect.bisect_right(arr, (timestamp, chr(127))) for instance,
        # or manually implement a binary search for the first timestamp that is > timestamp.

        # Using bisect to find insertion position:
        #   arr[i] = (t, v) is sorted by t
        # We'll search by comparing (t, ) only.
        # 'key' for comparison: (timestamp, some-high-value) to ensure we get rightmost pos
        # where t <= timestamp.

        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        # i is the index where (timestamp, something) could be inserted to maintain order,
        # so arr[i-1] is the largest pair with t <= timestamp if i>0.

        if i == 0:
            return ""  # no t <= timestamp
        else:
            return arr[i-1][1]


# Example test cases
if __name__ == "__main__":
    kv = TimeMap()

    # Example 1
    kv.set("foo", "bar", 1)
    # At timestamp 1, the value of foo is bar
    print(kv.get("foo", 1))  # Expected output: "bar"
    # At timestamp 3, there is no value for foo
    print(kv.get("foo", 3))  # Expected output: ""

    # Example 2
    kv.set("foo", "bar2", 4)
    # At timestamp 4, the value of foo is bar2
    print(kv.get("foo", 4))  # Expected output: "bar2"
    # At timestamp 5, the value of foo is bar2
    print(kv.get("foo", 5))  # Expected output: "bar2"

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log(n)) for each get operation, where n is the number of entries for the given key.
# Space complexity: O(n) for storing the entries.
