class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Finds the single element in a sorted array where every other
        element appears exactly twice. Uses O(log n) binary search.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Determine if mid is aligned with even or odd index
            # We'll check the neighbor to decide the side
            if mid % 2 == 0:
                # mid is even => compare with mid+1
                if nums[mid] == nums[mid + 1]:
                    # Single element must be on the right half
                    left = mid + 2
                else:
                    right = mid
            else:
                # mid is odd => compare with mid-1
                if nums[mid] == nums[mid - 1]:
                    # Single element is on the right half
                    left = mid + 1
                else:
                    right = mid

        return nums[left]


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    # Expected: 2
    print(solution.singleNonDuplicate(nums1))

    nums2 = [3, 3, 7, 7, 10, 11, 11]
    # Expected: 10
    print(solution.singleNonDuplicate(nums2))

    nums3 = [1, 1, 2]
    # Expected: 2
    print(solution.singleNonDuplicate(nums3))

    nums4 = [1, 2, 2]
    # Expected: 1
    print(solution.singleNonDuplicate(nums4))

    nums5 = [1, 1, 2, 2, 3]
    # Expected: 3
    print(solution.singleNonDuplicate(nums5))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log n) where n is the length of the list 'nums'. The binary search algorithm takes O(log n) time to find the single element.
# Space complexity: O(1) since we use only a constant amount of extra space.
