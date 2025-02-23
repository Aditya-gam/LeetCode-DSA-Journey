class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool

        Checks if num is a perfect square using binary search.
        """
        if num < 2:
            return True  # 1 is a perfect square

        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    print(solution.isPerfectSquare(16))  # Expected True (4*4 = 16)
    print(solution.isPerfectSquare(14))  # Expected False
    print(solution.isPerfectSquare(1))  # Expected True
    print(solution.isPerfectSquare(0))  # Expected True

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(log n), where n is the input number 'num'.
# Space complexity: O(1), since we are using only a constant amount of space.
