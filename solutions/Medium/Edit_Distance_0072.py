class Solution(object):
    def minDistance(self, word1, word2):
        """
        Returns the minimum number of operations required to convert word1 into word2,
        where the allowed operations are insert, delete, and replace.

        Parameters:
        word1 (str): The original string to be converted.
        word2 (str): The target string.

        Returns:
        int: Minimum number of operations (insertions, deletions, replacements).
        """
        m, n = len(word1), len(word2)

        # Create a 2D DP table (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Cases
        for i in range(m + 1):
            dp[i][0] = i  # delete all i characters to match empty
        for j in range(n + 1):
            dp[0][j] = j  # insert j characters to empty word1

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    # If characters match, carry over the previous value
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Calculate costs for insert, delete, replace
                    insert_op = dp[i][j-1] + 1
                    delete_op = dp[i-1][j] + 1
                    replace_op = dp[i-1][j-1] + 1
                    dp[i][j] = min(insert_op, delete_op, replace_op)

        # The bottom-right cell holds the final answer
        return dp[m][n]

# Example test cases


def test_minDistance():
    sol = Solution()

    # Example 1
    word1, word2 = "horse", "ros"
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (delete 'r')
    # rose -> ros (delete 'e')
    assert sol.minDistance(word1, word2) == 3

    # Example 2
    word1, word2 = "intention", "execution"
    # 5 operations as shown in the example
    assert sol.minDistance(word1, word2) == 5

    # Test Case: Both empty
    word1, word2 = "", ""
    # No operations needed
    assert sol.minDistance(word1, word2) == 0

    # Test Case: One empty, one non-empty
    word1, word2 = "abc", ""
    # 3 deletions
    assert sol.minDistance(word1, word2) == 3

    # Test Case: Same strings
    word1, word2 = "test", "test"
    # 0 operations
    assert sol.minDistance(word1, word2) == 0

    # Test Case: Partial overlap
    word1, word2 = "abc", "bc"
    # 1 deletion: remove 'a'
    assert sol.minDistance(word1, word2) == 1

    print("All test cases passed!")


test_minDistance()

# Complexity analysis
# Time complexity: O(m*n) - We fill an m x n DP table, where m and n are the lengths of the input strings.
# Space complexity: O(m*n) - We use a 2D DP table of size (m+1) x (n+1).
