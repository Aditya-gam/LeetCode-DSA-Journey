class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Check if there are two distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.

        :param nums: List[int] - Input array
        :param k: int - Maximum allowed distance between duplicate indices
        :return: bool - True if such a pair exists, False otherwise
        """
        index_map = {}  # Dictionary to store the last seen index of each number

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            # Update the last seen index for the current number
            index_map[num] = i

        return False


# Example test cases
sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False
print(sol.containsNearbyDuplicate([99, 99], 2))  # Output: True
print(sol.containsNearbyDuplicate(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 3))  # Output: True
print(sol.containsNearbyDuplicate(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 2))  # Output: False

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once, and each dictionary operation (insertion and lookup) is O(1) on average.

# Space Complexity: O(n)
# The hash map stores up to n elements in the worst case.
