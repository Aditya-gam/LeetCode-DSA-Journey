class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        This function determines if we can reach the last index of nums 
        from the first index, given that nums[i] is the max jump length at index i.
        """
        max_reach = 0  # the furthest index we can reach

        for i in range(len(nums)):
            # If we've gone beyond what we can reach, return False
            if i > max_reach:
                return False
            # Update max_reach
            max_reach = max(max_reach, i + nums[i])
            # If we can already reach or surpass the last index, no need to continue
            if max_reach >= len(nums) - 1:
                return True

        return False


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    # Jump from index 0 -> 1 (2 -> 3 is possible) then index 1 -> 4
    # Output: True
    assert solution.canJump(nums1) == True, "Expected True"

    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    # We get stuck at index 3 where nums[3]=0. No way to proceed.
    # Output: False
    assert solution.canJump(nums2) == False, "Expected False"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the nums list once
# Space complexity: O(1) - We use a constant amount of extra space
