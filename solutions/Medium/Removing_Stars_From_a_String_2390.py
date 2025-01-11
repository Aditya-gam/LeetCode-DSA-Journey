class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  # Remove the most recent character
            else:
                stack.append(char)  # Add character to stack

        return ''.join(stack)


# Example test cases
sol = Solution()
print(sol.removeStars("ab**cd"))  # "cd"
print(sol.removeStars("a*b*c*d*"))  # ""
print(sol.removeStars("lee*t*cod*e"))  # "lecoe"
print(sol.removeStars("erase*****"))  # ""

# Complexity analysis
# Time complexity: O(n)
# The time complexity is O(n) because we iterate through the input string once.

# Space complexity: O(n)
# The space complexity is O(n) because we store the characters in a stack. The worst-case scenario is when all characters are not stars. In this case, the stack will contain all characters in the input string.
