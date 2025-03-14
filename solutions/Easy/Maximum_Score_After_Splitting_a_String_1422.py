class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Total number of 1's in the string
        total_ones = s.count('1')

        max_score = 0
        left_zeros = 0
        right_ones = total_ones

        # Iterate through the string but stop before the last character to ensure non-empty right
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            # Calculate current score
            current_score = left_zeros + right_ones
            max_score = max(max_score, current_score)

        return max_score


# Example test cases
solution = Solution()

# Test case 1
s = "011101"
assert solution.maxScore(s) == 5  # Expected: 5

# Test case 2
s = "00111"
assert solution.maxScore(s) == 5  # Expected: 5

# Test case 3
s = "1111"
assert solution.maxScore(s) == 3  # Expected: 3

# Test case 4
s = "000"
assert solution.maxScore(s) == 2  # Expected: 2

# Test case 5
s = "10101"
assert solution.maxScore(s) == 4  # Expected: 4

print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n), where N is the length of the string. The count of 1s takes O(N), and iterating over the string also takes O(N).

# Space complexity: O(1), as we are using only a constant amount of space.
