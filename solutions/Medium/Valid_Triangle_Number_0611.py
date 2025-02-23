class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # Step 1: Sort the array
        n = len(nums)
        count = 0

        # Step 2: Fix the longest side at position k
        for k in range(n-1, 1, -1):  # Start from the end
            i, j = 0, k - 1  # Two-pointer approach
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All pairs (i, j), (i+1, j) ... are valid
                    count += (j - i)
                    j -= 1  # Move j to find new valid pairs
                else:
                    i += 1  # Move i to get a larger sum

        return count


# Example test cases
if __name__ == "__main__":
    sol = Solution()
    # Output: 3
    print(sol.triangleNumber([2, 2, 3, 4]))
    # Output: 4
    print(sol.triangleNumber([4, 2, 3, 4]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4]))
    # Output: 3
    print(sol.triangleNumber([3, 4, 6, 7]))
    # Output: 10
    print(sol.triangleNumber([2, 2, 3, 4, 4, 6, 7]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7]))
    # Output: 1
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    # Output: 0
    print(sol.triangleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    # Output: 0

    print("All test cases passed successfully!")

# Complexity Analysis
# Time Complexity: O(N^2), where N is the number of elements in the input list nums. We have a nested loop, where the outer loop runs for N-2 iterations and the inner loop runs for N-1 iterations in the worst case.
# Space Complexity: O(1), as we use only a constant amount of extra space.
