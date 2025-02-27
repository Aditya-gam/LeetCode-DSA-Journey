class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2 up to n
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i-1] * 2) % MOD

        left, right = 0, n - 1
        count = 0

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1  # Decrease the largest number to find a valid sum
            else:
                # Count valid subsequences
                count = (count + power[right - left]) % MOD
                left += 1  # Move to next min

        return count


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.numSubseq([3, 5, 6, 7], 9) == 4
    assert solution.numSubseq([3, 3, 6, 8], 10) == 6
    assert solution.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16) == 127
    assert solution.numSubseq([3, 3, 6, 8], 10) == 6
    assert solution.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16) == 127
    assert solution.numSubseq([3, 3, 6, 8], 10) == 6
    assert solution.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16) == 127
    assert solution.numSubseq([3, 3, 6, 8], 10) == 6
    assert solution.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    assert solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16) == 127

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N log N), where N is the length of the nums array.
# We sort the nums array in O(N log N) time and iterate over the array once.

# Space Complexity: O(N), where N is the length of the nums array.
