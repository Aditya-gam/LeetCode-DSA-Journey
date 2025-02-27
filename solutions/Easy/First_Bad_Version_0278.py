# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        Finds the index of the first bad version using binary search.
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Example test cases
solution = Solution()

# Example 1
n = 5
bad = 4
assert solution.firstBadVersion(n) == bad

# Example 2
n = 1
bad = 1

assert solution.firstBadVersion(n) == bad

# Example 3
n = 2
bad = 1
assert solution.firstBadVersion(n) == bad

# Example 4
n = 100
bad = 73
assert solution.firstBadVersion(n) == bad

print("All test cases passed!")

# Complexity Analysis
# Time complexity: O(log n), where n is the number of versions.
# Space complexity: O(1), since we are using only a constant amount of space.
