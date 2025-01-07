from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        Check if t is an anagram of s using sorting.

        :param s: str - First input string
        :param t: str - Second input string
        :return: bool - True if t is an anagram of s, False otherwise
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        """
        Check if t is an anagram of s using character frequency.

        :param s: str - First input string
        :param t: str - Second input string
        :return: bool - True if t is an anagram of s, False otherwise
        """
        return Counter(s) == Counter(t)


# Example test cases
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # Output: True
print(sol.isAnagram2("rat", "car"))         # Output: False
print(sol.isAnagram("a", "ab"))             # Output: False
print(sol.isAnagram2("", ""))                # Output: True
print(sol.isAnagram("a", "a"))              # Output: True
print(sol.isAnagram2("a", "b"))              # Output: False
print(sol.isAnagram("ab", "a"))             # Output: False
print(sol.isAnagram2("a", "ba"))             # Output: False
print(sol.isAnagram("ba", "a"))             # Output: False
print(sol.isAnagram2("a", "aa"))             # Output: False
print(sol.isAnagram("aa", "a"))             # Output: False
print(sol.isAnagram2("aa", "aa"))            # Output: True
print(sol.isAnagram("a", "a"*10**4))        # Output: True
print(sol.isAnagram2("a"*10**4, "a"))        # Output: True
print(sol.isAnagram("a"*10**4, "a"*10**4))  # Output: True
print(sol.isAnagram2("a"*10**4, "b"*10**4))  # Output: False
print(sol.isAnagram("a"*10**4, "a"*10**4 + "b"))  # Output: False
print(sol.isAnagram2("a"*10**4 + "b", "a"*10**4))  # Output: False
print(sol.isAnagram("a"*10**4 + "b", "a"*10**4 + "b"))  # Output: True
print(sol.isAnagram2("a"*10**4 + "b", "b" + "a"*10**4))  # Output: True
print(sol.isAnagram("a"*10**4 + "b", "a"*10**4 + "c"))  # Output: False
print(sol.isAnagram2("a"*10**4 + "c", "a"*10**4 + "b"))  # Output: False
print(sol.isAnagram("a"*10**4 + "b", "c" + "a"*10**4))  # Output: False
print(sol.isAnagram2("c" + "a"*10**4, "a"*10**4 + "b"))  # Output: False
print(sol.isAnagram("a"*10**4 + "b", "b" + "a"*10**4))  # Output: True
print(sol.isAnagram2("b" + "a"*10**4, "a"*10**4 + "b"))  # Output: True

# Complexity Analysis
# Sorting Method:
# Time Complexity: O(nlogn) (sorting both strings, where n is the length of the strings).
# Space Complexity: O(n) (for the sorted versions of the strings).

# Hash Map Method:
# Time Complexity: O(n) (counting characters in both strings).
# Space Complexity: O(1) (only 26 lowercase English letters, so the hash map size is constant).
