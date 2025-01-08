class Solution(object):
    def singleNumber(self, nums):
        """
        Find the single number in the array using XOR.

        :param nums: List[int] - Input array
        :return: int - The single number
        """
        result = 0
        for num in nums:
            result ^= num  # XOR all elements

        return result


# Example test cases
sol = Solution()
print(sol.singleNumber([2, 2, 1]))      # Output: 1
print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(sol.singleNumber([1]))           # Output: 1
print(sol.singleNumber([1, 1, 2]))      # Output: 2

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once.

# Space Complexity: O(1)
# Only a single variable result is used for computation.
