class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()

        # Calculate the product of the three largest numbers
        product1 = nums[-1] * nums[-2] * nums[-3]

        # Calculate the product of the two smallest and the largest number
        product2 = nums[0] * nums[1] * nums[-1]

        # Return the maximum of the two products
        return max(product1, product2)


# Example test cases
sol = Solution()
print(sol.maximumProduct([1, 2, 3]))  # Output: 6
print(sol.maximumProduct([1, 2, 3, 4]))  # Output: 24
print(sol.maximumProduct([-1, -2, -3]))  # Output: -6
print(sol.maximumProduct([-4, -3, -2, -1, 60]))  # Output: 720
print(sol.maximumProduct([-1, -2, -3, -4]))  # Output: -6
print(sol.maximumProduct([-1, -2, -3, 4]))  # Output: 24
print(sol.maximumProduct([-1, -2, 3, 4]))  # Output: 24
print(sol.maximumProduct([-1, 2, 3, 4]))  # Output: 24
print(sol.maximumProduct([-10, -10, 1, 3, 2]))  # Output: 300
print(sol.maximumProduct([-1, -2, -3, -4, 5]))  # Output: 60

# Complexity Analysis
# Time Complexity: O(nlogn)
# Sorting the array takes O(nlogn) time.
# Calculating the products and returning the maximum takes O(1).

# Space Complexity: O(1) (excluding the space required for sorting)
