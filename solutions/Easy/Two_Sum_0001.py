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
