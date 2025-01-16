from bisect import bisect_left


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Step 1: Sort potions
        potions.sort()
        m = len(potions)
        result = []

        # Step 2: For each spell, calculate successful pairs using binary search
        for spell in spells:
            threshold = (success + spell - 1) // spell  # ceil(success / spell)
            # Find the first index where potions[j] >= threshold
            index = bisect_left(potions, threshold)
            result.append(m - index)  # Count of successful pairs

        return result


# Example test cases\
solution = Solution()

# Test case 1
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
assert solution.successfulPairs(spells, potions, success) == [4, 0, 3]

# Test case 2
spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16
assert solution.successfulPairs(spells, potions, success) == [2, 0, 2]

# Test case 3
spells = [10, 20]
potions = [5, 10, 15]
success = 100
assert solution.successfulPairs(spells, potions, success) == [3, 2]

# Test case 4
spells = [1]
potions = [1]
success = 2
assert solution.successfulPairs(spells, potions, success) == [0]

# Test case 5
spells = [4, 8, 2]
potions = [10, 10, 10]
success = 40
assert solution.successfulPairs(spells, potions, success) == [3, 3, 0]

print("All test cases pass")

# Complexity Analysis
# Time Complexity: O((n+m)logm)
# Sorting potions: O(mlogm).
# Binary search for each spell: O(nlogm).

# Space Complexity: Sorting uses O(1) additional space if the sort is in-place.
