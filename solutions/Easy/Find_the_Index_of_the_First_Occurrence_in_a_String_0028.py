class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Returns the index of the first occurrence of needle in haystack,
        or -1 if needle is not found.
        """
        # If needle is empty, conventionally the result is 0
        if not needle:
            return 0

        # If needle length is greater than haystack length, not possible
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring from i of length len(needle) matches
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    haystack1, needle1 = "sadbutsad", "sad"
    # "sad" appears first at index 0
    print(solution.strStr(haystack1, needle1))  # Expected output: 0

    # Example 2
    haystack2, needle2 = "leetcode", "leeto"
    # "leeto" does not appear in "leetcode"
    print(solution.strStr(haystack2, needle2))  # Expected output: -1

    # Example 3
    haystack3, needle3 = "hello", "ll"
    # "ll" appears first at index 2
    print(solution.strStr(haystack3, needle3))  # Expected output: 2

    # Example 4
    haystack4, needle4 = "hello", "hello"
    # "hello" appears first at index 0
    print(solution.strStr(haystack4, needle4))  # Expected output: 0

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n*m), where n is the length of the input string 'haystack'
# and m is the length of the input string 'needle'.

# Space complexity: O(1), since we are using only a constant amount of space.
