class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        # Must have same number of elements
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # If pattern char c has been seen
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w

            # If word w has been mapped
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c

        return True


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    pattern1, s1 = "abba", "dog cat cat dog"
    # Expected: True
    print(solution.wordPattern(pattern1, s1))

    pattern2, s2 = "abba", "dog cat cat fish"
    # Expected: False
    print(solution.wordPattern(pattern2, s2))

    pattern3, s3 = "aaaa", "dog cat cat dog"
    # Expected: False
    print(solution.wordPattern(pattern3, s3))

    pattern4, s4 = "abba", "dog dog dog dog"
    # Expected: False
    print(solution.wordPattern(pattern4, s4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n) where n is the length of the string 's', since we iterate over each word once and perform constant time operations for each word.
# Space complexity: O(n) where n is the length of the string 's' since we use two dictionaries to store the mappings between characters of 'pattern' and words in 's'. The space complexity is O(n) since in the worst case, we may need to store a mapping for each character in 'pattern' and each word in 's'.
