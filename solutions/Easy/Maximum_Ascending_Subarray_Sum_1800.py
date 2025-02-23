class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This function returns the maximum sum of a strictly ascending subarray.
        """
        if not nums:
            # Edge case if nums were empty (though constraints say length >= 1)
            return 0

        max_sum = nums[0]          # Track maximum sum
        current_sum = nums[0]      # Track current ascending subarray sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Continue ascending subarray
                current_sum += nums[i]
            else:
                # Start a new ascending subarray
                current_sum = nums[i]

            # Update the maximum subarray sum
            max_sum = max(max_sum, current_sum)

        return max_sum


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [10, 20, 30, 5, 10, 50]
    # The strictly ascending subarrays are:
    # [10,20,30], sum = 60
    # [5,10,50], sum = 65
    # Maximum is 65
    assert solution.maxAscendingSum(nums1) == 65

    # Test case 2
    nums2 = [10, 20, 30, 40, 50]
    # This entire array is strictly ascending, sum = 150
    assert solution.maxAscendingSum(nums2) == 150

    # Test case 3
    nums3 = [12, 17, 15, 13, 10, 11, 12]
    # Strictly ascending subarrays:
    # [12,17], sum = 29
    # [15], sum = 15
    # [13], sum = 13
    # [10,11,12], sum = 33 <-- Maximum
    assert solution.maxAscendingSum(nums3) == 33

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the array once
# Space complexity: O(1) - We use a constant amount of extra space
