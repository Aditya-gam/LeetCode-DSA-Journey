class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sums = {
            0: 1}  # Initialize with 0 to handle subarrays starting from index 0
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num  # Update the cumulative sum

            # Check if (current_sum - k) exists in the hash map
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Update the frequency of current_sum in the hash map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count


# Example test cases
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Output: 2
print(sol.subarraySum([1, 2, 3], 3))  # Output: 2
print(sol.subarraySum([1, 2, 3, 4, 5], 10))  # Output: 1
print(sol.subarraySum([1, 2, 3, 4, 5], 5))  # Output: 2
print(sol.subarraySum([1, -1, 1], 1))  # Output: 3
print(sol.subarraySum([1, 2, 3, 4, 5], 1))  # Output: 0

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the array once, and each operation (hash map insertion and lookup) is O(1).

# Space Complexity: O(n)
# In the worst case, the hash map prefix_sums could store all n unique prefix sums.
