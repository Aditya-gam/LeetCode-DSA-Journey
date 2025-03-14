class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Finds the minimum element in the rotated sorted array nums 
        using O(log n) binary search.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # If mid element is greater than right, pivot is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [3, 4, 5, 1, 2]
    # Output: 1
    print(solution.findMin(nums1))

    # Example 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    # Output: 0
    print(solution.findMin(nums2))

    # Example 3
    nums3 = [11, 13, 15, 17]
    # Output: 11
    print(solution.findMin(nums3))

    # Example 4
    nums4 = [1]
    # Output: 1
    print(solution.findMin(nums4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log n), where n is the length of the input list 'nums'.
# Space complexity: O(1), since we are using only a constant amount of space.
