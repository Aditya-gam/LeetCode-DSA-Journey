class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Returns the starting and ending position of 'target' in 'nums'.
        If the target is not found, return [-1, -1].
        """
        # Helper function to find the left boundary (first occurrence) of the target
        def findLeftBound(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    # Move right pointer to find an even earlier occurrence
                    right = mid - 1
                    if nums[mid] == target:
                        index = mid
                else:
                    left = mid + 1
            return index

        # Helper function to find the right boundary (last occurrence) of the target
        def findRightBound(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    # Move left pointer to find an even later occurrence
                    left = mid + 1
                    if nums[mid] == target:
                        index = mid
                else:
                    right = mid - 1
            return index

        leftBound = findLeftBound(nums, target)
        rightBound = findRightBound(nums, target)

        return [leftBound, rightBound]


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    # The positions of 8 are indices 3 and 4
    # Expected: [3, 4]
    assert solution.searchRange(nums1, target1) == [3, 4], "Expected [3,4]"

    # Test case 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    # 6 is not in the list
    # Expected: [-1, -1]
    assert solution.searchRange(nums2, target2) == [-1, -1], "Expected [-1,-1]"

    # Test case 3
    nums3 = []
    target3 = 0
    # Empty array, target not found
    # Expected: [-1, -1]
    assert solution.searchRange(nums3, target3) == [-1, -1], "Expected [-1,-1]"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(log n), where n is the number of elements in the input array 'nums'.
# Space complexity: O(1) since we are using only a constant amount of space.
