class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1 = 0
        xor2 = 0

        # Compute XOR of all elements in nums1 and nums2
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num

        result = 0

        # If nums2 has an odd length, include xor1
        if len(nums2) % 2 == 1:
            result ^= xor1

        # If nums1 has an odd length, include xor2
        if len(nums1) % 2 == 1:
            result ^= xor2

        return result


# Example test cases
solution = Solution()

# Test case 1
nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
assert solution.xorAllNums(nums1, nums2) == 13  # Expected: 13

# Test case 2
nums1 = [1, 2]
nums2 = [3, 4]
assert solution.xorAllNums(nums1, nums2) == 0  # Expected: 0

# Test case 3
nums1 = [0]
nums2 = [0]
assert solution.xorAllNums(nums1, nums2) == 0  # Expected: 0

# Test case 4
nums1 = [1, 1, 1]
nums2 = [2, 2]
assert solution.xorAllNums(nums1, nums2) == 1  # Expected: 1

# Complexity Analysis
# Time Complexity: O(n+m), where n=len(nums1) and m=len(nums2).
# Computing xor1 takes O(n)
# Computing xor2 takes O(m)

# Space Complexity: O(1), Only a constant amount of extra space is used
