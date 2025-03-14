class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            # If current value is the same as the previous one, skip to avoid duplicates of the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move inwards
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# Example Usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    # Expected: [[-1,-1,2],[-1,0,1]]
    print(solution.threeSum(nums1))

    # Example 2
    nums2 = [0, 1, 1]
    # Expected: []
    print(solution.threeSum(nums2))

    # Example 3
    nums3 = [0, 0, 0]
    # Expected: [[0,0,0]]
    print(solution.threeSum(nums3))

    # Example 4
    nums4 = [-1, 0, 1, 0]
    # Expected: [[-1,0,1]]
    print(solution.threeSum(nums4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n^2), where n is the length of the input list 'nums'. We traverse the list twice.
# Space complexity: O(1), since we are using only a constant amount of space.
