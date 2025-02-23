class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize the first two values
        prev2, prev1 = nums[0], max(nums[0], nums[1])

        # Iterate through the houses
        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current

        return prev1


# Example test cases
# Test case 1
nums = [1, 2, 3, 1]
assert Solution().rob(nums) == 4

# Test case 2
nums = [2, 7, 9, 3, 1]
assert Solution().rob(nums) == 12

# Test case 3 (edge case with one house)
nums = [5]
assert Solution().rob(nums) == 5

# Test case 4 (no money in houses)
nums = [0, 0, 0, 0]
assert Solution().rob(nums) == 0

# Test case 5 (all houses have the same amount)
nums = [10, 10, 10, 10]
assert Solution().rob(nums) == 20

print("All test cases pass")

# Complexity analysis
# Time complexity: O(n), where n is the number of houses.
# Space complexity: O(1) since we are using a constant amount of space.
