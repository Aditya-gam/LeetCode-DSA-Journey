from typing import List


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Function: shortestCommonSupersequence
        Description: Finds the shortest common supersequence of two strings.

        Parameters:
        - str1 (str): First input string.
        - str2 (str): Second input string.

        Returns:
        - str: The shortest common supersequence of str1 and str2.
        """

        m, n = len(str1), len(str2)

        # Step 1: Compute LCS (Longest Common Subsequence) using DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Construct the Shortest Common Supersequence using LCS
        i, j = m, n
        result = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1

        while i > 0:
            result.append(str1[i - 1])
            i -= 1

        while j > 0:
            result.append(str2[j - 1])
            j -= 1

        return "".join(result[::-1])


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: General case with interleaving characters
    str1 = "abac"
    str2 = "cab"
    print("Test Case 1:", solution.shortestCommonSupersequence(
        str1, str2))  # Expected Output: "cabac"

    # Test Case 2: Both strings are the same
    str1 = "aaaaaaaa"
    str2 = "aaaaaaaa"
    print("Test Case 2:", solution.shortestCommonSupersequence(
        str1, str2))  # Expected Output: "aaaaaaaa"

    # Test Case 3: One string is a subsequence of the other
    str1 = "abc"
    str2 = "ac"
    print("Test Case 3:", solution.shortestCommonSupersequence(
        str1, str2))  # Expected Output: "abc"

    # Test Case 4: Completely different strings
    str1 = "xyz"
    str2 = "abc"
    print("Test Case 4:", solution.shortestCommonSupersequence(
        str1, str2))  # Expected Output: "xyzabc"

    # Test Case 5: One empty string
    str1 = "abc"
    str2 = ""
    print("Test Case 5:", solution.shortestCommonSupersequence(
        str1, str2))  # Expected Output: "abc"

    # Test Case 6: Large input edge case
    str1 = "a" * 500
    str2 = "b" * 500
    # Expected Output: 1000
    print("Test Case 6:", len(solution.shortestCommonSupersequence(str1, str2)))

"""
Time Complexity:
- O(m * n) for LCS computation.
- O(m + n) for reconstructing the SCS.
- Total: O(m * n)

Space Complexity:
- O(m * n) for the DP table.
- O(m + n) for result storage.
- Total: O(m * n)
"""
