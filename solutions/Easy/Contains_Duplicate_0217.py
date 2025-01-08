class Solution(object):
    def containsDuplicate(self, nums):
        """
        Check if any value appears at least twice in the array.

        :param nums: List[int] - Input array
        :return: bool - True if there is a duplicate, False otherwise
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Example test cases
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(sol.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
print(sol.containsDuplicate([1]))  # Output: False
print(sol.containsDuplicate([]))  # Output
print(sol.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))  # Output: True

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once, and each set operation (insertion and lookup) is O(1) on average.
# The time complexity is O(n) in total.

# Space Complexity: O(n)
# The set stores up to n elements in the worst case.
