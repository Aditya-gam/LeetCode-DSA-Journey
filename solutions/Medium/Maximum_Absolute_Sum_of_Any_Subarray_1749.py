from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Function: maxAbsoluteSum
        Description: Returns the maximum absolute sum of any subarray.

        Parameters:
        - nums (List[int]): List of integers.

        Returns:
        - int: Maximum absolute sum of any subarray.
        """

        max_sum, min_sum = 0, 0
        max_so_far, min_so_far = 0, 0

        for num in nums:
            max_so_far = max(num, max_so_far + num)
            min_so_far = min(num, min_so_far + num)

            max_sum = max(max_sum, max_so_far)
            min_sum = min(min_sum, min_so_far)

        return max(abs(max_sum), abs(min_sum))


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Mixed positive and negative values
    print("Test Case 1: Mixed positive and negative values")
    nums1 = [1, -3, 2, 3, -4]
    print("Expected Output: 5 | Actual Output:",
          solution.maxAbsoluteSum(nums1))

    # Test case 2: All negative values
    print("Test Case 2: All negative values")
    nums2 = [-1, -2, -3, -4]
    print("Expected Output: 10 | Actual Output:",
          solution.maxAbsoluteSum(nums2))

    # Test case 3: All positive values
    print("Test Case 3: All positive values")
    nums3 = [1, 2, 3, 4, 5]
    print("Expected Output: 15 | Actual Output:",
          solution.maxAbsoluteSum(nums3))

    # Test case 4: Alternating positive and negative values
    print("Test Case 4: Alternating positive and negative values")
    nums4 = [2, -5, 1, -4, 3, -2]
    print("Expected Output: 8 | Actual Output:",
          solution.maxAbsoluteSum(nums4))

    # Test case 5: Large single-element case
    print("Test Case 5: Single large positive and negative number")
    nums5 = [10000, -10000]
    print("Expected Output: 10000 | Actual Output:",
          solution.maxAbsoluteSum(nums5))

    # Test case 6: Large input array with alternating values
    print("Test Case 6: Large alternating array")
    nums6 = [1, -1] * 50000  # Length = 100000
    print("Expected Output: Computed Output:", solution.maxAbsoluteSum(nums6))

"""
Time Complexity:
- O(N) → We iterate through `nums` once while maintaining max and min subarray sums.
- Space Complexity:
  - O(1) → Only a few integer variables are used (constant space).
"""
