# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid-point
            result = guess(mid)

            if result == 0:  # Correct guess
                return mid
            elif result == -1:  # Picked number is smaller
                high = mid - 1
            else:  # Picked number is larger
                low = mid + 1

        return -1


# Example test cases
solution = Solution()

# Example 1
n = 10
pick = 6
assert Solution().guessNumber(n) == 6

# Example 2
n = 1
pick = 1
assert Solution().guessNumber(n) == 1

# Example 3
n = 2
pick = 1
assert Solution().guessNumber(n) == 1

# Example 4
n = 100
pick = 73
assert Solution().guessNumber(n) == 73

# Example 5
n = 231 - 1
pick = 231 // 2
assert Solution().guessNumber(n) == 231 // 2

print("All test cases pass")

# Complexity Analysis
# Time Complexity: O(logn), where n is the range of numbers to guess from.
# Space Complexity: O(1), as no extra space is used.
