class Solution(object):
    def strStr(self, haystack, needle):
        """
        Find the first occurrence of needle in haystack.

        :param haystack: str - The main string
        :param needle: str - The substring to search for
        :return: int - Index of the first occurrence, or -1 if not found
        """
        m, n = len(haystack), len(needle)

        # Edge case: If needle is empty, return 0
        if n == 0:
            return 0

        # Sliding window
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1


# Example test cases
sol = Solution()
print(sol.strStr("sadbutsad", "sad"))  # Output: 0
print(sol.strStr("leetcode", "leeto"))  # Output: -1
print(sol.strStr("hello", "ll"))  # Output: 2
print(sol.strStr("aaaaa", "bba"))  # Output: -1
print(sol.strStr("", ""))  # Output: 0
