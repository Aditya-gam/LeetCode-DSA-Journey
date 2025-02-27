class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Finds the length of the longest substring without repeating characters.
        """
        left = 0
        max_len = 0
        seen = {}

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                # If we've seen this char in the current window
                left = seen[char] + 1  # shift the window start

            seen[char] = right  # update the last seen index of char
            max_len = max(max_len, right - left + 1)

        return max_len


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "abcabcbb"
    # The longest substring without repeating chars is "abc", length=3
    print(solution.lengthOfLongestSubstring(s1))  # Expected: 3

    # Test case 2
    s2 = "bbbbb"
    # The longest substring is "b", length=1
    print(solution.lengthOfLongestSubstring(s2))  # Expected: 1

    # Test case 3
    s3 = "pwwkew"
    # The longest substring is "wke", length=3
    print(solution.lengthOfLongestSubstring(s3))  # Expected: 3

    # Test case 4
    s4 = ""
    # The longest substring is "", length=0
    print(solution.lengthOfLongestSubstring(s4))  # Expected: 0

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string 's'.
# Space complexity: O(min(m, n)), where m is the size of the character set and n is the length of the input string 's'.
