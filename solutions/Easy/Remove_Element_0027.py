class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int

        This function removes all instances of 'val' from 'nums' in-place 
        and returns the length of the modified array that doesn't include 'val'.
        """
        place = 0  # pointer to place the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[place] = nums[i]
                place += 1

        return place


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    assert k1 == 2  # Expected: 2
    # Validate that the first k elements in nums1 are not val1
    for i in range(k1):
        assert nums1[i] != val1

    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    assert k2 == 5  # Expected: 5
    # Validate that the first k elements in nums2 are not val2
    for i in range(k2):
        assert nums2[i] != val2

    # Test case 3
    nums3 = [1]
    val3 = 1
    k3 = solution.removeElement(nums3, val3)
    assert k3 == 0  # Expected: 0
    # Validate that the first k elements in nums3 are not val3
    for i in range(k3):
        assert nums3[i] != val3

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(1).
