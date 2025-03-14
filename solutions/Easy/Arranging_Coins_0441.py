import math


class Solution(object):
    def arrangeCoinsForula(self, n):
        """
        :type n: int
        :rtype: int

        Returns the number of complete rows of coins we can build into a staircase.
        """
        if n <= 1:
            return n

        # Solve k(k+1)/2 <= n => k^2 + k - 2n <= 0
        # k = floor( (-1 + sqrt(1 + 8*n)) / 2 )
        return int((math.isqrt(1 + 8*n) - 1) // 2)

    def arrangeCoinsSearch(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins_used = mid*(mid+1)//2

            if coins_used == n:
                return mid
            elif coins_used < n:
                left = mid + 1
            else:
                right = mid - 1

        return right


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 5
    print(solution.arrangeCoinsForula(n1))  # Expected: 2
    print(solution.arrangeCoinsSearch(n1))  # Expected: 2

    # Example 2
    n2 = 8
    print(solution.arrangeCoinsForula(n2))  # Expected: 3
    print(solution.arrangeCoinsSearch(n2))  # Expected: 3

    # Example 3
    n3 = 1
    print(solution.arrangeCoinsForula(n3))  # Expected: 1
    print(solution.arrangeCoinsSearch(n3))  # Expected: 1

    # Example 4
    n4 = 0
    print(solution.arrangeCoinsForula(n4))  # Expected: 0
    print(solution.arrangeCoinsSearch(n4))  # Expected: 0

    # Example 5
    n5 = 2147483647
    print(solution.arrangeCoinsForula(n5))  # Expected: 65535
    print(solution.arrangeCoinsSearch(n5))  # Expected: 65535

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(1) for the formula-based solution and O(logn) for the binary search solution.
# Space Complexity: O(1) for both solutions.
