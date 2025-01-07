class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.

        :param nums: List[int] - Input array
        :param k: int - Number of steps to rotate
        :return: None - Modifies nums in-place
        """
        n = len(nums)
        k %= n  # Reduce k if it's greater than n

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)


# Example test cases
sol = Solution()
nums1 = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
sol.rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]

nums3 = [1, 2, 3, 4, 5, 6]
sol.rotate(nums3, 4)
print(nums3)  # Output: [3, 4, 5, 6, 1, 2]

# Complexity Analysis
# Time Complexity: O(n)

# Each reversal takes O(n), and we perform three reversals, so the total time complexity is O(n).
# Space Complexity: O(1) No extra space is used except for a few variables.
