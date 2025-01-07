class Solution(object):
    def missingNumber(self, nums):
        """
        Find the missing number in the range [0, n].

        :param nums: List[int] - Input array containing n distinct numbers
        :return: int - The missing number
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# Example test cases
sol = Solution()
print(sol.missingNumber([3, 0, 1]))        # Output: 2
print(sol.missingNumber([0, 1]))           # Output: 2
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
print(sol.missingNumber([0]))              # Output: 1
print(sol.missingNumber([1]))              # Output: 0
print(sol.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 10
print(sol.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]))  # Output: 9
print(sol.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 11

# Complexity Analysis
# Time Complexity: O(n) Calculating the sum of elements in the array takes O(n).

# Space Complexity: O(1) Only a few variables are used for calculations.
