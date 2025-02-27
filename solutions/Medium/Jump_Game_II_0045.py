class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Returns the minimum number of jumps needed to reach the last index of nums.
        """
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index

        steps = 0
        currentEnd = 0
        farthest = 0

        for i in range(n - 1):
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])

            # If we've reached the boundary of our current jump
            if i == currentEnd:
                steps += 1       # we need to make another jump
                currentEnd = farthest  # expand the jump boundary

                # If this boundary crosses or reaches the last index, we can stop
                if currentEnd >= n - 1:
                    break

        return steps


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    # Minimum jumps to reach the last index is 2:
    #   0 -> 1, then 1 -> 4
    assert solution.jump(nums1) == 2  # Expected: 2

    # Test case 2
    nums2 = [2, 3, 0, 1, 4]
    # Minimum jumps is also 2:
    #   0 -> 1, then 1 -> 4
    assert solution.jump(nums2) == 2  # Expected: 2

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n) - We iterate through the nums list once
# Space complexity: O(1) - We use a constant amount of extra space
