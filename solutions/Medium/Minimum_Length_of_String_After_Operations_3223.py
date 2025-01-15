class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_frequency = [0] * 26
        total_length = 0
        for char in s:
            char_frequency[ord(char) - ord('a')] += 1
        for frequency in char_frequency:
            if frequency == 0:
                continue
            if frequency % 2 == 0:
                total_length += 2
            else:
                total_length += 1

        return total_length


# Example test cases
sol = Solution()
assert sol.minimumLength("aabccabba") == 3
assert sol.minimumLength("a") == 1
assert sol.minimumLength("ab") == 2
assert sol.minimumLength("aa") == 0
assert sol.minimumLength("aab") == 1
assert sol.minimumLength("aabb") == 0
assert sol.minimumLength("aabbc") == 1
assert sol.minimumLength("aabbc") == 1

print("All test cases passed successfully.")

# Complexity Analysis
# Time Complexity: O(N), where N is the length of the input string s. We iterate over the string s once to calculate the frequency of each character.
# Space Complexity: O(1), as we use a fixed-size array of size 26 to store the frequency of each character.
