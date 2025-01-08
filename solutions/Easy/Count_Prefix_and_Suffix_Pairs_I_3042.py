class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        Count the number of (i, j) pairs such that i < j and words[i] is both a prefix and suffix of words[j].

        :param words: List[str] - List of words
        :return: int - Count of valid pairs
        """
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                # Check prefix and suffix conditions
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1

        return count


# Example test cases
sol = Solution()
print(sol.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))  # Output: 4
print(sol.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))  # Output: 2
print(sol.countPrefixSuffixPairs(["abab", "ab"]))  # Output: 0
print(sol.countPrefixSuffixPairs(["a", "b", "c", "d"]))  # Output: 0
