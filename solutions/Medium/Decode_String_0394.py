class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)  # Build the repeat count
            elif char == "[":
                # Push current state onto the stack
                stack.append((current_string, k))
                current_string = ""  # Reset for the new block
                k = 0
            elif char == "]":
                # Pop from stack and decode
                previous_string, repeat_count = stack.pop()
                current_string = previous_string + current_string * repeat_count
            else:
                # Add character to current string
                current_string += char

        return current_string


# Example test cases
sol = Solution()
print(sol.decodeString("3[a]2[bc]"))  # "aaabcbc"
print(sol.decodeString("3[a2[c]]"))  # "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
print(sol.decodeString("abc3[cd]xyz"))  # "abccdcdcdxyz"

# Complexity Analysis
# Time Complexity: O(n)
# We iterate through the input string once, so the time complexity is O(n).

# Space Complexity: O(n)
# The space complexity is O(n) because we store the characters in a stack. The worst-case scenario is when all characters are not enclosed in brackets. In this case, the stack will contain all characters in the input string.
