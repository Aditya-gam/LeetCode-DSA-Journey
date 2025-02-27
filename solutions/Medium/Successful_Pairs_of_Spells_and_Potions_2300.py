import bisect


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Step 1: Sort potions for binary search
        potions.sort()
        m = len(potions)
        result = []

        # Step 2: For each spell, find the first potion that makes a successful pair
        for spell in spells:
            # Ceiling division to find threshold potion
            min_potion = (success + spell - 1) // spell
            # Binary search for the position
            index = bisect.bisect_left(potions, min_potion)
            result.append(m - index)  # Count successful pairs

        return result


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    # Test on the example in the problem statement
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 2) == [4, 3, 2]
    # Additional test cases
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 3) == [4, 3, 1]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 4) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 5) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 6) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 7) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 8) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 9) == [4, 3, 0]
    assert solution.successfulPairs([1, 2, 3], [1, 2, 3, 4], 10) == [4, 3, 0]

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(m log m + n log m), where m is the length of the potions array and n is the length of the spells array.
# We sort the potions array and perform binary search for each spell.
# The binary search takes O(log m) time for each spell.

# Space Complexity: O(1), since we are using a constant amount of space.
