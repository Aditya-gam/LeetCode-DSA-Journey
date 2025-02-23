class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        Returns the length of the last word in the string s.
        """
        # Remove trailing spaces and split by space
        words = s.rstrip().split(" ")
        # The last word in the list is the last word of the string
        return len(words[-1])


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    s1 = "Hello World"
    # Expected output: 5 ("World" has 5 characters)
    assert solution.lengthOfLastWord(s1) == 5

    # Test case 2:
    s2 = "   fly me   to   the moon  "
    # Expected output: 4 ("moon" has 4 characters)
    assert solution.lengthOfLastWord(s2) == 4

    # Test case 3:
    s3 = "luffy is still joyboy"
    # Expected output: 6 ("joyboy" has 6 characters)
    assert solution.lengthOfLastWord(s3) == 6

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string s.
# We need to traverse the string to find the last word.
# The split() function takes O(n) time to split the string into words.
# The len() function takes O(1) time to find the length of the last word.

# Space complexity: O(n), where n is the length of the input string s.
# We store the words in a list, which can have at most n words.
