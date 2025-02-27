class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        This function returns the index if target is found in the sorted list nums,
        or the index where target should be inserted if not found, in O(log n) time.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found, left is the correct insertion point
        return left


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    # Target is at index 2
    assert solution.searchInsert(nums1, target1) == 2

    # Test case 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    # 2 should be inserted at index 1
    assert solution.searchInsert(nums2, target2) == 1

    # Test case 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    # 7 should be inserted at index 4 (end)
    assert solution.searchInsert(nums3, target3) == 4

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(log n) - We perform binary search on the array.
# Space complexity: O(1) - We use a constant amount of extra space.
