class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        This function merges nums2 into nums1 in non-decreasing order.
        """
        # Pointers for nums1, nums2, and the merge position
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Compare elements from the back and place the larger one in nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are any elements left in nums2, place them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m, nums2, n = 3, [2, 5, 6], 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]  # Expected: [1,2,2,3,5,6]

    # Test case 2
    nums1 = [1]
    m, nums2, n = 1, [], 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]  # Expected: [1]

    # Test case 3
    nums1 = [0]
    m, nums2, n = 0, [1], 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]  # Expected: [1]

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(m+n), where m and n are the lengths of nums1 and nums2, respectively.
# Space Complexity: O(1).
