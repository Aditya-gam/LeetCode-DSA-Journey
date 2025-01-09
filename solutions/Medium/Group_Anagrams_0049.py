from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Group anagrams together.

        :param strs: List[str] - List of input strings
        :return: List[List[str]] - Grouped anagrams
        """
        anagram_dict = defaultdict(list)

        for word in strs:
            # Use sorted word as the key
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)

        # Return the grouped anagrams
        return list(anagram_dict.values())


# Example test cases
sol = Solution()
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams([""]))  # Output: [[""]]
print(sol.groupAnagrams(["a"]))  # Output: [["a"]]
print(sol.groupAnagrams(["a", "b", "c"]))  # Output: [["a"],["b"],["c"]]
# Output: [["abc"],["def"],["ghi"]]
print(sol.groupAnagrams(["abc", "def", "ghi"]))
# Output: [["abc","bca","cab"],["def","fed"],["ghi","ihg"]]
print(sol.groupAnagrams(["abc", "bca", "cab", "def", "ghi", "ihg", "fed"]))

# Complexity Analysis
# Time Complexity: O(n*m*log(m))
# Sorting each string takes O(mlog(m)), where m is the length of the string.
# Iterating through all strings takes O(n*mlog(m)), where n is the number of strings.

# Space Complexity: O(n*m)
# The space required for the dictionary is O(n*m), where m is the average length of the strings.
