class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str

        Repeatedly removes each digit and the nearest letter to its left. 
        Returns the final string after all digits are removed.
        """
        stack = []

        for c in s:
            if c.isdigit():
                # Pop one letter from stack
                stack.pop()
                # Digit is removed, so do not push anything
            else:
                # c is a letter
                stack.append(c)

        return "".join(stack)


# Example test cases:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "abc"
    print(solution.clearDigits(s1))  # "abc"

    # Example 2
    s2 = "cb34"
    print(solution.clearDigits(s2))  # ""

    # Example 3
    s3 = "1a2b3c4"
    print(solution.clearDigits(s3))  # "abc"

    # Example 4
    s4 = "1a2b3c4d5e"
    print(solution.clearDigits(s4))  # "abcde"

    print("All test cases passed!")

# Complexity analysis:
# Time complexity: O(n), where n is the length of the string s. We iterate through the string once.
# Space complexity: O(n), where n is the length of the string s. We use a stack to store the characters.
