class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # If the left portion [left..mid] is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in [left..mid]
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right portion [mid..right] is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums1, target1 = [4, 5, 6, 7, 0, 1, 2], 0
    print(solution.search(nums1, target1))  # Expected output: 4

    # Example 2:
    nums2, target2 = [4, 5, 6, 7, 0, 1, 2], 3
    print(solution.search(nums2, target2))  # Expected output: -1

    # Example 3:
    nums3, target3 = [1], 0
    print(solution.search(nums3, target3))  # Expected output: -1

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log(n)), where n is the length of the input list 'nums'.
# Space complexity: O(1), since we are using only a constant amount of space.
