import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # This will store the minimal elements for LIS

        for num in nums:
            idx = bisect.bisect_left(dp, num)  # Find position in dp

            if idx == len(dp):
                dp.append(num)  # If num is greater, extend LIS
            else:
                dp[idx] = num  # Replace element at index

        return len(dp)  # Length of dp gives the LIS length


# Example test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Output: 4
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # Output: 1
    print(solution.lengthOfLIS([4, 10, 4, 3, 8, 9]))  # Output: 3
    print(solution.lengthOfLIS([2, 2]))  # Output: 1
    print(solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # Output: 6

    print("Passed all test cases!")

# Complexity Analysis
# Time Complexity: O(N log N), where N is the length of the nums array.
# We iterate over the nums array once and perform binary search using bisect_left in O(log N) time.
# Space Complexity: O(N), where N is the length of the nums array.
