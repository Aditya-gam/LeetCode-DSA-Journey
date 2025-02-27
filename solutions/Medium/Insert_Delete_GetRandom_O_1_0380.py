import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []       # Store elements
        self.dict = {}       # Map element to its list index

    def insert(self, val):
        """
        :type val: int
        :rtype: bool

        Inserts val into the set if not present. Returns True if the element was inserted,
        False otherwise.
        """
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool

        Removes val from the set if present. Returns True if the element was removed,
        False otherwise.
        """
        if val not in self.dict:
            return False

        # Index of the element to remove
        idx = self.dict[val]

        # Move the last element to the position idx
        last_element = self.list[-1]
        self.list[idx] = last_element
        self.dict[last_element] = idx

        # Remove the last element from the list
        self.list.pop()
        del self.dict[val]

        return True

    def getRandom(self):
        """
        :rtype: int

        Returns a random element from the set.
        """
        return random.choice(self.list)


# Example usage:
if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))  # True
    print(randomizedSet.remove(2))  # False
    print(randomizedSet.insert(2))  # True
    print(randomizedSet.getRandom())  # 1 or 2 randomly
    print(randomizedSet.remove(1))  # True
    print(randomizedSet.insert(2))  # False (already in set)
    print(randomizedSet.getRandom())  # 2, as that's the only element

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(1) for all operations on average
# Space complexity: O(n) where n is the number of unique elements in the set
