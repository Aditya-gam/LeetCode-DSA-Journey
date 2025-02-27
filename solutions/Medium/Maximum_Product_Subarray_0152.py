class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the max and min product to the first element
        max_product = min_product = result = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current number is negative, swap max and min products
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # Update max_product and min_product
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            # Update the result with the maximum product found so far
            result = max(result, max_product)

        return result


# Example test cases
sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # Output: 6
print(sol.maxProduct([-2, 0, -1]))    # Output: 0
print(sol.maxProduct([-2]))           # Output: -2
print(sol.maxProduct([0, 0, 0]))      # Output: 0
print(sol.maxProduct([0, 1, 0]))      # Output: 1
print(sol.maxProduct([1, 0, 1]))      # Output: 1
print(sol.maxProduct([1, 1, 1]))      # Output: 1
print(sol.maxProduct([1, 2, 3]))      # Output: 6

# Complexity Analysis
# Time Complexity: O(n) where n is the length of the array. We traverse the array once.
# Space Complexity: O(1) as we use only a few variables for calculations.
