class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(left, right):
            """
            Expand around the center and return the length of the palindrome.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome
            return right - left - 1

        if not s or len(s) == 0:
            return ""

        start, end = 0, 0  # Track the start and end of the longest palindrome

        for i in range(len(s)):
            # Check for odd-length palindrome
            len1 = expand_around_center(i, i)
            # Check for even-length palindrome
            len2 = expand_around_center(i, i + 1)
            # Find the maximum length
            max_len = max(len1, len2)
            # Update start and end indices if we found a longer palindrome
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]


# Example test cases
# Test case 1
assert Solution().longestPalindrome("babad") in ["bab", "aba"]

# Test case 2
assert Solution().longestPalindrome("cbbd") == "bb"

# Test case 3
assert Solution().longestPalindrome("a") == "a"

# Test case 4
assert Solution().longestPalindrome("ac") in ["a", "c"]

# Test case 5
assert Solution().longestPalindrome("racecar") == "racecar"

# Test case 6 (Edge case with all unique characters)
assert Solution().longestPalindrome("abcdefg") in [
    "a", "b", "c", "d", "e", "f", "g"]

print("All test cases pass")

# Complexity analysis
# Time complexity: O(n^2), where n is the length of the input string s.
# Space complexity: O(1) since we are using a constant amount of space.
