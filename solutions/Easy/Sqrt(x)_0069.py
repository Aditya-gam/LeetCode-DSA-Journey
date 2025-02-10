class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        Returns the integer square root of x using binary search.
        """
        if x < 2:
            return x  # 0->0, 1->1

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:  # square < x
                left = mid + 1

        return right


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    x1 = 4
    print(solution.mySqrt(x1))  # Expected: 2

    # Example 2
    x2 = 8
    print(solution.mySqrt(x2))  # Expected: 2

    # Example 3
    x3 = 1
    print(solution.mySqrt(x3))  # Expected: 1

    # Example 4
    x4 = 0
    print(solution.mySqrt(x4))  # Expected: 0

    # Example 5
    x5 = 2147395599
    print(solution.mySqrt(x5))  # Expected: 46339

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(logx), where x is the input value. This is because we halve the search range in each iteration of the binary search.

# Space Complexity: O(1), as no additional data structures are used.
