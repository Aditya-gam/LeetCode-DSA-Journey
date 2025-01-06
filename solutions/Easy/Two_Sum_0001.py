class Solution(object):
    def twoSum(self, nums, target):
        """
        Find indices of two numbers that add up to the target.

        :param nums: List[int] - List of integers
        :param target: int - Target sum
        :return: List[int] - Indices of the two numbers
        """
        # Dictionary to store the number and its index
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in seen:
                return [seen[complement], i]
            # Otherwise, store the current number with its index
            seen[num] = i


# Example test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))          # Output: [0, 1]

# Complexity Analysis
# Time Complexity:O(n) - We iterate through the array once, and each lookup or insertion in the hash table is an O(1) operation.

# Space Complexity:O(n) - In the worst case, we store all n elements in the hash table.
