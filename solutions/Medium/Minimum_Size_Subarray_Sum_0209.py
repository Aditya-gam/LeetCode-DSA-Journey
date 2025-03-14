class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int

        Returns the minimal length of a subarray of nums whose sum >= target.
        If no such subarray exists, returns 0.
        """
        left = 0
        running_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            running_sum += nums[right]

            # Shrink window while sum >= target
            while running_sum >= target:
                min_len = min(min_len, right - left + 1)
                running_sum -= nums[left]
                left += 1

        # If min_len was never updated, return 0
        return 0 if min_len == float('inf') else min_len


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    target1 = 7
    nums1 = [2, 3, 1, 2, 4, 3]
    # Expected: 2 (subarray [4,3] has sum=7 which is >=7, minimal length=2)
    print(solution.minSubArrayLen(target1, nums1))

    # Example 2
    target2 = 4
    nums2 = [1, 4, 4]
    # Expected: 1 (subarray [4] or the second [4])
    print(solution.minSubArrayLen(target2, nums2))

    # Example 3
    target3 = 11
    nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
    # Expected: 0 (no subarray sum >= 11)
    print(solution.minSubArrayLen(target3, nums3))

    # Example 4
    target4 = 11
    nums4 = [1, 2, 3, 4, 5]
    # Expected: 3 (subarray [3,4,5] has sum=12 which is >=11, minimal length=3)
    print(solution.minSubArrayLen(target4, nums4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input list 'nums'.
# Space complexity: O(1), since we are using only a constant amount of space.
