class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This function returns the length of the longest strictly increasing 
        or strictly decreasing subarray in the given list.
        """
        # Edge case: if there's only one element, the answer is 1
        if len(nums) == 1:
            return 1

        incStreak = 1  # current length of strictly increasing subarray
        decStreak = 1  # current length of strictly decreasing subarray
        maxLen = 1     # track the maximum length

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                incStreak += 1
                decStreak = 1  # reset decreasing streak
            elif nums[i] < nums[i - 1]:
                decStreak += 1
                incStreak = 1  # reset increasing streak
            else:
                # elements are equal, reset both
                incStreak = 1
                decStreak = 1

            maxLen = max(maxLen, incStreak, decStreak)

        return maxLen


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 4, 3, 3, 2]
    # The longest subarray that is strictly increasing is [1,4] (length=2)
    # The longest subarray that is strictly decreasing is [4,3], [3,2], or [4,3,3,2] is not strictly decreasing
    # because 3 == 3. So the longest strictly decreasing subarray is [4,3] or [3,2], each of length=2.
    # Expected: 2
    assert solution.longestMonotonicSubarray(nums1) == 2

    # Test case 2
    nums2 = [3, 3, 3, 3]
    # Each element is the same, so we can only have subarrays of length 1.
    # Expected: 1
    assert solution.longestMonotonicSubarray(nums2) == 1

    # Test case 3
    nums3 = [3, 2, 1]
    # Strictly decreasing subarray is [3,2,1] of length 3.
    # Expected: 3
    assert solution.longestMonotonicSubarray(nums3) == 3

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the input list 'nums'.
# Space Complexity: O(1).
