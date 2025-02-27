class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Performs a binary search to find 'target' in the sorted array 'nums'.
        Returns the index of 'target' if found, otherwise -1.
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

        return -1


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    # Index of 9 is 4
    assert solution.search(nums1, target1) == 4, "Expected index 4"

    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    # 2 is not in the list, so return -1
    assert solution.search(nums2, target2) == -1, "Expected -1"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(log n) - We perform binary search on the array.
# Space complexity: O(1) - We use a constant amount of extra space.
