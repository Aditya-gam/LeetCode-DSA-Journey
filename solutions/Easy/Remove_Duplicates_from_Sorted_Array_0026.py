class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove duplicates in a sorted array in-place.

        :param nums: List[int] - Input sorted array
        :return: int - Count of unique elements
        """
        if not nums:
            return 0  # If the list is empty, return 0 immediately

        # The first element is always unique if the array is non-empty
        place = 1

        # Compare each element with the last placed unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[place - 1]:
                nums[place] = nums[i]
                place += 1

        return place


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 2  # Expected unique count: 2
    # The first 2 elements of nums1 should be [1, 2]
    assert nums1[:k1] == [1, 2]

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 5  # Expected unique count: 5
    # The first 5 elements of nums2 should be [0,1,2,3,4]
    assert nums2[:k2] == [0, 1, 2, 3, 4]

    print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(1).
