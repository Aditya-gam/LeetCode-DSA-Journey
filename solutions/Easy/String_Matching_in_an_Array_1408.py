class Solution(object):
    def stringMatching(self, words):
        """
        Find all strings in words that are a substring of another word.

        :param words: List[str] - List of input strings
        :return: List[str] - Strings that are substrings of another word
        """
        result = []

        # Compare each word with every other word
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  # Avoid duplicate entries for the same word

        return result


# Example test cases
sol = Solution()
# Output: ["as", "hero"]
print(sol.stringMatching(["mass", "as", "hero", "superhero"]))
# Output: ["et", "code"]
print(sol.stringMatching(["leetcode", "et", "code"]))
print(sol.stringMatching(["blue", "green", "bu"]))              # Output: []
print(sol.stringMatching(["a", "b", "c", "d", "e"]))            # Output: []
# Output: ["a", "b"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "ab"]))
print(sol.stringMatching(["a", "b", "c", "d", "e", "ba"]))      # Output: ["a"]
# Output: ["a", "b", "c"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "abc"]))
# Output: ["a", "b", "c"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "cba"]))
# Output: ["a", "b", "c", "d"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "abcd"]))
# Output: ["a", "b", "c", "d"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "dcba"]))
# Output: ["a", "b", "c", "d", "e"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "abcde"]))
# Output: ["a", "b", "c", "d", "e"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "edcba"]))
# Output: ["a", "b", "c", "d", "e"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "abcdef"]))
# Output: ["a", "b", "c", "d", "e"]
print(sol.stringMatching(["a", "b", "c", "d", "e", "fedcba"]))

# Complexity Analysis
# Time Complexity: O(n^2*m)
# n: Number of words in the list.
# m: Average length of each word.
# Comparing each word with every other word requires O(n^2), and checking if one word is a substring of another takes O(m).
#
# Space Complexity: O(r)
# r: Number of substrings in the result list.
