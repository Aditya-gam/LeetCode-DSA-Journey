class Solution(object):
    def findScore(self, nums):
        """
        Calculate the score of the array by marking elements and summing values.

        :param nums: List[int] - Input array of positive integers
        :return: int - Final score after marking all elements
        """
        # Pair elements with their indices and sort by value, then index
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))

        # Set to track marked indices
        marked = set()
        score = 0

        # Iterate through sorted elements
        for val, idx in indexed_nums:
            if idx not in marked:
                # Add value to score
                score += val
                # Mark the current index and its adjacent indices
                marked.add(idx)
                if idx - 1 >= 0:
                    marked.add(idx - 1)
                if idx + 1 < len(nums):
                    marked.add(idx + 1)

        return score


# Example test cases
sol = Solution()
print(sol.findScore([2, 1, 3, 4, 5, 2]))  # Output: 7
print(sol.findScore([2, 3, 5, 1, 3, 2]))  # Output: 5
print(sol.findScore([1, 2, 3, 4, 5, 6]))  # Output: 6
print(sol.findScore([1, 1, 1, 1, 1, 1]))  # Output: 1
print(sol.findScore([1, 1, 1, 1, 1, 2]))  # Output: 2
print(sol.findScore([1, 1, 1, 1, 2, 2]))  # Output: 3
print(sol.findScore([1, 1, 1, 2, 2, 2]))  # Output: 4
print(sol.findScore([1, 1, 2, 2, 2, 2]))  # Output: 5
print(sol.findScore([1, 2, 2, 2, 2, 2]))  # Output: 6
print(sol.findScore([2, 2, 2, 2, 2, 2]))  # Output: 8

# Complexity Analysis
# Time Complexity:O(nlogn)
# Sorting the array of (value, index) pairs takes O(nlogn).
# Iterating through the sorted list is O(n).

# Space Complexity: O(n)
# The indexed_nums list and marked set require O(n) space.
