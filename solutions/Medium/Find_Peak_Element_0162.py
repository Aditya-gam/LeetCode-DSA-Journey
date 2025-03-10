class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Compare mid and mid + 1 to decide the search direction
            if nums[mid] > nums[mid + 1]:
                # Peak is in the left half (including mid)
                high = mid
            else:
                # Peak is in the right half (excluding mid)
                low = mid + 1

        # low == high is the peak index
        return low


# Example test cases
solution = Solution()

# Example 1
nums = [1, 2, 3, 1]
assert Solution().findPeakElement(nums) == 2

# Example 2
nums = [1, 2, 1, 3, 5, 6, 4]
assert Solution().findPeakElement(nums) in [1, 5]

# Edge Case: Single element
nums = [1]
assert Solution().findPeakElement(nums) == 0

# Edge Case: Two elements
nums = [1, 2]
assert Solution().findPeakElement(nums) == 1

nums = [2, 1]
assert Solution().findPeakElement(nums) == 0

# Random case
nums = [10, 20, 15, 2, 23, 90, 67]
assert Solution().findPeakElement(nums) in [1, 5]

print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(log N) where N is the number of elements in the input array.
# Space Complexity: O(1) since we are using a constant amount of space.
