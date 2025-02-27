class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s1, t1 = "abc", "ahbgdc"
    # Output: True
    print(solution.isSubsequence(s1, t1))

    s2, t2 = "axc", "ahbgdc"
    # Output: False
    print(solution.isSubsequence(s2, t2))

    s3, t3 = "abc", "ahbgdcabc"
    # Output: True
    print(solution.isSubsequence(s3, t3))

    s4, t4 = "abc", "ahbgd"
    # Output: False
    print(solution.isSubsequence(s4, t4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string 't'.
# Space complexity: O(1), since we are using only a constant amount of space.
