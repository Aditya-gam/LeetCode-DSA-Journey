from collections import Counter


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # Count the frequency of each character
        freq = Counter(s)

        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)

        # Check constraints
        if k < odd_count or k > len(s):
            return False

        return True


# Example test cases
sol = Solution()
print(sol.canConstruct("annabelle", 2))  # Output: True
print(sol.canConstruct("leetcode", 3))   # Output: False
print(sol.canConstruct("true", 4))       # Output: True
print(sol.canConstruct("yzyzyzyzyzyzyzy", 2))  # Output: True
print(sol.canConstruct("cr", 7))         # Output: False
print(sol.canConstruct("a", 1))          # Output: True
print(sol.canConstruct("a", 2))          # Output: False
print(sol.canConstruct("a", 0))          # Output: False
print(sol.canConstruct("", 0))           # Output: True
print(sol.canConstruct("", 1))           # Output: False

# Complexity Analysis
# Time complexity: O(n) where n is the length of the string s. We iterate through the string to count the frequency of
# each character.
# Space complexity: O(1) since the maximum number of characters in the frequency dictionary is 26.
