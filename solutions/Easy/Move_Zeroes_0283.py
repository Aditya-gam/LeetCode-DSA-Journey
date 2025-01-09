class Solution(object):
    def moveZeroes(self, nums):
        """
        Move all zeroes in the array to the end while maintaining the order of non-zero elements.

        :param nums: List[int] - Input array
        :return: None - The array is modified in place
        """
        non_zero_pos = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1


# Example test cases
sol = Solution()
nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # Output: [0]

nums3 = [1, 2, 3, 4, 5]
sol.moveZeroes(nums3)
print(nums3)  # Output: [1, 2, 3, 4, 5]

nums4 = [0, 0, 0, 0, 0]
sol.moveZeroes(nums4)
print(nums4)  # Output: [0, 0, 0, 0, 0]

nums5 = [0, 0, 0, 1, 0]
sol.moveZeroes(nums5)
print(nums5)  # Output: [1, 0, 0, 0, 0]

nums6 = [1, 2, 3, 4, 0]
sol.moveZeroes(nums6)
print(nums6)  # Output: [1, 2, 3, 4, 0]

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once, making this a linear time solution.

# Space Complexity: O(1)
# The solution is in-place, requiring no extra space beyond a few variables.
