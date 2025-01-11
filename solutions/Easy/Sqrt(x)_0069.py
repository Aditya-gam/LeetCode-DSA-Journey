class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        low, high = 1, x // 2
        result = 1

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid  # store the last valid mid
                low = mid + 1
            else:
                high = mid - 1

        return result


# Example test cases
sol = Solution()
print(sol.mySqrt(4))  # Output: 2
print(sol.mySqrt(8))  # Output: 2
print(sol.mySqrt(9))  # Output: 3
print(sol.mySqrt(16))  # Output: 4
print(sol.mySqrt(25))  # Output: 5
print(sol.mySqrt(36))  # Output: 6

# Complexity Analysis
# Time Complexity: O(logx), where x is the input value. This is because we halve the search range in each iteration of the binary search.

# Space Complexity: O(1), as no additional data structures are used.
