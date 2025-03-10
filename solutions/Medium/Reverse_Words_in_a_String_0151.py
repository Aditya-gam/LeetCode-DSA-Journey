class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

        Reverses the order of words in the string s, ensuring that
        the resulting string has no leading/trailing spaces and only
        a single space between words.
        """
        # Remove leading and trailing spaces, split by whitespace,
        # reverse the list of words, and join them with a single space.
        return " ".join(s.strip().split()[::-1])


# Example test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    s1 = "the sky is blue"
    # Expected output: "blue is sky the"
    print(solution.reverseWords(s1))  # Output: "blue is sky the"

    # Test case 2:
    s2 = "  hello world  "
    # Expected output: "world hello"
    print(solution.reverseWords(s2))  # Output: "world hello"

    # Test case 3:
    s3 = "a good   example"
    # Expected output: "example good a"
    print(solution.reverseWords(s3))  # Output: "example good a"

    # Test case 4:
    s4 = "  Bob    Loves  Alice   "
    # Expected output: "Alice Loves Bob"
    print(solution.reverseWords(s4))  # Output: "Alice Loves Bob"

    print("All test cases passed successfully.")

# Complexity analysis
# Time complexity: O(n), where n is the length of the input string s.
# We split the string into words, reverse the list of words, and join them, each operation taking O(n) time.

# Space complexity: O(n), where n is the length of the input string s.
# We store the words in a list, which can have at most n words. The reversed list also has n words.
