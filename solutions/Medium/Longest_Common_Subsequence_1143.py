class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        Returns the length of the longest common subsequence between text1 and text2.

        Parameters:
        text1 (str): First input string.
        text2 (str): Second input string.

        Returns:
        int: The length of the longest common subsequence.
        """

        # Get lengths of both strings
        m, n = len(text1), len(text2)

        # Create a DP table of size (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # If characters match, extend the previous subsequence
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise, take the max of ignoring one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right corner holds the length of the LCS
        return dp[m][n]

# Example test cases


def test_longestCommonSubsequence():
    sol = Solution()

    # Test Case 1: Example 1
    text1, text2 = "abcde", "ace"
    # LCS = "ace", length = 3
    assert sol.longestCommonSubsequence(text1, text2) == 3

    # Test Case 2: Example 2
    text1, text2 = "abc", "abc"
    # LCS = "abc", length = 3
    assert sol.longestCommonSubsequence(text1, text2) == 3

    # Test Case 3: Example 3
    text1, text2 = "abc", "def"
    # No common subsequence, length = 0
    assert sol.longestCommonSubsequence(text1, text2) == 0

    # Test Case 4: Single character match
    text1, text2 = "a", "a"
    # LCS = "a", length = 1
    assert sol.longestCommonSubsequence(text1, text2) == 1

    # Test Case 5: No match with single character
    text1, text2 = "a", "b"
    # LCS = "", length = 0
    assert sol.longestCommonSubsequence(text1, text2) == 0

    # Test Case 6: Partial overlap
    text1, text2 = "abc", "cab"
    # Common subsequence could be "ab" or "ac", length = 2
    assert sol.longestCommonSubsequence(text1, text2) == 2

    # Test Case 7: Larger strings
    text1, text2 = "abxbxcxdxe", "abcde"
    # LCS = "abcde", length = 5
    assert sol.longestCommonSubsequence(text1, text2) == 5

    print("All test cases passed!")


test_longestCommonSubsequence()

# Complexity analysis
# Time complexity: O(m*n) - We fill an m x n DP table, where m and n are the lengths of the input strings.
# Space complexity: O(m*n) - We use an m x n DP table to store the intermediate results.
