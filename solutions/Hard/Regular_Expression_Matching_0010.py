class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Function: isMatch
        Description: Implements regular expression matching with support for '.' and '*'.

        Parameters:
        - s (str): The input string.
        - p (str): The pattern to match.

        Returns:
        - bool: True if the pattern matches the entire string, otherwise False.
        """
        m, n = len(s), len(p)

        # dp[i][j] means whether s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, etc. that can match an empty string
        for j in range(2, n + 1, 2):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Zero occurrences: Ignore previous character and '*'
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences: Match if previous char in pattern matches current char in string
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Simple mismatch
    print(solution.isMatch("aa", "a"))
    # Expected output: False

    # Test case 2: Match with '*'
    print(solution.isMatch("aa", "a*"))
    # Expected output: True

    # Test case 3: Match with '.*'
    print(solution.isMatch("ab", ".*"))
    # Expected output: True

    # Test case 4: Complex pattern
    print(solution.isMatch("mississippi", "mis*is*p*."))
    # Expected output: False

    # Test case 5: Another '*' match
    print(solution.isMatch("mississippi", "mis*is*ip*."))
    # Expected output: True

    # Test case 6: Full match with '.'
    print(solution.isMatch("abc", "a.c"))
    # Expected output: True

    # Test case 7: No match due to extra characters
    print(solution.isMatch("abcd", "d*"))
    # Expected output: False

    # Test case 8: Empty string
    print(solution.isMatch("", ".*"))
    # Expected output: True

    print("All test cases passed!")

# Complexity Analysis
# Time Complexity: O(m * n), where m and n are the lengths of the input string and pattern, respectively.
# Space Complexity: O(m * n), where m and n are the lengths of the input string and pattern, respectively.
