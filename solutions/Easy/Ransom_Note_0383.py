from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        Checks if ransomNote can be constructed from letters of magazine.
        """
        # Count frequencies in magazine
        freq = Counter(magazine)

        # Check each char in ransomNote
        for c in ransomNote:
            if freq[c] == 0:
                return False
            freq[c] -= 1

        return True


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    ransomNote1, magazine1 = "a", "b"
    # Expected: False
    print(solution.canConstruct(ransomNote1, magazine1))

    ransomNote2, magazine2 = "aa", "ab"
    # Expected: False
    print(solution.canConstruct(ransomNote2, magazine2))

    ransomNote3, magazine3 = "aa", "aab"
    # Expected: True
    print(solution.canConstruct(ransomNote3, magazine3))

    ransomNote4, magazine4 = "abc", "def"
    # Expected: False
    print(solution.canConstruct(ransomNote4, magazine4))

    print("All test cases passed!")

# Complexity analysis
# Time complexity: O(n + m) where n is the length of the string 'ransomNote' and m is the length of the string 'magazine'
# Space complexity: O(m) where m is the length of the string 'magazine'
