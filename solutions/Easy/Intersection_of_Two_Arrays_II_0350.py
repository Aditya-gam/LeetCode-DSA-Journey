class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Find the intersection of two arrays, including duplicates.

        :param nums1: List[int] - First input array
        :param nums2: List[int] - Second input array
        :return: List[int] - Intersection of the arrays
        """
        from collections import Counter

        # Count elements in nums1
        count = Counter(nums1)
        result = []

        # Iterate through nums2 and check for common elements
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1  # Decrement count to handle duplicates

        return result


# Example test cases
sol = Solution()
print(sol.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
print(sol.intersect([1, 2, 3, 4], [5, 6, 7, 8]))  # Output: []
print(sol.intersect([1, 2, 3, 4], []))  # Output: []

# Complexity Analysis
# Time Complexity: O(m+n), where m is the length of nums1 and n is the length of nums2.
# O(m) to build the hash map.
# O(n) to traverse nums2.

# Space Complexity: O(m) to store the counts in the hash map.
