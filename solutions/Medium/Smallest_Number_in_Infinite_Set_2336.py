import heapq


class SmallestInfiniteSet(object):

    def __init__(self):
        # Min-heap to store numbers that are added back
        self.added_back = []
        self.current = 1  # Smallest integer in the infinite set
        self.added_set = set()  # To avoid duplicates in the heap

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_set.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)


# Example test cases

# Example 1
obj = SmallestInfiniteSet()
assert obj.popSmallest() == 1  # Pops 1
assert obj.popSmallest() == 2  # Pops 2
obj.addBack(1)                 # Adds 1 back
assert obj.popSmallest() == 1  # Pops 1 again
assert obj.popSmallest() == 3  # Pops 3
assert obj.popSmallest() == 4  # Pops 4

# Example 2
obj = SmallestInfiniteSet()
obj.addBack(2)                 # Adds 2 back
assert obj.popSmallest() == 1  # Pops 1
assert obj.popSmallest() == 2  # Pops 2
obj.addBack(1)                 # Adds 1 back
assert obj.popSmallest() == 1  # Pops 1 again

# Complexity Analysis
# Time Complexity: O(logn), where n is the number of elements added back to the heap.
# popSmallest: O(logn) when retrieving the smallest number from the heap, where n is the number of elements in the heap.
# addBack: O(logn) for adding a number to the heap.

# Space Complexity: O(k), where k is the number of elements added back to the heap.
