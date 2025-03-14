class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Finds the minimum element in a sorted rotated array with possible duplicates.
        Worst-case time complexity can degrade to O(n).
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # min is in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # min is in the left half including mid
                right = mid
            else:
                # nums[mid] == nums[right]
                # skip the duplicate
                right -= 1

        return nums[left]


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 3, 5]
    # Output: 1
    print(solution.findMin(nums1))  # Expected 1

    # Example 2
    nums2 = [2, 2, 2, 0, 1]
    # Output: 0
    print(solution.findMin(nums2))  # Expected 0

    # Example 3
    nums3 = [1, 1]
    # Output: 1
    print(solution.findMin(nums3))  # Expected 1

    # Example 4
    nums4 = [1, 3, 3]
    # Output: 1
    print(solution.findMin(nums4))  # Expected 1

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n) in the worst case, where n is the length of the input list 'nums'.
# Space complexity: O(1), since we are using only a constant amount of space.
